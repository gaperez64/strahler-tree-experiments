# Development and command reference

## Build and validation

Build commands and requirements are in [README.md](../README.md#build).

Run shell examples from the repository root. Every executable accepts
`--version`, using the Meson project version. Meson's
`vcs_tag()` runs `git describe --tags --always --dirty` in the source directory
on every build and appends ` (git <describe>)` when available; without Git or
`.git`, only the Meson version is printed.

CI checks formatting with clang-format 18, treats compiler and clang-tidy
warnings as errors, enforces 75% line coverage, and runs ASan/UBSan and
Valgrind separately. To run the memory check locally after building:

```sh
ci/check-valgrind.sh build
```

## Releases

Published GitHub releases build and test all seven commands, including
`lenstree`, on Ubuntu 24.04 x86_64 and macOS 15 arm64 with Apple Clang.
The release assets are `strahler-tree-experiments-<version>-linux-x86_64.tar.gz`
and `strahler-tree-experiments-<version>-macos-arm64.tar.gz`, each containing
`bin/`, README.md, LICENSE, and LICENSE-APACHE-2.0. Dispatch
[the release workflow](../.github/workflows/release.yml) with an existing tag
to rebuild and replace its assets.
Update the Meson project version before tagging so `--version` matches the release.

## Regenerating example trees

[DECOMP.md](../DECOMP.md) lists the trees for every PGSolver game in
`examples/` and reports differences in their shapes. [ALGOS.md](../ALGOS.md)
explains the algorithms and metrics. Edit ALGOS.md directly.

DOT/PNG trees, progress-measure leaf streams, run statistics with timings
removed (`.stats`), and final tree statistics (`.metrics`) are in
[decomp/](../decomp/). The inventory tables show nodes, leaves and height;
the Tree column links to all metrics, including Strahler, width and arity.
Both [DECOMP.md](../DECOMP.md) and [ALGOS.md](../ALGOS.md) define them.
Build release tools, then regenerate with Python 3.10+ (standard library only).
Graphviz is needed only for new or changed pictures:

```sh
meson setup build --reconfigure --buildtype=release -Db_ndebug=true
meson compile -C build pg2adot pg2pmdot
python3 scripts/gen_decomp.py
python3 scripts/gen_decomp.py --check
```

`--build-dir DIR` selects the binaries (default `build`); `--timeout SECONDS`
sets the safety timeout (default 600 per subprocess), and `--max-host-leaves N`
sets the host limit (default 10000). Set labels show at most 8 vertex IDs per
set. Every run verifies its winning regions and trees. Each adaptive run is
also checked against incremental adaptive lifting for the same outcome and
identical DOT; one copy of the tree is stored. Progress-measure leaf streams
keep their raw first-occurrence order.

The generator tries every backend on each game, with and without preprocessing
and, where supported, iterative shaving. It skips measured slow pairs listed
in `SKIP_RUNS` in `scripts/gen_decomp.py`. These have fixed
`skipped (> N s locally)` outcomes.
A safety timeout aborts generation with a non-zero exit before any outputs
are updated. Measure that pair locally before adding it to the skip list.
Host-limit runs keep statistics and inventory rows but discard all tree
output, including any partial tree returned by an adaptive run. There are
no vertex cutoffs.

PNG files contain a `dot-sha256` text chunk with the SHA-256 hash of their
DOT source. A valid PNG with a matching hash is reused unchanged, so
regenerating only the prose needs no Graphviz installation. New, missing or
stale pictures require Graphviz; `--dot PATH` selects its executable, with
`STRAHLER_DOT` as the environment default. The generator renders all needed
pictures before updating outputs, so a rendering failure leaves the checked-in
files untouched.

`--check` reruns the tools and reports missing, changed or obsolete outputs
without writing files or rendering pictures. It exits 0 when everything is
current and non-zero otherwise. It checks PNG integrity and the stored DOT hash;
different Graphviz versions may render the same DOT differently. CI checks
freshness on PRs and non-main pushes, and refreshes generated files on pushes
to `main`.

For new benchmarks, use `python3 scripts/make_trees.py GAME_OR_DIR...`.
It uses the same backend names, limits and metrics, but ignores the examples'
skip list. Adaptive backends run once, without the inventory's cold/incremental
comparison.
`--backends LIST` selects comma-separated DECOMP.md row names;
`--out DIR` defaults to `trees/`, with one game directory per unique stem and
`summary.csv` splitting Even/Odd metrics into separate columns. Every tree has
the same `.metrics` file as the inventory. The CSV includes each `.metrics`
field with `_even` and `_odd` suffixes, alongside wins, parameters, game
metadata, outcome and the DOT path. Means have three decimal places in both
formats; metrics and parameters describe the final round, while wins include
all shaving rounds and their attractors. The build, timeout, host-limit and
Graphviz options match `gen_decomp.py`; `--no-png` disables pictures, and missing
Graphviz only warns. Progress goes to stderr;
timeouts and solver errors are recorded per pair and cause a non-zero exit.
Multi-round progress-measure PNGs show each round in a separate panel.

## Command reference

Every command accepts `--help` (stdout, exit 0) and `--version`. Use exact
long option names and attach values with `=`: `--name=value`. Short options,
abbreviations, and space-separated option values are rejected. Invalid options
or values exit 2 with one error line and `Try '<prog> --help'.` on stderr.
Options precede input operands; `--` ends option parsing. Game files and `-`
for standard input remain positional inputs in `pg2adot` and `pg2pmdot`.

Migration: `genstree` and `lenstree` use `--strahler=K`, `--log-leaves=T`,
`--height=H`, and `--leaf=L` in place of `-k K`, `-t T`, `-h H`, and `-l L`.
`genstree` also replaces `-j`, `-d`, and `-p P` with `--count`, `--dot`, and
`--p-level=P`. `pgfilt -n` becomes `pgfilt --normalize`. Former `-h` help flags
become `--help`. `str-tree INDEX [P]` becomes `str-tree --index=INDEX [--p-level=P]`.

### `genstree`

Build `U^k_{t,h}` with required `--strahler=K --log-leaves=T --height=H`
(`1 <= K <= H`, `T >= 0`).
The default output is leaf labels as `Bits` and `Blocks`. Use `--count` for the
leaf count, `--leaf=L` for one leaf (1-based), `--dot` for DOT, or `--p-level=P`
to add p-level group sizes. Counts saturate at the `unsigned` maximum, reported as
"at least" that value. Use `--help` for the full option list.

```sh
./build/genstree --strahler=4 --log-leaves=2 --height=4 --count
./build/genstree --strahler=4 --log-leaves=2 --height=4 --dot | dot -Tsvg > tree.svg
```

### `lenstree`

The Boost-based implementation computes leaf counts and individual leaf
labels. It is built when Boost is available. `--strahler=K`, `--log-leaves=T`,
and `--height=H` are required. It prints the count by default; `--leaf=L`
selects one leaf (1-based).

```sh
./build/lenstree --strahler=4 --log-leaves=2 --height=4
./build/lenstree --strahler=4 --log-leaves=2 --height=4 --leaf=3
```

### `pms2dot`

Read one line of progress-measure branches from standard input and write
their prefix tree as DOT. A branch is a comma-separated vector of bitstrings
ending in `|`; use `e` for an empty bitstring. Input order is preserved by
default.

`--check-order` rejects branches that are out of order. `--reorder` sorts them
before building the tree. These options are mutually exclusive. Bitstrings
use the paper's binary-tree order `0β < ε < 1β`, applied recursively after
equal leading bits. Vectors use the lexicographic order induced by that
bitstring order.

```sh
printf '00,e|0,e|e,e|10,e|1,e|\n' | ./build/pms2dot --check-order > tree.dot
printf '1,0|e,1|0,1|e,0|\n' | ./build/pms2dot --reorder > sorted-tree.dot
```

### `pgfilt`

Read and check one PGSolver game from standard input. By default, `pgfilt`
prints vertex/edge counts, maximum priority, owner counts and external ID
range. Use `--normalize` to print the game in a consistent PGSolver format.
An optional `start ID;` line is accepted and ignored.

Priorities are left unchanged by default. Use `--priority-mode=compact` to
remove unnecessary gaps while keeping their order and parity. Distinct
priorities remain distinct.

```sh
./build/pgfilt < game.pg
./build/pgfilt --normalize < game.pg > normalized.pg
./build/pgfilt --priority-mode=compact --normalize \
  < game.pg > compact.pg
```

### `pg2adot`

Compute and check attractor decompositions of a PGSolver game and write
them as DOT. Pass a file name, `-`, or no file name; the latter two read from
standard input. The default algorithm is attractor-decomposition lifting.

- `--player=both|even|odd` selects the trees to print (default `both`).
- `--view=classic|tree-relative|jurdzinski` selects how the decomposition is
  drawn. The default is `classic`.
- `--labels=counts|sets|none` selects node and edge labels (default `counts`).
- `--max-set-items=N` limits vertex IDs per set label (default 32).
- `--priority-mode=original|compact` selects the priority bounds shown in the
  tree. The default is `original`.
- `--algorithm=lifting|zielonka|zielonka-sym|lifting-sym` selects the solver;
  the default is `lifting`. `zielonka` runs enhanced Zielonka. All four share
  preprocessing, statistics and verification.
- `--initial-shave=LIST` solves and removes dominions before building either tree.
  Use a comma list of `single` (all remaining priorities have one parity),
  `loops` (winning self-loops, including forced losing-owner loops), and
  `wcwc` (winner-controlled winning cycles), or `all` / `none` alone.
  The default is `none`. Each discovered dominion is removed with its winner's
  attractor in the current game. Rules run in the order single, loops, wcwc,
  repeating to a fixpoint as removals expose further dominions.
- `--iter-shave` attracts and removes certified dominions after lifting
  stabilises. Fixed hosts are reused until complete or a round makes no
  progress; both adaptive modes advance to the next t on the smaller game.
  It also supports `lifting-sym`; Zielonka variants reject it. DOT retains
  each shaved region's round, adaptive t, and certified decomposition, plus
  the final residual decomposition. Verification replays the certificates
  and attractors; `--stats` lists rounds and vertices shaved per round.
  Restricted hosts can still end partial. `--shave` has been removed in
  favour of `--initial-shave`; there is no alias.
- `--compress` merges consecutive distinct priorities of the same parity,
  following Oink's priority compression. This is stronger than gap removal.
  `--priority-mode` still controls only display: in `original` mode a merged
  level shows its largest original priority, and an intervening empty
  bound shows that priority plus the compact offset.
- `--tree-k=K` lifts in the smaller Strahler host `U^K_{t,H}`. The result may
  be partial.
- `--adaptive-t` lifts in `U^K_{t,H}` with `t = 0, 1, ...` and the largest
  useful `K = min(H, t + 1)` until the result is complete. It reports the
  smallest such `t` on standard error, together with the smallest `t` at which
  each player's whole winning region was found. `--start-t=T` starts the
  search at `T`, and `--tree-k=K` caps `K`; a capped search can end partial.
  Both adaptive modes require `--algorithm=lifting`.
- `--adaptive-t=incremental` uses certified opponent wins as TOP seeds. It
  produces exactly the same least labellings and trees at every tried host as
  `--adaptive-t`, usually with fewer lifts. Bare `--adaptive-t` starts each
  host from bottom. Adaptive `--stats` includes `total_lifts` across all
  tried hosts.
  See [the incremental analysis](incremental-t.md) for proofs and results.
- `--kary=A` lifts in the full `A`-ary tree with each player's full height
  `H`, which is not bounded by a Strahler number. The result may be partial;
  it is complete when `A` is at least the number of vertices.
- `--tree-file=FILE` lifts in the ordered tree stored in `FILE` in the
  leaf-stream format that `pms2dot` reads, such as `0|1|`. The result may be
  partial.
- `--max-host-leaves=N` refuses to build Strahler or `A`-ary hosts with more
  than `N` leaves. The default is 1000000. With `--adaptive-t`, a later host
  limit stops the search with a warning and keeps the previous certificates
  as partial. A limit before both players have run is an error.
- `--stats` prints statistics to standard error. Ordinary lifting reports each
  player's host and its size, rounds, vertex lifts, vertices left at the top,
  and the size and Strahler number of each decomposition. Zielonka adds
  nonempty calls and attractor counts to region sizes and tree metrics.
  Symmetric variants report calls, attractors, Move/Set counts, certification
  lifts and the Even separator size; `lifting-sym` also reports host sizes.
  With preprocessing, it also reports residual and shaved sizes and counts per
  rule, including attracted vertices; a vertex is counted only against the
  rule that removed it.
- `--no-verify` skips the decomposition and shaved-region closure checks and
  is intended for debugging.

Verification is on by default; shaving, compression and statistics are off.
Host choices are mutually exclusive, except `--tree-k` can cap adaptive `K`.
`--start-t` requires adaptive search. Both Zielonka variants reject host options.

`--algorithm=zielonka-sym` runs McNaughton-Zielonka with memory (Algorithm 8
of Thejaswini Raghavan's thesis). It keeps both players' decomposition labellings
across recursive calls and starts with trivial decompositions. Complete n-ary
hosts are represented lazily, so only visited nodes consume space. It always
returns both winning regions with decompositions and accepts no host options.

`--algorithm=lifting-sym` runs Algorithm 9 with asymmetric certification
(thesis §8.3). It uses the default, `--tree-k`, `--kary` or `--tree-file` hosts and
leaf limit. Both `--adaptive-t` and `--adaptive-t=incremental` are rejected:
Algorithm 9 runs on a fixed pair of hosts. With restricted hosts, Theorem F's
returned set is only a separator: final short lifts certify the two dominions,
leaving other vertices Unresolved. Universal hosts give complete results.

By default, `pg2adot` lifts in a Strahler tree that is guaranteed to contain a
decomposition of each winning region, so the result is complete. That host
grows quickly: for thousands of vertices and more than a few priorities it
exceeds the leaf limit, and `pg2adot` stops with an error. Use `--adaptive-t`,
`--tree-k`, `--kary`, or `--algorithm=zielonka` for such games.

`pg2adot` removes priority gaps internally before solving, so large numeric
gaps do not add empty levels or exhaust the recursion limit. It still shows
bounds on the original priority scale by default. Use
`--priority-mode=compact` to show the internal bounds instead.

With shaving, roots and tree metrics describe only the residual game. A shaded
`shaved (Even)` / `shaved (Odd)` node attached to the corresponding root reports
the solved vertices separately, including their IDs with `--labels=sets`.
An empty residual is a complete result with no decomposition; shaved vertices
count as won when deciding completeness. Verification checks the residual
decomposition and, in the full game, that shaved regions are closed under their
winner's attractor and that the loser cannot force an exit. The rules establish
their winning parity. The implementation follows the behavior of
[Oink](https://github.com/trolando/oink) (Apache-2.0); cycle searches use
the shared attractor code in place of Oink's SCC implementation.

```sh
./build/pg2adot game.pg > decomposition.dot
./build/pg2adot --adaptive-t --stats game.pg > decomposition.dot
./build/pg2adot --tree-k=1 --labels=sets game.pg > dominions.dot
./build/pg2adot --priority-mode=compact game.pg > compact.dot
./build/pg2adot --player=both --labels=sets --max-set-items=8 game.pg \
  | dot -Tsvg > decomposition.svg
./build/pg2adot --view=tree-relative --labels=sets game.pg \
  | dot -Tsvg > tree-relative.svg
./build/pg2adot --view=jurdzinski --labels=sets game.pg \
  | dot -Tsvg > jurdzinski.svg
```

Small sample games are in `tests/games/`:

```sh
./build/pg2adot tests/games/ordered_two_children.pg
```

### `pg2pmdot`

Lift Strahler or succinct progress measures and draw the ordered prefix tree
of each player's distinct non-top final measures. Leaves show the vertices
holding that measure. The tool reads a PGSolver file, `-`, or standard input.
`--format=dot|leaves` defaults to `dot`.

```sh
./build/pg2pmdot --algorithm=strahler --labels=sets game.pg > measures.dot
./build/pg2pmdot --algorithm=succinct --stats game.pg > measures.dot
./build/pg2pmdot --k=1 --t=1 game.pg > partial.dot
./build/pg2pmdot --algorithm=succinct --bits=0 game.pg > partial.dot
./build/pg2pmdot --format=leaves game.pg
./build/pg2pmdot --iter-shave --initial-shave=all --compress game.pg
```

`--algorithm=strahler|succinct` defaults to `strahler`. Both algorithms share
`pg2adot`'s `--player`, `--labels`, `--max-set-items`, `--priority-mode`,
`--initial-shave`, `--compress`, `--stats`, `--no-verify`, and `--version` options.
Priorities are made gap-free internally. DOT's `p` labels identify the counter
priority of each component, on the original scale by default. Preprocessing
keeps shaved vertices in separate shaded nodes; they have no progress measure.
An empty residual produces empty trees and empty leaf streams.

By default, each player starts from bottom on the full residual game at every
parameter choice. Neither player's dominion is removed before the other's
run. Search stops at the first choice whose non-top sets cover the residual.
Oink's counter player is the opponent of the winner named on our tree:
Even's tree uses odd counters and Odd's tree uses even counters.

Strahler search starts at `(k,t)=(1,1)` and uses Oink's priority queue with its
integer `max(k,t)/min(k,t)` comparison, pushing `(k+1,t)` before `(k,t+1)`.
`t_max=floor(log2(n))`. Full-game mode bounds `k` by
`min(t_max+2, max_depth+1)`, including the measure tree's extra root.
This bound is one level larger than Oink's outer search limit. Oink's
smaller limit can depend on attraction/removal to solve vertices that never
receive a finite measure, even at the final parameters. For example, after
`--compress`, `strahler_two.pg` needs `k=2` to give every winner a measure,
although Oink's outer limit is `k=1`. Each run caps `k` at its own
`depth+1`. Succinct search uses Oink's bounded schedule, starting at one
bit and increasing through `ceil(log2(n))`; zero/one-vertex games also support
a zero-bit budget. Depth is the number of counter-parity levels, including
empty intervening levels.

`--k=K --t=T` fixes Strahler parameters; `--bits=B` fixes succinct's budget.
These results may be partial. Roots say `partial` and, with `--player=both`,
a dashed Unresolved node lists the remaining vertices. `--stats` reports the
chosen parameters, depths, vertex counts, lifts, attempts and top counts on
standard error. Verification checks the actual truncated progress condition
on every edge (one successor for the winner, all for its opponent) and checks
dominion closure using the shared attractor code.

`--iter-shave` (formerly `--incremental`, with no alias) follows Oink's
removal order: run odd counters first, remove Even's non-top dominion and its
attractor, then run even counters on the remaining game. It prints a separate
DOT graph for every round. Roots
show that round's parameters; an `attracted` node lists removed vertices that
have no finite measure. Succinct repeats a bit budget if it made progress;
Strahler keeps Oink's original outer bound
`k_max=min(t_max+2,max_depth)` and can end partial when that search is
exhausted. Fixed parameters request just one round. Each graph describes that
round's residual; the trees do not accumulate wins from earlier rounds.

`--format=leaves` prints `even: ` and `odd: ` lines, with `e` for an empty
bitstring and `|` after each distinct measure. Remove the player prefix to
feed one line to `pms2dot --reorder`. Raw streams retain Oink's first occurrence
order in ascending (priority, external ID) vertex order. DOT sorts branches in the paper's order
`0β < ε < 1β`. Oink's unspecified tie ordering, its preprocessing, and its
last-residual-only printer can make other byte comparisons differ. Incremental
leaf output adds `# round ...` parameter lines before each pair of streams.

An optional live differential test compares both backends with pinned Oink
on seeded random games and quick examples. Set `OINK_BIN` and run
`meson test -C build oink-oracle --print-errorlogs`; see
[the oracle instructions](../tests/README.md#live-oink-oracle) for the required
upstream printer fixes and known Strahler search limit.

### `str-tree`

Check p-level successors in the tree compiled into `src/str-tree.cc`.
Use `--help` to list its options.

- With no arguments, check every leaf and its successor.
- With `--index=INDEX`, check one leaf.
- With `--index=INDEX --p-level=P`, compute that leaf's p-level successor.

`INDEX` is zero-based. `--p-level` requires `--index` and defaults to `h - 2`;
an explicit `P` must be between 0 and `h - 1`.

To compile a different generated tree into this command:

```sh
./build/genstree --strahler=3 --log-leaves=2 --height=5 --p-level=2 > examples/k3t2h5p2.hpp
python3 src/convert_out.py examples/k3t2h5p2.hpp
```

Fill in `k`, `t`, `h`, and `p` in the generated header. Update the example
include in `src/str-tree.cc` and rebuild.

Comments A through H in `src/str-tree.cc` refer to the case analysis on
page 19 of [the paper](https://arxiv.org/pdf/2003.08627).

## Reading attractor decompositions

### Complete and partial results

The default host, `--algorithm=zielonka`, and `--algorithm=zielonka-sym` always
give a complete result: the Even and Odd roots decompose the two winning
regions. A restricted host from `--tree-k`, `--kary`, `--tree-file`, or a capped
or interrupted `--adaptive-t` search still certifies that each root region is
won by its player, but it may leave some vertices unresolved. The result is
complete exactly when the two regions cover the game, even with a restricted host.

Partial roots use `D` for a certified dominion; complete roots use `W` for
the winning region. `result (synthetic; partial)` connects partial roots.
With `--player=both`, a dashed `Unresolved` node lists the remaining vertices
as `U`, without attributing them to either player. A player without a certified
dominion is shown as `D = empty; no certified dominion`.

### Classic view

Each Even or Odd root is the decomposition of that player's winning region, or
of its certified dominion `D` in a partial result.
The `result (synthetic)` node only connects the two roots when
`--player=both` is used. If a player has an empty winning region, its box says
`W=empty; no decomposition`.

Node labels describe the subtree rooted at that box:

| Label | Meaning |
| --- | --- |
| `Even` or `Odd` | The player whose decomposition this is. |
| `d` | The priority bound at this node. It has the same parity as the player. By default it uses the game's original priority scale. |
| `W` | The vertices in this node's subgame. At a root, this is the player's winning region. |
| `A` | The player's attractor within `W` to vertices with priority `d`. This can be empty if priority `d` does not occur. |
| `nodes`, `leaves` | The numbers of nodes and leaves in the complete Even or Odd tree. These totals are shown only at the root. |
| `height` | The number of nodes on the tree's longest root-to-leaf path. It is shown only at the root. |
| `Strahler` | The Strahler number of the complete Even or Odd tree. It is shown only at that tree's root. |

An edge labelled `i`, `S_i`, and `A_i` records one decomposition step:

| Label | Meaning |
| --- | --- |
| `i` | The step number. Children are shown in the order in which they were removed. |
| `S_i` | The child subgame, which is a trap for the other player. The child node's `W` is this same set. |
| `A_i` | The current player's attractor to `S_i` in the vertices remaining at step `i`. It is removed before the next step. |

With `--labels=counts`, vertical bars give set sizes: for example, `|W|=3`
means that `W` contains three vertices. With `--labels=sets`, `W={...}` also
lists their PGSolver vertex IDs. A suffix such as `+5 more` means that
`--max-set-items` hid five IDs. With `--labels=none`, nodes show only the player
and `d`, and edges have no labels.

If the input priorities contain gaps, consecutive tree nodes can have `d`
values that differ by more than two. The missing values would only create
empty levels, so they are not included. The reported node count, height, and
Strahler number describe this gap-free tree. With
`--priority-mode=compact`, child bounds decrease by two as usual.

DOT uses Graphviz's HTML-like labels for variables and subscripts.
`dot` renders them directly without LaTeX or dot2tex.

The reported Strahler number belongs to the tree that `pg2adot` built. The
command does not search for the smallest value over every possible
decomposition. Lifting and Zielonka can build different trees for the same
game; `tests/games/lifted_shape.pg` is an example.

[The disagreement study](disagreements.md) compares shapes and vertex
sets, with seeded generators, shrinking, and paired canonical goldens in
`tests/games/disagree_*.pg` and `tests/golden/disagree_*.json`.

### Tree-relative view

`--view=tree-relative` shows the same tree and priority bounds using the
notation from Section 6.1 of
[Thejaswini Raghavan's thesis](https://thejaswiniraghavan.github.io/PhD_Thesis.pdf).
The decomposition and its size stay the same; only the labels change.

At each node, the displayed sets form the disjoint partition
`V = H + T + R_1 + ... + R_k + S`:

| Label | Meaning |
| --- | --- |
| `V` | The region represented by this node. At a root it is the player's winning region. At a child it is the `R_i` set on the incoming edge. |
| `H` | Vertices in the node's core whose priority is `d`. |
| `T` | The other vertices in the player's attractor to `H`, computed inside the core. |
| `R_i` | The region passed to child `i`. It is a trap for the other player in the region remaining at that step. |
| `S` | The part of `V` outside the core. |

The core itself is `H + T + R_1 + ... + R_k`. The verifier checks this
partition, the attractors, the traps, and every recursive child. Here, "trap"
means a trap for the other player. This matches the construction in Algorithm
5 and its correspondence with classic attractor decompositions; the player
name in the prose definition in Section 6.1 points in the opposite direction.

For example, the first child in `ordered_two_children.pg` is shown as
`R_1={1,2}`. Its node has `V={1,2}`, `H={1}`, `T={}`, and `S={2}`.

### Jurdziński view

`--view=jurdzinski` expands the decomposition into the `leafy(T)` shape from
the attractor-decomposition lifting description. Nodes have simple labels
on priority levels, in place of tables.

For an Even decomposition:

- A box at even level `d` contains `H`, the vertices whose priority is exactly
  `d`.
- The `−∞` ellipse one level below contains `T`, the rest of the attractor to
  `H`.
- A numbered box is a recursive child two levels below its parent.
- The `i+` ellipse immediately after child `i` contains `S_i`, the part of the
  child's attractor outside its recursive subgame.

Thus boxes contain vertices of their exact level, while ellipses may contain
vertices of that level or lower. Odd decompositions use the same construction
with the parities reversed. Empty added leaves are omitted from the drawing.
A box with no numbered children has no `S_i` ellipses, but it may still have a
nonempty `T` ellipse one level below it.
The root summary reports the size and Strahler number of the base tree `T`,
before these leaves are added.

The row labels use the compact levels that define the tree, so adjacent rows
differ by one. With the default `--priority-mode=original`, a row also shows
its source priority bound when that number differs from its compact level.

With the default `--algorithm=lifting`, these nodes are exactly the parts of
the lifting host that the final labelling occupies; see
[attractor-decomposition lifting](#attractor-decomposition-lifting).
In a partial result the root reads `Even dominion` or `Odd dominion`.

## Implementation notes

### Attractor-decomposition lifting

`pg2adot` follows the lifting formulation of attractor decompositions from
[A symmetric attractor-decomposition lifting algorithm for parity
games](https://arxiv.org/abs/2010.08288), run separately for each player `P`.
The code is split into these parts:

| File | Role |
| --- | --- |
| `src/pg_attractor.c` | `pg_attractor_through`: reach a target while staying in a safe set that need not be total. |
| `src/ad_lift_tree.c` | The host tree `leafy_∞(T)`, flattened into its depth-first order. |
| `src/ad_lift.c` | The lifting loop, a direct labelling verifier, and materialization. |
| `src/ad_lift_solve.c` | Host selection, both players, and the complete or partial result. |

The base ordered tree `T` is the host or search tree. Each regular
node `η` has a level of `P`'s parity, two below its parent. The host adds a
`−∞` leaf below `η`, a `c+` leaf after each child `c`, and a top element `∞`.
In depth-first order the block of `η` is `η, −∞(η), block(c_1), c_1+, ...,
block(c_m), c_m+`, and `after(η)` is `η+`, or `∞` at the root. The `−∞` and
`c+` leaves lie one level below `η`.

A labelling maps each vertex to a host position. It must be
priority compatible: a regular position holds exactly its level, a `−∞` or
`c+` position holds priorities up to its level, and `∞` holds anything. A
vertex `v` labelled `μ(v)` is valid when:

- at a regular `η`, its edges to vertices labelled below `after(η)` are
  allowed, and `v` has one allowed edge if `P` owns it and only allowed edges
  otherwise;
- at a `−∞` or `c+` position `ℓ`, `P` can force a visit to `{μ < ℓ}` without
  leaving `{μ ≤ ℓ}`. An opponent edge out of `{μ ≤ ℓ}` is an escape, so this is
  `pg_attractor_through` and not `pg_attractor` on the safe set;
- at `∞`, always.

Starting from the least compatible labelling, each round
evaluates every vertex against the same labelling and moves every invalid
vertex to its next compatible position. If `ν` is any valid labelling with
`μ ≤ ν`, an invalid vertex `v` is valid at `ν(v)` when the others keep their
smaller `μ` labels, because lower labels only relax the regular test and only
enlarge the lazy target and safe sets. Hence `μ(v) < next(v) ≤ ν(v)`, and the
round keeps `μ ≤ ν`. The loop ends with every vertex valid, so its result is
the least valid labelling. `AD_LIFT_SCHEDULE_SINGLE` lifts one vertex at a
time and reaches the same labelling; the tests compare the two.

For any host, the vertices below `∞` form a dominion `D_P(T)` of
`P`. With `H` regular levels, the Strahler tree `U^K_{t,H}` contains every
ordered tree with fewer than `2^(t+1)` leaves, height `H`, and Strahler number
at most `K`. A decomposition of a region with `n` vertices has at most `n`
leaves, so with `t_full = ⌊log₂ n⌋` and `K = k_full = min(H, t_full + 1)` the
host contains a decomposition of `P`'s winning region, and `D_P` is that whole
region. `--adaptive-t` asks for the smallest `t` for which
`U^{min(H,t+1)}_{t,H}` already suffices. The full `n`-ary tree of height `H`
is universal for the same reason: no node of such a decomposition has more
than `n` children. Smaller hosts give possibly smaller dominions. Player `P`'s root
level is the least level of `P`'s parity that bounds all priorities, as in the
Zielonka solver.

For a regular node `η`, the classic decomposition node
has `A = fibre(η) ∪ fibre(−∞(η))`. For each child `c`, the trap `S_i` holds the
vertices labelled in `[c, after(c))`, and the attractor `A_i` adds
`fibre(c+)`. Empty host branches are pruned. In the least labelling, a vertex
in the block of a child `c` of `η` never has a `P` edge, or only opponent
edges, to labels before `c`; otherwise it would be valid at the position just
before `c`. This makes each `S_i` an opponent trap in the remaining vertices
and each `A_i` its attractor. `ad_lift_solve` checks the labelling directly
with `ad_lift_verify` and the materialized trees with both `ad_tree_verify`
and `ad_tree_relative_verify`.

### Symmetric algorithms and thesis correspondence

`src/ad_sym.c` shares the player-swapped recursion for thesis Algorithms 8
and 9. Algorithm 8 uses lazy complete hosts; Algorithm 9 uses supplied hosts
and `ad_lift_continue` to certify its final labels without resetting progress.
[The thesis correspondence and corrected entry invariant](symmetric.md)
cover errata, the added trap-closure operation, proofs and debug checks.
