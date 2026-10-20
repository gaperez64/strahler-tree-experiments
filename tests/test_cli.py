#!/usr/bin/env python3
"""Check the CLI contract for one executable, including its value syntax."""

import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys

binary = Path(sys.argv[1]).resolve()
version = sys.argv[2]
program = binary.name
wrapper = shlex.split(os.environ.get("STRAHLER_TEST_WRAPPER", ""))


def run(*arguments, input=""):
    result = subprocess.run([*wrapper, str(binary), *arguments], input=input,
                            text=True, capture_output=True, timeout=90)
    assert result.returncode != 99, result.stderr
    return result


def invalid(*arguments):
    result = run(*arguments)
    assert result.returncode == 2, (arguments, result)
    lines = result.stderr.splitlines()
    assert len(lines) == 2, (arguments, result.stderr)
    assert lines[0].startswith(f"{program}: "), result.stderr
    assert lines[1] == f"Try '{program} --help'.", result.stderr


help_result = run("--help")
assert help_result.returncode == 0, help_result
assert help_result.stdout.startswith(f"Usage: {program} [OPTIONS]"), help_result
assert "--help" in help_result.stdout and "--version" in help_result.stdout
assert not help_result.stderr, help_result.stderr
version_result = run("--version")
assert version_result.returncode == 0, version_result
assert re.fullmatch(rf"{re.escape(program)} {re.escape(version)}( \(git [^)]+\))?\n",
                    version_result.stdout), version_result
assert not version_result.stderr, version_result.stderr
source = Path(__file__).resolve().parents[1]
if (source / ".git").exists() and shutil.which("git"):
    describe = subprocess.run(["git", "-C", str(source), "describe", "--tags",
                               "--always", "--dirty"], check=True, text=True,
                              capture_output=True).stdout.strip()
    assert version_result.stdout == f"{program} {version} (git {describe})\n", version_result
else:
    assert version_result.stdout == f"{program} {version}\n", version_result

for arguments in [("--unknown-option",), ("-h",), ("--he",),
                  ("--help=bad",), ("--version=bad",)]:
    invalid(*arguments)

if program in ("genstree", "lenstree"):
    base = ("--strahler=2", "--log-leaves=1", "--height=2")
    assert run(*base).returncode == 0
    assert run(*base, "--leaf=1").returncode == 0
    assert run(*base, "--version").stdout == version_result.stdout
    invalid()
    invalid(*base, "operand")
    for option in ("strahler", "log-leaves", "height", "leaf"):
        for value in ("", "-1", "+1", " 1", "1 ", "1x", "999999999999999999999"):
            invalid(*base, f"--{option}={value}")
        invalid(*base, f"--{option}", "1")
    for option in ("strahler", "height", "leaf"):
        invalid(*base, f"--{option}=0")
    invalid("--strahler=3", "--log-leaves=1", "--height=2")
    invalid(*base, "--leaf=4")
    if program == "genstree":
        invalid(*base, "--p-level=0")
    else:
        # Counts exceed UINT_MAX; selection also crosses overflowing child sums.
        for k, t, h, leaf, bits, levels in [
            (3, 30, 3, 2, "0" * 32, "0" * 30 + "11"),
            (6, 10, 11, 1975102018, "0" * 15, "111111111112345"),
            (7, 9, 12, 2030528384, "0" * 15, "011111111112345"),
        ]:
            arguments = (f"--strahler={k}", f"--log-leaves={t}", f"--height={h}")
            result = run(*arguments)
            assert result.returncode == 0, result
            assert result.stdout.endswith("It has 4294967295 leaves\n"), result
            result = run(*arguments, f"--leaf={leaf}")
            assert result.returncode == 0, result
            assert result.stdout.endswith(f"Leaf no {leaf} is {bits} {levels}\n"), result
elif program == "str-tree":
    assert run("--index=0").returncode == 0
    assert run("--index=0", "--p-level=2").returncode == 0
    for arguments in [("0",), ("0", "2"), ("--p-level=2",),
                      ("--index", "0"), ("--index=-1",), ("--index=999999",),
                      ("--index=x",), ("--index=0", "--p-level=999999")]:
        invalid(*arguments)
elif program == "pms2dot":
    invalid("--check-order", "--reorder")
    invalid("--reorder", "--check-order")
    invalid("--check-order=bad")
    invalid("operand")
else:
    invalid("--priority-mode=bad")
    invalid("--priority-mode", "original")
    if program == "pgfilt":
        invalid("-n")
        invalid("operand")
    else:
        invalid("first.pg", "second.pg")
        if program == "pg2adot":
            for arguments in [("--tree-file=",), ("--adaptive-t=bad",),
                              ("--start-t=2",), ("--tree-k=1", "--kary=2"),
                              ("--algorithm=zielonka", "--tree-k=1"),
                              ("--algorithm=lifting-sym", "--adaptive-t")]:
                invalid(*arguments)
        else:
            invalid("--k=1")
            invalid("--algorithm=succinct", "--k=1", "--t=1")
        game = "parity 0;\n0 0 0 0;\n"
        for arguments in [(), ("-",), ("--", "-")]:
            result = run(*arguments, input=game)
            assert result.returncode == 0, result
        for option in ("max-set-items", "tree-k" if program == "pg2adot" else "k"):
            for value in ("", "-1", "+1", " 1", "1x", "999999999999999999999"):
                invalid(f"--{option}={value}")
