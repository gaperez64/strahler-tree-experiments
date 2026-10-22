# equivchecking, part 3

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>equivchecking/games/ABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 30922 vertices / 95682 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30922 | 95682 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 30922 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.356 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 30922 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.807 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 30922 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 1.075 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 30922 | 0 / 8 | 0 / 7 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.908 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 30922 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.235 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 30922 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.080 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 30922 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.288 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 30922 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.164 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 30922 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.896 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 30922 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.599 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 30922 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.535 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 30922 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.515 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 30922 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.909 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 30922 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.640 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 30922 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.560 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 30922 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.519 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 30922 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.465 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 30922 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.464 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 30922 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.495 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 30922 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.495 | 124.797 | odd | false | true | false | - |

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
| lifting-sym | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym+iter | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
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
<summary>equivchecking/games/ABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 97762 vertices / 240530 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 97762 | 240530 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 6.876 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 4.154 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 97762 | 0 / 6 | 0 / 5 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.972 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 97762 | 0 / 5 | 0 / 4 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.439 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 97762 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.085 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 97762 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.051 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 97762 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.883 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 97762 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.823 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 97762 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.029 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 97762 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.146 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 97762 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.940 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 97762 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.835 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.655 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.655 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 97762 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 0.799 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 97762 | 0 / 9 | 0 / 8 | 0 / 2 | — / — | 0.768 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.426 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/ABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 86802 vertices / 268594 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 86802 | 268594 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 86802 | 0 / 13 | 0 / 12 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 6.641 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 86802 | 0 / 12 | 0 / 11 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 4.731 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 86802 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 2.504 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 86802 | 0 / 8 | 0 / 7 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 2.023 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 86802 | 0 / 55 | 0 / 27 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.345 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 86802 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.224 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 86802 | 0 / 11 | 0 / 5 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.926 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 86802 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.884 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 86802 | 0 / 55 | 0 / 27 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.321 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 86802 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.384 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 86802 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.043 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 86802 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.917 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 86802 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.699 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 86802 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.675 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 86802 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 0.843 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 86802 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 0.811 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 467 vertices / 808 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 467 | 808 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.600 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.600 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.599 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.587 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| zielonka | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 467 vertices / 808 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 467 | 808 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.600 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.599 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.599 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.599 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.393 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 467 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 467 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 7 vertices / 10 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7 | 10 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.442 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.398 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 558 vertices / 883 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 558 | 883 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.883 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.876 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.875 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.877 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.384 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.405 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 558 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 124.797 | even | true | true | false | - |
| zielonka | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 558 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 1127 vertices / 2060 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1127 | 2060 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.260 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.260 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.259 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.286 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.406 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.405 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 1127 vertices / 2060 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1127 | 2060 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.270 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.272 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.251 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.291 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.385 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.400 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.390 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1127 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1127 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 11 vertices / 18 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11 | 18 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 11 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 11 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.401 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_ABP(BW)_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 1306 vertices / 2207 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1306 | 2207 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.621 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.653 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.656 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.672 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.416 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.415 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.400 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1306 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1306 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 353 vertices / 607 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 353 | 607 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.551 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.549 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.550 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.536 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 353 vertices / 607 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 353 | 607 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.550 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.551 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.548 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.556 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.406 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.395 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.395 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 353 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| zielonka | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 7 vertices / 10 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7 | 10 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_ABP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 423 vertices / 665 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 423 | 665 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.580 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.580 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.580 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.578 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.396 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.395 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 423 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 845 vertices / 1531 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 845 | 1531 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.089 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.089 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.089 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.090 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| zielonka | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 845 vertices / 1531 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 845 | 1531 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.090 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.089 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.089 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.090 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 845 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 845 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_ABP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 11 vertices / 18 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11 | 18 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 11 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 11 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.416 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_ABP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 983 vertices / 1645 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 983 | 1645 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.230 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.230 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.231 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.232 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.416 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.417 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.416 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 983 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| zielonka | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.384 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 983 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_CABP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 3457 vertices / 8945 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3457 | 8945 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.270 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.219 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.245 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 14.305 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.472 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.442 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.537 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3457 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.415 | 124.797 | even | true | true | false | - |
| zielonka | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.400 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3457 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_CABP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.401 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Buffer_CABP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 3761 vertices / 9457 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3761 | 9457 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 13.598 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 13.671 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 13.627 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 13.666 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3761 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.400 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_CABP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 8961 vertices / 25073 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8961 | 25073 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.568 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.568 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.586 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.586 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.482 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.442 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8961 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.442 | 124.797 | even | true | true | false | - |
| zielonka | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8961 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_CABP_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.415 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_CABP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 9553 vertices / 26273 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9553 | 26273 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.425 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.562 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.560 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.566 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.568 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.544 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.545 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.473 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.464 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.463 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9553 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.445 | 124.797 | even | true | true | false | - |
| zielonka | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 604354 vertices / 1658402 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 604354 | 1658402 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 189.086 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.190 | 188.320 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 189.078 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.126 | 188.234 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 10.670 | 188.391 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.313 | 188.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 604354 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 5.854 | 188.402 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.312 | 188.461 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 189.074 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.252 | 188.191 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 189.090 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.234 | 188.363 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 604354 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 8.200 | 188.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.486 | 188.336 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 604354 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.308 | 188.281 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.494 | 188.348 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 604354 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 10.234 | 188.410 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.373 | 188.406 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 604354 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.631 | 188.281 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.394 | 188.281 | odd | false | true | false | - |
| zielonka | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.437 | 188.340 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.233 | 188.445 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.867 | 188.445 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.259 | 188.465 | odd | false | true | false | - |

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
| pm-strahler | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 604354 vertices / 1658402 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 604354 | 1658402 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 189.133 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.207 | 188.395 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 189.219 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.147 | 188.465 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 10.642 | 188.332 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.340 | 188.254 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 604354 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 5.883 | 188.445 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.322 | 188.445 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 188.941 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.258 | 188.430 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 189.199 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.243 | 188.336 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 604354 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 8.328 | 188.266 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.492 | 188.273 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 604354 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.323 | 188.406 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.504 | 188.340 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 604354 | 0 / 31 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 10.074 | 188.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.383 | 188.133 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 604354 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.641 | 188.406 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.399 | 188.324 | odd | false | true | false | - |
| zielonka | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.404 | 188.336 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.229 | 188.336 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 604354 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 1.888 | 188.453 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 604354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.269 | 188.328 | odd | false | true | false | - |

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
| pm-strahler | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.397 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.398 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=2_windowsize=1)eq=branching-bisim.gm · 912641 vertices / 2762529 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 912641 | 2762529 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 298.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 297.988 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 297.988 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 297.910 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.986 | 298.109 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.109 | 298.117 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.278 | 298.062 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.325 | 297.980 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 298.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 298.102 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 298.121 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 298.121 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 297.797 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 298.066 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.789 | 298.004 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.870 | 298.066 | even | true | true | false | - |
| pm-succinct | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.587 | 297.984 | even | true | true | false | - |
| pm-succinct+pre | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.576 | 298.066 | even | true | true | false | - |
| pm-succinct+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.788 | 297.914 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.384 | 298.004 | even | true | true | false | - |
| zielonka | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.714 | 297.992 | even | true | true | false | - |
| zielonka+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.777 | 298.121 | even | true | true | false | - |
| zielonka-sym | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.026 | 297.988 | even | true | true | false | - |
| zielonka-sym+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.086 | 297.996 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=2_windowsize=1)eq=branching-sim.gm · 912641 vertices / 2762529 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 912641 | 2762529 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 298.094 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 298.000 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 298.121 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 298.105 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.008 | 298.125 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.090 | 297.992 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.292 | 298.055 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.345 | 297.996 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 298.102 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 297.992 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 297.848 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 298.113 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 297.941 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 298.004 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.764 | 298.066 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.899 | 298.000 | even | true | true | false | - |
| pm-succinct | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.450 | 298.004 | even | true | true | false | - |
| pm-succinct+pre | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.544 | 297.988 | even | true | true | false | - |
| pm-succinct+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.799 | 298.004 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 912641 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.469 | 297.871 | even | true | true | false | - |
| zielonka | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.724 | 298.105 | even | true | true | false | - |
| zielonka+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.798 | 297.984 | even | true | true | false | - |
| zielonka-sym | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.025 | 297.984 | even | true | true | false | - |
| zielonka-sym+pre | complete | 912641 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.054 | 297.852 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=2_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=2_capacity=2_windowsize=1)eq=weak-bisim.gm · 966897 vertices / 3278913 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 966897 | 3278913 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 350.715 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 350.535 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 350.672 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 350.672 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.057 | 350.562 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.077 | 350.680 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.391 | 350.809 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.381 | 350.680 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 350.680 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 350.812 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 350.625 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 350.793 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 350.621 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 350.691 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 16.404 | 350.691 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 16.408 | 350.672 | even | true | true | false | - |
| pm-succinct | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.458 | 350.754 | even | true | true | false | - |
| pm-succinct+pre | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 14.365 | 350.695 | even | true | true | false | - |
| pm-succinct+iter | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 9.979 | 350.594 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 966897 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 9.510 | 350.484 | even | true | true | false | - |
| zielonka | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.866 | 350.680 | even | true | true | false | - |
| zielonka+pre | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.887 | 350.789 | even | true | true | false | - |
| zielonka-sym | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.229 | 350.809 | even | true | true | false | - |
| zielonka-sym+pre | complete | 966897 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.195 | 350.750 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-bisim.gm · 2076302 vertices / 5857418 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2076302 | 5857418 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 655.109 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.344 | 655.105 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 654.969 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.325 | 655.105 | odd | false | true | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.043 | 654.977 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.318 | 654.918 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2076302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 18.219 | 654.980 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.297 | 654.969 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.050 | 654.980 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.260 | 654.973 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.056 | 655.109 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.499 | 654.977 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2076302 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 28.666 | 654.988 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.811 | 654.969 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2076302 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 6.194 | 655.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.728 | 654.984 | odd | false | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.045 | 654.973 | - | false | - | - | deadline exceeded |
| pm-succinct+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.681 | 655.074 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2076302 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.978 | 654.988 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.758 | 654.918 | odd | false | true | false | - |
| zielonka | complete | 0 / 2076302 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 3.722 | 655.129 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.215 | 654.844 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2076302 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 5.109 | 655.109 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.032 | 655.105 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-sim.gm · 2076302 vertices / 5857418 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2076302 | 5857418 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.050 | 654.977 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.353 | 654.922 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.051 | 655.043 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.357 | 654.922 | odd | false | true | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.042 | 655.105 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.315 | 655.047 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2076302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 18.311 | 655.105 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.282 | 654.836 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.052 | 654.883 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.262 | 655.023 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.054 | 654.832 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.501 | 654.980 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2076302 | 0 / 31 | 0 / 15 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 28.605 | 654.969 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.826 | 654.852 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2076302 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 6.151 | 654.969 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.721 | 655.051 | odd | false | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 654.973 | - | false | - | - | deadline exceeded |
| pm-succinct+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.678 | 655.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2076302 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.992 | 654.922 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.747 | 654.984 | odd | false | true | false | - |
| zielonka | complete | 0 / 2076302 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 3.706 | 654.977 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.179 | 655.043 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2076302 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 5.138 | 654.836 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2076302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.022 | 654.980 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 16 | 0 / 15 | 0 / 15 | 0.000 / 1.875 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.419 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.418 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=1_windowsize=1)eq=weak-bisim.gm · 2162594 vertices / 6445442 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2162594 | 6445442 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.066 | 737.598 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.718 | 737.508 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.066 | 737.578 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.514 | 737.578 | odd | false | true | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 737.594 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.560 | 737.602 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2162594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 23.505 | 737.465 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.531 | 737.578 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 737.582 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.494 | 737.598 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.080 | 737.578 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.831 | 737.473 | odd | false | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 737.270 | - | false | - | - | deadline exceeded |
| pm-strahler+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 4.361 | 737.270 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2162594 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 7.384 | 737.477 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 4.144 | 737.270 | odd | false | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 737.402 | - | false | - | - | deadline exceeded |
| pm-succinct+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 4.117 | 737.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2162594 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 9.160 | 737.566 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 4.149 | 737.422 | odd | false | true | false | - |
| zielonka | complete | 0 / 2162594 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 4.007 | 737.469 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.450 | 737.480 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2162594 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 5.519 | 737.473 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2162594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.364 | 737.465 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=2_windowsize=1)eq=branching-bisim.gm · 3471553 vertices / 11083645 edges · 8 complete · 16 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3471553 | 11083645 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1168.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1168.691 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1168.508 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.076 | 1168.742 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 17.741 | 1168.703 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 18.133 | 1168.770 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.617 | 1168.770 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.833 | 1168.496 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1168.645 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.084 | 1168.633 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 1168.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.070 | 1168.629 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.056 | 1168.582 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.066 | 1168.711 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.060 | 1168.648 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.070 | 1168.574 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 1168.715 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 1168.570 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 1168.445 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 1168.441 | - | true | - | - | deadline exceeded |
| zielonka | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.470 | 1168.750 | even | true | true | false | - |
| zielonka+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.963 | 1168.582 | even | true | true | false | - |
| zielonka-sym | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.041 | 1168.609 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.298 | 1168.750 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=2_windowsize=1)eq=branching-sim.gm · 3471553 vertices / 11083645 edges · 8 complete · 16 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3471553 | 11083645 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.082 | 1168.746 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.081 | 1168.578 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.081 | 1168.641 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.074 | 1168.637 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 18.202 | 1168.492 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 18.588 | 1168.770 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.577 | 1168.629 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.759 | 1168.641 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1168.727 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 1168.609 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.068 | 1168.770 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 1168.641 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 1168.590 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.056 | 1168.512 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.060 | 1168.648 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1168.465 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 1168.438 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.054 | 1168.645 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 1168.578 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 1168.504 | - | true | - | - | deadline exceeded |
| zielonka | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.457 | 1168.492 | even | true | true | false | - |
| zielonka+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.952 | 1168.633 | even | true | true | false | - |
| zielonka-sym | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.045 | 1168.504 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3471553 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.331 | 1168.629 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=2_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.408 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.417 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.417 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_Onebit_(datasize=3_capacity=2_windowsize=1)eq=weak-bisim.gm · 3644173 vertices / 12968893 edges · 8 complete · 16 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3644173 | 12968893 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.084 | 1359.883 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.082 | 1360.012 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 1359.879 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.074 | 1359.965 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 21.038 | 1359.902 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 21.038 | 1360.031 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 17.937 | 1359.902 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 17.947 | 1359.918 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.085 | 1360.000 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 1359.879 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1360.133 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.075 | 1360.039 | - | true | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 1359.945 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.076 | 1359.996 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 1359.953 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 1359.953 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1360.000 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1360.078 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.090 | 1359.805 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.086 | 1360.016 | - | true | - | - | deadline exceeded |
| zielonka | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 6.166 | 1360.008 | even | true | true | false | - |
| zielonka+pre | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 6.339 | 1360.016 | even | true | true | false | - |
| zielonka-sym | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.836 | 1360.004 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3644173 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.906 | 1360.008 | even | true | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 447 vertices / 788 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 447 | 788 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.663 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.659 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.661 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.650 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.416 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 447 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| zielonka | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 447 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_Par_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 7 vertices / 10 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7 | 10 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 532 vertices / 859 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 532 | 859 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.009 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.008 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.008 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.010 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.396 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 532 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 124.797 | even | true | true | false | - |
| zielonka | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 532 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 1095 vertices / 2052 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1095 | 2052 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.852 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.851 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.851 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.904 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |

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

