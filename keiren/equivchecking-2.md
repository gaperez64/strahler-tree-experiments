# equivchecking, part 2

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>equivchecking/games/ABP(BW)_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 9907 vertices / 20295 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9907 | 20295 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.570 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.569 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.563 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.574 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.504 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.515 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.442 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.463 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9907 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9907 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| zielonka | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9907 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_Par_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 1993 vertices / 3489 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1993 | 3489 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.736 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.694 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.398 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.443 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.422 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1993 | 0 / 39 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1993 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1993 | 0 / 39 | 0 / 19 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1993 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1993 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1993 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Par_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 8206 vertices / 19646 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8206 | 19646 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.568 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.578 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 8206 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 8206 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 8206 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8206 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.426 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 8206 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 8206 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.431 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 8206 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8206 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8206 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 20317 vertices / 41753 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20317 | 41753 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.052 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.056 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.107 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.155 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.650 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.659 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.493 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.525 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.516 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| zielonka | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.425 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 20317 vertices / 41753 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20317 | 41753 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.445 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.011 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.984 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.362 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.409 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.650 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.660 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.518 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 20317 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.518 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.465 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 20317 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| zielonka | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 20317 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_Par_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3977 vertices / 6973 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3977 | 6973 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.587 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.584 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.484 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.496 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3977 | 0 / 39 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3977 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3977 | 0 / 39 | 0 / 19 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3977 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3977 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Par_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 16910 vertices / 40450 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16910 | 40450 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.436 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.432 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.917 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.027 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.264 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.177 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 16910 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.556 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 16910 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.556 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 16910 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.462 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16910 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 16910 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 16910 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.483 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 16910 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16910 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| zielonka | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16910 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 44926 vertices / 110170 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 44926 | 110170 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 3.206 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.999 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 44926 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.087 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 44926 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.878 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.074 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 44926 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.136 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 44926 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.728 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 44926 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.655 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 44926 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.643 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 44926 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.170 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 44926 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.759 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 44926 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.674 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 44926 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.634 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.552 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.551 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.613 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.604 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 44926 vertices / 110170 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 44926 | 110170 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 3.191 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.007 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 44926 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.088 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 44926 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.866 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.095 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 44926 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.145 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 44926 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.727 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 44926 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.656 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 44926 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.689 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 44926 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.171 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 44926 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.781 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 44926 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.696 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 44926 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.644 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.551 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.579 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 44926 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.622 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 44926 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.616 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.415 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 39614 vertices / 123530 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39614 | 123530 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 39614 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 3.053 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 39614 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.318 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 39614 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.341 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 39614 | 0 / 8 | 0 / 7 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.154 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 39614 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.023 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 39614 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.210 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 39614 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.788 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 39614 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.696 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 39614 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.675 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 39614 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.278 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 39614 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.872 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 39614 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.717 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 39614 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.665 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 39614 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.562 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 39614 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.563 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 39614 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.636 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 39614 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.623 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 7 | 0 / 7 | 0.000 / 7.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 5 | 0 / 5 | 0.000 / 1.667 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 124458 vertices / 306210 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 124458 | 306210 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.215 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 5.350 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 124458 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.476 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 124458 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.828 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 124458 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.519 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 124458 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.228 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 124458 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.978 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 124458 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.964 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 124458 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.421 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 124458 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.343 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 124458 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.086 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 124458 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.962 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.707 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.699 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.876 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.833 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 124458 vertices / 306210 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 124458 | 306210 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.184 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 5.363 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 124458 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.472 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 124458 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.808 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 124458 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.557 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 124458 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.241 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 124458 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.997 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 124458 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.939 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 124458 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.453 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 124458 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.354 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 124458 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.092 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 124458 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.952 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.708 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.707 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 124458 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.876 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 124458 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.854 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.415 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.417 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.416 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.415 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP(BW)_SWP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 109890 vertices / 343274 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 109890 | 343274 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 109890 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 8.565 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 109890 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 6.199 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 109890 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 3.290 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 109890 | 0 / 8 | 0 / 7 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.577 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 109890 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.881 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 109890 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 109890 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.072 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 109890 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.010 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 109890 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.815 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 109890 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.649 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 109890 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.210 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 109890 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.042 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 109890 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.742 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 109890 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.738 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 109890 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.939 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 109890 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.909 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 7 | 0 / 7 | 0.000 / 7.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 5 | 0 / 5 | 0.000 / 1.667 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 28 | 0 / 27 | 0 / 27 | 0.000 / 1.929 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 7855 vertices / 15904 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7855 | 15904 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.708 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.435 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 7855 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.435 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7855 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7855 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 412 vertices / 691 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 412 | 691 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.480 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.449 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.422 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 323 / 89 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 323 / 89 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 323 / 89 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 323 / 89 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 323 / 89 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 323 / 89 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 6511 vertices / 15242 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6511 | 15242 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 22.634 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 22.453 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 22.463 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 22.437 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.696 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 6511 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 6511 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 6511 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6511 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.416 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 6511 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 6511 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 6511 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6511 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| zielonka | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.400 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6511 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 16119 vertices / 32732 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16119 | 32732 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.603 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.603 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.573 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.584 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.588 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.578 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.471 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.468 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.494 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| zielonka | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.421 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.421 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 16119 vertices / 32732 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16119 | 32732 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.432 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.581 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.592 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.582 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.581 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.578 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.578 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.497 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 16119 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.487 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.446 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16119 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.434 | 124.797 | even | true | true | false | - |
| zielonka | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 816 vertices / 1377 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 816 | 1377 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.537 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.537 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.453 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.453 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 639 / 177 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 639 / 177 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 639 / 177 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 639 / 177 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 124.797 | even | true | true | false | - |
| zielonka | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 639 / 177 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 639 / 177 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 13425 vertices / 31402 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13425 | 31402 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.591 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.591 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.582 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.583 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 13425 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.525 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 13425 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.514 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 13425 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13425 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 13425 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.452 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 13425 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 13425 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13425 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| zielonka | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13425 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 5925 vertices / 11971 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5925 | 11971 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.470 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.582 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.533 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.578 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.696 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.697 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.711 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.452 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.421 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 5925 vertices / 11971 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5925 | 11971 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.407 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.489 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.540 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 26.515 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.700 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.690 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5925 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5925 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5925 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 12133 vertices / 24579 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12133 | 24579 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.605 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.535 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.534 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.462 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.451 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 12133 vertices / 24579 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12133 | 24579 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.576 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.581 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.567 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.536 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.546 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 12133 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12133 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| zielonka | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12133 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 614 vertices / 1028 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 614 | 1028 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.508 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.509 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.444 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.453 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 485 / 129 | 2 / 9 | 1 / 4 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.391 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 485 / 129 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.395 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 485 / 129 | 2 / 9 | 1 / 4 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 485 / 129 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| zielonka | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 485 / 129 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 485 / 129 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_ABP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 10121 vertices / 23559 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10121 | 23559 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.577 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.556 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.557 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.558 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10121 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.484 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10121 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.485 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10121 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10121 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10121 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10121 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.442 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10121 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10121 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10121 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 57905 vertices / 147937 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 57905 | 147937 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.538 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.533 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.543 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | metrics: deadline exceeded |
| pm-strahler | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.527 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.806 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.896 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.866 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.052 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 57905 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.076 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.717 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 57905 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.731 | 124.797 | even | true | true | false | - |
| zielonka | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.559 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.551 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.573 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 57905 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.588 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.409 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 50865 vertices / 168209 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50865 | 168209 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.507 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.517 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.503 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.515 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.840 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 50865 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.362 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 50865 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.563 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 50865 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.851 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 50865 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.842 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 50865 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.963 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 50865 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.945 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 50865 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.720 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 50865 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.717 | 124.797 | even | true | true | false | - |
| zielonka | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.542 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.541 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.561 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 50865 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.563 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 134097 vertices / 345057 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 134097 | 345057 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.725 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.735 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.734 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.745 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.715 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.857 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.396 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.398 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.902 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.913 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.089 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.085 | 124.797 | even | true | true | false | - |
| zielonka | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.646 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.646 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.697 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.707 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 134097 vertices / 345057 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 134097 | 345057 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.743 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.736 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.731 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.743 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.572 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.875 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.386 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.403 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.903 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 134097 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.904 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.064 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 134097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.073 | 124.797 | even | true | true | false | - |
| zielonka | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.646 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.646 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.696 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 134097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.714 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_CABP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 118225 vertices / 391905 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 118225 | 391905 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.673 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.673 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.682 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.681 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 118225 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.048 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 118225 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.330 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 118225 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.346 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 118225 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.365 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 118225 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.702 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 118225 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.722 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 118225 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.080 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 118225 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.096 | 124.797 | even | true | true | false | - |
| zielonka | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.644 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.655 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.687 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 118225 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.688 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.401 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.427 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.426 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.427 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | - | - | false | - |
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
<summary>equivchecking/games/ABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.409 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | - | - | false | - |

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
<summary>equivchecking/games/ABP_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 7383 vertices / 15080 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7383 | 15080 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.701 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.709 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.421 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.421 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.431 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 7383 vertices / 15080 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7383 | 15080 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.700 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.700 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.476 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.420 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.431 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 7383 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7383 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| zielonka | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7383 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_Par_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 1883 vertices / 3288 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1883 | 3288 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.673 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.672 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1883 | 0 / 39 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1883 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1883 | 0 / 39 | 0 / 19 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1883 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.396 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1883 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1883 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_Par_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 6124 vertices / 14585 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6124 | 14585 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 23.778 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 23.635 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 23.666 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 23.742 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.690 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.688 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.700 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 6124 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 6124 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 6124 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6124 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 6124 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 6124 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 6124 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6124 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6124 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 15111 vertices / 30956 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15111 | 30956 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.566 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.575 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.582 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.569 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.578 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 15111 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 15111 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.425 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 15111 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_Par_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3759 vertices / 6572 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3759 | 6572 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.504 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.503 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.379 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.496 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3759 | 0 / 39 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3759 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3759 | 0 / 39 | 0 / 19 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3759 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3759 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3759 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 20 | 0 / 19 | 0 / 19 | 0.000 / 1.900 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/ABP_Par_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 12590 vertices / 29963 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12590 | 29963 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.556 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.576 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.578 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.566 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 12590 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.515 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 12590 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.516 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 12590 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12590 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 12590 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 12590 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 12590 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.427 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12590 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| zielonka | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.430 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12590 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/ABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 34954 vertices / 85706 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 34954 | 85706 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.571 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 34954 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.882 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 34954 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.701 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.353 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.638 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 34954 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.993 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 34954 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.620 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 34954 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.580 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 34954 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.581 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 34954 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.964 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 34954 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.652 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 34954 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.590 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 34954 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.568 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.507 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.500 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 34954 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.541 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 34954 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.518 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.417 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |

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

