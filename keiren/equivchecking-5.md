# equivchecking, part 5

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>equivchecking/games/Par_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 39822 vertices / 98011 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39822 | 98011 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.850 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.872 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 39822 | 0 / 7 | 0 / 6 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.066 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 39822 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.910 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.419 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 39822 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.107 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 39822 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.716 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 39822 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.657 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 39822 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.654 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 39822 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.102 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 39822 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.752 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 39822 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.666 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 39822 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.631 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.552 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.552 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.602 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.594 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 6 | 0 / 6 | 0.000 / 6.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Par_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 39822 vertices / 98011 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39822 | 98011 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.813 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.870 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 39822 | 0 / 7 | 0 / 6 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.065 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 39822 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.878 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 28.947 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 39822 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.089 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 39822 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.715 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 39822 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.645 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 39822 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.636 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 39822 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.060 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 39822 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.731 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 39822 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.656 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 39822 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.614 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.542 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.541 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 39822 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.593 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 39822 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.592 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 6 | 0 / 6 | 0.000 / 6.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Par_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.459 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Par_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 107824 vertices / 265669 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 107824 | 265669 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 8.026 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 4.841 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 107824 | 0 / 7 | 0 / 6 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.442 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 107824 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.757 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 107824 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.368 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 107824 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.134 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 107824 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.917 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 107824 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.886 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 107824 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.265 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 107824 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.248 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 107824 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.000 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 107824 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.897 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.666 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.677 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.842 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.802 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 6 | 0 / 6 | 0.000 / 6.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Par_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 107824 vertices / 265669 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 107824 | 265669 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 7.848 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 4.738 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 107824 | 0 / 7 | 0 / 6 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 107824 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.742 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 107824 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.398 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 107824 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.154 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 107824 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.958 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 107824 | 0 / 15 | 0 / 7 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.886 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 107824 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.307 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 107824 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.237 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 107824 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.010 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 107824 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.895 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.674 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.667 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 107824 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 0.827 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 107824 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.790 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 6 | 0 / 6 | 0.000 / 6.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 5 | 0 / 5 | 0.000 / 5.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 8 | 0 / 7 | 0 / 7 | 0.000 / 1.750 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Par_SWP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.417 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Par_SWP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 95288 vertices / 299105 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 95288 | 299105 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 95288 | 0 / 14 | 0 / 13 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 7.461 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 95288 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 5.523 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 95288 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.978 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 95288 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.500 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 95288 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.594 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 95288 | 0 / 33 | 0 / 16 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.199 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 95288 | 0 / 19 | 0 / 9 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.040 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 95288 | 0 / 17 | 0 / 8 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.979 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 95288 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.592 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 95288 | 0 / 33 | 0 / 16 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.211 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 95288 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.182 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 95288 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.033 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 95288 | 0 / 14 | 0 / 13 | 0 / 2 | — / — | 0.698 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 95288 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.697 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 95288 | 0 / 14 | 0 / 13 | 0 / 2 | — / — | 0.887 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 95288 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.855 | 124.797 | odd | false | true | false | - |

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
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 240097 vertices / 733857 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 240097 | 733857 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.074 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.084 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.077 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.098 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.479 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.844 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.453 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.473 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.249 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.681 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.545 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.427 | 124.797 | even | true | true | false | - |
| zielonka | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.733 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.742 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.785 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.784 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 240097 vertices / 733857 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 240097 | 733857 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.058 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.077 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.066 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.098 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.577 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.867 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.493 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.512 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.203 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 240097 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.668 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.539 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 240097 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.424 | 124.797 | even | true | true | false | - |
| zielonka | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.733 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.732 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.783 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 240097 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.794 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 28226 vertices / 86306 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 28226 | 86306 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.591 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.520 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 15.063 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 15.139 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 3137 / 25089 | 2 / 51 | 1 / 25 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.917 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 3137 / 25089 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.452 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 3137 / 25089 | 2 / 51 | 1 / 25 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.784 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3137 / 25089 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.436 | 124.797 | even | true | true | false | - |
| zielonka | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 3137 / 25089 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.464 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3137 / 25089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 26 | 1 / 25 | 1 / 25 | 1.000 / 1.923 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 26 | 1 / 25 | 1 / 25 | 1.000 / 1.923 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=branching-bisim.gm · 37636481 vertices / 120755185 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 37636481 | 120755185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.075 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.188 | 1025.840 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.116 | 1025.785 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.860 | 1025.605 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 5.819 | 1025.477 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.778 | 991.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.272 | 1025.789 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.400 | 1025.664 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.266 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.219 | 1025.836 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.092 | 1025.922 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.028 | 1025.918 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.295 | 1025.676 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.244 | 1025.562 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.193 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.176 | 1025.605 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.176 | 1025.727 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.171 | 1025.664 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.245 | 1025.805 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.218 | 1025.805 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.060 | 1025.727 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.090 | 1025.789 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.998 | 1025.672 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.038 | 1025.719 | - | - | - | - | 1:1: failed to allocate the input buffer |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=strong-bisim.gm · 3782172 vertices / 11533061 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3782172 | 11533061 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1325.207 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.247 | 1325.094 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.076 | 1325.090 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.319 | 1325.184 | even | - | - | false | - |
| lifting-adaptive | complete | 154251 / 3627921 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 18.133 | 1324.957 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.040 | 1325.102 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 154251 / 3627921 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 17.289 | 1325.000 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.965 | 1325.090 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 1325.055 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.967 | 1324.957 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.070 | 1325.156 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.317 | 1325.102 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1325.172 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 7.285 | 1325.102 | even | - | - | false | - |
| pm-strahler+iter | complete | 154251 / 3627921 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 9.782 | 1325.109 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 7.198 | 1325.090 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1325.039 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 7.270 | 1324.996 | even | - | - | false | - |
| pm-succinct+iter | complete | 154251 / 3627921 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 12.839 | 1325.172 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 7.104 | 1325.055 | even | - | - | false | - |
| zielonka | complete | 154251 / 3627921 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 6.692 | 1325.102 | even | - | - | false | - |
| zielonka+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.814 | 1325.230 | even | - | - | false | - |
| zielonka-sym | complete | 154251 / 3627921 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 9.370 | 1325.105 | even | - | - | false | - |
| zielonka-sym+pre | complete | 154251 / 3627921 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.998 | 1325.102 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=weak-bisim.gm · 32926785 vertices / 167527601 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 32926785 | 167527601 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.457 | 1025.703 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.461 | 1025.598 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.472 | 1025.656 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.072 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 6.058 | 1025.719 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.047 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.624 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.625 | 1025.730 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.615 | 1025.789 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.083 | 1025.797 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.104 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.102 | 1025.586 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.174 | 1025.738 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.174 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.183 | 1025.738 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.181 | 1025.680 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.181 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.161 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.177 | 1025.672 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.174 | 1025.609 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.051 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.046 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.002 | 1025.730 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.084 | 1025.797 | - | - | - | - | 1:1: failed to allocate the input buffer |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=1)eq=branching-bisim.gm · 488629 vertices / 1500793 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 488629 | 1500793 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 164.980 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 165.055 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 164.922 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 165.055 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.820 | 164.777 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.850 | 164.863 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.855 | 164.918 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.897 | 165.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 165.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 165.035 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 164.926 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 164.863 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 20.173 | 164.918 | even | true | true | false | - |
| pm-strahler+pre | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 17.825 | 164.863 | even | true | true | false | - |
| pm-strahler+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.334 | 164.996 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.006 | 164.871 | even | true | true | false | - |
| pm-succinct | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.895 | 164.914 | even | true | true | false | - |
| pm-succinct+pre | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.980 | 164.930 | even | true | true | false | - |
| pm-succinct+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 2.664 | 164.801 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 2.661 | 164.930 | even | true | true | false | - |
| zielonka | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.085 | 164.988 | even | true | true | false | - |
| zielonka+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.085 | 164.910 | even | true | true | false | - |
| zielonka-sym | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.229 | 164.918 | even | true | true | false | - |
| zielonka-sym+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.237 | 164.777 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=1)eq=branching-sim.gm · 488629 vertices / 1500793 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 488629 | 1500793 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 164.922 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 164.906 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 164.895 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 164.914 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.825 | 165.055 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.855 | 165.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.843 | 165.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.895 | 164.926 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 164.926 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 165.055 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 165.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 164.984 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 20.708 | 164.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 17.814 | 164.934 | even | true | true | false | - |
| pm-strahler+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.318 | 164.914 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.992 | 164.863 | even | true | true | false | - |
| pm-succinct | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.870 | 164.934 | even | true | true | false | - |
| pm-succinct+pre | complete | 488629 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.931 | 164.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 2.665 | 164.859 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 488629 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 2.655 | 164.801 | even | true | true | false | - |
| zielonka | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.097 | 164.992 | even | true | true | false | - |
| zielonka+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.115 | 165.055 | even | true | true | false | - |
| zielonka-sym | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.248 | 165.043 | even | true | true | false | - |
| zielonka-sym+pre | complete | 488629 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.260 | 165.051 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 54758 vertices / 168878 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 54758 | 168878 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 124.797 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 6049 / 48709 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.641 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.541 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6049 / 48709 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.761 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.562 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 6049 / 48709 | 2 / 51 | 1 / 25 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.743 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.592 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 6049 / 48709 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.548 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.518 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 6049 / 48709 | 2 / 51 | 1 / 25 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.328 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.517 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 6049 / 48709 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.570 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.528 | 124.797 | even | true | true | false | - |
| zielonka | complete | 6049 / 48709 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.539 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.530 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 6049 / 48709 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.570 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6049 / 48709 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 26 | 1 / 25 | 1 / 25 | 1.000 / 1.923 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 26 | 1 / 25 | 1 / 25 | 1.000 / 1.923 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=1)eq=weak-bisim.gm · 440569 vertices / 2057941 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 440569 | 2057941 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 196.555 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 196.711 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 196.707 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 196.840 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.667 | 196.699 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.738 | 196.852 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.717 | 196.723 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.737 | 196.711 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 196.719 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 196.785 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 196.660 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 196.695 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 440569 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 17.600 | 196.562 | even | true | true | false | - |
| pm-strahler+pre | complete | 440569 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 16.336 | 196.727 | even | true | true | false | - |
| pm-strahler+iter | complete | 440569 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 3.477 | 196.668 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 440569 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 3.162 | 196.727 | even | true | true | false | - |
| pm-succinct | complete | 440569 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.554 | 196.793 | even | true | true | false | - |
| pm-succinct+pre | complete | 440569 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.553 | 196.727 | even | true | true | false | - |
| pm-succinct+iter | complete | 440569 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 2.475 | 196.715 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 440569 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 2.452 | 196.680 | even | true | true | false | - |
| zielonka | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.170 | 196.848 | even | true | true | false | - |
| zielonka+pre | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.190 | 196.848 | even | true | true | false | - |
| zielonka-sym | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.315 | 196.707 | even | true | true | false | - |
| zielonka-sym+pre | complete | 440569 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.334 | 196.578 | even | true | true | false | - |

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
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=2)eq=strong-bisim.gm · 14808231 vertices / 45377590 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14808231 | 45377590 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.935 | 1455.289 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.956 | 1453.234 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.882 | 1455.234 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.499 | 1469.730 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 10.416 | 1469.859 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.384 | 1470.105 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.079 | 1471.234 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.048 | 1471.340 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 10.037 | 1471.340 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.853 | 1470.969 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.832 | 1471.234 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.863 | 1471.086 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 9.888 | 1471.000 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.888 | 1471.020 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.858 | 1471.238 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.592 | 1471.156 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 7.583 | 1471.105 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.581 | 1471.180 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.409 | 1471.305 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.419 | 1471.367 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 8.244 | 1471.219 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.331 | 1471.230 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.165 | 1471.160 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.145 | 1471.340 | - | - | - | - | 4194304:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/CABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 24812174 vertices / 100409150 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 24812174 | 100409150 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.356 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.355 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.336 | 1025.602 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.784 | 1025.586 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 10.765 | 1025.707 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.764 | 1025.547 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.277 | 1025.789 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.277 | 1025.500 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 13.277 | 1025.379 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.595 | 1025.598 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.574 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.585 | 1025.473 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 6.736 | 1025.680 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.735 | 1025.680 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.695 | 1025.613 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.385 | 1025.676 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 7.354 | 1025.551 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.242 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.641 | 1025.609 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.498 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 7.467 | 1025.730 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.370 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.374 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.239 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=branching-sim.gm · 37636481 vertices / 120755185 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 37636481 | 120755185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.459 | 1025.637 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.479 | 1025.598 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.469 | 1025.715 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.278 | 1025.602 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 6.255 | 1025.730 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.228 | 1025.672 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.097 | 1025.727 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.058 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.118 | 1025.566 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.208 | 1025.730 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.178 | 1025.711 | - | - | - | - | 1:1: failed to allocate the input buffer |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.127 | 1025.789 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.304 | 1025.598 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.304 | 1025.801 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.293 | 1025.707 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.579 | 1025.723 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.568 | 1025.734 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.568 | 1025.805 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.178 | 1025.672 | - | - | - | - | 1:1: failed to allocate the input buffer |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.177 | 1025.738 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.084 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.065 | 1025.840 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.044 | 1025.859 | - | - | - | - | 1:1: failed to allocate the input buffer |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.085 | 1025.840 | - | - | - | - | 1:1: failed to allocate the input buffer |

</details>

