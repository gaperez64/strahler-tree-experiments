#!/usr/bin/env bash
set -euo pipefail

binary=$1
algorithm=$2
golden=$3
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT
tests/run-with-input.sh tests/games/pm_cycle.pg "$binary" \
  --algorithm="$algorithm" --format=leaves --player=even > "$scratch/output"
sed 's/^even: //' "$scratch/output" > "$scratch/stream"
diff -u "$golden" "$scratch/stream"
