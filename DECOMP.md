# Decompositions

This page is generated; do not hand-edit it. See the [regeneration instructions](docs/developing.md#regenerating-example-trees).

The tables list each example game and the trees found by each backend.
[ALGOS.md](ALGOS.md) explains how the trees are built, their metrics and search parameters.

Read paired values as Even / Odd, including the parameters. Won counts include vertices
solved during preprocessing. Tree metrics cover the remaining game: decomposition trees
or the occupied progress-measure trees, including their extra root. Heights count nodes.
Empty trees have zero metrics; connector boxes, preprocessed regions and unresolved
vertices do not count. These are the metrics of the trees found, with no guarantee
that their Strahler numbers are the smallest possible.

A `complete` result assigns every vertex to a winner. A `partial` result proves wins
for the listed vertices and leaves the rest unresolved. A `host limit` means the search
tree exceeded the allowed size; statistics are kept, without a tree. A `skipped` row
records a method whose earlier local run exceeded the time shown. Unknown winning
counts are `?`; a dash means no value or tree is available. Each backend name links
to its run statistics. PNG links open the pictures; DOT links open their graph descriptions,
and leaves links list the distinct progress measures.

## Preprocessing and shaving

The `+pre` rows pass `--initial-shave=all --compress` before running the selected solver:

1. Compress priority gaps and merge consecutive distinct priorities of the same parity, preserving winners. Choose the levels from the full input and keep them fixed throughout shaving.
2. Shave simple winning regions in this order: all remaining vertices if their priorities have one parity; winning self-loops whose owner matches their priority's parity or whose loop is the only remaining move; cycles whose vertices are all owned by one player and whose highest priority has that player's parity. Remove each region's attractor too, Even before Odd: these are the vertices from which its winner can force play into the region. Repeat the rules until a full pass removes nothing.
3. Run the solver on the remainder. Shaved regions appear separately and count towards Won, once per vertex, but are excluded from tree metrics. If nothing remains, the result is complete with empty trees. Displayed priorities normally use the original scale; a merged level uses its largest original priority.

Adaptive solvers use the remainder's priority and size bounds. Compression and shaving can lower these bounds, allowing lower t values and smaller hosts.

The `+iter` rows add `--iter-shave`, available only for lifting-based backends, including progress measures. After lifting stabilises, remove certified dominions and their attractors, then retry the remainder. Fixed hosts are reused; adaptive lifting advances to the next t on the smaller game, keeping the initial residual's host bounds. Shaved rounds show the round and t that certified them; progress measures print a graph per round with its parameters. Won counts all rounds and initial shaving, including attracted vertices, once each. Tree metrics and parameters describe only the final round: the residual decomposition or occupied measure tree, excluding earlier certificates and attracted vertices. `+pre+iter` combines both steps.

Source: [Oink, TACAS 2018](https://arxiv.org/abs/1801.03859), trivial dominions and priority compression.

## Inventory

### Button.tlsf.ehoa.pg

| Vertices | Edges | Distinct priorities | Maximum priority | Won (Even / Odd) |
| ---: | ---: | ---: | ---: | --- |
| 7 | 10 | 3 | 4 | 4 / 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Strahler E / O | Parameters E / O | Tree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [lifting](decomp/Button.tlsf.ehoa/lifting.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting.png) · [DOT](decomp/Button.tlsf.ehoa/lifting.dot) |
| [lifting+pre](decomp/Button.tlsf.ehoa/lifting+pre.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting+pre.png) · [DOT](decomp/Button.tlsf.ehoa/lifting+pre.dot) |
| [lifting+iter](decomp/Button.tlsf.ehoa/lifting+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting+iter.dot) |
| [lifting+pre+iter](decomp/Button.tlsf.ehoa/lifting+pre+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting+pre+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting+pre+iter.dot) |
| [lifting-adaptive](decomp/Button.tlsf.ehoa/lifting-adaptive.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=1, t=0 / H=2, K=1, t=0 | [PNG](decomp/Button.tlsf.ehoa/lifting-adaptive.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-adaptive.dot) |
| [lifting-adaptive+pre](decomp/Button.tlsf.ehoa/lifting-adaptive+pre.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=1, t=0 / H=2, K=1, t=0 | [PNG](decomp/Button.tlsf.ehoa/lifting-adaptive+pre.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-adaptive+pre.dot) |
| [lifting-adaptive+iter](decomp/Button.tlsf.ehoa/lifting-adaptive+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=1, t=0 / H=2, K=1, t=0 | [PNG](decomp/Button.tlsf.ehoa/lifting-adaptive+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-adaptive+iter.dot) |
| [lifting-adaptive+pre+iter](decomp/Button.tlsf.ehoa/lifting-adaptive+pre+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=1, t=0 / H=2, K=1, t=0 | [PNG](decomp/Button.tlsf.ehoa/lifting-adaptive+pre+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-adaptive+pre+iter.dot) |
| [lifting-sym](decomp/Button.tlsf.ehoa/lifting-sym.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting-sym.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-sym.dot) |
| [lifting-sym+pre](decomp/Button.tlsf.ehoa/lifting-sym+pre.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting-sym+pre.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-sym+pre.dot) |
| [lifting-sym+iter](decomp/Button.tlsf.ehoa/lifting-sym+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting-sym+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-sym+iter.dot) |
| [lifting-sym+pre+iter](decomp/Button.tlsf.ehoa/lifting-sym+pre+iter.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | H=2, K=2, t=2 / H=2, K=2, t=2 | [PNG](decomp/Button.tlsf.ehoa/lifting-sym+pre+iter.png) · [DOT](decomp/Button.tlsf.ehoa/lifting-sym+pre+iter.dot) |
| [pm-strahler](decomp/Button.tlsf.ehoa/pm-strahler.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-strahler.png) · [DOT](decomp/Button.tlsf.ehoa/pm-strahler.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-strahler.leaves) |
| [pm-strahler+pre](decomp/Button.tlsf.ehoa/pm-strahler+pre.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-strahler+pre.png) · [DOT](decomp/Button.tlsf.ehoa/pm-strahler+pre.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-strahler+pre.leaves) |
| [pm-strahler+iter](decomp/Button.tlsf.ehoa/pm-strahler+iter.stats) | complete | 4 / 3 | 0 / 5 | 0 / 3 | 0 / 3 | 0 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-strahler+iter.png) · [DOT](decomp/Button.tlsf.ehoa/pm-strahler+iter.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-strahler+iter.leaves) |
| [pm-strahler+pre+iter](decomp/Button.tlsf.ehoa/pm-strahler+pre+iter.stats) | complete | 4 / 3 | 0 / 5 | 0 / 3 | 0 / 3 | 0 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-strahler+pre+iter.png) · [DOT](decomp/Button.tlsf.ehoa/pm-strahler+pre+iter.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-strahler+pre+iter.leaves) |
| [pm-succinct](decomp/Button.tlsf.ehoa/pm-succinct.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-succinct.png) · [DOT](decomp/Button.tlsf.ehoa/pm-succinct.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-succinct.leaves) |
| [pm-succinct+pre](decomp/Button.tlsf.ehoa/pm-succinct+pre.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-succinct+pre.png) · [DOT](decomp/Button.tlsf.ehoa/pm-succinct+pre.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-succinct+pre.leaves) |
| [pm-succinct+iter](decomp/Button.tlsf.ehoa/pm-succinct+iter.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-succinct+iter.png) · [DOT](decomp/Button.tlsf.ehoa/pm-succinct+iter.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-succinct+iter.leaves) |
| [pm-succinct+pre+iter](decomp/Button.tlsf.ehoa/pm-succinct+pre+iter.stats) | complete | 4 / 3 | 2 / 5 | 1 / 3 | 2 / 3 | 1 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/Button.tlsf.ehoa/pm-succinct+pre+iter.png) · [DOT](decomp/Button.tlsf.ehoa/pm-succinct+pre+iter.dot) · [leaves](decomp/Button.tlsf.ehoa/pm-succinct+pre+iter.leaves) |
| [zielonka](decomp/Button.tlsf.ehoa/zielonka.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | — / — | [PNG](decomp/Button.tlsf.ehoa/zielonka.png) · [DOT](decomp/Button.tlsf.ehoa/zielonka.dot) |
| [zielonka+pre](decomp/Button.tlsf.ehoa/zielonka+pre.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | — / — | [PNG](decomp/Button.tlsf.ehoa/zielonka+pre.png) · [DOT](decomp/Button.tlsf.ehoa/zielonka+pre.dot) |
| [zielonka-sym](decomp/Button.tlsf.ehoa/zielonka-sym.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | — / — | [PNG](decomp/Button.tlsf.ehoa/zielonka-sym.png) · [DOT](decomp/Button.tlsf.ehoa/zielonka-sym.dot) |
| [zielonka-sym+pre](decomp/Button.tlsf.ehoa/zielonka-sym+pre.stats) | complete | 4 / 3 | 1 / 2 | 1 / 1 | 1 / 2 | 1 / 1 | — / — | [PNG](decomp/Button.tlsf.ehoa/zielonka-sym+pre.png) · [DOT](decomp/Button.tlsf.ehoa/zielonka-sym+pre.dot) |

### FairSchedulern=2_compact.gm

| Vertices | Edges | Distinct priorities | Maximum priority | Won (Even / Odd) |
| ---: | ---: | ---: | ---: | --- |
| 5596 | 130825 | 13 | 4947802324994 | 5596 / 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Strahler E / O | Parameters E / O | Tree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [lifting](decomp/FairSchedulern=2_compact/lifting.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+pre](decomp/FairSchedulern=2_compact/lifting+pre.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+iter](decomp/FairSchedulern=2_compact/lifting+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+pre+iter](decomp/FairSchedulern=2_compact/lifting+pre+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-adaptive](decomp/FairSchedulern=2_compact/lifting-adaptive.stats) | complete | 5596 / 0 | 29 / 0 | 6 / 0 | 8 / 0 | 2 / 0 | H=8, K=2, t=1 / H=8, K=2, t=1 | [PNG](decomp/FairSchedulern=2_compact/lifting-adaptive.png) · [DOT](decomp/FairSchedulern=2_compact/lifting-adaptive.dot) |
| [lifting-adaptive+pre](decomp/FairSchedulern=2_compact/lifting-adaptive+pre.stats) | complete | 5596 / 0 | 17 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | [PNG](decomp/FairSchedulern=2_compact/lifting-adaptive+pre.png) · [DOT](decomp/FairSchedulern=2_compact/lifting-adaptive+pre.dot) |
| [lifting-adaptive+iter](decomp/FairSchedulern=2_compact/lifting-adaptive+iter.stats) | complete | 5596 / 0 | 22 / 0 | 5 / 0 | 7 / 0 | 2 / 0 | H=8, K=2, t=1 / H=8, K=2, t=1 | [PNG](decomp/FairSchedulern=2_compact/lifting-adaptive+iter.png) · [DOT](decomp/FairSchedulern=2_compact/lifting-adaptive+iter.dot) |
| [lifting-adaptive+pre+iter](decomp/FairSchedulern=2_compact/lifting-adaptive+pre+iter.stats) | complete | 5596 / 0 | 17 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | [PNG](decomp/FairSchedulern=2_compact/lifting-adaptive+pre+iter.png) · [DOT](decomp/FairSchedulern=2_compact/lifting-adaptive+pre+iter.dot) |
| [lifting-sym](decomp/FairSchedulern=2_compact/lifting-sym.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+pre](decomp/FairSchedulern=2_compact/lifting-sym+pre.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+iter](decomp/FairSchedulern=2_compact/lifting-sym+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+pre+iter](decomp/FairSchedulern=2_compact/lifting-sym+pre+iter.stats) | host limit | — | — | — | — | — | — | — |
| [pm-strahler](decomp/FairSchedulern=2_compact/pm-strahler.stats) | complete | 5596 / 0 | 386 / 0 | 81 / 0 | 8 / 0 | 3 / 0 | k=3, t=2, depth=7 / k=3, t=2, depth=8 | [PNG](decomp/FairSchedulern=2_compact/pm-strahler.png) · [DOT](decomp/FairSchedulern=2_compact/pm-strahler.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-strahler.leaves) |
| [pm-strahler+pre](decomp/FairSchedulern=2_compact/pm-strahler+pre.stats) | complete | 5596 / 0 | 63 / 0 | 13 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=5 / k=2, t=2, depth=6 | [PNG](decomp/FairSchedulern=2_compact/pm-strahler+pre.png) · [DOT](decomp/FairSchedulern=2_compact/pm-strahler+pre.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-strahler+pre.leaves) |
| [pm-strahler+iter](decomp/FairSchedulern=2_compact/pm-strahler+iter.stats) | complete | 5596 / 0 | 379 / 0 | 80 / 0 | 8 / 0 | 3 / 0 | k=3, t=2, depth=7 / k=3, t=2, depth=8 | [PNG](decomp/FairSchedulern=2_compact/pm-strahler+iter.png) · [DOT](decomp/FairSchedulern=2_compact/pm-strahler+iter.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-strahler+iter.leaves) |
| [pm-strahler+pre+iter](decomp/FairSchedulern=2_compact/pm-strahler+pre+iter.stats) | complete | 5596 / 0 | 21 / 0 | 4 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=5 / k=2, t=2, depth=6 | [PNG](decomp/FairSchedulern=2_compact/pm-strahler+pre+iter.png) · [DOT](decomp/FairSchedulern=2_compact/pm-strahler+pre+iter.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-strahler+pre+iter.leaves) |
| [pm-succinct](decomp/FairSchedulern=2_compact/pm-succinct.stats) | complete | 5596 / 0 | 101 / 0 | 21 / 0 | 8 / 0 | 3 / 0 | bits=2, depth=7 / bits=2, depth=8 | [PNG](decomp/FairSchedulern=2_compact/pm-succinct.png) · [DOT](decomp/FairSchedulern=2_compact/pm-succinct.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-succinct.leaves) |
| [pm-succinct+pre](decomp/FairSchedulern=2_compact/pm-succinct+pre.stats) | complete | 5596 / 0 | 92 / 0 | 23 / 0 | 6 / 0 | 3 / 0 | bits=3, depth=5 / bits=3, depth=6 | [PNG](decomp/FairSchedulern=2_compact/pm-succinct+pre.png) · [DOT](decomp/FairSchedulern=2_compact/pm-succinct+pre.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-succinct+pre.leaves) |
| [pm-succinct+iter](decomp/FairSchedulern=2_compact/pm-succinct+iter.stats) | complete | 5596 / 0 | 94 / 0 | 20 / 0 | 8 / 0 | 3 / 0 | bits=2, depth=7 / bits=2, depth=8 | [PNG](decomp/FairSchedulern=2_compact/pm-succinct+iter.png) · [DOT](decomp/FairSchedulern=2_compact/pm-succinct+iter.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-succinct+iter.leaves) |
| [pm-succinct+pre+iter](decomp/FairSchedulern=2_compact/pm-succinct+pre+iter.stats) | complete | 5596 / 0 | 87 / 0 | 22 / 0 | 6 / 0 | 3 / 0 | bits=2, depth=5 / bits=2, depth=6 | [PNG](decomp/FairSchedulern=2_compact/pm-succinct+pre+iter.png) · [DOT](decomp/FairSchedulern=2_compact/pm-succinct+pre+iter.dot) · [leaves](decomp/FairSchedulern=2_compact/pm-succinct+pre+iter.leaves) |
| [zielonka](decomp/FairSchedulern=2_compact/zielonka.stats) | complete | 5596 / 0 | 22 / 0 | 8 / 0 | 8 / 0 | 3 / 0 | — / — | [PNG](decomp/FairSchedulern=2_compact/zielonka.png) · [DOT](decomp/FairSchedulern=2_compact/zielonka.dot) |
| [zielonka+pre](decomp/FairSchedulern=2_compact/zielonka+pre.stats) | complete | 5596 / 0 | 17 / 0 | 8 / 0 | 5 / 0 | 3 / 0 | — / — | [PNG](decomp/FairSchedulern=2_compact/zielonka+pre.png) · [DOT](decomp/FairSchedulern=2_compact/zielonka+pre.dot) |
| [zielonka-sym](decomp/FairSchedulern=2_compact/zielonka-sym.stats) | complete | 5596 / 0 | 22 / 0 | 8 / 0 | 8 / 0 | 3 / 0 | — / — | [PNG](decomp/FairSchedulern=2_compact/zielonka-sym.png) · [DOT](decomp/FairSchedulern=2_compact/zielonka-sym.dot) |
| [zielonka-sym+pre](decomp/FairSchedulern=2_compact/zielonka-sym+pre.stats) | complete | 5596 / 0 | 17 / 0 | 8 / 0 | 5 / 0 | 3 / 0 | — / — | [PNG](decomp/FairSchedulern=2_compact/zielonka-sym+pre.png) · [DOT](decomp/FairSchedulern=2_compact/zielonka-sym+pre.dot) |

### cabp_swp.ehoa.pg

| Vertices | Edges | Distinct priorities | Maximum priority | Won (Even / Odd) |
| ---: | ---: | ---: | ---: | --- |
| 875281 | 1469041 | 3 | 4 | 0 / 875281 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Strahler E / O | Parameters E / O | Tree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [lifting](decomp/cabp_swp.ehoa/lifting.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+pre](decomp/cabp_swp.ehoa/lifting+pre.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+iter](decomp/cabp_swp.ehoa/lifting+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting+pre+iter](decomp/cabp_swp.ehoa/lifting+pre+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-adaptive](decomp/cabp_swp.ehoa/lifting-adaptive.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [lifting-adaptive+pre](decomp/cabp_swp.ehoa/lifting-adaptive+pre.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [lifting-adaptive+iter](decomp/cabp_swp.ehoa/lifting-adaptive+iter.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [lifting-adaptive+pre+iter](decomp/cabp_swp.ehoa/lifting-adaptive+pre+iter.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [lifting-sym](decomp/cabp_swp.ehoa/lifting-sym.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+pre](decomp/cabp_swp.ehoa/lifting-sym+pre.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+iter](decomp/cabp_swp.ehoa/lifting-sym+iter.stats) | host limit | — | — | — | — | — | — | — |
| [lifting-sym+pre+iter](decomp/cabp_swp.ehoa/lifting-sym+pre+iter.stats) | host limit | — | — | — | — | — | — | — |
| [pm-strahler](decomp/cabp_swp.ehoa/pm-strahler.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [pm-strahler+pre](decomp/cabp_swp.ehoa/pm-strahler+pre.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [pm-strahler+iter](decomp/cabp_swp.ehoa/pm-strahler+iter.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [pm-strahler+pre+iter](decomp/cabp_swp.ehoa/pm-strahler+pre+iter.stats) | skipped (> 60 s locally) | — | — | — | — | — | — | — |
| [pm-succinct](decomp/cabp_swp.ehoa/pm-succinct.stats) | complete | 0 / 875281 | 0 / 136 | 0 / 90 | 0 / 3 | 0 / 3 | bits=5, depth=1 / bits=5, depth=2 | [PNG](decomp/cabp_swp.ehoa/pm-succinct.png) · [DOT](decomp/cabp_swp.ehoa/pm-succinct.dot) · [leaves](decomp/cabp_swp.ehoa/pm-succinct.leaves) |
| [pm-succinct+pre](decomp/cabp_swp.ehoa/pm-succinct+pre.stats) | complete | 0 / 875281 | 0 / 136 | 0 / 90 | 0 / 3 | 0 / 3 | bits=5, depth=1 / bits=5, depth=2 | [PNG](decomp/cabp_swp.ehoa/pm-succinct+pre.png) · [DOT](decomp/cabp_swp.ehoa/pm-succinct+pre.dot) · [leaves](decomp/cabp_swp.ehoa/pm-succinct+pre.leaves) |
| [pm-succinct+iter](decomp/cabp_swp.ehoa/pm-succinct+iter.stats) | complete | 0 / 875281 | 0 / 5 | 0 / 3 | 0 / 3 | 0 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/cabp_swp.ehoa/pm-succinct+iter.png) · [DOT](decomp/cabp_swp.ehoa/pm-succinct+iter.dot) · [leaves](decomp/cabp_swp.ehoa/pm-succinct+iter.leaves) |
| [pm-succinct+pre+iter](decomp/cabp_swp.ehoa/pm-succinct+pre+iter.stats) | complete | 0 / 875281 | 0 / 5 | 0 / 3 | 0 / 3 | 0 / 2 | bits=1, depth=1 / bits=1, depth=2 | [PNG](decomp/cabp_swp.ehoa/pm-succinct+pre+iter.png) · [DOT](decomp/cabp_swp.ehoa/pm-succinct+pre+iter.dot) · [leaves](decomp/cabp_swp.ehoa/pm-succinct+pre+iter.leaves) |
| [zielonka](decomp/cabp_swp.ehoa/zielonka.stats) | complete | 0 / 875281 | 0 / 15 | 0 / 14 | 0 / 2 | 0 / 2 | — / — | [PNG](decomp/cabp_swp.ehoa/zielonka.png) · [DOT](decomp/cabp_swp.ehoa/zielonka.dot) |
| [zielonka+pre](decomp/cabp_swp.ehoa/zielonka+pre.stats) | complete | 0 / 875281 | 0 / 15 | 0 / 14 | 0 / 2 | 0 / 2 | — / — | [PNG](decomp/cabp_swp.ehoa/zielonka+pre.png) · [DOT](decomp/cabp_swp.ehoa/zielonka+pre.dot) |
| [zielonka-sym](decomp/cabp_swp.ehoa/zielonka-sym.stats) | complete | 0 / 875281 | 0 / 15 | 0 / 14 | 0 / 2 | 0 / 2 | — / — | [PNG](decomp/cabp_swp.ehoa/zielonka-sym.png) · [DOT](decomp/cabp_swp.ehoa/zielonka-sym.dot) |
| [zielonka-sym+pre](decomp/cabp_swp.ehoa/zielonka-sym+pre.stats) | complete | 0 / 875281 | 0 / 15 | 0 / 14 | 0 / 2 | 0 / 2 | — / — | [PNG](decomp/cabp_swp.ehoa/zielonka-sym+pre.png) · [DOT](decomp/cabp_swp.ehoa/zielonka-sym+pre.dot) |

## Tree disagreements

These pairs produced different tree shapes despite agreeing on the winners.
The comparison includes child order and uses only complete results with the same
preprocessing and iterative-shaving choices. Decomposition methods are compared with each other, as are
progress-measure methods; the two families describe different things. Trees with
the same shape are omitted even if their vertex sets differ. Shortened labels in
the pictures cannot establish whether full sets match. See [the disagreement study](docs/disagreements.md)
for comparisons of full vertex sets and smaller trees.

| Game | Player | Backend A | Backend B | Differences |
| --- | --- | --- | --- | --- |
| Button.tlsf.ehoa.pg | Even | pm-strahler+iter | pm-succinct+iter | ordered shape; nodes, leaves, height, Strahler |
| Button.tlsf.ehoa.pg | Even | pm-strahler+pre+iter | pm-succinct+pre+iter | ordered shape; nodes, leaves, height, Strahler |
| FairSchedulern=2_compact.gm | Even | lifting-adaptive | zielonka | ordered shape; nodes, leaves, Strahler |
| FairSchedulern=2_compact.gm | Even | lifting-adaptive | zielonka-sym | ordered shape; nodes, leaves, Strahler |
| FairSchedulern=2_compact.gm | Even | lifting-adaptive+pre | zielonka+pre | ordered shape; leaves, Strahler |
| FairSchedulern=2_compact.gm | Even | lifting-adaptive+pre | zielonka-sym+pre | ordered shape; leaves, Strahler |
| FairSchedulern=2_compact.gm | Even | pm-strahler | pm-succinct | ordered shape; nodes, leaves |
| FairSchedulern=2_compact.gm | Even | pm-strahler+pre | pm-succinct+pre | ordered shape; nodes, leaves, Strahler |
| FairSchedulern=2_compact.gm | Even | pm-strahler+iter | pm-succinct+iter | ordered shape; nodes, leaves |
| FairSchedulern=2_compact.gm | Even | pm-strahler+pre+iter | pm-succinct+pre+iter | ordered shape; nodes, leaves, Strahler |
