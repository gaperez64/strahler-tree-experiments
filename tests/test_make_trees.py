#!/usr/bin/env python3
"""Exercise the benchmark wrapper with real solvers and optional Graphviz."""

import csv
from contextlib import redirect_stderr
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from test_gen_decomp import BUILD_DIR, ROOT, decomp, fake_dot
import make_trees


class MakeTreesTests(unittest.TestCase):
    def command(self, out, *args):
        return [sys.executable, str(ROOT / "scripts/make_trees.py"),
                "--build-dir", str(BUILD_DIR), "--out", str(out), *map(str, args)]

    def test_backends_are_inventory_names(self):
        self.assertEqual(len(decomp.BACKENDS), 24)
        self.assertEqual(len({b.name for b in decomp.BACKENDS}), 24)
        result = subprocess.run(self.command("unused", "--backends", "unknown",
                                            ROOT / "tests/games/strahler_two.pg"),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown backends", result.stderr)
        self.assertIn("valid names: lifting, lifting+pre", result.stderr)
        self.assertIn("pm-succinct+pre+iter", result.stderr)

    def test_multi_round_metrics_and_png(self):
        stats = (ROOT / "tests/golden/pm_strahler_iter_stats.out").read_text().split("# round", 1)[0]
        source = (ROOT / "tests/golden/pm_strahler_incremental.out").read_text()
        backend = next(b for b in decomp.BACKENDS if b.name == "pm-strahler+iter")
        metrics = decomp.run_metrics(backend, decomp.Run("complete", stats, source), 5)
        self.assertEqual(metrics["won"], (5, 0))
        self.assertIn("k=2", metrics["parameters"][0])
        self.assertEqual(metrics["info"], decomp.tree_info(
            "digraph " + source.rsplit("digraph ", 1)[-1], True))
        self.assertEqual(tuple(metrics["info"][0][0][name] for name in
                               ("nodes", "leaves", "height", "strahler")), (3, 1, 3, 1))
        ad = (ROOT / "tests/golden/pg2adot_iter_pre.out").read_text()
        backend = next(b for b in decomp.BACKENDS if b.name == "lifting-adaptive+pre+iter")
        metrics = decomp.run_metrics(backend, decomp.Run("complete", ad, ad), 7)
        self.assertEqual(metrics["won"], (7, 0))
        self.assertEqual(tuple(metrics["info"][0][0][name] for name in
                               ("nodes", "leaves", "height", "strahler")), (2, 1, 2, 1))
        with tempfile.TemporaryDirectory() as directory:
            dot = fake_dot(Path(directory))
            png = decomp.render_png(source.encode(), "a" * 64, dot)
            rendered = dot.with_suffix(".calls").read_text()
            self.assertEqual(rendered.count("digraph "), 1)
            self.assertIn("subgraph cluster_0", rendered)
            self.assertIn("subgraph cluster_1", rendered)
            self.assertIn("round0_n1 -> round0_n2", rendered)
            self.assertIn("round1_n1 -> round1_n2", rendered)
            self.assertEqual(decomp.png_dot_hash(png), "a" * 64)

    def test_timeout_records_each_pair(self):
        with (tempfile.TemporaryDirectory() as directory,
              patch.object(sys, "argv", self.command(directory, "--no-png",
                  "--backends", "zielonka,pm-succinct+pre",
                  ROOT / "tests/games/strahler_two.pg")[1:]),
              patch.object(decomp, "invoke", return_value=decomp.Run("timeout (1 s)")),
              redirect_stderr(io.StringIO())):
            folder = Path(directory) / "strahler_two"
            folder.mkdir()
            stale_metrics = folder / "zielonka.metrics"
            stale_metrics.write_text("old")
            self.assertEqual(make_trees.main(), 1)
            self.assertFalse(stale_metrics.exists())
            self.assertFalse(list(Path(directory).rglob("*.metrics")))
            with (Path(directory) / "summary.csv").open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 2)
            self.assertTrue(all(row["outcome"] == "timeout (1 s)" for row in rows))

    def test_discovery_rejects_colliding_stems(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for suffix in ("pg", "gm"):
                shutil.copyfile(ROOT / "tests/games/strahler_two.pg", root / f"same.{suffix}")
            with self.assertRaisesRegex(ValueError, "unique stems"):
                decomp.discover_games([root])

    def test_adaptive_selection_keeps_completed_tree(self):
        source = (ROOT / "tests/golden/pg2adot_adaptive_stats.out").read_text()
        start = source.index("digraph ")
        completed = decomp.Run("complete", source[:start], source[start:])
        with (tempfile.TemporaryDirectory() as directory,
              patch.object(sys, "argv", self.command(directory, "--no-png",
                  "--backends", "lifting-adaptive",
                  ROOT / "tests/games/strahler_two.pg")[1:]),
              patch.object(decomp, "invoke", side_effect=[
                  completed, decomp.Run("timeout (1 s)")]) as invoke,
              redirect_stderr(io.StringIO())):
            self.assertEqual(make_trees.main(), 0)
            invoke.assert_called_once()
            self.assertIn("--adaptive-t", invoke.call_args.args[0])
            with (Path(directory) / "summary.csv").open() as stream:
                row, = csv.DictReader(stream)
            self.assertEqual(row["outcome"], "complete")
            self.assertEqual((Path(directory) / row["tree"]).read_text(), completed.dot)

    @unittest.skipUnless((BUILD_DIR / "pg2adot").is_file(), "build the CLI tools")
    def test_batch_accepts_replaced_vertices_and_literal_backslashes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = root / "inputs"
            inputs.mkdir()
            for name, records in (
                ("a-replaced", "0 1 1 0;\n0 0 0 0;\n"),
                ("b-backslash", '0 0 0 0 "name\\";\n'),
                ("c-later", "0 0 0 0;\n"),
            ):
                (inputs / (name + ".pg")).write_text("parity 0;\n" + records)
            out = root / "out"
            result = subprocess.run(self.command(out, "--no-png", "--backends",
                "zielonka", inputs), capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            with (out / "summary.csv").open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 3)
            for row in rows:
                self.assertEqual(row["outcome"], "complete")
                self.assertEqual(tuple(row[key] for key in (
                    "vertices", "edges", "distinct_priorities", "maximum_priority",
                    "won_even", "won_odd")), ("1", "1", "1", "0", "1", "0"))
                self.assertEqual(tuple(row[key] for key in (
                    "height_even", "min_leaf_depth_even", "mean_leaf_depth_even",
                    "min_leaf_depth_odd", "mean_leaf_depth_odd")),
                    ("1", "1", "1.000", "0", "0.000"))
                self.assertTrue((out / row["tree"]).is_file())

    @unittest.skipUnless(all((BUILD_DIR / name).is_file()
                             for name in ("pg2adot", "pg2pmdot")), "build the CLI tools")
    def test_generation_with_and_without_graphviz(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inputs = root / "inputs/nested"
            inputs.mkdir(parents=True)
            game = inputs / "cabp_swp.ehoa.pg"
            shutil.copyfile(ROOT / "tests/games/strahler_two.pg", game)
            (inputs / "not-a-game.pg").write_text("ignore this file\n")
            dot = fake_dot(root)
            for mode, options in (
                ("png", ["--dot", dot]),
                ("missing", ["--dot", root / "missing-dot"]),
                ("disabled", ["--no-png", "--dot", dot]),
            ):
                with self.subTest(mode=mode):
                    out = root / mode
                    result = subprocess.run(self.command(out, "--backends",
                        "lifting-adaptive+iter,pm-strahler+iter", *options,
                        root / "inputs", game), capture_output=True, text=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stdout, "")
                    self.assertEqual(result.stderr.count(": complete"), 2)
                    self.assertEqual("warning:" in result.stderr, mode == "missing")
                    with (out / "summary.csv").open() as stream:
                        rows = list(csv.DictReader(stream))
                    self.assertEqual(len(rows), 2)
                    self.assertTrue(all(row["won_even"] == "5" and
                                        row["won_odd"] == "0" for row in rows))
                    for row in rows:
                        path = out / row["tree"]
                        self.assertTrue(path.is_file())
                        self.assertIn("outcome: complete", path.with_suffix(".stats").read_text())
                        lines = path.with_suffix(".metrics").read_text().splitlines()
                        self.assertEqual([line.split(":")[0] for line in lines],
                                         list(decomp.TREE_METRICS))
                        for line in lines:
                            metric, values = line.split(": ")
                            for player, value in (part.split("=") for part in values.split()):
                                self.assertEqual(row[f"{metric}_{player}"], value)
                                if metric.startswith("mean_"):
                                    self.assertRegex(value, r"^\d+\.\d{3}$")
                        self.assertEqual(path.with_suffix(".png").exists(), mode == "png")
                        if mode == "png":
                            self.assertIsNotNone(decomp.png_dot_hash(path.with_suffix(".png").read_bytes()))
                    self.assertTrue((out / game.stem / "pm-strahler+iter.leaves").is_file())
            shutil.copyfile(ROOT / "tests/games/incomplete.pg", inputs / "incomplete.pg")
            result = subprocess.run(self.command(root / "invalid", "--no-png",
                "--backends", "zielonka,pm-succinct+pre", root / "inputs"),
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            with (root / "invalid/summary.csv").open() as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), 4)
            self.assertEqual(sum(row["outcome"] == "complete" for row in rows), 2)
            self.assertEqual(sum(row["outcome"].startswith("error:") for row in rows), 2)


if __name__ == "__main__":
    unittest.main()
