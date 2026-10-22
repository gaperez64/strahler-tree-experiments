#!/usr/bin/env python3
"""A 46 MB game fits in 240 MiB of address space (the old reader does not)."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile


def main():
    if (sys.platform == "darwin" or sys.argv[2] != "none" or
            os.environ.get("STRAHLER_TEST_WRAPPER") or os.environ.get("VALGRIND_OPTS")):
        return 77
    try:
        import resource
    except ImportError:
        return 77
    if not hasattr(resource, "RLIMIT_AS"):
        return 77
    _, hard = resource.getrlimit(resource.RLIMIT_AS)
    if hard != resource.RLIM_INFINITY and hard < 240 * 1024**2:
        return 77

    def cap():
        resource.setrlimit(resource.RLIMIT_AS, (240 * 1024**2, 240 * 1024**2))

    probe = subprocess.run([sys.executable, "-c",
                            "try: bytearray(300 * 1024**2)\n"
                            "except MemoryError: raise SystemExit(0)\n"
                            "raise SystemExit(77)"], preexec_fn=cap,
                           capture_output=True, timeout=10)
    if probe.returncode != 0:
        return 77
    binary = Path(sys.argv[1]).resolve()
    count = 1_000_000
    with tempfile.TemporaryFile(mode="w+", dir=binary.parent) as stream:
        stream.write(f"parity {count - 1};\n")
        for vertex in range(count):
            stream.write(f"{vertex} {vertex % 8} {vertex % 2} " +
                         ",".join(str((vertex + edge) % count)
                                  for edge in range(5)) + ";\n")
        stream.seek(0)
        result = subprocess.run([str(binary)], stdin=stream, preexec_fn=cap,
                                text=True, capture_output=True, timeout=30)
    assert result.returncode == 0, result.stderr
    assert result.stdout.startswith("vertices: 1000000\nedges: 5000000\n"), result
    return 0


if __name__ == "__main__":
    sys.exit(main())
