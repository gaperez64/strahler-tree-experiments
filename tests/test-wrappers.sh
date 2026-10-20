#!/usr/bin/env bash
set -euo pipefail

genstree=$1
pgfilt=$2
version=$3
# Use the system Bash to catch macOS's empty-array nounset failure.
env -u STRAHLER_TEST_WRAPPER /bin/bash --posix \
  tests/check-version.sh "$genstree" "$version"
env -u STRAHLER_TEST_WRAPPER /bin/bash --posix \
  tests/run-with-input.sh tests/games/sparse.pg "$pgfilt" > /dev/null

scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
export WRAPPER_LOG="$scratch/calls"
cat > "$scratch/wrapper" <<'WRAPPER'
#!/usr/bin/env bash
set -euo pipefail
echo wrapped >> "$WRAPPER_LOG"
if [[ ${WRAPPER_FAIL:-0} == 1 ]]; then
  exit 99
fi
exec "$@"
WRAPPER
chmod +x "$scratch/wrapper"
export STRAHLER_TEST_WRAPPER="$scratch/wrapper"

tests/run-single-test.sh "$genstree" tests/golden/j_k2_t1_h2.out \
  "$scratch/actual" EMPTY --strahler=2 --log-leaves=1 --height=2 --count
tests/run-with-input.sh tests/games/sparse.pg "$pgfilt" > /dev/null
tests/check-version.sh "$genstree" "$version"
test "$(wc -l < "$WRAPPER_LOG")" -eq 3

# Matching output must never hide a wrapper's failure.
export WRAPPER_FAIL=1
: > "$scratch/empty"
status=0
tests/run-single-test.sh "$genstree" "$scratch/empty" "$scratch/actual" EMPTY \
  || status=$?
test "$status" -eq 99
