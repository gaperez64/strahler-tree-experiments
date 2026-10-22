# pgsolver, part 8

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=6.gm · 50000 vertices / 567435 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 567435 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.349 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.348 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.653 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.333 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.662 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.652 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.663 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25225 / 24775 | 125000 / 100001 | 5 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.172 | 159.648 | even | true | true | false | - |
| pm-strahler+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.672 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25225 / 24775 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.085 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.663 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25225 / 24775 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.677 | 159.781 | even | true | true | false | - |
| pm-succinct+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.684 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25225 / 24775 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.498 | 159.664 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.661 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.322 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.630 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.329 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25225 / 24775 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.596 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 124995 / 99997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=7.gm · 50000 vertices / 649493 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 649493 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.366 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.707 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.375 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.363 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.353 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.349 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.692 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24949 / 25051 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.071 | 147.727 | even | true | true | false | - |
| pm-strahler+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.714 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24949 / 25051 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.149 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.711 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24949 / 25051 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.603 | 147.754 | even | true | true | false | - |
| pm-succinct+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.711 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24949 / 25051 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.347 | 147.664 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.701 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.338 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.665 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24949 / 25051 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.628 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=8.gm · 50000 vertices / 651438 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 651438 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.375 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.706 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.374 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.362 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.352 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.353 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25000 / 25000 | 125000 / 100001 | 5 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.280 | 159.625 | even | true | true | false | - |
| pm-strahler+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.714 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25000 / 25000 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.181 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.704 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25000 / 25000 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.853 | 159.672 | even | true | true | false | - |
| pm-succinct+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.702 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25000 / 25000 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.622 | 159.531 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.702 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.366 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.704 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.354 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25000 / 25000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 124995 / 99997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=9.gm · 50000 vertices / 592216 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 592216 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.378 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.728 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.677 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.356 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.340 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.676 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.339 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24906 / 25094 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.995 | 147.730 | even | true | true | false | - |
| pm-strahler+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.685 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24906 / 25094 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.112 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.694 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24906 / 25094 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.589 | 147.672 | even | true | true | false | - |
| pm-succinct+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.694 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24906 / 25094 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.336 | 147.809 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.692 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.332 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.639 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24906 / 25094 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(10000).gm · 10000 vertices / 99990000 edges · 8 complete · 8 out of memory · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 99990000 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 8.673 | 1528.699 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 13.913 | 1529.289 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 9.017 | 1528.688 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 17.658 | 1528.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 15.515 | 1528.707 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 12.418 | 1528.848 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 11.341 | 1528.586 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 11.551 | 1529.625 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 9.838 | 1528.602 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 14.480 | 1529.207 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 10.587 | 1528.535 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 12.472 | 1529.094 | even | true | true | false | - |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 13.038 | 1528.672 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.525 | 1529.023 | - | true | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.292 | 1528.707 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.616 | 1529.152 | - | true | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 10.944 | 1528.473 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.260 | 1528.891 | - | true | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.412 | 1528.672 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 15.022 | 1528.867 | - | true | - | - | Failed to allocate memory |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 13.984 | 1528.535 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 15.656 | 1529.125 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 10.603 | 1528.457 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 14.648 | 1529.395 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

