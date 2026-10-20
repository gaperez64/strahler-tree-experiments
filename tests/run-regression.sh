#!/usr/bin/env bash
# Regression harness for the command-line tools
# Usage:
#   tests/run-regression.sh                # run tests (via meson)
#   tests/run-regression.sh --generate-goldens

# Decide whether to generate goldens
GENERATE=0
if [ "${1:-}" = "--generate-goldens" ]; then
  GENERATE=1
fi
if [ "${GENERATE_GOLDENS:-0}" = "1" ]; then
  GENERATE=1
fi

if [ "$GENERATE" -eq 0 ]; then
  echo "Running regression tests via meson..."
  BUILD_DIR="build"
  if [ ! -d "$BUILD_DIR" ]; then
    echo "Error: Build directory '$BUILD_DIR' not found. Please run 'meson setup build'."
    exit 1
  fi
  meson test -C "$BUILD_DIR"
  exit $?
fi

# Locate binaries for golden generation
GENSTREE_BIN=""
if [ -x "./build/genstree" ]; then
  GENSTREE_BIN="./build/genstree"
elif [ -x "./genstree" ]; then
  GENSTREE_BIN="./genstree"
elif command -v genstree >/dev/null 2>&1; then
  GENSTREE_BIN="$(command -v genstree)"
else
  echo "Error: genstree binary not found in build/ or project root or PATH."
  exit 2
fi

PMS2DOT_BIN=""
if [ -x "./build/pms2dot" ]; then
  PMS2DOT_BIN="./build/pms2dot"
elif [ -x "./pms2dot" ]; then
  PMS2DOT_BIN="./pms2dot"
elif command -v pms2dot >/dev/null 2>&1; then
  PMS2DOT_BIN="$(command -v pms2dot)"
else
  echo "Error: pms2dot binary not found in build/ or project root or PATH."
  exit 2
fi

PGFILT_BIN=""
if [ -x "./build/pgfilt" ]; then
  PGFILT_BIN="./build/pgfilt"
elif [ -x "./pgfilt" ]; then
  PGFILT_BIN="./pgfilt"
elif command -v pgfilt >/dev/null 2>&1; then
  PGFILT_BIN="$(command -v pgfilt)"
else
  echo "Error: pgfilt binary not found in build/ or project root or PATH."
  exit 2
fi

PG2ADOT_BIN=""
if [ -x "./build/pg2adot" ]; then
  PG2ADOT_BIN="./build/pg2adot"
elif [ -x "./pg2adot" ]; then
  PG2ADOT_BIN="./pg2adot"
elif command -v pg2adot >/dev/null 2>&1; then
  PG2ADOT_BIN="$(command -v pg2adot)"
else
  echo "Error: pg2adot binary not found in build/ or project root or PATH."
  exit 2
fi

PG2PMDOT_BIN=""
if [ -x "./build/pg2pmdot" ]; then
  PG2PMDOT_BIN="./build/pg2pmdot"
elif [ -x "./pg2pmdot" ]; then
  PG2PMDOT_BIN="./pg2pmdot"
elif command -v pg2pmdot >/dev/null 2>&1; then
  PG2PMDOT_BIN="$(command -v pg2pmdot)"
else
  echo "Error: pg2pmdot binary not found in build/ or project root or PATH."
  exit 2
fi

LENSTREE_BIN=""
if [ -x "./build/lenstree" ]; then
  LENSTREE_BIN="./build/lenstree"
elif [ -x "./lenstree" ]; then
  LENSTREE_BIN="./lenstree"
elif command -v lenstree >/dev/null 2>&1; then
  LENSTREE_BIN="$(command -v lenstree)"
fi

echo "Using genstree binary: $GENSTREE_BIN"
echo "Using pms2dot binary: $PMS2DOT_BIN"
echo "Using pgfilt binary: $PGFILT_BIN"
echo "Using pg2adot binary: $PG2ADOT_BIN"
echo "Using pg2pmdot binary: $PG2PMDOT_BIN"
echo "Using lenstree binary: $LENSTREE_BIN"

GENSTREE_CASES=(
  "2 1 2" "3 1 3" "4 2 4" "3 2 4" "1 2 4" "1 2 2" "2 2 2"
)

PMS2DOT_CASES=(
  "0|1|" "0,0|0,1|1,0|1,1|" "0,e,1|0,1,1|1,e,0|" "0,0,1,e,1|0,1,1,0,0|" "0,1|1,0|0,0|" "|" "e,e|0,e|" "1,0|0,0|1,1|0,1|"
)

mkdir -p tests/actual tests/golden

sanitize_output() {
  local file=$1
  local binary=$2
  local program=${binary##*/}
  sed -e "s|[^[:space:]]*/${program}|${program}|g" "$file" > "$file.tmp" &&
    mv "$file.tmp" "$file"
}

echo "Generating golden files into tests/golden/ ..."
while IFS='|' read -r name fixture flags; do
  read -r -a arguments <<< "$flags"
  "$PG2ADOT_BIN" "${arguments[@]}" "tests/games/$fixture.pg" \
    > "tests/golden/pg2adot_$name.out" 2>&1
done <<'CASES'
shave_loops|shave_loops|--initial-shave=loops --labels=sets
shave_wcwc|shave_wcwc|--initial-shave=wcwc --labels=sets
shave_single|shave_single|--initial-shave=single --labels=sets
shave_relative|shave_wcwc|--initial-shave=loops,wcwc --view=tree-relative --labels=sets --max-set-items=2
shave_empty_jurdzinski|shave_single|--initial-shave=all --view=jurdzinski
compress_original|compress|--compress --labels=sets
compress_compact|compress|--compress --priority-mode=compact
compress_jurdzinski|compress|--compress --view=jurdzinski
shave_partial|shave_partial|--initial-shave=loops --tree-k=1 --labels=sets
shave_stats_lifting|shave_single|--algorithm=lifting --initial-shave=all --compress --stats --labels=none
shave_stats_zielonka|shave_single|--algorithm=zielonka --initial-shave=all --compress --stats --labels=none
sym_h4|thesis_h4|--algorithm=zielonka-sym --stats --player=even --labels=none
sym_f4|thesis_f4|--algorithm=zielonka-sym --stats --player=even --labels=none
sym_lifting_stats|strahler_two|--algorithm=lifting-sym --kary=1 --stats --player=even --labels=none
CASES

for algorithm in strahler succinct; do
  while IFS='|' read -r name fixture flags; do
    read -r -a arguments <<< "$flags"
    if [[ "$name" == partial* ]]; then
      if [ "$algorithm" = strahler ]; then
        arguments=(--k=1 --t=1 "${arguments[@]}")
      else
        arguments=(--bits=0 "${arguments[@]}")
      fi
    fi
    "$PG2PMDOT_BIN" "--algorithm=$algorithm" "${arguments[@]}" \
      "tests/games/$fixture.pg" > "tests/golden/pm_${algorithm}_$name.out" 2>&1
    sanitize_output "tests/golden/pm_${algorithm}_$name.out" "$PG2PMDOT_BIN"
  done <<'CASES'
counts|ordered_two_children|
sets|strahler_two|--labels=sets --max-set-items=1
none|split_winners|--labels=none
leaves|pm_cycle|--format=leaves
partial|strahler_two|--labels=sets
partial_leaves|strahler_two|--format=leaves
incremental|strahler_two|--iter-shave --labels=sets
incremental_leaves|strahler_two|--iter-shave --format=leaves
iter_stats|strahler_two|--iter-shave --stats --format=leaves
shave_compress|shave_partial|--initial-shave=loops --compress --labels=sets
shave_empty|shave_single|--initial-shave=all --compress --labels=sets
compress_original|compress|--compress --labels=sets
compress_compact|compress|--compress --priority-mode=compact
stats|pm_cycle|--stats --format=leaves
preprocess_stats|shave_partial|--stats --format=leaves --initial-shave=loops --compress
CASES
done

while IFS='|' read -r name fixture options; do
  "$PG2ADOT_BIN" --iter-shave --stats --labels=sets $options \
    "tests/games/$fixture.pg" > "tests/golden/pg2adot_iter_$name.out" 2>&1
  sanitize_output "tests/golden/pg2adot_iter_$name.out" "$PG2ADOT_BIN"
done <<'CASES'
fixed|strahler_two|--tree-k=1
kary|strahler_two|--kary=1 --view=jurdzinski
tree|iter_shave|--tree-file=tests/trees/chain_three.tree --view=tree-relative
adaptive|strahler_two|--adaptive-t
incremental|strahler_two|--adaptive-t=incremental
sym|strahler_two|--algorithm=lifting-sym --tree-k=1
capped|strahler_two|--adaptive-t --tree-k=1
limit|strahler_two|--adaptive-t --max-host-leaves=1
pre|shave_partial|--initial-shave=loops --compress --adaptive-t
empty|shave_single|--initial-shave=all --adaptive-t
no_progress|disagree_lifting_strahler|--kary=1
CASES

for ct in "${GENSTREE_CASES[@]}"; do
  read -r k t h <<< "$ct"
  name="k${k}_t${t}_h${h}.out"
  echo "  $GENSTREE_BIN -k $k -t $t -h $h > tests/golden/$name"
  "$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" > "tests/golden/$name" 2>&1
  sanitize_output "tests/golden/$name" "$GENSTREE_BIN"

  echo "  $GENSTREE_BIN -k $k -t $t -h $h -j > tests/golden/j_$name"
  "$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" -j > "tests/golden/j_$name" 2>&1
  sanitize_output "tests/golden/j_$name" "$GENSTREE_BIN"

  echo "  $GENSTREE_BIN -k $k -t $t -h $h -d > tests/golden/d_$name"
  "$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" -d > "tests/golden/d_$name" 2>&1
  sanitize_output "tests/golden/d_$name" "$GENSTREE_BIN"

  echo "  $GENSTREE_BIN -k $k -t $t -h $h -p 1 > tests/golden/p1_$name"
  "$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" -p 1 > "tests/golden/p1_$name" 2>&1
  sanitize_output "tests/golden/p1_$name" "$GENSTREE_BIN"

  total=$("$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" -j | grep -o '[0-9]\+ leaves' | cut -d' ' -f1)
  for l in 1 $total; do
    echo "  $GENSTREE_BIN -k $k -t $t -h $h -l $l > tests/golden/l${l}_$name"
    "$GENSTREE_BIN" -k "$k" -t "$t" -h "$h" -l "$l" > "tests/golden/l${l}_$name" 2>&1
    sanitize_output "tests/golden/l${l}_$name" "$GENSTREE_BIN"
  done
done

for i in "${!PMS2DOT_CASES[@]}"; do
  case="${PMS2DOT_CASES[$i]}"
  name="pms_${i}.out"
  echo "  echo \"$case\" | $PMS2DOT_BIN > tests/golden/$name"
  echo "$case" | "$PMS2DOT_BIN" > "tests/golden/$name" 2>&1
  sanitize_output "tests/golden/$name" "$PMS2DOT_BIN"
done

echo "  $PGFILT_BIN < tests/games/sparse.pg > tests/golden/pgfilt_summary.out"
"$PGFILT_BIN" < tests/games/sparse.pg > tests/golden/pgfilt_summary.out 2>&1
sanitize_output "tests/golden/pgfilt_summary.out" "$PGFILT_BIN"
echo "  $PGFILT_BIN --normalize < tests/games/sparse.pg > tests/golden/pgfilt_normalize.out"
"$PGFILT_BIN" --normalize < tests/games/sparse.pg > tests/golden/pgfilt_normalize.out 2>&1
sanitize_output "tests/golden/pgfilt_normalize.out" "$PGFILT_BIN"
echo "  $PGFILT_BIN < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_summary.out"
"$PGFILT_BIN" < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_summary.out 2>&1
sanitize_output "tests/golden/pgfilt_gap_summary.out" "$PGFILT_BIN"
echo "  $PGFILT_BIN --normalize < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_normalize.out"
"$PGFILT_BIN" --normalize < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_normalize.out 2>&1
sanitize_output "tests/golden/pgfilt_gap_normalize.out" "$PGFILT_BIN"
echo "  $PGFILT_BIN --priority-mode=compact < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_compact_summary.out"
"$PGFILT_BIN" --priority-mode=compact < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_compact_summary.out 2>&1
sanitize_output "tests/golden/pgfilt_gap_compact_summary.out" "$PGFILT_BIN"
echo "  $PGFILT_BIN --priority-mode=compact --normalize < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_compact_normalize.out"
"$PGFILT_BIN" --priority-mode=compact --normalize < tests/games/priority_gap_start.pg > tests/golden/pgfilt_gap_compact_normalize.out 2>&1
sanitize_output "tests/golden/pgfilt_gap_compact_normalize.out" "$PGFILT_BIN"

echo "  $PG2ADOT_BIN tests/games/ordered_two_children.pg > tests/golden/pg2adot_counts.out"
"$PG2ADOT_BIN" tests/games/ordered_two_children.pg > tests/golden/pg2adot_counts.out 2>&1
sanitize_output "tests/golden/pg2adot_counts.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_sets.out"
"$PG2ADOT_BIN" --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --view=tree-relative tests/games/ordered_two_children.pg > tests/golden/pg2adot_tree_relative_counts.out"
"$PG2ADOT_BIN" --view=tree-relative tests/games/ordered_two_children.pg > tests/golden/pg2adot_tree_relative_counts.out 2>&1
sanitize_output "tests/golden/pg2adot_tree_relative_counts.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --view=tree-relative --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_tree_relative_sets.out"
"$PG2ADOT_BIN" --view=tree-relative --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_tree_relative_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_tree_relative_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --view=jurdzinski tests/games/ordered_two_children.pg > tests/golden/pg2adot_jurdzinski_counts.out"
"$PG2ADOT_BIN" --view=jurdzinski tests/games/ordered_two_children.pg > tests/golden/pg2adot_jurdzinski_counts.out 2>&1
sanitize_output "tests/golden/pg2adot_jurdzinski_counts.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --view=jurdzinski --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_jurdzinski_sets.out"
"$PG2ADOT_BIN" --view=jurdzinski --labels=sets --max-set-items=1 tests/games/ordered_two_children.pg > tests/golden/pg2adot_jurdzinski_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_jurdzinski_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN tests/games/priority_gap_start.pg > tests/golden/pg2adot_gap_original.out"
"$PG2ADOT_BIN" tests/games/priority_gap_start.pg > tests/golden/pg2adot_gap_original.out 2>&1
sanitize_output "tests/golden/pg2adot_gap_original.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --priority-mode=compact tests/games/priority_gap_start.pg > tests/golden/pg2adot_gap_compact.out"
"$PG2ADOT_BIN" --priority-mode=compact tests/games/priority_gap_start.pg > tests/golden/pg2adot_gap_compact.out 2>&1
sanitize_output "tests/golden/pg2adot_gap_compact.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --labels=sets tests/games/lifted_shape.pg > tests/golden/pg2adot_lifted_shape_sets.out"
"$PG2ADOT_BIN" --labels=sets tests/games/lifted_shape.pg > tests/golden/pg2adot_lifted_shape_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_lifted_shape_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --algorithm=zielonka --labels=sets tests/games/lifted_shape.pg > tests/golden/pg2adot_lifted_shape_zielonka_sets.out"
"$PG2ADOT_BIN" --algorithm=zielonka --labels=sets tests/games/lifted_shape.pg > tests/golden/pg2adot_lifted_shape_zielonka_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_lifted_shape_zielonka_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --tree-k=1 --labels=sets tests/games/strahler_two.pg > tests/golden/pg2adot_partial_sets.out"
"$PG2ADOT_BIN" --tree-k=1 --labels=sets tests/games/strahler_two.pg > tests/golden/pg2adot_partial_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_partial_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --tree-k=1 --view=tree-relative tests/games/strahler_two.pg > tests/golden/pg2adot_partial_tree_relative.out"
"$PG2ADOT_BIN" --tree-k=1 --view=tree-relative tests/games/strahler_two.pg > tests/golden/pg2adot_partial_tree_relative.out 2>&1
sanitize_output "tests/golden/pg2adot_partial_tree_relative.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --tree-file=tests/trees/one_child.tree --view=jurdzinski --labels=sets tests/games/ordered_two_children.pg > tests/golden/pg2adot_partial_jurdzinski_tree_file.out"
"$PG2ADOT_BIN" --tree-file=tests/trees/one_child.tree --view=jurdzinski --labels=sets tests/games/ordered_two_children.pg > tests/golden/pg2adot_partial_jurdzinski_tree_file.out 2>&1
sanitize_output "tests/golden/pg2adot_partial_jurdzinski_tree_file.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --adaptive-t --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_stats.out"
"$PG2ADOT_BIN" --adaptive-t --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_stats.out 2>&1
sanitize_output "tests/golden/pg2adot_adaptive_stats.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --adaptive-t=incremental --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_incremental_stats.out"
"$PG2ADOT_BIN" --adaptive-t=incremental --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_incremental_stats.out 2>&1
sanitize_output "tests/golden/pg2adot_incremental_stats.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --adaptive-t --max-host-leaves=1 --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_limit.out"
"$PG2ADOT_BIN" --adaptive-t --max-host-leaves=1 --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_limit.out 2>&1
sanitize_output "tests/golden/pg2adot_adaptive_limit.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --max-host-leaves=5 tests/games/strahler_two.pg > tests/golden/pg2adot_host_limit.out"
"$PG2ADOT_BIN" --max-host-leaves=5 tests/games/strahler_two.pg > tests/golden/pg2adot_host_limit.out 2>&1
sanitize_output "tests/golden/pg2adot_host_limit.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --tree-file=tests/trees/invalid.tree tests/games/strahler_two.pg > tests/golden/pg2adot_invalid_tree.out"
"$PG2ADOT_BIN" --tree-file=tests/trees/invalid.tree tests/games/strahler_two.pg > tests/golden/pg2adot_invalid_tree.out 2>&1
sanitize_output "tests/golden/pg2adot_invalid_tree.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --adaptive-t --tree-k=1 --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_capped.out"
"$PG2ADOT_BIN" --adaptive-t --tree-k=1 --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_adaptive_capped.out 2>&1
sanitize_output "tests/golden/pg2adot_adaptive_capped.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --kary=1 --labels=sets tests/games/strahler_two.pg > tests/golden/pg2adot_kary_partial_sets.out"
"$PG2ADOT_BIN" --kary=1 --labels=sets tests/games/strahler_two.pg > tests/golden/pg2adot_kary_partial_sets.out 2>&1
sanitize_output "tests/golden/pg2adot_kary_partial_sets.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --kary=2 --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_kary_stats.out"
"$PG2ADOT_BIN" --kary=2 --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_kary_stats.out 2>&1
sanitize_output "tests/golden/pg2adot_kary_stats.out" "$PG2ADOT_BIN"
echo "  $PG2ADOT_BIN --algorithm=zielonka --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_zielonka_stats.out"
"$PG2ADOT_BIN" --algorithm=zielonka --stats --player=even --labels=none tests/games/strahler_two.pg > tests/golden/pg2adot_zielonka_stats.out 2>&1
sanitize_output "tests/golden/pg2adot_zielonka_stats.out" "$PG2ADOT_BIN"

echo "  $PMS2DOT_BIN -h > tests/golden/pms_h.out"
"$PMS2DOT_BIN" -h > "tests/golden/pms_h.out" 2>&1 || true
sanitize_output "tests/golden/pms_h.out" "$PMS2DOT_BIN"

echo "  unordered progress measures | $PMS2DOT_BIN --check-order > tests/golden/pms_err_order.out"
echo -n "0,0|1,0|0,1|" | "$PMS2DOT_BIN" --check-order \
  > tests/golden/pms_err_order.out 2>&1 || true
sanitize_output "tests/golden/pms_err_order.out" "$PMS2DOT_BIN"

if [ -n "$LENSTREE_BIN" ]; then
  for ct in "${GENSTREE_CASES[@]}"; do
    read -r k t h <<< "$ct"
    name="len_k${k}_t${t}_h${h}.out"
    echo "  $LENSTREE_BIN -k $k -t $t -h $h > tests/golden/$name"
    "$LENSTREE_BIN" -k "$k" -t "$t" -h "$h" > "tests/golden/$name" 2>&1
    sanitize_output "tests/golden/$name" "$LENSTREE_BIN"
  done
fi

echo "Generating error case goldens..."
"$GENSTREE_BIN" -t 1 -h 2 > /dev/null 2> tests/golden/gen_err_k.out || true
sanitize_output "tests/golden/gen_err_k.out" "$GENSTREE_BIN"
"$GENSTREE_BIN" -k 0 -t 1 -h 2 > /dev/null 2> tests/golden/gen_err_k_val.out || true
sanitize_output "tests/golden/gen_err_k_val.out" "$GENSTREE_BIN"
"$GENSTREE_BIN" -k 2 -t 1 -h 2 -l 0 > /dev/null 2> tests/golden/gen_err_l.out || true
sanitize_output "tests/golden/gen_err_l.out" "$GENSTREE_BIN"
"$PMS2DOT_BIN" -x > /dev/null 2> tests/golden/pms_err_flag.out || true
sanitize_output "tests/golden/pms_err_flag.out" "$PMS2DOT_BIN"
if [ -n "$LENSTREE_BIN" ]; then
  "$LENSTREE_BIN" -k 1 > /dev/null 2> tests/golden/len_err_args.out || true
  sanitize_output "tests/golden/len_err_args.out" "$LENSTREE_BIN"
  "$LENSTREE_BIN" -k 0 -t 1 -h 2 > /dev/null 2> tests/golden/len_err_k.out || true
  sanitize_output "tests/golden/len_err_k.out" "$LENSTREE_BIN"
fi

echo "Done. Review and commit tests/golden/* if outputs are correct."
exit 0
