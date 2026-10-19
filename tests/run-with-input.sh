#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 INPUT COMMAND [ARGS...]" >&2
  exit 2
fi

input=$1
shift
read -r -a wrapper <<< "${STRAHLER_TEST_WRAPPER:-}"
exec ${wrapper[@]+"${wrapper[@]}"} "$@" < "$input"
