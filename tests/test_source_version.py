#!/usr/bin/env python3
"""Build a source copy inside an unrelated tagged Git checkout."""

import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile

source = Path(__file__).resolve().parents[1]
version, meson = sys.argv[1:]
if not shutil.which("git"):
    sys.exit(77)

with tempfile.TemporaryDirectory(prefix="source version ") as directory:
    parent = Path(directory)
    copied = parent / "source copy"
    copied.mkdir()
    for name in ("meson.build", "meson_options.txt"):
        shutil.copy2(source / name, copied / name)
    for name in ("src", "tests", "ci", "scripts"):
        shutil.copytree(source / name, copied / name,
                        ignore=shutil.ignore_patterns("actual", "__pycache__"))

    def run(*command):
        return subprocess.run(command, check=True, text=True, timeout=90)

    run("git", "init", str(parent))
    run("git", "-C", str(parent), "-c", "user.name=Version test",
        "-c", "user.email=version@example.invalid", "-c", "commit.gpgsign=false",
        "commit", "--allow-empty", "-m", "Unrelated repository")
    run("git", "-C", str(parent), "tag", "unrelated-version")
    build = parent / "build"
    run(meson, "setup", str(build), str(copied), "-Dlenstree=disabled")
    run(meson, "compile", "-C", str(build), "-j1", "genstree")
    wrapper = shlex.split(os.environ.get("STRAHLER_TEST_WRAPPER", ""))
    result = subprocess.run([*wrapper, str(build / "genstree"), "--version"],
                            check=True, text=True, capture_output=True, timeout=90)
    assert result.stdout == f"genstree {version}\n", result
    assert not result.stderr, result
