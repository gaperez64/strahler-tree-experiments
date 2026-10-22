# equivchecking, part 1

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 11135 vertices / 22616 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11135 | 22616 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.581 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.559 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.549 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.505 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.506 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.432 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.432 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.453 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.453 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.422 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.422 | 90.051 | even | true | true | false | - |
| zielonka | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 90.051 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 19045 vertices / 44820 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19045 | 44820 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.971 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.899 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.140 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.159 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 19045 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.575 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 19045 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.576 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 19045 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.443 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19045 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.444 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 19045 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.494 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 19045 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.484 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 19045 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.431 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19045 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.433 | 90.051 | even | true | true | false | - |
| zielonka | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.411 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.422 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19045 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 90.051 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 77529 vertices / 198673 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 77529 | 198673 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.569 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.620 | 92.246 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.578 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.588 | 92.246 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.246 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.021 | 92.246 | even | true | true | false | - |
| pm-strahler+pre | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.297 | 92.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.987 | 92.246 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.994 | 92.246 | even | true | true | false | - |
| pm-succinct | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.255 | 92.246 | even | true | true | false | - |
| pm-succinct+pre | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.250 | 92.246 | even | true | true | false | - |
| pm-succinct+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.792 | 92.246 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.801 | 92.246 | even | true | true | false | - |
| zielonka | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.562 | 92.246 | even | true | true | false | - |
| zielonka+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.562 | 92.246 | even | true | true | false | - |
| zielonka-sym | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.583 | 92.246 | even | true | true | false | - |
| zielonka-sym+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.593 | 92.246 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 156729 vertices / 523185 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 156729 | 523185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.756 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.777 | 92.246 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.774 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.765 | 92.246 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 92.246 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 156729 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.020 | 92.246 | even | true | true | false | - |
| pm-strahler+pre | complete | 156729 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.355 | 92.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 156729 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.671 | 92.246 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 156729 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.662 | 92.246 | even | true | true | false | - |
| pm-succinct | complete | 156729 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.129 | 92.246 | even | true | true | false | - |
| pm-succinct+pre | complete | 156729 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.127 | 92.246 | even | true | true | false | - |
| pm-succinct+iter | complete | 156729 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.289 | 92.246 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 156729 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.288 | 92.246 | even | true | true | false | - |
| zielonka | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.685 | 92.246 | even | true | true | false | - |
| zielonka+pre | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.695 | 92.246 | even | true | true | false | - |
| zielonka-sym | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.752 | 92.246 | even | true | true | false | - |
| zielonka-sym+pre | complete | 156729 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.749 | 92.246 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 7855 vertices / 15904 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7855 | 15904 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.246 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 92.246 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 92.246 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 92.246 | even | true | true | false | - |
| lifting-sym | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.697 | 92.246 | even | true | true | false | - |
| lifting-sym+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.697 | 92.246 | even | true | true | false | - |
| lifting-sym+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.690 | 92.246 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.709 | 92.246 | even | true | true | false | - |
| pm-strahler | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.464 | 92.246 | even | true | true | false | - |
| pm-strahler+pre | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 92.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 92.246 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 92.246 | even | true | true | false | - |
| pm-succinct | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 92.246 | even | true | true | false | - |
| pm-succinct+pre | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.432 | 92.246 | even | true | true | false | - |
| pm-succinct+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 92.246 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 92.246 | even | true | true | false | - |
| zielonka | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 92.246 | even | true | true | false | - |
| zielonka+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.400 | 92.246 | even | true | true | false | - |
| zielonka-sym | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 92.246 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 92.246 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_ABP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 310 vertices / 516 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 310 | 516 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.426 | 92.246 | even | true | true | false | - |
| lifting+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 92.246 | even | true | true | false | - |
| lifting+iter | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.425 | 92.246 | even | true | true | false | - |
| lifting+pre+iter | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 92.246 | even | true | true | false | - |
| lifting-adaptive | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 92.246 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 92.246 | even | true | true | false | - |
| lifting-sym | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 92.246 | even | true | true | false | - |
| lifting-sym+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 92.246 | even | true | true | false | - |
| lifting-sym+iter | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 92.246 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 92.246 | even | true | true | false | - |
| pm-strahler | complete | 245 / 65 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.382 | 92.246 | even | true | true | false | - |
| pm-strahler+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 92.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 245 / 65 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 92.246 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.398 | 92.246 | even | true | true | false | - |
| pm-succinct | complete | 245 / 65 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.439 | 92.246 | even | true | true | false | - |
| pm-succinct+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.440 | 92.246 | even | true | true | false | - |
| pm-succinct+iter | complete | 245 / 65 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 92.246 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 92.246 | even | true | true | false | - |
| zielonka | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.392 | 92.246 | even | true | true | false | - |
| zielonka+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 92.246 | even | true | true | false | - |
| zielonka-sym | complete | 245 / 65 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.394 | 92.246 | even | true | true | false | - |
| zielonka-sym+pre | complete | 245 / 65 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 92.246 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_ABP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 4921 vertices / 11463 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4921 | 11463 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 16.667 | 92.246 | even | true | true | false | - |
| lifting+pre | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 16.700 | 92.246 | even | true | true | false | - |
| lifting+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 16.672 | 92.246 | even | true | true | false | - |
| lifting+pre+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 16.737 | 92.246 | even | true | true | false | - |
| lifting-adaptive | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 92.246 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 92.246 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 92.246 | even | true | true | false | - |
| lifting-sym | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 92.246 | even | true | true | false | - |
| lifting-sym+pre | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.688 | 92.246 | even | true | true | false | - |
| lifting-sym+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 92.246 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 92.246 | even | true | true | false | - |
| pm-strahler | complete | 4921 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.422 | 92.246 | even | true | true | false | - |
| pm-strahler+pre | complete | 4921 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.422 | 92.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 4921 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 92.246 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4921 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 92.246 | even | true | true | false | - |
| pm-succinct | complete | 4921 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 92.246 | even | true | true | false | - |
| pm-succinct+pre | complete | 4921 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 92.246 | even | true | true | false | - |
| pm-succinct+iter | complete | 4921 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.390 | 92.246 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4921 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.390 | 92.246 | even | true | true | false | - |
| zielonka | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 92.246 | even | true | true | false | - |
| zielonka+pre | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 92.246 | even | true | true | false | - |
| zielonka-sym | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 92.246 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 92.246 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 57905 vertices / 147937 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 57905 | 147937 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 92.461 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 92.461 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 92.461 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.538 | 92.461 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | true | - | - | metrics: deadline exceeded |
| pm-strahler | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.556 | 92.461 | even | true | true | false | - |
| pm-strahler+pre | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.752 | 92.461 | even | true | true | false | - |
| pm-strahler+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.851 | 92.461 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.844 | 92.461 | even | true | true | false | - |
| pm-succinct | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.031 | 92.461 | even | true | true | false | - |
| pm-succinct+pre | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.033 | 92.461 | even | true | true | false | - |
| pm-succinct+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.707 | 92.461 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.729 | 92.461 | even | true | true | false | - |
| zielonka | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.563 | 92.461 | even | true | true | false | - |
| zielonka+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.550 | 92.461 | even | true | true | false | - |
| zielonka-sym | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.614 | 92.461 | even | true | true | false | - |
| zielonka-sym+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.571 | 92.461 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_CABP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 92.461 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 92.461 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 92.461 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 92.461 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 92.461 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 92.461 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 92.461 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 92.461 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 92.461 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 92.461 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 92.461 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 92.461 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 92.461 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 92.461 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 92.461 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 92.461 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 92.461 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 92.461 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 92.461 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 92.461 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 92.461 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 15111 vertices / 30956 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15111 | 30956 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 92.461 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 92.461 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 92.461 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 92.461 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 92.461 | even | true | true | false | - |
| lifting-sym | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.594 | 92.461 | even | true | true | false | - |
| lifting-sym+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.573 | 92.461 | even | true | true | false | - |
| lifting-sym+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.600 | 92.461 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 92.461 | even | true | true | false | - |
| pm-strahler | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.569 | 92.461 | even | true | true | false | - |
| pm-strahler+pre | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.567 | 92.461 | even | true | true | false | - |
| pm-strahler+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.452 | 92.461 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 92.461 | even | true | true | false | - |
| pm-succinct | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 92.461 | even | true | true | false | - |
| pm-succinct+pre | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.474 | 92.461 | even | true | true | false | - |
| pm-succinct+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 92.461 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.434 | 92.461 | even | true | true | false | - |
| zielonka | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 92.461 | even | true | true | false | - |
| zielonka+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 92.461 | even | true | true | false | - |
| zielonka-sym | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 92.461 | even | true | true | false | - |
| zielonka-sym+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 92.461 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 34954 vertices / 85706 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 34954 | 85706 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 92.461 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.439 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.569 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 34954 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.900 | 92.461 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 34954 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.693 | 92.461 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.371 | 92.461 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 92.461 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.409 | 92.461 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 34954 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.996 | 92.461 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 34954 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.621 | 92.461 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 34954 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.590 | 92.461 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 34954 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.593 | 92.461 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 34954 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.953 | 92.461 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 34954 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.641 | 92.461 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 34954 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.579 | 92.461 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 34954 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.560 | 92.461 | odd | false | true | false | - |
| zielonka | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.497 | 92.461 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.496 | 92.461 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.539 | 92.461 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.516 | 92.461 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 4 | 0 / 4 | 0.000 / 4.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 5 | 0 / 5 | 0.000 / 1.667 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| zielonka | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/ABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 97762 vertices / 240530 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 97762 | 240530 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 93.762 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 93.762 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 93.762 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 93.762 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 6.926 | 93.762 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 4.077 | 93.762 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 97762 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.934 | 93.762 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 97762 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.438 | 93.762 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 93.762 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 93.762 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 93.762 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 93.762 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 97762 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.050 | 93.762 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 97762 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.057 | 93.762 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 97762 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.873 | 93.762 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 97762 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.822 | 93.762 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 97762 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.999 | 93.762 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 97762 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.181 | 93.762 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 97762 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.928 | 93.762 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 97762 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.824 | 93.762 | odd | false | true | false | - |
| zielonka | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.636 | 93.762 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.635 | 93.762 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.768 | 93.762 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.742 | 93.762 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 4 | 0 / 4 | 0.000 / 4.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 5 | 0 / 5 | 0.000 / 1.667 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| zielonka | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 8 | 0 / 8 | 0.000 / 8.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Buffer_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 3457 vertices / 8945 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3457 | 8945 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.248 | 93.762 | even | true | true | false | - |
| lifting+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.197 | 93.762 | even | true | true | false | - |
| lifting+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.227 | 93.762 | even | true | true | false | - |
| lifting+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.307 | 93.762 | even | true | true | false | - |
| lifting-adaptive | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 93.762 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 93.762 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 93.762 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 93.762 | even | true | true | false | - |
| lifting-sym | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 93.762 | even | true | true | false | - |
| lifting-sym+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 93.762 | even | true | true | false | - |
| lifting-sym+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 93.762 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 93.762 | even | true | true | false | - |
| pm-strahler | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 93.762 | even | true | true | false | - |
| pm-strahler+pre | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 93.762 | even | true | true | false | - |
| pm-strahler+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 93.762 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 93.762 | even | true | true | false | - |
| pm-succinct | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.411 | 93.762 | even | true | true | false | - |
| pm-succinct+pre | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.400 | 93.762 | even | true | true | false | - |
| pm-succinct+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.411 | 93.762 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 93.762 | even | true | true | false | - |
| zielonka | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.384 | 93.762 | even | true | true | false | - |
| zielonka+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 93.762 | even | true | true | false | - |
| zielonka-sym | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 93.762 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 93.762 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 8961 vertices / 25073 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8961 | 25073 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 93.762 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 93.762 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 93.762 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 93.762 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 93.762 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 93.762 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.415 | 93.762 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.460 | 93.762 | even | true | true | false | - |
| lifting-sym | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.556 | 93.762 | even | true | true | false | - |
| lifting-sym+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.576 | 93.762 | even | true | true | false | - |
| lifting-sym+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.536 | 93.762 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.565 | 93.762 | even | true | true | false | - |
| pm-strahler | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.577 | 93.762 | even | true | true | false | - |
| pm-strahler+pre | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.587 | 93.762 | even | true | true | false | - |
| pm-strahler+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 93.762 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.485 | 93.762 | even | true | true | false | - |
| pm-succinct | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.466 | 93.762 | even | true | true | false | - |
| pm-succinct+pre | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.456 | 93.762 | even | true | true | false | - |
| pm-succinct+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 93.762 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.442 | 93.762 | even | true | true | false | - |
| zielonka | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 93.762 | even | true | true | false | - |
| zielonka+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 93.762 | even | true | true | false | - |
| zielonka-sym | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 93.762 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 93.762 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 631474 vertices / 1832290 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 631474 | 1832290 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 212.980 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.276 | 212.953 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 212.953 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.196 | 212.918 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 631474 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 13.688 | 212.855 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.396 | 212.855 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 631474 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 7.179 | 212.707 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.387 | 212.984 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 212.859 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.250 | 212.910 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 212.699 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.274 | 212.883 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 631474 | 0 / 45 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 24.902 | 212.855 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.487 | 212.848 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 631474 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.478 | 212.848 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.513 | 212.785 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 631474 | 0 / 45 | 0 / 22 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 22.850 | 212.859 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.391 | 212.859 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 631474 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.761 | 212.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.360 | 212.848 | odd | false | true | false | - |
| zielonka | complete | 0 / 631474 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.377 | 212.711 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.203 | 212.980 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 631474 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.788 | 212.984 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 631474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.222 | 212.910 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 23 | 0 / 22 | 0 / 22 | 0.000 / 1.913 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 23 | 0 / 22 | 0 / 22 | 0.000 / 1.913 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 447 vertices / 788 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 447 | 788 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.641 | 94.590 | even | true | true | false | - |
| lifting+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.651 | 94.590 | even | true | true | false | - |
| lifting+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.660 | 94.590 | even | true | true | false | - |
| lifting+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.650 | 94.590 | even | true | true | false | - |
| lifting-adaptive | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 94.590 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 94.590 | even | true | true | false | - |
| lifting-sym | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 94.590 | even | true | true | false | - |
| lifting-sym+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.391 | 94.590 | even | true | true | false | - |
| lifting-sym+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.393 | 94.590 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 94.590 | even | true | true | false | - |
| pm-strahler | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 94.590 | even | true | true | false | - |
| pm-strahler+pre | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 94.590 | even | true | true | false | - |
| pm-strahler+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 94.590 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 94.590 | even | true | true | false | - |
| pm-succinct | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 94.590 | even | true | true | false | - |
| pm-succinct+pre | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 94.590 | even | true | true | false | - |
| pm-succinct+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 94.590 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 94.590 | even | true | true | false | - |
| zielonka | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 94.590 | even | true | true | false | - |
| zielonka+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 94.590 | even | true | true | false | - |
| zielonka-sym | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 94.590 | even | true | true | false | - |
| zielonka-sym+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 94.590 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 1264 vertices / 2193 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1264 | 2193 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.276 | 94.590 | even | true | true | false | - |
| lifting+pre | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.283 | 94.590 | even | true | true | false | - |
| lifting+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.318 | 94.590 | even | true | true | false | - |
| lifting+pre+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.332 | 94.590 | even | true | true | false | - |
| lifting-adaptive | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 94.590 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 94.590 | even | true | true | false | - |
| lifting-sym | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 94.590 | even | true | true | false | - |
| lifting-sym+pre | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 94.590 | even | true | true | false | - |
| lifting-sym+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 94.590 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 94.590 | even | true | true | false | - |
| pm-strahler | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 94.590 | even | true | true | false | - |
| pm-strahler+pre | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 94.590 | even | true | true | false | - |
| pm-strahler+iter | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 94.590 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.380 | 94.590 | even | true | true | false | - |
| pm-succinct | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.382 | 94.590 | even | true | true | false | - |
| pm-succinct+pre | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.381 | 94.590 | even | true | true | false | - |
| pm-succinct+iter | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.380 | 94.590 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1264 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 94.590 | even | true | true | false | - |
| zielonka | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 94.590 | even | true | true | false | - |
| zielonka+pre | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 94.590 | even | true | true | false | - |
| zielonka-sym | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 94.590 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1264 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 94.590 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 2266 vertices / 5418 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2266 | 5418 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 5.594 | 94.590 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 94.590 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 5.594 | 94.590 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.390 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2266 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.379 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.451 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.442 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2266 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.379 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 94.590 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2266 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.370 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.380 | 94.590 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2266 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 94.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2266 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 94.590 | odd | false | true | false | - |
| zielonka | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.391 | 94.590 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 94.590 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.393 | 94.590 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 94.590 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 2266 vertices / 5418 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2266 | 5418 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 5.618 | 94.590 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 94.590 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 5.596 | 94.590 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 94.590 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.379 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2266 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.379 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 94.590 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.441 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.441 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 94.590 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2266 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.380 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 94.590 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2266 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.370 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.369 | 94.590 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2266 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 94.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2266 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.401 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 94.590 | odd | false | true | false | - |
| zielonka | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.402 | 94.590 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 94.590 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2266 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.393 | 94.590 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2266 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 94.590 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=2_windowsize=1)eq=branching-bisim.gm · 3697 vertices / 9561 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3697 | 9561 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.001 | 94.590 | even | true | true | false | - |
| lifting+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.011 | 94.590 | even | true | true | false | - |
| lifting+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.058 | 94.590 | even | true | true | false | - |
| lifting+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.053 | 94.590 | even | true | true | false | - |
| lifting-adaptive | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 94.590 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 94.590 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 94.590 | even | true | true | false | - |
| lifting-sym | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 94.590 | even | true | true | false | - |
| lifting-sym+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 94.590 | even | true | true | false | - |
| lifting-sym+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 94.590 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 94.590 | even | true | true | false | - |
| pm-strahler | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.451 | 94.590 | even | true | true | false | - |
| pm-strahler+pre | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.452 | 94.590 | even | true | true | false | - |
| pm-strahler+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 94.590 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 94.590 | even | true | true | false | - |
| pm-succinct | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 94.590 | even | true | true | false | - |
| pm-succinct+pre | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 94.590 | even | true | true | false | - |
| pm-succinct+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 94.590 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 94.590 | even | true | true | false | - |
| zielonka | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.384 | 94.590 | even | true | true | false | - |
| zielonka+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.386 | 94.590 | even | true | true | false | - |
| zielonka-sym | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 94.590 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 94.590 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.408 | 94.590 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 94.590 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 94.590 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 94.590 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 94.590 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 94.590 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 94.590 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 94.590 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 94.590 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 94.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 94.590 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.394 | 94.590 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 94.590 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 94.590 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 94.590 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 7106 vertices / 17154 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7106 | 17154 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 94.590 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 94.590 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 94.590 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 94.590 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7106 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.464 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7106 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.421 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 94.590 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7106 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 94.590 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7106 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 94.590 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7106 | 0 / 41 | 0 / 20 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.472 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 94.590 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7106 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.390 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 94.590 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7106 | 0 / 41 | 0 / 20 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.472 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.382 | 94.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7106 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.390 | 94.590 | odd | false | true | false | - |
| zielonka | complete | 0 / 7106 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.393 | 94.590 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 94.590 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7106 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.392 | 94.590 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7106 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 94.590 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 21 | 0 / 20 | 0 / 20 | 0.000 / 1.905 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 21 | 0 / 20 | 0 / 20 | 0.000 / 1.905 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=2_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 94.590 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 94.590 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 94.590 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 94.590 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 94.590 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 94.590 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 94.590 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 94.590 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 94.590 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.408 | 94.590 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 94.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 94.590 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 94.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 94.590 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 94.590 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 94.590 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 94.590 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 94.590 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 94.590 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/CABP_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 74039 vertices / 191547 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 74039 | 191547 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.559 | 95.508 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.570 | 95.508 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.567 | 95.508 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.577 | 95.508 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.174 | 95.508 | even | true | true | false | - |
| pm-strahler+pre | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.466 | 95.508 | even | true | true | false | - |
| pm-strahler+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.945 | 95.508 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.966 | 95.508 | even | true | true | false | - |
| pm-succinct | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.340 | 95.508 | even | true | true | false | - |
| pm-succinct+pre | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.282 | 95.508 | even | true | true | false | - |
| pm-succinct+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.784 | 95.508 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.812 | 95.508 | even | true | true | false | - |
| zielonka | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 95.508 | even | true | true | false | - |
| zielonka+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 95.508 | even | true | true | false | - |
| zielonka-sym | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.593 | 95.508 | even | true | true | false | - |
| zielonka-sym+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.604 | 95.508 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 104074 vertices / 315882 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 104074 | 315882 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 95.508 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.508 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.526 | 95.508 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 104074 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.797 | 95.508 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.622 | 95.508 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 104074 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.892 | 95.508 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 95.508 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.573 | 95.508 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 95.508 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.571 | 95.508 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 104074 | 0 / 45 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.349 | 95.508 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.634 | 95.508 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 104074 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.652 | 95.508 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.610 | 95.508 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 104074 | 0 / 45 | 0 / 22 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.853 | 95.508 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.590 | 95.508 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 104074 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.704 | 95.508 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.608 | 95.508 | odd | false | true | false | - |
| zielonka | complete | 0 / 104074 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.600 | 95.508 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.579 | 95.508 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 104074 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.663 | 95.508 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 104074 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.580 | 95.508 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 23 | 0 / 22 | 0 / 22 | 0.000 / 1.913 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 23 | 0 / 22 | 0 / 22 | 0.000 / 1.913 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Onebit_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 5322498 vertices / 21604226 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5322498 | 21604226 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.800 | 1609.117 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.706 | 1609.934 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.749 | 1610.867 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.693 | 1644.047 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 19.661 | 1644.035 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 19.507 | 1644.133 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.145 | 1644.246 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.145 | 1644.082 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 13.187 | 1644.203 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.266 | 1644.379 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.299 | 1644.391 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.308 | 1644.406 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 6.697 | 1644.258 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.583 | 1644.145 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.470 | 1644.281 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.409 | 1644.352 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.409 | 1644.352 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.409 | 1644.289 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.386 | 1644.328 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.406 | 1644.082 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.377 | 1644.191 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.397 | 1644.277 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.292 | 1644.410 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.335 | 1644.438 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

<details>
<summary>equivchecking/games/Par_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 9507 vertices / 19696 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9507 | 19696 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 96.406 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 96.406 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 96.406 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 96.406 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 96.406 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 96.406 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 96.406 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 96.406 | even | true | true | false | - |
| lifting-sym | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.560 | 96.406 | even | true | true | false | - |
| lifting-sym+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.557 | 96.406 | even | true | true | false | - |
| lifting-sym+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.573 | 96.406 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.552 | 96.406 | even | true | true | false | - |
| pm-strahler | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.535 | 96.406 | even | true | true | false | - |
| pm-strahler+pre | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.524 | 96.406 | even | true | true | false | - |
| pm-strahler+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.422 | 96.406 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.423 | 96.406 | even | true | true | false | - |
| pm-succinct | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.442 | 96.406 | even | true | true | false | - |
| pm-succinct+pre | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.443 | 96.406 | even | true | true | false | - |
| pm-succinct+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 96.406 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 96.406 | even | true | true | false | - |
| zielonka | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 96.406 | even | true | true | false | - |
| zielonka+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 96.406 | even | true | true | false | - |
| zielonka-sym | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 96.406 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 96.406 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Par_Par_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 7878 vertices / 19287 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7878 | 19287 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 28.211 | 96.406 | even | true | true | false | - |
| lifting+pre | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 28.038 | 96.406 | even | true | true | false | - |
| lifting+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 28.027 | 96.406 | even | true | true | false | - |
| lifting+pre+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 28.146 | 96.406 | even | true | true | false | - |
| lifting-adaptive | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 96.406 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 96.406 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 96.406 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 96.406 | even | true | true | false | - |
| lifting-sym | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 96.406 | even | true | true | false | - |
| lifting-sym+pre | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.689 | 96.406 | even | true | true | false | - |
| lifting-sym+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.689 | 96.406 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.697 | 96.406 | even | true | true | false | - |
| pm-strahler | complete | 7878 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 96.406 | even | true | true | false | - |
| pm-strahler+pre | complete | 7878 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.473 | 96.406 | even | true | true | false | - |
| pm-strahler+iter | complete | 7878 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 96.406 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7878 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.413 | 96.406 | even | true | true | false | - |
| pm-succinct | complete | 7878 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.432 | 96.406 | even | true | true | false | - |
| pm-succinct+pre | complete | 7878 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.431 | 96.406 | even | true | true | false | - |
| pm-succinct+iter | complete | 7878 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 96.406 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7878 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 96.406 | even | true | true | false | - |
| zielonka | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 96.406 | even | true | true | false | - |
| zielonka+pre | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 96.406 | even | true | true | false | - |
| zielonka-sym | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 96.406 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7878 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 96.406 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Par_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 35234 vertices / 110927 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 35234 | 110927 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 96.406 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 96.406 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 96.406 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 96.406 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 35234 | 0 / 14 | 0 / 13 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.713 | 96.406 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 35234 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.161 | 96.406 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 35234 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.248 | 96.406 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 35234 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.063 | 96.406 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 96.406 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 35234 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.438 | 96.406 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 96.406 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 35234 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.764 | 96.406 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 35234 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.136 | 96.406 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 35234 | 0 / 33 | 0 / 16 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.094 | 96.406 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 35234 | 0 / 19 | 0 / 9 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.686 | 96.406 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 35234 | 0 / 17 | 0 / 8 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.634 | 96.406 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 35234 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.174 | 96.406 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 35234 | 0 / 33 | 0 / 16 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.142 | 96.406 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 35234 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.725 | 96.406 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 35234 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.644 | 96.406 | odd | false | true | false | - |
| zielonka | complete | 0 / 35234 | 0 / 14 | 0 / 13 | 0 / 2 | — / — | 0.526 | 96.406 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 35234 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.525 | 96.406 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 35234 | 0 / 14 | 0 / 13 | 0 / 2 | — / — | 0.593 | 96.406 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 35234 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.582 | 96.406 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 13 | 0 / 13 | 0.000 / 13.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 17 | 0 / 16 | 0 / 16 | 0.000 / 1.882 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 10 | 0 / 9 | 0 / 9 | 0.000 / 1.800 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 8 | 0 / 8 | 0.000 / 1.778 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 17 | 0 / 16 | 0 / 16 | 0.000 / 1.882 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 13 | 0 / 13 | 0.000 / 13.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 13 | 0 / 13 | 0.000 / 13.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 214897 vertices / 1007185 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 214897 | 1007185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 96.738 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 96.676 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 96.867 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 96.738 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.028 | 96.867 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.040 | 96.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.019 | 96.805 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.057 | 96.742 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 96.852 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 96.598 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 96.785 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 96.836 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 214897 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.618 | 96.812 | even | true | true | false | - |
| pm-strahler+pre | complete | 214897 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.736 | 96.777 | even | true | true | false | - |
| pm-strahler+iter | complete | 214897 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.095 | 96.613 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 214897 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.159 | 96.680 | even | true | true | false | - |
| pm-succinct | complete | 214897 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.041 | 96.746 | even | true | true | false | - |
| pm-succinct+pre | complete | 214897 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.892 | 96.750 | even | true | true | false | - |
| pm-succinct+iter | complete | 214897 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.488 | 96.543 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 214897 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.410 | 96.746 | even | true | true | false | - |
| zielonka | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.821 | 96.852 | even | true | true | false | - |
| zielonka+pre | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.769 | 96.809 | even | true | true | false | - |
| zielonka-sym | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.883 | 96.746 | even | true | true | false | - |
| zielonka-sym+pre | complete | 214897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.836 | 96.730 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 11135 vertices / 22616 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11135 | 22616 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 118.895 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 118.895 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 118.895 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 118.895 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.425 | 118.895 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.427 | 118.895 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 118.895 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 118.895 | even | true | true | false | - |
| lifting-sym | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.586 | 118.895 | even | true | true | false | - |
| lifting-sym+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.643 | 118.895 | even | true | true | false | - |
| lifting-sym+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.569 | 118.895 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.576 | 118.895 | even | true | true | false | - |
| pm-strahler | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.527 | 118.895 | even | true | true | false | - |
| pm-strahler+pre | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.520 | 118.895 | even | true | true | false | - |
| pm-strahler+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.445 | 118.895 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 118.895 | even | true | true | false | - |
| pm-succinct | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.454 | 118.895 | even | true | true | false | - |
| pm-succinct+pre | complete | 11135 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.464 | 118.895 | even | true | true | false | - |
| pm-succinct+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 118.895 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 11135 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 118.895 | even | true | true | false | - |
| zielonka | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 118.895 | even | true | true | false | - |
| zielonka+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 118.895 | even | true | true | false | - |
| zielonka-sym | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 118.895 | even | true | true | false | - |
| zielonka-sym+pre | complete | 11135 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 118.895 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 412 vertices / 691 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 412 | 691 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.445 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.446 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 323 / 89 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 323 / 89 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 323 / 89 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 323 / 89 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| zielonka | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 9205 vertices / 21682 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9205 | 21682 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.560 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.580 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.585 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.574 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9205 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9205 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9205 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.417 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9205 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.416 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9205 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9205 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.435 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9205 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9205 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| zielonka | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9205 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 22915 vertices / 46698 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22915 | 46698 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.442 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.457 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.456 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.993 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.060 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.364 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.238 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.660 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.669 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.498 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.496 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.526 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.534 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.465 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| zielonka | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.442 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 22915 vertices / 46698 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22915 | 46698 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.455 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.445 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.466 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.299 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.339 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.419 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.360 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.671 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.660 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.494 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.517 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 22915 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.465 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 22915 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.466 | 124.797 | even | true | true | false | - |
| zielonka | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 22915 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 816 vertices / 1377 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 816 | 1377 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.538 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.537 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.463 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.455 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 639 / 177 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 639 / 177 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.396 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 639 / 177 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 639 / 177 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| zielonka | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 5 | 1 / 4 | 1 / 4 | 1.000 / 1.600 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 77529 vertices / 198673 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 77529 | 198673 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.611 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.633 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.636 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.643 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.423 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.660 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.182 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.164 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.419 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 77529 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.401 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.914 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 77529 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.916 | 124.797 | even | true | true | false | - |
| zielonka | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.664 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.639 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.649 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 77529 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.660 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.447 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.448 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.422 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.426 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.450 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.491 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.480 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.429 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 68025 vertices / 226281 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 68025 | 226281 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.550 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.560 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.557 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.568 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 68025 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.733 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 68025 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.979 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 68025 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.968 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 68025 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.959 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 68025 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.137 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 68025 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.134 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 68025 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.809 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 68025 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.814 | 124.797 | even | true | true | false | - |
| zielonka | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.571 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.594 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 68025 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.602 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 178233 vertices / 459921 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 178233 | 459921 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.840 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.850 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.861 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.861 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.804 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.012 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.755 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.763 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.436 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.452 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.286 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.304 | 124.797 | even | true | true | false | - |
| zielonka | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.697 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.710 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.769 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.780 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 178233 vertices / 459921 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 178233 | 459921 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.837 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.847 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.847 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.868 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.880 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.013 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.777 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.795 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.456 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 178233 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.462 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.316 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 178233 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.305 | 124.797 | even | true | true | false | - |
| zielonka | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.708 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.708 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.802 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 178233 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.781 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_CABP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.430 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.560 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.561 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.549 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.415 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.415 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.415 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 9907 vertices / 20295 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9907 | 20295 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.560 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.569 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.553 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.584 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.516 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.507 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.435 | 124.797 | even | true | true | false | - |
| zielonka | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

