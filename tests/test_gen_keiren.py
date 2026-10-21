#!/usr/bin/env python3
"""Offline checks for range downloads, bounded runs, resume and static reports."""

import argparse
import bz2
from contextlib import contextmanager, redirect_stderr
import csv
import io
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import urllib.error
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import gen_keiren as keiren  # noqa: E402

BUILD_DIR = (Path(sys.argv.pop(1)).resolve()
             if len(sys.argv) > 1 and not sys.argv[1].startswith("-")
             else ROOT / "build")
GAME = b"parity 1;\n0 0 0 0;\n1 1 1 1;\n"


class LocalResponse(io.BytesIO):
    status = 206

    def __init__(self, data, start, end):
        super().__init__(data[start:end + 1])
        self.headers = {"Content-Range": f"bytes {start}-{end}/{len(data)}"}

    def geturl(self):
        return "https://signed.example/archive.zip"


class KeirenTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.work = Path(temporary.name)
        self.game = self.work / "input.gm"
        self.game.write_bytes(GAME)

    def local_zip(self):
        path = self.work / "local.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("mlsolver/games/b.gm.bz2", bz2.compress(GAME))
            archive.writestr("mlsolver/games/a.gm.bz2", bz2.compress(GAME))
            archive.writestr("__MACOSX/mlsolver/games/hidden.gm.bz2", b"skip")
            archive.writestr("mlsolver/.DS_Store", b"skip")
            archive.writestr("mlsolver/games/data.yaml", b"skip")
        return path

    def test_range_listing_extraction_and_expired_redirect(self):
        data = self.local_zip().read_bytes()
        requests = []
        expired = False
        def local_open(request, timeout):
            nonlocal expired
            requests.append(request.full_url)
            if request.full_url.startswith("https://signed") and not expired:
                expired = True
                raise urllib.error.HTTPError(request.full_url, 403, "expired", {}, io.BytesIO())
            span = request.get_header("Range").removeprefix("bytes=")
            start, end = map(int, span.split("-"))
            return LocalResponse(data, start, end)
        with patch.object(keiren.urllib.request, "urlopen", side_effect=local_open), patch.object(keiren.time, "sleep"):
            with keiren.remote_zip(10792904) as archive:
                members = keiren.game_members(archive)
                self.assertEqual([entry.filename for entry in members],
                    ["mlsolver/games/a.gm.bz2", "mlsolver/games/b.gm.bz2"])
                keiren.extract_game(archive, members[0], self.work / "extracted.gm")
            self.assertEqual((self.work / "extracted.gm").read_bytes(), GAME)
        self.assertTrue(expired)
        self.assertGreaterEqual(requests.count(keiren.download_url(10792904)), 2)

    def test_full_response_is_rejected_without_reading(self):
        def full_response(*args, **kwargs):
            response = LocalResponse(b"too big", 0, 0)
            response.status = 200
            response.read = lambda *args: self.fail("full archive was read")
            return response
        with patch.object(keiren.urllib.request, "urlopen", side_effect=full_response), patch.object(keiren.time, "sleep"):
            with self.assertRaisesRegex(OSError, "range"):
                keiren.RangeReader("https://example/archive.zip")

    def process(self, code, *, timeout=3, memory=256 * 1024 ** 2):
        result = keiren.execute([sys.executable, "-c", code], self.game,
                                self.work / "out", self.work / "err",
                                time.monotonic() + timeout, memory)
        return result, keiren.classify(result, (self.work / "err").read_text(), memory)

    def test_process_failures_and_individual_rss(self):
        for code, expected, detail in (
            ("import time; time.sleep(10)", "timeout", "deadline"),
            ("import os,signal; os.kill(os.getpid(),signal.SIGSEGV)", "crash", "SIGSEGV"),
            ("import sys; print('broken',file=sys.stderr); sys.exit(7)", "error", "exit 7: broken"),
            ("import sys; print('1:2: bad vertex',file=sys.stderr); sys.exit(3)", "invalid input", "bad vertex"),
            ("import sys; print('more than the limit of 100',file=sys.stderr); sys.exit(4)", "host limit", "100"),
            ("import sys; print('result=partial',file=sys.stderr)", "partial", ""),
            ("import sys; print('result=complete',file=sys.stderr)", "complete", ""),
        ):
            with self.subTest(expected=expected):
                result, (outcome, message) = self.process(code, timeout=0.15 if expected == "timeout" else 3)
                self.assertEqual(outcome, expected)
                self.assertIn(detail, message)
                self.assertGreater(result.peak_rss_mib, 0)
        big, _ = self.process("x=bytearray(80*1024*1024)")
        small, _ = self.process("pass")
        self.assertGreater(big.peak_rss_mib, small.peak_rss_mib + 40)
        memory = 256 * 1024 ** 2
        for diagnostic in ("ENOMEM", "std::bad_alloc", "Out of memory",
                           "out-of-memory", "Cannot allocate memory",
                           "failed to allocate a buffer", "allocation failed"):
            with self.subTest(diagnostic=diagnostic):
                self.assertEqual(keiren.classify(keiren.ProcessResult(3, 1),
                    diagnostic, memory)[0], "out of memory")
        for sig in (signal.SIGKILL, signal.SIGABRT, signal.SIGSEGV):
            for rss, address in ((256, 0), (1, memory)):
                with self.subTest(sig=sig, rss=rss):
                    result = keiren.ProcessResult(-sig, rss, address)
                    self.assertEqual(keiren.classify(result, "", memory)[0], "out of memory")
            self.assertEqual(keiren.classify(keiren.ProcessResult(-sig, 1),
                "", memory)[0], "crash")
        self.assertEqual(keiren.classify(keiren.ProcessResult(-signal.SIGTERM, 256),
            "", memory)[0], "crash")
        self.assertEqual(keiren.classify(keiren.ProcessResult(-signal.SIGKILL, 256,
            timed_out=True), "out of memory", memory)[0], "timeout")

    @unittest.skipIf(sys.platform == "darwin", "macOS does not enforce RLIMIT_AS")
    def test_memory_limit(self):
        _, (outcome, _) = self.process("x=bytearray(512*1024*1024)")
        self.assertEqual(outcome, "out of memory")

    @unittest.skipIf(sys.platform == "darwin" or os.environ.get("ASAN_OPTIONS"),
                     "requires a small enforced address-space cap without ASan")
    @unittest.skipUnless(all((BUILD_DIR / name).is_file() for name in ("pg2adot", "pg2pmdot")), "build the solvers")
    def test_input_buffer_memory_failure(self):
        game = b"parity 0;\n0 0 0 0;\n"
        self.game.write_bytes(game + b" " * (8_388_606 - len(game)))
        memory = 12 * 1024 ** 2
        for binary in ("pg2adot", "pg2pmdot"):
            with self.subTest(binary=binary):
                result = keiren.execute([BUILD_DIR / binary, "--stats"], self.game,
                    self.work / "out", self.work / "err", time.monotonic() + 5, memory)
                diagnostic = (self.work / "err").read_text()
                self.assertGreater(result.code, 0, diagnostic)
                self.assertIn("failed to allocate the input buffer", diagnostic)
                self.assertEqual(keiren.classify(result, diagnostic, memory)[0], "out of memory")

    @unittest.skipUnless((BUILD_DIR / "pg2adot").is_file(), "build the solver")
    def test_default_host_limit(self):
        with patch.object(sys, "argv", [keiren.SCRIPT, "run", "--results",
                str(self.work / "results.csv"), "--work-dir", str(self.work),
                "--build-dir", str(BUILD_DIR)]), patch.object(keiren, "run", return_value=0) as run:
            self.assertEqual(keiren.main(), 0)
        limit = run.call_args.args[0].max_host_leaves
        self.assertEqual(limit, 2 * sys.maxsize + 1)
        for value, status in ((limit, 0), (limit + 1, 2)):
            result = subprocess.run([str(BUILD_DIR / "pg2adot"),
                f"--max-host-leaves={value}"], input=GAME, capture_output=True)
            self.assertEqual(result.returncode, status, result.stderr)

    @unittest.skipIf(sys.platform == "darwin" or os.environ.get("ASAN_OPTIONS"),
                     "requires a small enforced address-space cap without ASan")
    @unittest.skipUnless((BUILD_DIR / "pg2adot").is_file(), "build the solver")
    def test_saturated_host_uses_memory_budget(self):
        self.game.write_text("parity 1024;\n" + "".join(
            f"{v} {v} {v % 2} {v};\n" for v in range(1025)))
        memory = 12 * 1024 ** 2
        for algorithm in ("lifting", "lifting-sym"):
            with self.subTest(algorithm=algorithm):
                result = keiren.execute([BUILD_DIR / "pg2adot", f"--algorithm={algorithm}",
                    f"--max-host-leaves={keiren.MAX_HOST_LEAVES}"], self.game,
                    self.work / "out", self.work / "err", time.monotonic() + 5, memory)
                diagnostic = (self.work / "err").read_text()
                self.assertGreater(result.code, 0, diagnostic)
                self.assertIn("Failed to allocate memory", diagnostic)
                self.assertNotIn("more than the limit", diagnostic)
                self.assertEqual(keiren.classify(result, diagnostic, memory)[0], "out of memory")

    @unittest.skipUnless(all((BUILD_DIR / b.binary).is_file() for b in keiren.decomp.BACKENDS), "build the solvers")
    def test_all_backends_keep_only_metrics(self):
        args = self.args(self.work / "unused.csv")
        with keiren.ThreadPoolExecutor(max_workers=3) as pool:
            rows = list(pool.map(lambda backend: keiren.run_one(
                backend, self.game, [2, 2, 2, 1], args), keiren.decomp.BACKENDS))
        self.assertEqual(len(rows), 24)
        for row in rows:
            self.assertEqual(row["outcome"], "complete", row)
            self.assertEqual((row["won_even"], row["won_odd"]), (1, 1))
            self.assertEqual(row["start_winner"], "even", row)
            self.assertNotIn("tree", row)
        self.assertEqual(list(self.work.iterdir()), [self.game])

    @unittest.skipUnless(all((BUILD_DIR / name).is_file() for name in ("pg2adot", "pg2pmdot")), "build the solvers")
    def test_start_statistics(self):
        commands = [("pg2adot", [f"--algorithm={name}"]) for name in
                    ("lifting", "lifting-sym", "zielonka", "zielonka-sym")]
        commands += [("pg2pmdot", [f"--algorithm={name}"]) for name in ("strahler", "succinct")]
        sparse = "20 0 0 20;\n3 0 0 3;\n20 101 1 20;\n"
        for binary, options in commands:
            for directive, vertex, winner in (("", 0, "unresolved"), ("start 20;\n", 20, "odd"),
                                               ("start 3;\n", 3, "even"), ("start 999;\n", 999, "unresolved")):
                for preprocess in ([], ["--compress", "--priority-mode=compact"],
                                   ["--initial-shave=all", "--compress"]):
                    with self.subTest(binary=binary, options=options, vertex=vertex, preprocess=preprocess):
                        result = subprocess.run([str(BUILD_DIR / binary), *options, *preprocess,
                            "--player=even", "--stats"], input=directive + sparse,
                            text=True, capture_output=True, check=True)
                        self.assertEqual(re.findall(r"^start:.*$", result.stderr, re.MULTILINE),
                                         [f"start: vertex={vertex} winner={winner}"])
        # Vertex 4 is attracted in the first round and absent from the final regions.
        game = (ROOT / "tests/games/strahler_two.pg").read_text()
        for binary, options in (("pg2adot", ["--tree-k=1"]),
                                ("pg2adot", ["--algorithm=lifting-sym", "--tree-k=1"]),
                                ("pg2pmdot", ["--k=1", "--t=1"]),
                                ("pg2pmdot", ["--algorithm=succinct", "--bits=0"])):
            for start, incremental, winner in ((1, False, "unresolved"), (0, False, "even"),
                                               (4, True, "even"), (1, True, "even")):
                with self.subTest(binary=binary, options=options, start=start, incremental=incremental):
                    # Fixed PM parameters stop after one round; use parameter search for iter-shave.
                    flags = ([flag for flag in options if flag.startswith("--algorithm=")] if
                             incremental and binary == "pg2pmdot" else options)
                    result = subprocess.run([str(BUILD_DIR / binary), *flags, "--stats",
                        *(["--iter-shave", "--compress"] if incremental else [])],
                        input=game.replace("parity 4;", f"parity 4;\nstart {start};"),
                        text=True, capture_output=True, check=True)
                    self.assertIn(f"start: vertex={start} winner={winner}\n", result.stderr)
                    if incremental and "--algorithm=succinct" not in options:
                        self.assertRegex(result.stderr, r"(?:round=2|rounds=2)")
        result = subprocess.run([str(BUILD_DIR / "pg2pmdot"), "--algorithm=succinct",
            "--iter-shave", "--stats"], text=True, capture_output=True, check=True,
            input=(ROOT / "tests/games/thesis_f4.pg").read_text().replace(
                "parity 19;", "parity 19;\nstart 13;"))
        self.assertIn("succinct: round=2 result=complete", result.stderr)
        self.assertIn("start: vertex=13 winner=odd\n", result.stderr)

    def args(self, path):
        # ASan reserves terabytes of virtual address space before a solver starts.
        memory = 256 * 1024 if os.environ.get("ASAN_OPTIONS") else 2
        return argparse.Namespace(results=path, work_dir=self.work / "scratch", archives=["mlsolver"],
            backends=[keiren.decomp.BACKENDS[-2]], build_dir=BUILD_DIR, timeout=30,
            memory=memory, jobs=3, max_host_leaves=keiren.MAX_HOST_LEAVES, max_games=1)

    @unittest.skipUnless((BUILD_DIR / "pg2adot").is_file(), "build the solver")
    def test_real_run_resume_and_deleted_games(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        metadata = self.work / "metadata.yaml"
        metadata.write_text("- case: fixture\n  instances:\n  - compact: 'False'\n    files:\n      orig: cases/mlsolver/data/a.yaml\n    solutions:\n      orig:\n        pbespgsolve: 'true'\n")
        args = self.args(self.work / "results.csv")
        with patch.object(keiren, "remote_zip", archive), patch.object(keiren, "download_metadata", return_value=metadata), redirect_stderr(io.StringIO()):
            self.assertEqual(keiren.run(args), 0)
            rows = keiren.load_results(args.results)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["outcome"], "complete")
            self.assertEqual((rows[0]["won_even"], rows[0]["won_odd"]), ("1", "1"))
            self.assertEqual(rows[0]["reference_solution"], "true")
            self.assertEqual(rows[0]["start_winner"], "even")
            self.assertEqual(rows[0]["reference_agrees"], "true")
            self.assertGreater(float(rows[0]["peak_rss_mib"]), 0)
            self.assertFalse(list(args.work_dir.rglob("*.gm")))
            # A pilot limit counts newly attempted games; the first is skipped on restart.
            self.assertEqual(keiren.run(args), 0)
            self.assertEqual(len(keiren.load_results(args.results)), 2)
            with patch.object(keiren, "extract_game") as extract:
                self.assertEqual(keiren.run(args), 0)
                extract.assert_not_called()
        with args.results.open() as stream:
            self.assertEqual(csv.DictReader(stream).fieldnames, keiren.FIELDS)
        output = self.work / "KEIREN.md"
        with patch.object(keiren.urllib.request, "urlopen", side_effect=AssertionError("offline")):
            keiren.render(args.results, output)
        self.assertIn("1 / 1", output.read_text())

    def test_download_failure_then_resume(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        with patch.object(keiren, "remote_zip", archive), patch.object(keiren, "download_metadata", side_effect=OSError("offline")), redirect_stderr(io.StringIO()):
            with patch.object(keiren, "extract_game", side_effect=OSError("disk full")):
                self.assertEqual(keiren.run(args), 1)
            self.assertEqual(keiren.load_results(args.results)[0]["outcome"], "download failed")
            with patch.object(keiren, "capped_json", return_value=([2, 2, 2, 1], "complete", "", 1)), patch.object(keiren, "run_one", return_value={"backend": args.backends[0].name, "outcome": "timeout"}):
                self.assertEqual(keiren.run(args), 0)
            self.assertEqual([row["outcome"] for row in keiren.load_results(args.results)], ["timeout"])
        with patch.object(keiren, "remote_zip", side_effect=OSError("offline")), patch.object(keiren, "download_metadata", side_effect=OSError("offline")), redirect_stderr(io.StringIO()):
            self.assertEqual(keiren.run(args), 1)
        rows = keiren.load_results(args.results)
        self.assertEqual(rows[-1]["game"], "(archive listing)")
        self.assertEqual(rows[-1]["backend"], "")
        keiren.save_results(args.results, [rows[-1], *[
            dict(archive="mlsolver", game=f"mlsolver/games/{name}.gm",
                 backend=args.backends[0].name, outcome="timeout") for name in ("a", "b")]])
        with patch.object(keiren, "remote_zip", archive), patch.object(keiren, "download_metadata", side_effect=OSError("offline")), patch.object(keiren, "extract_game") as extract, redirect_stderr(io.StringIO()):
            self.assertEqual(keiren.run(args), 0)
            extract.assert_not_called()
        self.assertEqual(len(keiren.load_results(args.results)), 2)

    def test_metrics_share_the_backend_deadline(self):
        args = self.args(self.work / "unused.csv")
        args.timeout = 0.25
        calls = []
        def execute(command, game, out, err, deadline, memory):
            calls.append(deadline)
            err.write_text("result=complete\n")
            out.write_text("{}")
            time.sleep(0.14)
            return keiren.ProcessResult(0, 3)
        with patch.object(keiren, "execute", side_effect=execute):
            row = keiren.run_one(args.backends[0], self.game, [2, 2, 2, 1], args)
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0], calls[1])
        self.assertEqual(row["outcome"], "timeout")
        # A failed parser must remain a row, with its own failure classification.
        with patch.object(keiren, "execute", side_effect=execute), patch.object(keiren, "capped_json", return_value=(None, "out of memory", "MemoryError", 30)):
            row = keiren.run_one(args.backends[0], self.game, None, args)
        self.assertEqual(row["outcome"], "out of memory")
        self.assertEqual(row["peak_rss_mib"], "30.000")
        self.game.write_text("parity 1;\nbad record;\n")
        _, outcome, detail, _ = keiren.capped_json("_game_info", [self.game],
            self.game, self.work, time.monotonic() + 3, 256 * 1024 ** 2)
        self.assertEqual(outcome, "error")
        self.assertIn("ValueError: invalid PGSolver vertex record", detail)

    def test_atomic_results_and_reference_mapping(self):
        path = self.work / "results.csv"
        keiren.save_results(path, [])
        old = path.read_bytes()
        with patch.object(keiren.os, "fsync", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                keiren.save_results(path, [{"game": "never published"}])
        self.assertEqual(path.read_bytes(), old)
        self.assertEqual(path.stat().st_mode & 0o777, 0o644)
        self.assertFalse(list(self.work.glob(".results-*")))
        source = self.work / "data.yaml"
        source.write_text("- files:\n    orig: games/a.gm\n    reduced: games/other.gm\n  solutions:\n    orig:\n      pbespgsolve: 'true'\n      pgsolver: 'false'\n- files:\n    orig: games/b.gm.bz2\n  solutions:\n    orig:\n      pbespgsolve: 'false'\n")
        self.assertEqual(keiren.reference_solutions(source), {"games/b.gm": "false"})
        references = {"/old/root/mlsolver/games/a.gm": "true", "pgsolver/games/a.gm": "false"}
        self.assertEqual(keiren.reference_for_game(references, "mlsolver/games/a.gm"), "true")
        self.assertEqual(keiren.reference_for_game(references, "pgsolver/games/a.gm"), "false")
        self.assertEqual(keiren.reference_for_game(references, "unknown/games/a.gm"), "")
        source.write_text("- case: nested\n  properties:\n  - files:\n      orig: cases/modelchecking/data/deadlock.yaml\n    solutions:\n      orig:\n        pbespgsolve: 'true'\n  - files:\n      orig: cases/modelchecking/data/liveness.yaml\n    solutions:\n      orig:\n        pbespgsolve: 'false'\n")
        self.assertEqual(keiren.reference_solutions(source), {
            "modelchecking/games/deadlock.gm": "true",
            "modelchecking/games/liveness.gm": "false"})

    def test_reference_agreement_and_start_cross_check(self):
        for reference in ("true", "false", ""):
            for winner in ("even", "odd", "unresolved", ""):
                for outcome in ("complete", "partial"):
                    row = dict(outcome=outcome, reference_solution=reference, start_winner=winner)
                    keiren.flag_winners([row])
                    expected = (str((reference == "true") == (winner == "even")).lower()
                                if reference and winner in ("even", "odd") else "")
                    self.assertEqual(row["reference_agrees"], expected, row)
        rows = [dict(outcome="complete", won_even=1, won_odd=1, start_winner=p)
                for p in ("even", "odd")]
        keiren.flag_winners(rows)
        self.assertEqual([row["winner_disagrees"] for row in rows], ["true", "true"])
        rows[1]["outcome"] = "partial"
        keiren.flag_winners(rows)
        self.assertEqual([row["winner_disagrees"] for row in rows], ["false", ""])

    def test_old_csv_renders_but_cannot_resume(self):
        results = self.work / "old.csv"
        with results.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=[f for f in keiren.FIELDS if f != "start_winner"])
            writer.writeheader()
            writer.writerow(dict(archive="mlsolver", game="games/old.gm", backend="zielonka",
                                 outcome="complete", reference_solution="true"))
        original = results.read_bytes()
        with patch.object(keiren, "download_metadata") as download:
            with self.assertRaisesRegex(ValueError, "lacks start_winner.*delete or migrate"):
                keiren.run(self.args(results))
            download.assert_not_called()
        output = self.work / "KEIREN.md"
        keiren.render(results, output)
        self.assertIn("Older pilot rows", output.read_text())
        self.assertNotIn("REFERENCE MISMATCH", output.read_text())
        self.assertEqual(results.read_bytes(), original)

    def test_render_all_metrics_checks_and_pagination(self):
        rows = []
        for game in range(30):
            for backend, won in (("zielonka", 2), ("lifting", 1)):
                row = dict(archive="mlsolver", game=f"games/{game}.gm", backend=backend,
                    outcome="complete", won_even=won, won_odd=2-won, vertices=2, edges=3,
                    reference_solution="true", start_winner="odd" if backend == "lifting" else "even",
                    detail="pipe | <test>", timeout_seconds=30, memory_gib=2, jobs=3,
                    max_host_leaves=10000, machine="offline fixture")
                for metric in keiren.decomp.TREE_METRICS:
                    row[metric + "_even"] = 1
                    row[metric + "_odd"] = 0
                rows.append(row)
        results = self.work / "results.csv"
        keiren.save_results(results, rows)
        output = self.work / "KEIREN.md"
        with patch.object(keiren.urllib.request, "urlopen", side_effect=AssertionError("network")), patch.object(keiren.subprocess, "Popen", side_effect=AssertionError("solver")):
            keiren.render(results, output)
        report = output.read_text()
        self.assertTrue(report.startswith("# Keiren benchmark metrics\n\nSource: [Parity games]"))
        for metric in keiren.decomp.TREE_METRICS:
            self.assertIn(metric, report)
        self.assertIn("winner counts or start winners disagree", report)
        self.assertIn("reference mismatch", report)
        self.assertIn("pipe \\| &lt;test&gt;", report)
        self.assertEqual(report.count("<details>\n"), 30)
        self.assertNotIn("<details open", report)
        self.assertIn("<summary>games/0.gm · 2 vertices / 3 edges · 2 complete · WINNER DISAGREEMENT · REFERENCE MISMATCH</summary>\n\n", report)
        self.assertEqual(report.count("\n\n</details>\n"), 30)
        self.assertLess(report.index("## Winner checks"), report.index("<details>"))
        self.assertLess(report.index("## Summary"), report.index("<details>"))
        keiren.render(results, output, page_limit=22_000)
        pages = list((self.work / "keiren").glob("*.md"))
        self.assertGreater(len(pages), 1)
        self.assertLess(output.stat().st_size, 22_000)
        self.assertTrue(all(page.stat().st_size < 22_000 for page in pages))
        self.assertEqual(sum(page.read_text().count("<details>\n<summary>games/") for page in pages), 30)
        self.assertIn("| mlsolver | 30 | 30 |", output.read_text())
        for page in pages:
            text = page.read_text()
            winners, details = text.split("## Inventory\n\n", 1)
            games = re.findall(r"<summary>(games/\d+\.gm)", details)
            self.assertNotIn("<details>", winners)
            self.assertIn(f"(keiren/{page.name})", output.read_text())
            for game in games:
                self.assertIn(f"| mlsolver | {game} | winner counts or start winners disagree |", winners)
                self.assertIn(f"| mlsolver | {game} | reference mismatch |", winners)
            self.assertEqual(winners.count("| winner counts or start winners disagree |"), len(games))
            self.assertEqual(winners.count("| reference mismatch |"), len(games))

        # Force the full check list alone beyond the limit, across archives.
        large = [dict(row, archive=archive, game=row["game"].replace(".gm", "é" * 100 + ".gm"))
                 for archive in ("mlsolver", "pgsolver") for row in rows]
        keiren.save_results(results, large)
        keiren.render(results, output, page_limit=22_000)
        pages = list((self.work / "keiren").glob("*.md"))
        self.assertLessEqual(output.stat().st_size, 22_000)
        self.assertEqual(sum(page.read_text().split("## Inventory\n\n")[0].count(
            "| reference mismatch |") for page in pages), 60)
        for archive in ("mlsolver", "pgsolver"):
            self.assertIn(f"| {archive} | 30 | 30 |", output.read_text())
        self.assertTrue(all(page.stat().st_size <= 22_000 for page in pages))
        keiren.save_results(results, [dict(rows[0], detail="x" * 22_000)])
        with self.assertRaisesRegex(ValueError, "one game's report exceeds the page limit"):
            keiren.render(results, output, page_limit=22_000)
        keiren.save_results(results, rows[:1])
        keiren.render(results, output)
        self.assertFalse(list((self.work / "keiren").glob("*.md")))


if __name__ == "__main__":
    unittest.main()
