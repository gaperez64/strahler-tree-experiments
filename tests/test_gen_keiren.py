#!/usr/bin/env python3
"""Offline checks for range downloads, bounded runs, resume and static reports."""

import argparse
import bz2
from contextlib import contextmanager, redirect_stderr
import csv
import io
import json
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


def build_uses_sanitizer(build_dir):
    try:
        result = subprocess.run(["meson", "introspect", "--buildoptions", build_dir],
                                check=True, capture_output=True, text=True, timeout=10)
        value = next(option["value"] for option in json.loads(result.stdout)
                     if option["name"] == "b_sanitize")
        return bool(value) and value != "none"
    except (OSError, subprocess.SubprocessError, ValueError, StopIteration):
        for name in ("pg2adot", "pg2pmdot"):
            try:
                if b"__asan_" in (build_dir / name).read_bytes():
                    return True
            except OSError:
                pass
        return False


SANITIZED_BUILD = build_uses_sanitizer(BUILD_DIR)


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

    def test_corrupt_zip64_offsets_on_both_sides_of_4gib(self):
        path = self.work / "wrapped.zip"
        wrap = 1 << 32
        names = ["games/a.gm.bz2", "games/b.gm.bz2"]
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(names[0], bz2.compress(GAME))
            # A sparse gap covers k=1 without allocating or reading 4 GiB.
            archive.start_dir = archive.fp.seek(wrap)
            archive.writestr(names[1], bz2.compress(GAME))
            for member in archive.infolist():
                member.header_offset += wrap
        with zipfile.ZipFile(path) as archive:
            self.assertEqual([member.header_offset for member in archive.infolist()], [wrap, 2 * wrap])
            for member in archive.infolist():
                original_offset = member.header_offset
                keiren.extract_game(archive, member, self.work / "extracted.gm")
                self.assertEqual((self.work / "extracted.gm").read_bytes(), GAME)
                self.assertEqual(member.header_offset, original_offset)
            # Signatures alone must not select the other member at the wrapped offset.
            missing = zipfile.ZipInfo("games/missing.gm.bz2")
            missing.header_offset = wrap
            with self.assertRaisesRegex(zipfile.BadZipFile, "no matching local header"):
                keiren.open_member(archive, missing)

    def test_corrupt_offset_with_data_descriptor_and_crc_check(self):
        class Unseekable(io.BytesIO):
            def seek(self, *args):
                raise OSError("unseekable")
        stream = Unseekable()
        name = "games/é.gm.bz2"
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(name, bz2.compress(GAME))
            archive.getinfo(name).header_offset += 1 << 32
        with zipfile.ZipFile(io.BytesIO(stream.getvalue())) as archive:
            member = archive.getinfo(name)
            self.assertTrue(member.flag_bits & 8)
            keiren.extract_game(archive, member, self.work / "extracted.gm")
            self.assertEqual((self.work / "extracted.gm").read_bytes(), GAME)
            member.CRC ^= 1
            with patch.object(keiren.time, "sleep"), self.assertRaisesRegex(zipfile.BadZipFile, "CRC"):
                keiren.extract_game(archive, member, self.work / "extracted.gm")
            self.assertFalse((self.work / "extracted.gm").exists())

    def test_recovered_member_can_extend_past_broken_start_dir_with_crc_check(self):
        stream = io.BytesIO()
        name, content = "games/a.gm.bz2", bz2.compress(GAME)
        with zipfile.ZipFile(stream, "w") as archive:
            archive.writestr(name, content)
            archive.getinfo(name).header_offset += 1 << 32
        data = bytearray(stream.getvalue())
        data_offset = 30 + len(name)
        for corrupt in (False, True):
            with self.subTest(corrupt=corrupt):
                if corrupt:
                    data[data_offset + len(content) - 1] ^= 1
                with zipfile.ZipFile(io.BytesIO(data)) as archive:
                    member = archive.getinfo(name)
                    archive.start_dir = data_offset + 1
                    with keiren.open_member(archive, member) as source:
                        if corrupt:
                            with self.assertRaisesRegex(zipfile.BadZipFile, "CRC"):
                                source.read()
                        else:
                            self.assertEqual(source.read(), content)
                    self.assertEqual(member.header_offset, 1 << 32)

    def test_unchanged_offset_with_wrapped_next_boundary_keeps_crc_check(self):
        stream = io.BytesIO()
        name = "games/a.gm.bz2"
        with zipfile.ZipFile(stream, "w") as archive:
            archive.writestr(name, bz2.compress(GAME))
            archive.writestr("games/b.gm.bz2", bz2.compress(GAME))
            archive.infolist()[1].header_offset = 50
        for corrupt in (False, True):
            with self.subTest(corrupt=corrupt), zipfile.ZipFile(io.BytesIO(stream.getvalue())) as archive:
                member = archive.getinfo(name)
                self.assertEqual((member.header_offset, member._end_offset), (0, 50))
                if corrupt:
                    member.CRC ^= 1
                    with patch.object(keiren.time, "sleep"), self.assertRaisesRegex(zipfile.BadZipFile, "CRC"):
                        keiren.extract_game(archive, member, self.game)
                    self.assertFalse(self.game.exists())
                else:
                    keiren.extract_game(archive, member, self.game)
                    self.assertEqual(self.game.read_bytes(), GAME)
                self.assertEqual((member.header_offset, member._end_offset), (0, 50))

    def test_zip_without_metadata_encoding_attribute(self):
        with zipfile.ZipFile(self.local_zip()) as archive:
            member = keiren.game_members(archive)[0]
            self.assertFalse(member.flag_bits & 0x800)
            # Python 3.10's ZipFile has no metadata_encoding attribute.
            legacy = argparse.Namespace(fp=archive.fp, open=archive.open)
            keiren.extract_game(legacy, member, self.game)
            self.assertEqual(self.game.read_bytes(), GAME)

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
        # A forked child can inherit the test process's RSS peak before exec.
        baseline, _ = self.process("pass")
        allocation = int(baseline.peak_rss_mib) + 80
        big, _ = self.process(f"x=bytearray({allocation}*1024*1024)",
                              memory=(allocation + 128) * 1024 ** 2)
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

    def test_failure_detail_skips_preprocessing_and_trailing_statistics(self):
        for code, diagnostic, outcome in (
            (4, "Solver failed: priority depth exceeds the safe recursion depth", "error"),
            (4, "Error: errno=12", "error"),
            (4, "std::bad_alloc\ncleanup finished", "out of memory"),
            (3, "1:1: failed to allocate the input buffer", "out of memory"),
            (3, "89:1: unexpected keyword", "invalid input"),
            (4, "more than the limit of 100", "host limit"),
        ):
            with self.subTest(diagnostic=diagnostic):
                stderr = ("preprocess: residual=3001 shaved_even=0\n"
                          "earlier message\n" + diagnostic + "\n"
                          "lifting even: region=0 tree_nodes=0\n")
                actual, detail = keiren.classify(keiren.ProcessResult(code, 1), stderr, 1 << 30)
                self.assertEqual(actual, outcome)
                self.assertIn(diagnostic.splitlines()[0], detail)
                self.assertNotIn("preprocess", detail)

    def test_sanitizer_detection_uses_build_options_then_binary_symbols(self):
        for value in ("none", [], "address,undefined", ["address", "undefined"], "undefined"):
            result = subprocess.CompletedProcess([], 0, json.dumps([
                dict(name="b_sanitize", value=value)]))
            with (self.subTest(value=value), patch.dict(os.environ, ASAN_OPTIONS="halt_on_error=1"),
                  patch.object(subprocess, "run", return_value=result)):
                self.assertEqual(build_uses_sanitizer(self.work), bool(value) and value != "none")
        for error in (FileNotFoundError(), subprocess.CalledProcessError(1, "meson"),
                      ValueError("invalid JSON")):
            with patch.object(subprocess, "run", side_effect=error):
                for binary in ("pg2adot", "pg2pmdot"):
                    path = self.work / binary
                    path.write_bytes(b"plain binary")
                    self.assertFalse(build_uses_sanitizer(self.work))
                    path.write_bytes(b"binary __asan_init symbol")
                    self.assertTrue(build_uses_sanitizer(self.work))
                    path.unlink()
                self.assertFalse(build_uses_sanitizer(self.work))

    @unittest.skipIf(sys.platform == "darwin" or SANITIZED_BUILD,
                     "requires a small enforced address-space cap without sanitizers")
    @unittest.skipUnless(all((BUILD_DIR / name).is_file() for name in ("pg2adot", "pg2pmdot")), "build the solvers")
    def test_padded_input_under_memory_cap(self):
        game = b"parity 0;\n0 0 0 0;\n"
        self.game.write_bytes(game + b" " * (8_388_606 - len(game)))
        memory = 12 * 1024 ** 2
        for binary in ("pg2adot", "pg2pmdot"):
            with self.subTest(binary=binary):
                result = keiren.execute([BUILD_DIR / binary, "--stats"], self.game,
                    self.work / "out", self.work / "err", time.monotonic() + 5, memory)
                diagnostic = (self.work / "err").read_text()
                self.assertEqual(result.code, 0, diagnostic)
                self.assertIn("result=complete", diagnostic)
                self.assertIn("start: vertex=0 winner=even", diagnostic)
                self.assertEqual(keiren.classify(result, diagnostic, memory)[0], "complete")

    @unittest.skipIf(sys.platform == "darwin" or SANITIZED_BUILD,
                     "requires a small enforced address-space cap without sanitizers")
    @unittest.skipUnless(all((BUILD_DIR / name).is_file() for name in ("pg2adot", "pg2pmdot")), "build the solvers")
    def test_graph_allocation_memory_failure(self):
        with self.game.open("w") as stream:
            stream.write("parity 99999;\n")
            stream.writelines(f"{vertex} 0 0 {vertex};\n" for vertex in range(100_000))
        memory = 12 * 1024 ** 2
        for binary in ("pg2adot", "pg2pmdot"):
            with self.subTest(binary=binary):
                result = keiren.execute([BUILD_DIR / binary, "--stats"], self.game,
                    self.work / "out", self.work / "err", time.monotonic() + 5, memory)
                diagnostic = (self.work / "err").read_text()
                self.assertGreater(result.code, 0, diagnostic)
                self.assertEqual(keiren.classify(result, diagnostic, memory)[0], "out of memory")
                self.assertNotIn("result=complete", diagnostic)
                self.assertNotRegex(diagnostic, r"winner=(even|odd)")

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

    @unittest.skipIf(sys.platform == "darwin" or SANITIZED_BUILD,
                     "requires a small enforced address-space cap without sanitizers")
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
        memory = 256 * 1024 if SANITIZED_BUILD else 2
        return argparse.Namespace(results=path, work_dir=self.work / "scratch", archives=["mlsolver"],
            backends=[keiren.decomp.BACKENDS[-2]], build_dir=BUILD_DIR, timeout=30, metadata_timeout=600,
            memory=memory, jobs=3, max_host_leaves=keiren.MAX_HOST_LEAVES, max_games=1,
            games=re.compile(""), retry=[], refresh_metadata=False, backfill_build=None)

    def test_games_filter_uses_search_on_saved_member_path(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        for pattern, expected in ((r"games/b\.gm$", ["mlsolver/games/b.gm"]),
                                  (r"^mlsolver/games/b\.gm$", ["mlsolver/games/b.gm"]),
                                  (r"^b\.gm$", []), (r"\.bz2$", [])):
            args.games = re.compile(pattern)
            keiren.save_results(args.results, [])
            with (self.subTest(pattern=pattern), patch.object(keiren, "remote_zip", archive),
                  patch.object(keiren, "download_metadata", side_effect=OSError("offline")),
                  patch.object(keiren, "measure_game", return_value=[
                      dict(backend=args.backends[0].name, outcome="complete")]) as measure,
                  redirect_stderr(io.StringIO())):
                self.assertEqual(keiren.run(args), 0)
                self.assertEqual([call.args[1].filename.removesuffix(".bz2")
                                  for call in measure.call_args_list], expected)
                self.assertEqual([row["game"] for row in keiren.load_results(args.results)], expected)

    def test_games_filter_intersects_retry_outcomes(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.retry = ["error"]
        args.max_games = None
        original = [dict(archive="mlsolver", game=f"mlsolver/games/{game}.gm",
                         backend=args.backends[0].name, outcome=outcome, detail="old")
                    for game, outcome in (("a", "error"), ("b", "complete"))]
        for pattern, expected in ((r"games/b\.gm$", []), (r"games/[ab]\.gm$", ["mlsolver/games/a.gm"])):
            args.games = re.compile(pattern)
            keiren.save_results(args.results, original)
            old = keiren.load_results(args.results)
            with (self.subTest(pattern=pattern), patch.object(keiren, "remote_zip", archive),
                  patch.object(keiren, "download_metadata", side_effect=OSError("offline")),
                  patch.object(keiren, "measure_game", return_value=[
                      dict(backend=args.backends[0].name, outcome="complete", detail="new")]) as measure,
                  redirect_stderr(io.StringIO())):
                self.assertEqual(keiren.run(args), 0)
            self.assertEqual([call.args[1].filename.removesuffix(".bz2")
                              for call in measure.call_args_list], expected)
            saved = keiren.load_results(args.results)
            self.assertEqual([row for row in saved if row["game"] not in expected],
                             [row for row in old if row["game"] not in expected])
            self.assertEqual([row["detail"] for row in saved if row["game"] in expected], ["new"] * len(expected))

    def test_games_filter_argument_validation(self):
        for value in ("", r"games/a\.gm$", "["):
            with (self.subTest(value=value), patch.object(sys, "argv", [keiren.SCRIPT, "run",
                      "--games=" + value, "--results", str(self.work / "results.csv"),
                      "--work-dir", str(self.work / "scratch")]),
                  patch.object(keiren.decomp, "validate_run_arguments", return_value=BUILD_DIR),
                  patch.object(keiren, "run", return_value=0) as run,
                  redirect_stderr(io.StringIO()) as stderr):
                if value == "[":
                    with self.assertRaises(SystemExit) as error:
                        keiren.main()
                    self.assertEqual(error.exception.code, 2)
                    self.assertIn("invalid --games regex: unterminated character set", stderr.getvalue())
                    run.assert_not_called()
                else:
                    self.assertEqual(keiren.main(), 0)
                    self.assertEqual(run.call_args.args[0].games.pattern, value)

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
        with (patch.object(keiren, "remote_zip", archive),
              patch.object(keiren, "download_metadata", return_value=metadata),
              patch.object(keiren, "solver_build", wraps=keiren.solver_build) as build,
              redirect_stderr(io.StringIO())):
            self.assertEqual(keiren.run(args), 0)
            build.assert_called_once_with(BUILD_DIR)
            rows = keiren.load_results(args.results)
            self.assertEqual(len(rows), 1)
            self.assertRegex(rows[0]["solver_build"], r"^pg2adot 0\.2.*?, \w+ -O\w+$")
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

    def test_retry_replaces_whole_games_only_when_published(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.backends = list(keiren.decomp.BACKENDS[-2:])
        args.max_games = None
        original = [dict(archive="mlsolver", game=f"mlsolver/games/{game}.gm",
                         backend=backend.name, outcome=outcome, detail="old detail")
                    for game, outcomes in (("a", ("complete", "error")), ("b", ("timeout", "complete")))
                    for backend, outcome in zip(args.backends, outcomes)]
        keiren.save_results(args.results, original)
        old_bytes = args.results.read_bytes()
        old_rows = keiren.load_results(args.results)
        def measure(archive, member, pending, args):
            self.assertEqual(pending, args.backends)
            if member.filename.endswith("a.gm.bz2"):
                self.assertEqual(args.results.read_bytes(), old_bytes)
                return [dict(backend=backend.name, outcome="complete", detail="new") for backend in pending]
            current = keiren.load_results(args.results)
            self.assertEqual(current[:2], old_rows[2:])
            self.assertEqual([row["detail"] for row in current[2:]], ["new", "new"])
            raise KeyboardInterrupt
        with patch.object(keiren, "remote_zip", archive), patch.object(keiren, "download_metadata", side_effect=OSError("offline")), redirect_stderr(io.StringIO()):
            with patch.object(keiren, "measure_game") as measured:
                self.assertEqual(keiren.run(args), 0)
                measured.assert_not_called()
            self.assertEqual(args.results.read_bytes(), old_bytes)
            args.retry = ["error", "timeout"]
            with patch.object(keiren, "measure_game", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    keiren.run(args)
            self.assertEqual(args.results.read_bytes(), old_bytes)
            with patch.object(keiren, "measure_game", side_effect=measure):
                with self.assertRaises(KeyboardInterrupt):
                    keiren.run(args)
        rows = keiren.load_results(args.results)
        self.assertEqual(rows[:2], old_rows[2:])
        self.assertEqual([row["game"] for row in rows[2:]], ["mlsolver/games/a.gm"] * 2)
        self.assertEqual([row["outcome"] for row in rows[2:]], ["complete", "complete"])

    def test_retry_argument_validation(self):
        for value, expected in (("download failed,error", ["download failed", "error"]),
                                ("", []), ("typo", None)):
            with self.subTest(value=value), patch.object(sys, "argv", [keiren.SCRIPT, "run",
                    "--retry=" + value, "--results", str(self.work / "results.csv"),
                    "--work-dir", str(self.work / "scratch")]), patch.object(keiren.decomp,
                    "validate_run_arguments", return_value=BUILD_DIR), patch.object(keiren,
                    "run", return_value=0) as run, redirect_stderr(io.StringIO()):
                if expected is None:
                    with self.assertRaises(SystemExit) as error:
                        keiren.main()
                    self.assertEqual(error.exception.code, 2)
                    run.assert_not_called()
                else:
                    self.assertEqual(keiren.main(), 0)
                    self.assertEqual(run.call_args.args[0].retry, expected)

    def test_refresh_metadata_preserves_saved_solver_results(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(file_id):
            self.assertEqual(file_id, keiren.ARCHIVES["mlsolver"])
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.refresh_metadata = True
        args.max_games = None
        original = [dict(archive="mlsolver", game="mlsolver/games/a.gm",
                         backend=backend.name, outcome=outcome, detail=detail,
                         seconds="1.234", peak_rss_mib="5.678", start_winner="even",
                         reference_agrees="true", winner_disagrees="false", memory_gib="2")
                    for backend, outcome, detail in zip(keiren.decomp.BACKENDS[:3],
                        ("complete", "error", "partial"),
                        ("game metadata out of memory: MemoryError", "solver failed", "metrics: other error"))]
        original += [dict(archive="mlsolver", game="mlsolver/games/b.gm", backend="lifting",
                          outcome="complete", vertices="2", edges="2", distinct_priorities="2",
                          maximum_priority="1", detail="already measured"),
                     dict(archive="pgsolver", game="pgsolver/games/other.gm", backend="lifting",
                          outcome="complete", detail="game metadata error: other archive")]
        keiren.save_results(args.results, original)
        expected = keiren.load_results(args.results)
        for row in expected[:3]:
            row.update(zip(keiren.GAME_FIELDS, ("2", "2", "2", "1")))
        expected[0]["detail"] = ""
        with (patch.object(keiren, "remote_zip", archive),
              patch.object(keiren, "download_metadata") as references,
              patch.object(keiren, "extract_game", wraps=keiren.extract_game) as extract,
              patch.object(keiren, "capped_json", wraps=keiren.capped_json) as metadata,
              patch.object(keiren, "measure_game") as measure,
              patch.object(keiren, "run_one") as backend,
              redirect_stderr(io.StringIO())):
            self.assertEqual(keiren.run(args), 0)
            self.assertEqual(keiren.load_results(args.results), expected)
            extract.assert_called_once()
            metadata.assert_called_once()
            self.assertEqual(metadata.call_args.args[0], "_game_info")
            self.assertEqual(metadata.call_args.args[-1], int(args.memory * 1024 ** 3))
            references.assert_not_called()
            measure.assert_not_called()
            backend.assert_not_called()
            # No missing rows in the selected archive: even its directory is skipped.
            with patch.object(keiren, "remote_zip") as remote:
                self.assertEqual(keiren.run(args), 0)
                remote.assert_not_called()
        self.assertFalse(list(args.work_dir.rglob("input.gm")))

    def test_games_filter_restricts_metadata_refresh(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.refresh_metadata = True
        args.games = re.compile(r"games/b\.gm$")
        keiren.save_results(args.results, [dict(archive="mlsolver", game=f"mlsolver/games/{game}.gm",
            backend=args.backends[0].name, outcome="error", detail="solver failed") for game in ("a", "b")])
        expected = keiren.load_results(args.results)
        expected[1].update(zip(keiren.GAME_FIELDS, ("2", "2", "2", "1")))
        with (patch.object(keiren, "remote_zip", archive),
              patch.object(keiren, "download_metadata") as references,
              patch.object(keiren, "extract_game", wraps=keiren.extract_game) as extract,
              patch.object(keiren, "capped_json", return_value=([2, 2, 2, 1], "complete", "", 1)),
              patch.object(keiren, "run_one") as backend,
              redirect_stderr(io.StringIO())):
            self.assertEqual(keiren.run(args), 0)
            self.assertEqual(keiren.load_results(args.results), expected)
            extract.assert_called_once()
            self.assertEqual(extract.call_args.args[1].filename, "mlsolver/games/b.gm.bz2")
            references.assert_not_called()
            backend.assert_not_called()
            with patch.object(keiren, "remote_zip") as remote:
                self.assertEqual(keiren.run(args), 0)
                remote.assert_not_called()

    def test_refresh_metadata_publishes_one_game_before_interruption(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.refresh_metadata = True
        args.max_games = None
        keiren.save_results(args.results, [dict(archive="mlsolver", game=f"mlsolver/games/{game}.gm",
            backend="lifting", outcome="complete", detail="game metadata out of memory: MemoryError")
            for game in ("a", "b")])
        old_bytes = args.results.read_bytes()
        old_rows = keiren.load_results(args.results)
        extract_game = keiren.extract_game
        def extract(stream, member, game):
            if member.filename.endswith("a.gm.bz2"):
                self.assertEqual(args.results.read_bytes(), old_bytes)
                return extract_game(stream, member, game)
            current = keiren.load_results(args.results)
            self.assertEqual(current[0]["vertices"], "2")
            self.assertEqual(current[0]["detail"], "")
            self.assertEqual(current[1], old_rows[1])
            raise KeyboardInterrupt
        with (patch.object(keiren, "remote_zip", archive),
              patch.object(keiren, "extract_game", side_effect=extract),
              patch.object(keiren, "run_one") as backend,
              redirect_stderr(io.StringIO())):
            with self.assertRaises(KeyboardInterrupt):
                keiren.run(args)
            backend.assert_not_called()
        self.assertEqual(keiren.load_results(args.results)[1], old_rows[1])
        self.assertFalse(list(args.work_dir.rglob("input.gm")))

    def test_refresh_metadata_fills_any_missing_field(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.refresh_metadata = True
        for missing in keiren.GAME_FIELDS:
            with self.subTest(missing=missing):
                row = dict(archive="mlsolver", game="mlsolver/games/a.gm",
                           backend="lifting", outcome="complete",
                           **dict(zip(keiren.GAME_FIELDS, ("2", "2", "2", "1"))))
                row[missing] = ""
                keiren.save_results(args.results, [row])
                with (patch.object(keiren, "remote_zip", archive),
                      patch.object(keiren, "run_one") as backend,
                      redirect_stderr(io.StringIO())):
                    self.assertEqual(keiren.run(args), 0)
                    backend.assert_not_called()
                saved = keiren.load_results(args.results)[0]
                self.assertEqual([saved[field] for field in keiren.GAME_FIELDS], ["2", "2", "2", "1"])

    def test_refresh_metadata_failures_preserve_csv(self):
        archive_path = self.local_zip()
        @contextmanager
        def archive(_):
            with zipfile.ZipFile(archive_path) as stream:
                yield stream
        args = self.args(self.work / "results.csv")
        args.refresh_metadata = True
        keiren.save_results(args.results, [dict(archive="mlsolver", game="mlsolver/games/a.gm",
            backend="lifting", outcome="complete", detail="game metadata out of memory: MemoryError")])
        old_bytes = args.results.read_bytes()
        for failure in ("download", "metadata", "listing", "publish"):
            with (self.subTest(failure=failure),
                  patch.object(keiren, "remote_zip", archive),
                  patch.object(keiren.time, "sleep"),
                  patch.object(keiren, "run_one") as backend,
                  redirect_stderr(io.StringIO())):
                if failure == "download":
                    broken = patch.object(keiren, "extract_game", side_effect=OSError("offline"))
                elif failure == "metadata":
                    broken = patch.object(keiren, "capped_json", return_value=(None, "out of memory", "MemoryError", 1))
                elif failure == "listing":
                    broken = patch.object(keiren, "remote_zip", side_effect=OSError("offline"))
                else:
                    broken = patch.object(keiren.os, "fsync", side_effect=OSError("disk full"))
                with broken:
                    if failure == "publish":
                        with self.assertRaisesRegex(RuntimeError, "previous results preserved"):
                            keiren.run(args)
                    else:
                        self.assertEqual(keiren.run(args), 1)
                backend.assert_not_called()
                self.assertEqual(args.results.read_bytes(), old_bytes)
        self.assertFalse(list(args.work_dir.rglob("input.gm")))

    def test_refresh_metadata_argument_needs_no_solver_binaries(self):
        with (patch.object(sys, "argv", [keiren.SCRIPT, "run", "--refresh-metadata",
                  "--archives=equivchecking", "--build-dir", str(self.work / "missing-build"),
                  "--results", str(self.work / "results.csv"), "--work-dir", str(self.work / "scratch")]),
              patch.object(keiren, "run", return_value=0) as run):
            self.assertEqual(keiren.main(), 0)
        args = run.call_args.args[0]
        self.assertTrue(args.refresh_metadata)
        self.assertEqual(args.archives, ["equivchecking"])
        self.assertEqual(args.metadata_timeout, 600)

    def test_metadata_timeout_argument_validation(self):
        for value in ("12.5", "0", "-1", "nan", "inf"):
            with (self.subTest(value=value),
                  patch.object(sys, "argv", [keiren.SCRIPT, "run", "--metadata-timeout=" + value,
                      "--results", str(self.work / "results.csv"),
                      "--work-dir", str(self.work / "scratch")]),
                  patch.object(keiren.decomp, "validate_run_arguments", return_value=BUILD_DIR),
                  patch.object(keiren, "run", return_value=0) as run,
                  redirect_stderr(io.StringIO())):
                if value == "12.5":
                    self.assertEqual(keiren.main(), 0)
                    self.assertEqual(run.call_args.args[0].metadata_timeout, 12.5)
                    self.assertEqual(run.call_args.args[0].timeout, 30)
                else:
                    with self.assertRaises(SystemExit) as error:
                        keiren.main()
                    self.assertEqual(error.exception.code, 2)
                    run.assert_not_called()

    def test_metadata_deadline_is_independent_in_measurement_and_refresh(self):
        args = self.args(self.work / "results.csv")
        args.work_dir.mkdir()
        args.timeout, args.metadata_timeout = 0.01, 123
        with (zipfile.ZipFile(self.local_zip()) as archive,
              patch.object(keiren.time, "monotonic", return_value=1000),
              patch.object(keiren, "capped_json", return_value=([2, 2, 2, 1], "complete", "", 1)) as metadata,
              patch.object(keiren, "run_one", return_value={"backend": "zielonka", "outcome": "complete", "detail": ""}) as backend):
            member = keiren.game_members(archive)[0]
            rows = keiren.measure_game(archive, member, args.backends, args)
            self.assertEqual(rows[0]["vertices"], 2)
            backend.assert_called_once()
            self.assertTrue(keiren.refresh_metadata(archive, member, rows, args))
            self.assertEqual(metadata.call_count, 2)
            for call in metadata.call_args_list:
                self.assertEqual(call.args[0], "_game_info")
                self.assertEqual(call.args[-2:], (1123, int(args.memory * 1024 ** 3)))

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

    def test_solver_build_records_first_version_line_and_optional_meson_options(self):
        version = subprocess.CompletedProcess([], 0, "pg2adot 0.2 (git example)\nignored\n")
        options = subprocess.CompletedProcess([], 0, json.dumps([
            dict(name="buildtype", value="release"), dict(name="optimization", value="3")]))
        with patch.object(keiren.subprocess, "run", side_effect=[version, options]) as run:
            self.assertEqual(keiren.solver_build(BUILD_DIR), "pg2adot 0.2 (git example), release -O3")
            self.assertEqual([call.args[0] for call in run.call_args_list], [
                [BUILD_DIR / "pg2adot", "--version"],
                ["meson", "introspect", "--buildoptions", BUILD_DIR]])
        for unavailable in (FileNotFoundError(), subprocess.CalledProcessError(1, "meson"),
                            subprocess.CompletedProcess([], 0, "not JSON"),
                            subprocess.CompletedProcess([], 0, "[]")):
            with (self.subTest(unavailable=unavailable),
                  patch.object(keiren.subprocess, "run", side_effect=[version, unavailable])):
                self.assertEqual(keiren.solver_build(BUILD_DIR), "pg2adot 0.2 (git example)")

    def test_backfill_build_loads_old_csv_and_only_fills_empty_cells_atomically(self):
        results = self.work / "results.csv"
        for has_build in (False, True):
            fields = keiren.FIELDS if has_build else keiren.FIELDS[:-1]
            with results.open("w", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                for game in ("a", "b"):
                    row = dict(archive="mlsolver", game=f"games/{game}.gm", backend="zielonka",
                               outcome="complete", detail="preserved")
                    if has_build:
                        row["solver_build"] = "recorded build" if game == "a" else ""
                    writer.writerow(row)
            expected = keiren.load_results(results)
            if not has_build:
                self.assertEqual([row["solver_build"] for row in expected], ["", ""])
            original = results.read_bytes()
            for row in expected:
                if not row["solver_build"]:
                    row["solver_build"] = "earlier build"
            with (self.subTest(has_build=has_build),
                  patch.object(sys, "argv", [keiren.SCRIPT, "run", "--backfill-build=earlier build",
                      "--results", str(results), "--build-dir", str(self.work / "missing")]),
                  patch.object(keiren.subprocess, "run", side_effect=AssertionError("process")),
                  patch.object(keiren, "remote_zip", side_effect=AssertionError("download")),
                  patch.object(keiren, "download_metadata", side_effect=AssertionError("metadata")),
                  patch.object(keiren.time, "sleep")):
                with patch.object(keiren.os, "fsync", side_effect=OSError("disk full")):
                    with self.assertRaisesRegex(RuntimeError, "previous results preserved"):
                        keiren.main()
                self.assertEqual(results.read_bytes(), original)
                self.assertEqual(keiren.main(), 0)
                self.assertEqual(keiren.load_results(results), expected)
                self.assertEqual(keiren.main(), 0)
                self.assertEqual(keiren.load_results(results), expected)
                self.assertFalse(list(self.work.glob(".results-*")))

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

    def test_render_marks_stale_preprocessing_details_without_editing_csv(self):
        stale = "preprocess: residual=3001 shaved_even=0"
        diagnostic = "exit 4: Solver failed: priority depth exceeds the safe recursion depth"
        rows = [dict(archive="mlsolver", game="mlsolver/games/a.gm",
                     backend=backend, outcome=outcome, detail=detail)
                for backend, outcome, detail in (
                    ("zielonka+pre", "error", stale),
                    ("lifting+pre+iter", "out of memory", stale),
                    ("zielonka-sym+pre", "error", "exit 4: " + stale),
                    ("pm-strahler+pre", "complete", stale),
                    ("zielonka", "error", stale),
                    ("lifting+pre", "error", diagnostic),
                    ("lifting-sym+pre", "partial", ""))]
        results = self.work / "results.csv"
        keiren.save_results(results, rows)
        original = results.read_bytes()
        output = self.work / "KEIREN.md"
        keiren.render(results, output)
        report = output.read_text()
        inventory = report.split("## Inventory\n\n", 1)[1]
        self.assertEqual(inventory.count("| (error text not recorded) |"), 3)
        self.assertEqual(inventory.count(stale), 2)
        self.assertIn(diagnostic, inventory)
        self.assertEqual(report.count("Older non-complete +pre rows with only preprocessing statistics"), 1)
        self.assertEqual(results.read_bytes(), original)

    def test_dataset_notes_count_games_and_preprocessing_from_rows(self):
        rows = []
        for n, priorities in ((1, "1502"), (2, "3002"), (3, "5000")):
            game = f"pgsolver/games/recursiveladder({n}).gm"
            rows.extend([
                dict(archive="pgsolver", game=game, backend="zielonka", outcome="error",
                     distinct_priorities=priorities, detail="exit 4: Solver failed: priority depth exceeds the safe recursion depth"),
                dict(archive="pgsolver", game=game, backend="zielonka+pre",
                     outcome="error" if n == 1 else "complete", detail="exit 4: preprocess: residual=3001" if n == 1 else ""),
            ])
        rows.extend(dict(archive="mlsolver", game="games/huge.gm", backend=backend,
                         outcome="out of memory", detail="1:1: failed to allocate the input buffer")
                    for backend in ("zielonka", "lifting"))
        rows.extend([
            dict(archive="pgsolver", game="pgsolver/games/recursiveladder(1).gm",
                 backend="pm-strahler+pre", outcome="complete"),
            dict(archive="mlsolver", game="games/bad.gm", backend="zielonka", outcome="invalid input"),
            dict(archive="mlsolver", game="mlsolver/games/FLCTLStarLimitClosuren=1.gm",
                 backend="zielonka", outcome="complete", reference_agrees="false"),
            dict(archive="equivchecking", game="games/download.gm", backend="zielonka", outcome="download failed"),
        ])
        notes = keiren.dataset_notes(rows)
        for expected in ("3 pgsolver games", "1,502 and 5,000 distinct priorities",
                         "compression gets 2 games", "remaining 1 recursiveladder",
                         "1 of the largest games (2 backend runs)", "1 games are invalid",
                         "`games/bad.gm`", "1 games still marked", "likely error in the reference data"):
            self.assertIn(expected, notes)
        self.assertEqual(keiren.dataset_notes([]), "")
        self.assertEqual(rows[1]["detail"], "exit 4: preprocess: residual=3001")

    def test_build_notes_count_rows_games_and_name_minority_build_games(self):
        rows = [dict(archive="pgsolver", game=f"games/{game}.gm", backend=backend,
                     outcome="complete", solver_build=build)
                for build, games in (("old release -O3", "abc"), ("stream release -O3", "cd"))
                for game in games for backend in ("zielonka", "lifting")]
        rows.append(dict(archive="mlsolver", game="(archive listing)", backend="",
                         outcome="download failed", solver_build=""))
        notes = keiren.dataset_notes(rows)
        for expected in ("| old release -O3 | 6 | 3 |", "| stream release -O3 | 4 | 2 |",
                         "| (unrecorded) | 1 | 0 |", "non-majority build", "parser allocation failure",
                         "- pgsolver: <code>games/c.gm</code>", "- pgsolver: <code>games/d.gm</code>"):
            self.assertIn(expected, notes)
        self.assertNotIn("<code>games/a.gm</code>", notes)
        self.assertNotIn("<code>games/b.gm</code>", notes)
        self.assertNotIn("non-majority build", keiren.dataset_notes(rows[:6]))
        self.assertNotIn("non-majority build", keiren.dataset_notes(rows[:4] + rows[6:10]))

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
