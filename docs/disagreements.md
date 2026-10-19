# Zielonka versus attractor-decomposition lifting

The final trees can differ for either player. Neither algorithm minimizes
leaf count or Strahler number: there are checked counterexamples in **both
directions for both metrics**. Their heights can differ too. Ordered tree
embedding can be incomparable even on four vertices.

The least-labelling statement is different: in a fixed host containing a
Zielonka witness, lifting's labelling is pointwise no larger than the
embedded Zielonka labelling. This is the thesis's host-relative order, not
an order of bare tree shapes or their size statistics.

## What was compared

[find_disagreements.py](../scripts/find_disagreements.py) uses only Python's
standard library and the checked `pg2adot` binaries. It runs both default
algorithms with complete, unlimited classic set labels and compact priority
bounds. No C output format was needed. Each tree is encoded as

```
[priority_bound, vertex_set_W, top_attractor_A,
 [[child_attractor_A_i, child_tree], ...]]
```

Children retain their removal order, sets are sorted external vertex IDs,
and a missing winning region is `null`. A child's W is its incoming trap
S_i. This records all classic node/edge sets and consequently all derived
tree-relative H/T/R/S sets. Shape comparison discards all metadata and keeps
the ordered children. Winning regions must agree before a disagreement is
counted. Every C run verifies its witness; the experiment uses no
`--no-verify` shortcut.

The main sample has seed 20261019, exactly two distinct uniformly sampled
successors per vertex (clamped at n), independent uniform owners, and
uniform priorities in `0..2h-1`. Here **h is the generator parameter**, not
necessarily the compact host height H: priorities may be absent, and the
two players have different parity bounds. It completed 109,413 games in
751 CPU seconds, plus 48 deterministic ladder/nested-cycle cases and the
small example. CPU time includes Python and all child processes.

| n | h | Games | Even shape differences | Odd shape differences |
| --- | --- | ---: | ---: | ---: |
| 4 | 2 | 9118 | 6 (0.066%) | 0 |
| 4 | 3 | 9118 | 1 (0.011%) | 3 (0.033%) |
| 4 | 4 | 9118 | 5 (0.055%) | 2 (0.022%) |
| 8 | 2 | 9118 | 16 (0.175%) | 0 |
| 8 | 3 | 9118 | 30 (0.329%) | 7 (0.077%) |
| 8 | 4 | 9118 | 41 (0.450%) | 19 (0.208%) |
| 16 | 2 | 9118 | 16 (0.175%) | 0 |
| 16 | 3 | 9118 | 64 (0.702%) | 6 (0.066%) |
| 16 | 4 | 9118 | 84 (0.921%) | 26 (0.285%) |
| 32 | 2 | 9117 | 10 (0.110%) | 0 |
| 32 | 3 | 9117 | 38 (0.417%) | 11 (0.121%) |
| 32 | 4 | 9117 | 92 (1.009%) | 29 (0.318%) |

These are per-player frequencies over all sampled games, including games
where that player wins nothing. They describe this distribution, not a
distribution-independent rate. No winning-region disagreements or timeouts
occurred in these random runs. All 48 structured cases agreed.

A second sample (seed 17, out-degree 3, priorities weighted toward smaller
values) ran 1,000 games per `(n,h)` for n=6,12,24 and h=3,5, using 91.5 CPU
seconds. It also found both directions for leaves. Targeted edge/owner/
priority mutations of a saturated binary-tree game produced the example
where lifting has larger Strahler number. The search, pilot runs, shrinking
and independent-model experiments stayed within roughly 20 CPU minutes.
Raw counts, parameters and shrunk witnesses are in
[research/disagreements.json](research/disagreements.json) and
[research/disagreements-low.json](research/disagreements-low.json).

## Five checked fixtures

`()` below denotes a leaf. Tree height counts nodes. JSON goldens in
`tests/golden/disagree_*.json` contain both algorithms' complete trees and
sets; `test_research` checks them against fresh verified C runs.

| Game | Player | Vertices | Lifting shape | Zielonka shape | Main difference |
| --- | --- | ---: | --- | --- | --- |
| [disagree_shape.pg](../tests/games/disagree_shape.pg) | Even | 4 | `(((),),((),))` | `(((),()),)` | 5 vs 4 nodes; incomparable shapes |
| [disagree_lifting_leaves.pg](../tests/games/disagree_lifting_leaves.pg) | Even | 8 | `(((),),((),()))` | `(((),()),)` | 3 vs 2 leaves |
| [disagree_lifting_strahler.pg](../tests/games/disagree_lifting_strahler.pg) | Even | 10 | `(((),()),((),()))` | `(((),(),(),()),)` | Strahler 3 vs 2; both have 4 leaves |
| [disagree_odd_strahler.pg](../tests/games/disagree_odd_strahler.pg) | Odd | 5 | `(((),),)` | `(((),()),)` | Strahler 1 vs 2; 1 vs 2 leaves |
| [disagree_zielonka_height.pg](../tests/games/disagree_zielonka_height.pg) | Even | 13 | `(((),),)` | `(((),((),)),)` | height 3 vs 4; Strahler 1 vs 2 |

Each fixture is **1-minimal for its stated disagreement** under vertex
deletion, edge deletion and individual priority lowering: none of those
single edits preserves the selected difference while keeping a total game.
Vertex deletion removes incident edges and renumbers the survivors; edits
making a dead end are rejected. The shrinker first tries vertex chunks and
then repeats single edits to a fixed point. These are the smallest examples
found for their categories, not proven global minima. The raw main report
also contains a five-vertex, equal-Strahler example with 2 lifting leaves
versus 3 Zielonka leaves.

The four-vertex example makes the changed sets explicit. Even wins all four
vertices. Lifting's root children have traps `{1,3}` and `{0}`, whereas
Zielonka's single root child has trap `{0,1,3}`. The incoming attractors are
`{1,3}` / `{0,2}` versus `{0,1,2,3}`. The root top attractor is empty in
both. Lifting removes a smaller early core, so the remaining vertices form a
later sibling; Zielonka groups them under the same child and splits them
one level lower.

## Why the trees differ; the order and attached sets

Zielonka first removes the opposing attractor to the next highest priority,
solves the lower subgame without a host restriction, and takes its whole
winning region as the next child core. Lifting instead tries to place the
next certified core in the next available host branch. That branch can be
too narrow for Zielonka's whole core, so lifting finishes a smaller core
there, attracts to it, and continues in later branches. This changes the
subgames passed to recursive children, not just a drawing convention.

The default universal host contains every Zielonka decomposition: it has
enough height, at most n leaves are needed, and Strahler is at most
`floor(log2(n))+1`. Embed Zielonka's tree in that host and map top-attractor
vertices to its regular/minus-infinity positions, child cores recursively,
and child-attractor side vertices to the corresponding plus positions.
This is a valid labelling. The short-lift leastness proof in
[ad_lift.c](../src/ad_lift.c) gives `mu_lifting <= mu_embedded_Zielonka`.
The tests check this inequality on every paired fixture, using an explicit
host embedding. This is the applicable comparison in
[the thesis's Section 7.2.1](https://thejaswiniraghavan.github.io/PhD_Thesis.pdf#page=118).
Across unspecified embeddings or hosts, bare shapes have no such intrinsic
pointwise order. In particular, the four-vertex shapes do not embed in
each other.

**Same shape implies the same attached sets for these two algorithms.**
There were no same-shape/different-set cases. There is also a structural
reason, rather than just sampling evidence. If the shapes agree, embed the
Zielonka witness along exactly the occupied nodes of the lifting witness.
Leastness gives the same pointwise inequality. Both root top attractors are
the unique attractor to the root priority. In the remainder, every vertex
of Zielonka's first core must then lie in lifting's first core: it cannot
have a later label, and cannot have moved into the already fixed top
attractor. Conversely lifting's first core is an opponent trap of priorities
at most d-2. It therefore avoids the opposing attractor to priority d-1 and
is contained in the whole winning region of Zielonka's lower subgame, its
first core. The two cores are equal. Their attractors are consequently
equal. Induct within the child and then over the remaining siblings. This
proves equality of every stored and derived set when the ordered shapes
agree. For differing shapes, the goldens preserve all sets rather than
pretending that differently located nodes have a canonical correspondence.

The metrics are not monotone consequences of this pointwise order. The
eight-vertex example has more lifting leaves; the five-vertex Odd example
has more Zielonka leaves. The ten-vertex example has larger lifting
Strahler number; the five-vertex Odd example has larger Zielonka Strahler
number. The height example shows that lifting can avoid an unnecessary
deeper subgame. The random sample had one larger Zielonka height and no
larger lifting height; no general height inequality is claimed.

## Examples and reproduction

`examples/Button.tlsf.ehoa.pg` finishes with identical trees for both
algorithms. The large `cabp_swp.ehoa.pg` cannot be compared with the default
lifting settings: its Even host `U^2_{19,2}` has 1,048,575 leaves, exceeding
the default 1,000,000 limit. Timed attempts and their outcomes are recorded
in [research/examples.json](research/examples.json); this is a resource
exclusion, not a decomposition disagreement.

```sh
python3 scripts/find_disagreements.py --samples=10000 --cpu-seconds=750 \
  --examples examples/Button.tlsf.ehoa.pg --output=/tmp/disagreements.json
python3 scripts/find_disagreements.py --seed=17 --n=6,12,24 --h=3,5 \
  --out-degree=3 --priority-distribution=low --samples=1000 \
  --cpu-seconds=100 --examples --output=/tmp/disagreements-low.json
python3 scripts/find_disagreements.py --samples=0 --n=1 --h=1 \
  --examples tests/games/disagree_*.pg --output=/tmp/fixtures.json
```

For exactly the same number of random samples per cell as the main report,
use `--samples=9118` with a larger CPU limit; the time-limited recorded run
stopped three cells short of completing that last round. Fixed seeds
reproduce the game stream, whereas CPU cutoffs depend on the machine.
