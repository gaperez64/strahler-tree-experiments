# Incremental lifting in t

`--adaptive-t=incremental` is sound and preserves the **exact least labelling
and final decomposition at every host** used by ordinary `--adaptive-t`.
It seeds a player's already certified opponent dominion at TOP and initializes
everything else at the least priority-compatible position. It does not reuse
that player's old finite labels. The default remains cold adaptive lifting.
The runs keep the existing Even-then-Odd order, including budget exits.

Two parts of the proposed analysis need separating: embeddings give the
suggested upper bound on least labellings, but the actual adaptive hosts need
not embed when K changes. Even their certified dominions can shrink.

## The actual operator

In [ad_lift.c](../src/ad_lift.c), labels are positions of
`leafy_infinity(T)` in depth-first order. For player P:

* A regular node eta accepts exactly priority `level(eta)`. A P vertex needs
  one successor below `after(eta)`; an opponent vertex needs all successors
  below it. Only edges within the active subgame count.
* A lazy position ell accepts priorities at most its level. P must force a
  visit to `{mu < ell}` while staying in `{mu <= ell}`. Opponent edges out of
  the safe set count as escapes. This is `pg_attractor_through`, not an
  attractor in the induced safe subgame.
* TOP accepts every priority and is always valid.

One short lift advances an invalid vertex to its next compatible position.
A round advances every invalid vertex against the same old labelling.
This inflationary operator is monotone on the product of the compatible
position chains. Indeed, at a fixed candidate label, lowering other labels
only helps validity. If two current labels of v differ, a single compatible
step from the smaller one cannot pass the larger one. If they agree,
invalidity in the larger labelling implies invalidity in the smaller one.

**Warm-start criterion.** Starting at a compatible labelling sigma returns
the least fixed point mu precisely when `sigma <= mu`. Sufficiency follows
from the no-overshoot argument already in the source: an invalid vertex is
valid at its label in any valid upper bound, so its next step stays below
that bound. Necessity follows because no coordinate ever decreases. A seed
need not itself be valid or a pre-fixed point.

## What an embedding proves, and what it does not

Let e be a rooted, level- and sibling-order-preserving embedding of the old
base tree into the new one. Extend it to regular nodes, minus-infinity
positions, each child's plus position, and TOP. This extension preserves
compatibility, strict order, and `after` boundaries on mapped regular nodes.

**Embedding lemma.** Every valid old labelling nu maps to a valid new
labelling `e(nu)`. Regular edge tests are preserved. For a lazy mapped label,
the safe and target vertex sets are unchanged, so the same reachability
strategy works. Therefore

```
mu_new <= e(mu_old),       D_P(old) subset D_P(new).
```

The inequality has the direction in the question. Copying the old solution
is generally an **upper** seed. In fact the embedded old solution is already
valid, so upward iteration stops immediately. Old TOP vertices stay TOP,
even if the new least labelling would certify them. `strahler_two.pg` gives
an immediate example: Even certifies three vertices in the chain at t=0,
and all five at t=1. Copying the chain solution misses vertices 1 and 2.
The copied witness remains a valid decomposition of its old dominion, but
does not compute the new least labelling or necessarily the winning region.

For **fixed K**, `U^K_{t,H}` embeds in `U^K_{t+1,H}`. This follows by
simultaneous induction in the U/V recurrence in [stree.c](../src/stree.c):
V's two outer copies grow in t and its middle U grows inductively; for U,
embed its two V lists and its middle U separately. The K=1 and t=0 chains
are the bases. Hence fixed-K dominions persist.

For the actual choice `K=min(H,t+1)`, the embedding claim is **false**.
For H=4, `U^3_{2,4}` has 103 leaves and 192 nodes, whereas `U^4_{3,4}` has
111 leaves and 176 nodes, with a different distribution of branch capacity.
The following 16-leaf, 29-node, Strahler-3 ordered tree embeds in the former
and not the latter. `()` is a leaf; each tuple lists a node's children:

```python
((((), (), (), ()),),
 (((), ()), ((),), ((),)),
 (((), (), (), ()), ((),), ((),), ((),), ((),)))
```

Greedy matching of ordered children is a complete embedding decision
procedure: choosing an earlier feasible match never removes a later option.
`tests/test_research.py` checks this obstruction, matches the Python host
recurrence against C-generated hosts, and checks the resulting game below
with the C solver.

**A game witnessing non-monotone dominions.** `saturated_game` in
[incremental_t.py](../scripts/incremental_t.py) turns this tree into a
70-vertex game. Give every usable regular or lazy position a vertex with
that position's priority and ownership Odd; omit TOP and level -1 leaves.
A regular vertex points to every vertex before its after boundary, including
itself. A lazy vertex points to every earlier vertex.

The identity labelling is valid. Conversely, any entirely finite valid
Even labelling embeds the source tree in its host. A regular vertex's
Odd-controlled self-loop prevents a lazy label, so it must map to a regular
node of the same level. Mutual edges between a parent and child force their
host intervals to nest. A plus vertex between siblings has edges to all
earlier regular vertices; their self-loops force their labels strictly below
its lazy label. Its priority places it between child blocks, forcing the
sibling order. These facts give a rooted ordered embedding.

Every vertex can reach the root regular vertex and that root can reach
every vertex. Since Odd owns everything, an Even dominion is either empty
or the whole game. Thus the C solver certifies **70 vertices at (K,t)=(3,2)
and zero at (4,3)**. This refutes non-TOP persistence for the adaptive
sequence, not just its proposed embedding proof. Certificates retained from
earlier runs remain true statements about who wins the original game.

For a drop before the adaptive loop can terminate, take the disjoint union
with the saturated game of the complete binary tree of four regular levels.
That adds 36 vertices. The two components require, respectively, the
obstruction above and a Strahler-4 tree. C gives Even dominion sizes 70 at
t=2 and 36 at t=3, and completes at t=4 on all 106 vertices.

## Projections and a useful lower seed

As finite chains, the position sets of any embedded hosts have the usual
floor and ceiling adjoints. Their existence alone does not transfer the
lifting constraints. Even with an old root at level 2 and one child at
level 0, embedded as the first child of a three-child host:

* Floor maps a self-loop at the second new regular level-0 child to the old
  first child's plus position. The resulting lazy labelling has an empty
  lower target and is invalid.
* Ceiling maps that same second child to TOP. Add a priority-2 vertex whose
  only edge enters the self-loop. It is valid at the new root regular
  position, but becomes invalid there after ceiling sends its successor to
  TOP.

These are executable assertions in `test_adjoints_do_not_preserve_validity`.
They disprove using these adjoints as validity-preserving projections; they
do not prove that every possible game-dependent projection is impossible.
No useful general reuse of the old **finite** labels is established here.

There is a simpler useful lower seed. Let C be any certified opponent
dominion in the **original active game**, found on any previous host, or by
the opponent's run earlier in the same round. Every valid P labelling has
its non-TOP vertices in a P dominion. Consequently every vertex of C must
be TOP in P's least labelling, for every host. Set

```
sigma(v) = TOP                         if v belongs to C,
           least compatible position otherwise.
```

Then `sigma <= mu_P` coordinatewise, proving exactness by the warm-start
criterion. No embedding or host monotonicity is needed. The implementation
keeps the full game and all outgoing edges, so escapes into known opponent
wins still invalidate regular and lazy labels correctly. It uses the
opponent's most recently certified region; retaining additional historical
certificates or computing extra attractors is unnecessary for correctness
and was not added.

Short lifts visit each intervening compatible position exactly once per
vertex. Thus seeding these known TOP coordinates can only reduce lift
counts, regardless of how the rounds change. Extra adaptive rounds can still
make the total exceed a single cold run at an oracle-provided final t.

## Removing certified dominions: scheme (i)

The experiment also implements this separately: at each t, lift Even and
then Odd on the current residual, immediately remove each nonempty certified
dominion's attractor, and retain its witness. Keep the original compact
priority bounds and the original sequence of hosts. Attractor removal
preserves a total residual and sound winning-region assignments. At the
universal final host every residual vertex is assigned.

The retained witness is an ordered sequence of `(dominion, attractor, tree)`
chunks per player. It is not, without additional assembly, a single classic
tree at the original root level. A precise composition is an empty root
**two priority levels higher** with the per-round trees as its children in
removal order. Its edges carry those dominions and their removed attractors.
Restricted to the final winning region, each retained core is an opponent
trap in the appropriate remainder and each stored attractor is still its
attractor. This proves the assembled classic witness is valid. The Python
experiment independently verifies all these conditions.

This adds a root, can add leaves or increase the Strahler number, and need
not fit the final lifting host. It is a composition of successful residual
searches, not the least decomposition at that host. For tree comparisons
the experiment pads the cold tree with the same empty root, so a reported
difference is not merely this extra root. We implemented certified-TOP
seeding in the CLI because it preserves the exact requested tree without
adding a second witness-assembly path to the C solver.

## Reproduction and evidence

```sh
meson compile -C build
python3 scripts/incremental_t.py --samples=50 --output=/tmp/incremental-t.json
meson test -C build --print-errorlogs
```

Every experimental input checks the independent Python operator against C's
cold final tree **and exact lift count**; C's cold-adaptive, cold-final and
incremental final witnesses must be identical. Winning regions are compared
with the independently verified residual composition. The tests also compare
the complete seeded and cold label arrays, exercise partial results, K caps,
start t, leaf budgets, and require actual lift savings. Counts and selected
results are recorded in [research/incremental-t.json](research/incremental-t.json).

The final sample contains 628 games: 600 random games, 12 ladder/nested-cycle
cases, the 70-vertex obstruction, the small repository example, and all 14
valid test games including the five new disagreements. All winning regions
and all cold/incremental final trees agree. The aggregate lift counts are:

| Method | Vertex lifts |
| --- | ---: |
| One cold run at the final t | 99,636 |
| Existing cold adaptive search | 114,627 |
| Certified-TOP incremental search | 54,686 |
| Residual/attractor scheme (i) | 52,417 |

Incremental uses fewer lifts than cold adaptive on 414/628 games and fewer
than the oracle-final cold run on 408/628 games. The residual composition,
after matching the extra root on the cold side, has the same shape and sets
on 572/628 games and differs on 56. Its regions always agree. These are
lift-count comparisons, not wall-time guarantees: host construction,
verification and sorting still have costs. On `strahler_two.pg`, for
example, cold final/cold adaptive/incremental/residual use 35/58/29/19
lifts respectively; the exact incremental tree is preserved even when
residual removal is cheaper.

The large `cabp_swp.ehoa.pg` is excluded from this model comparison. Default
lifting rejects its host at the leaf limit; a timed incremental attempt
did not finish within 10 seconds. Zielonka does finish, finding all 875,281
vertices Odd-winning, with a 15-node, 14-leaf, height-2, Strahler-2 tree.
No equality or speedup claim is made for that excluded input.

The thesis order used here is the pointwise order on decomposition labels
in one fixed leafy host, as defined in
[Section 7.2.1 of Raghavan's thesis](https://thejaswiniraghavan.github.io/PhD_Thesis.pdf#page=118).
The host-dependent least labelling should not be confused with minimizing
leaves, height, or the Strahler number of the pruned tree.

Validation: all 135 available Meson checks pass natively and under the full
Valgrind wrapper (14 are expected-failure checks); clang-tidy passes. Changed
C/header files pass clang-format 21 and the diff passes whitespace checks.
The repository's requested clang-format 18 and optional Graphviz are
unavailable here. A whole-repository format check with version 21 reports
only the two untouched array-pointer declarations in `src/stree.c`; they
were left unchanged rather than reformatting unrelated code for a different
formatter version. No exhaustive game enumeration or global minimality
claim is made.
