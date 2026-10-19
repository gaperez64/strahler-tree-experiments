#!/usr/bin/env python3
"""Small wrapper checks, including a real two-pass generation when built."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import gen_decomp as decomp  # noqa: E402

BUILD_DIR = (Path(sys.argv.pop(1)).resolve()
             if len(sys.argv) > 1 and not sys.argv[1].startswith("-")
             else ROOT / "build")


class DecompTests(unittest.TestCase):
    def test_content_discovery_and_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            examples = root / "examples"
            (examples / "nested").mkdir(parents=True)
            game = examples / "nested/game.gm"
            game.write_text('\nparity 80;\nstart 4;\n'
                            '4 9 0 4,20 "name; with \\"quote\\"";\n'
                            '20 2 1 4;\n')
            (examples / "fake.pg").write_text("// not a parity game\n")
            (examples / "tree.hpp").write_text("int tree[] = {0};\n")
            self.assertEqual(decomp.discover_games(root), [game])
            self.assertEqual(decomp.game_info(game), (2, 3, 2, 9))
            (examples / "game.pg").write_text("parity 0;\n0 0 0 0;\n")
            with self.assertRaisesRegex(ValueError, "unique stems"):
                decomp.discover_games(root)

    def test_stable_stats(self):
        self.assertEqual(decomp.stable_stats(
            "lifting: result=complete lifts=3 elapsed=0.03 time_ms=4\n"
            "CPU time: 0.2 s\nwall-time: 0.3 s\ntiming: 2\n"
            "Solver failed: /repo/build/file\n", Path("/repo"),
            Path("/repo/build")),
            "lifting: result=complete lifts=3\nSolver failed: build/file\n")

    def test_tree_metrics_exclude_placeholders(self):
        ad = (ROOT / "tests/golden/pg2adot_sets.out").read_text()
        pm = (ROOT / "tests/golden/pm_strahler_sets.out").read_text()
        self.assertEqual(decomp.tree_info(ad, False),
                         [((0, 0, 0, 0), ()), ((3, 2, 2, 2), (2, 0, 0))])
        self.assertEqual(decomp.tree_info(pm, True),
                         [((5, 2, 3, 2), (2, 1, 0, 1, 0)),
                          ((0, 0, 0, 0), ())])

    def test_limits_errors_discard_output_and_timeouts_abort(self):
        game = ROOT / "examples/Button.tlsf.ehoa.pg"
        with patch.object(decomp.subprocess, "run") as run:
            for code, stderr, outcome in (
                (4, "Solver failed: more than the limit of 100\n",
                 "host limit"),
                (0, "Warning: more than 100 leaves\nresult=partial\n",
                 "host limit"),
                (4, "bad game\nmore detail\n", "error: bad game"),
            ):
                run.return_value = subprocess.CompletedProcess(
                    [], code, "partial DOT", stderr)
                result = decomp.invoke(["tool"], game, ROOT, BUILD_DIR, 1)
                self.assertEqual(result.outcome, outcome)
                self.assertFalse(result.dot)
            run.side_effect = subprocess.TimeoutExpired(
                "tool", 1, output=b"partial DOT", stderr=b"partial stats")
            with self.assertRaisesRegex(SystemExit,
                                        r"Button.*safety timeout.*skip list"):
                decomp.invoke(["tool"], game, ROOT, BUILD_DIR, 1)
        with self.assertRaisesRegex(SystemExit, r"safety timeout.*skip list"):
            decomp.invoke(
                [sys.executable, "-c", "import time; time.sleep(1)"],
                game, ROOT, BUILD_DIR, 0.01)

    def test_timeout_aborts_generation_without_syncing_outputs(self):
        with (patch.object(sys, "argv", ["gen_decomp.py"]),
              patch.object(decomp.os, "access", return_value=True),
              patch.object(decomp.subprocess, "run", side_effect=
                           subprocess.TimeoutExpired("tool", 600)) as run,
              patch.object(decomp, "sync_outputs") as sync,
              redirect_stdout(io.StringIO())):
            with self.assertRaisesRegex(SystemExit, "safety timeout after 600 s"):
                decomp.main()
            self.assertEqual(run.call_args.kwargs["timeout"], 600)
            sync.assert_not_called()

    def test_backends_skip_only_listed_pairs_and_cap_labels(self):
        for name in ("cabp_swp.ehoa.pg", "FairSchedulern=2_compact.gm"):
            game = ROOT / "examples" / name
            for backend in decomp.BACKENDS:
                for pre in (False, True):
                    with (self.subTest(game=name, backend=backend.name,
                                       pre=pre),
                          patch.object(decomp, "invoke",
                                       return_value=decomp.Run("host limit"))
                          as invoke):
                        result = decomp.run_backend(
                            backend, pre, game, ROOT, BUILD_DIR, 1, 100)
                        if (name == "cabp_swp.ehoa.pg" and backend.name in
                                ("lifting-adaptive", "pm-strahler")):
                            self.assertEqual(
                                result, decomp.Run("skipped (> 60 s locally)"))
                            invoke.assert_not_called()
                            continue
                        self.assertEqual(result.outcome, "host limit")
                        invoke.assert_called_once()
                        command = invoke.call_args.args[0]
                        self.assertIn("--labels=sets", command)
                        self.assertIn("--max-set-items=8", command)
                        self.assertEqual("--shave=all" in command, pre)
                        self.assertEqual("--compress" in command, pre)

    def test_adaptive_equality_is_enforced(self):
        backend = decomp.BACKENDS[1]
        game = ROOT / "examples/Button.tlsf.ehoa.pg"
        with patch.object(decomp, "invoke", side_effect=[
            decomp.Run("complete", dot="cold"),
            decomp.Run("complete", dot="different"),
        ]):
            with self.assertRaisesRegex(AssertionError,
                                        "adaptive trees differ"):
                decomp.run_backend(backend, False, game, ROOT, BUILD_DIR,
                                   1, 100)

    @unittest.skipUnless(all((BUILD_DIR / name).is_file()
                             for name in ("pg2adot", "pg2pmdot")),
                         "build the CLI tools to run the integration check")
    def test_determinism_and_stale_files(self):
        with (tempfile.TemporaryDirectory() as directory,
              redirect_stdout(io.StringIO())):
            root = Path(directory) / "repo"
            (root / "examples").mkdir(parents=True)
            (root / "scripts").mkdir()
            shutil.copyfile(ROOT / "examples/Button.tlsf.ehoa.pg",
                            root / "examples/small.gm")
            shutil.copyfile(ROOT / "tests/games/shave_single.pg",
                            root / "examples/all-shaved.pg")
            shutil.copyfile(ROOT / "scripts/decomp_methods.md",
                            root / "scripts/decomp_methods.md")
            outputs = [Path(directory) / name for name in ("one", "two")]
            for output in outputs:
                output.mkdir()
                decomp.generate(root, output, BUILD_DIR, 5, 10_000)
            self.assertEqual(decomp.output_files(outputs[0]),
                             decomp.output_files(outputs[1]))
            self.assertEqual(len(list(outputs[0].rglob("*.dot"))), 28)
            self.assertEqual(len(list(outputs[0].rglob("*.leaves"))), 8)
            for dot in (outputs[0] / "decomp/all-shaved").glob("*+pre.dot"):
                info = decomp.tree_info(dot.read_text(),
                                        dot.name.startswith("pm-"))
                self.assertEqual(info, [((0, 0, 0, 0), ())] * 2)
            self.assertTrue(decomp.sync_outputs(root, outputs[0], True))
            decomp.sync_outputs(root, outputs[0], False)
            self.assertFalse(decomp.sync_outputs(root, outputs[1], True))
            stale = root / "decomp/small/obsolete.dot"
            stale.write_text("old")
            (root / "DECOMP.md").write_text("stale inventory")
            (root / "decomp/small/lifting.dot").unlink()
            before = decomp.output_files(root)
            report = io.StringIO()
            with redirect_stdout(report):
                self.assertTrue(decomp.sync_outputs(root, outputs[1], True))
            for name in ("DECOMP.md", "obsolete.dot", "lifting.dot"):
                self.assertIn(name, report.getvalue())
            self.assertEqual(before, decomp.output_files(root))
            decomp.sync_outputs(root, outputs[1], False)
            self.assertFalse(decomp.sync_outputs(root, outputs[1], True))


if __name__ == "__main__":
    unittest.main()
