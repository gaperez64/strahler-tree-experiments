#!/usr/bin/env bash
set -euo pipefail

if [[ $# -gt 1 ]]; then
  echo "Usage: $0 [BUILD_DIR]" >&2
  exit 2
fi

build_dir=${1:-build}
export STRAHLER_TEST_WRAPPER="valgrind --quiet --leak-check=full --show-leak-kinds=definite,indirect,possible --errors-for-leak-kinds=definite,indirect,possible --error-exitcode=99"

# Exit 99 is a Meson error even for should_fail tests; the harnesses preserve it.
exec meson test -C "$build_dir" --print-errorlogs --timeout-multiplier 10 \
  --no-suite python --wrapper="$STRAHLER_TEST_WRAPPER"
