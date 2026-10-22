# equivchecking, part 5

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

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
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 12239050 vertices / 33790242 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12239050 | 33790242 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.846 | 1006.715 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.845 | 1006.594 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.844 | 1006.672 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.845 | 1006.598 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 3.845 | 1006.730 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.844 | 1006.734 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.844 | 1006.664 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.844 | 1006.594 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.842 | 1006.602 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.795 | 1006.660 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.847 | 1006.730 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.865 | 1006.711 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 3.961 | 1006.637 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.846 | 1006.629 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.911 | 1006.664 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.794 | 1006.598 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 3.857 | 1006.680 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.813 | 1006.680 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.770 | 1006.613 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.833 | 1006.613 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 3.812 | 1006.605 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.772 | 1006.605 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.792 | 1006.590 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.792 | 1006.605 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 12239050 vertices / 33790242 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12239050 | 33790242 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.939 | 1006.715 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.939 | 1006.727 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.938 | 1006.602 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.904 | 1006.660 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 3.903 | 1006.598 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.913 | 1006.594 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.873 | 1006.730 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.843 | 1006.598 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.853 | 1006.594 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.797 | 1006.547 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.836 | 1006.547 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.857 | 1006.605 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 3.758 | 1006.613 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.305 | 1006.617 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.812 | 1006.598 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.891 | 1006.613 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 3.849 | 1006.555 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.767 | 1006.480 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.805 | 1006.680 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.822 | 1006.480 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 3.782 | 1006.715 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.819 | 1006.672 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.813 | 1006.734 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.779 | 1006.609 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 10685466 vertices / 40545186 edges · 2 complete · 6 timeout · 16 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10685466 | 40545186 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.905 | 1481.156 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.255 | 1493.781 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.058 | 1482.398 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.765 | 1494.684 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.153 | 1685.074 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.134 | 1636.285 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.240 | 1666.668 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.146 | 1637.441 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 12.765 | 1481.242 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.723 | 1493.762 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.126 | 1482.719 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.644 | 1494.809 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.067 | 1452.422 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.416 | 1452.473 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.050 | 1452.473 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.390 | 1452.363 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 9.039 | 1452.492 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.231 | 1452.355 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.936 | 1452.555 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.815 | 1452.492 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 0 / 10685466 | 0 / 13 | 0 / 12 | 0 / 2 | — / — | 24.065 | 1452.422 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 10685466 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 22.978 | 1452.480 | odd | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.140 | 1608.691 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.144 | 1807.637 | - | - | - | - | deadline exceeded |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 0 / 1 | 0 / 12 | 0 / 12 | 0.000 / 12.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-bisim.gm · 40556396 vertices / 112380248 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 40556396 | 112380248 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.188 | 1426.977 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.177 | 1426.980 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.187 | 1427.109 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.074 | 1427.164 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 7.148 | 1427.027 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.165 | 1427.234 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.790 | 1427.129 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.645 | 1427.133 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.638 | 1426.977 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.858 | 1427.152 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.847 | 1426.922 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.797 | 1426.961 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.217 | 1426.980 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.227 | 1427.105 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.225 | 1426.922 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.124 | 1426.914 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 7.139 | 1426.918 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.073 | 1427.094 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.774 | 1426.758 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.682 | 1426.867 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 8.704 | 1427.035 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.246 | 1427.105 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.262 | 1427.156 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.206 | 1427.223 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-sim.gm · 40556396 vertices / 112380248 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 40556396 | 112380248 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.404 | 1427.164 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.393 | 1427.109 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.310 | 1427.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.699 | 1427.109 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 14.546 | 1426.969 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.587 | 1427.109 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.670 | 1427.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.619 | 1427.227 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.706 | 1427.156 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.529 | 1427.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.517 | 1427.227 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.484 | 1427.105 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 7.155 | 1427.238 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.215 | 1427.039 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.075 | 1427.105 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.826 | 1427.180 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.786 | 1427.172 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.714 | 1427.031 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.417 | 1427.223 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.416 | 1427.180 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 6.425 | 1427.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.507 | 1427.148 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.519 | 1427.219 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.497 | 1427.234 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/ABP(BW)_Onebit_(datasize=3_capacity=1_windowsize=1)eq=weak-bisim.gm · 35431922 vertices / 134886692 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 35431922 | 134886692 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.474 | 1517.914 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.431 | 1517.793 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.463 | 1517.965 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.894 | 1517.797 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 11.852 | 1517.902 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.842 | 1517.859 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.126 | 1517.711 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.147 | 1517.844 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.137 | 1518.012 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.384 | 1517.859 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.374 | 1517.855 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.322 | 1517.730 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.159 | 1517.555 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.118 | 1517.723 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.108 | 1517.930 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.766 | 1517.719 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 16.758 | 1509.859 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 16.758 | 1517.723 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.400 | 1517.797 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.419 | 1517.805 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 10.375 | 1517.730 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.003 | 1517.730 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.996 | 1517.965 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.977 | 1517.461 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 9488018 vertices / 26181506 edges · 4 complete · 9 timeout · 11 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9488018 | 26181506 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.581 | 1607.098 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.389 | 1419.145 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.580 | 1608.438 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.311 | 1419.770 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.112 | 1347.582 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.097 | 1303.938 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.102 | 1348.727 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.096 | 1304.910 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.185 | 1607.312 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.308 | 1418.938 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.437 | 1608.367 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.353 | 1419.902 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 25.326 | 1926.324 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 26.081 | 1930.387 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.306 | 1911.629 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 31.401 | 1867.273 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.176 | 1917.438 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.155 | 1924.910 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.138 | 1591.059 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.185 | 1932.332 | - | - | - | - | deadline exceeded |
| zielonka | complete | 0 / 9488018 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 19.157 | 1215.109 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 9488018 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 15.267 | 1215.090 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 9488018 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 28.245 | 1528.891 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 9488018 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 25.298 | 1497.074 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 9488018 vertices / 26181506 edges · 4 complete · 8 timeout · 12 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9488018 | 26181506 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.657 | 1607.184 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.375 | 1419.324 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.605 | 1608.418 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.122 | 1419.559 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.114 | 1347.211 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.088 | 1303.977 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.119 | 1348.664 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.094 | 1304.938 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.245 | 1607.188 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.495 | 1419.109 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.337 | 1608.180 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.530 | 1419.766 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 25.401 | 1926.176 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 26.662 | 1930.973 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.775 | 1929.023 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 27.775 | 1932.090 | - | - | - | - | Failed to allocate memory |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.172 | 1925.953 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.793 | 1931.078 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.165 | 1915.391 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.203 | 1932.156 | - | - | - | - | deadline exceeded |
| zielonka | complete | 0 / 9488018 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 21.220 | 1214.918 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 9488018 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 14.906 | 1215.109 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 9488018 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 27.517 | 1528.844 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 9488018 | 0 / 10 | 0 / 9 | 0 / 2 | — / — | 24.721 | 1497.000 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 9 | 0 / 9 | 0.000 / 9.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 8326786 vertices / 31295586 edges · 1 complete · 15 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8326786 | 31295586 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.961 | 1749.891 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.768 | 1833.613 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.959 | 1742.520 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.428 | 1834.344 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.113 | 1308.551 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.104 | 1269.602 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.150 | 1309.809 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1270.758 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.220 | 1829.906 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.297 | 1833.340 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.141 | 1830.762 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.122 | 1834.441 | - | - | - | - | Failed to allocate memory |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.152 | 1881.461 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.135 | 1870.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.136 | 1851.547 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.175 | 1886.273 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.146 | 1714.723 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.156 | 1688.863 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.149 | 1586.410 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.187 | 1590.367 | - | - | - | - | deadline exceeded |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.092 | 1129.980 | - | - | - | - | deadline exceeded |
| zielonka+pre | complete | 0 / 8326786 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 17.343 | 1129.984 | odd | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.091 | 1466.305 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.088 | 1437.207 | - | - | - | - | deadline exceeded |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-bisim.gm · 31611530 vertices / 87556070 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 31611530 | 87556070 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.929 | 1415.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.929 | 1415.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.938 | 1415.344 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.266 | 1415.355 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 9.266 | 1415.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.226 | 1415.664 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.241 | 1415.461 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.190 | 1415.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.201 | 1415.543 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.508 | 1415.594 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.505 | 1415.734 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.496 | 1415.734 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 6.188 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.179 | 1415.594 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.138 | 1415.605 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.381 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.433 | 1415.613 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.442 | 1415.617 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.339 | 1415.613 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.372 | 1415.555 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.422 | 1415.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.325 | 1415.672 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.425 | 1415.734 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.364 | 1415.594 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=branching-sim.gm · 31611530 vertices / 87556070 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 31611530 | 87556070 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.337 | 1415.734 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.378 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.450 | 1415.355 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.719 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 7.647 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.627 | 1415.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.422 | 1415.590 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.393 | 1415.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.372 | 1415.590 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.960 | 1415.469 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.980 | 1415.594 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.969 | 1415.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 6.900 | 1415.613 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.998 | 1415.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.015 | 1415.539 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.490 | 1415.613 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.413 | 1415.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.417 | 1415.617 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.349 | 1415.555 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.377 | 1415.613 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.451 | 1415.672 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.346 | 1415.598 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.347 | 1415.715 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.377 | 1415.539 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/ABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=weak-bisim.gm · 27799634 vertices / 104694734 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 27799634 | 104694734 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.451 | 1511.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.471 | 1511.469 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.480 | 1511.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.418 | 1511.477 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 10.685 | 1511.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.398 | 1511.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 21.940 | 1511.211 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 21.826 | 1511.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 21.653 | 1511.227 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 16.524 | 1511.590 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.391 | 1511.477 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.387 | 1511.344 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 11.007 | 1511.551 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.994 | 1511.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.973 | 1511.367 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.215 | 1511.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 11.216 | 1511.492 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.173 | 1511.547 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.438 | 1511.617 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.398 | 1511.367 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 9.397 | 1511.477 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.495 | 1511.574 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 13.508 | 1511.379 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.532 | 1511.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/CABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 7626354 vertices / 30467442 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7626354 | 30467442 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.053 | 1784.977 | - | - | - | - | Failed to allocate memory |
| lifting+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.493 | 1048.840 | odd | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.102 | 1785.980 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.355 | 1048.965 | odd | - | - | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.091 | 1175.219 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.208 | 1049.023 | odd | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.098 | 1176.277 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.217 | 1048.719 | odd | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.773 | 1785.105 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.038 | 1048.965 | odd | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.709 | 1785.871 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.127 | 1049.031 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.211 | 1834.996 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 11.478 | 1684.230 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 7626354 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 17.553 | 1766.191 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 10.155 | 1694.203 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.188 | 1784.949 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 9.440 | 1691.523 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 7626354 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 22.869 | 1766.426 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 10.426 | 1694.059 | odd | - | - | false | - |
| zielonka | complete | 0 / 7626354 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 8.884 | 1049.012 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.070 | 1048.969 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 7626354 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 13.726 | 1288.086 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 7626354 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.984 | 1048.762 | odd | - | - | false | - |

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
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/CABP_Onebit_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 24812174 vertices / 100409150 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 24812174 | 100409150 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.977 | 1535.469 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.968 | 1535.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.955 | 1535.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.736 | 1535.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 9.672 | 1535.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.714 | 1535.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.581 | 1535.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.500 | 1535.461 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.500 | 1535.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 19.834 | 1535.504 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.834 | 1535.441 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.818 | 1535.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 9.796 | 1535.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.755 | 1535.492 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.719 | 1535.363 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.986 | 1535.492 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 9.943 | 1535.414 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.935 | 1535.680 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.989 | 1535.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.969 | 1535.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 16.957 | 1535.344 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.793 | 1535.352 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.791 | 1535.469 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.791 | 1535.715 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/Onebit_SWP_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 19026506 vertices / 78220622 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19026506 | 78220622 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.941 | 1502.367 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.951 | 1501.973 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.938 | 1502.258 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.136 | 1502.262 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 8.114 | 1502.137 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.124 | 1502.434 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.209 | 1502.062 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.179 | 1502.363 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.178 | 1502.297 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.513 | 1502.188 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.524 | 1502.391 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.513 | 1502.348 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 10.092 | 1502.020 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.124 | 1502.285 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.948 | 1502.293 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.895 | 1502.043 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 8.760 | 1502.246 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.730 | 1502.316 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.930 | 1502.090 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.909 | 1502.203 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 8.889 | 1502.270 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.645 | 1501.934 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.635 | 1502.426 | - | - | - | - | 16196318:14: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.606 | 1502.199 | - | - | - | - | 16196318:14: failed to allocate the successor list |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 10927074 vertices / 30319218 edges · 2 complete · 8 timeout · 14 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10927074 | 30319218 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.212 | 1536.473 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.533 | 1549.027 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.243 | 1537.703 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.657 | 1549.789 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.127 | 1553.848 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.121 | 1511.168 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.141 | 1555.273 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.114 | 1512.562 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.871 | 1536.219 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.514 | 1548.824 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.039 | 1537.715 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.815 | 1549.875 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 11.030 | 1835.055 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 17.111 | 1840.797 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.790 | 1835.098 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 15.286 | 1840.773 | - | - | - | - | Failed to allocate memory |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.127 | 1814.801 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.179 | 1609.211 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.713 | 1814.551 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.663 | 1840.477 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 0 / 10927074 | 0 / 12 | 0 / 11 | 0 / 2 | — / — | 23.499 | 1400.297 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 10927074 | 0 / 11 | 0 / 10 | 0 / 2 | — / — | 22.772 | 1400.340 | odd | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.097 | 1750.266 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.095 | 1718.664 | - | - | - | - | deadline exceeded |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 0 / 1 | 0 / 11 | 0 / 11 | 0.000 / 11.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 10 | 0 / 10 | 0.000 / 10.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 10927074 vertices / 30319218 edges · 9 timeout · 15 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10927074 | 30319218 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.530 | 1536.145 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.831 | 1548.793 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.560 | 1537.734 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 12.075 | 1549.832 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.124 | 1553.848 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.129 | 1511.336 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.127 | 1555.137 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.129 | 1512.562 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.888 | 1536.367 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.407 | 1548.848 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.757 | 1537.766 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.808 | 1549.891 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 11.349 | 1834.957 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.688 | 1840.723 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 12.410 | 1835.020 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.051 | 1840.699 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 31.600 | 1823.273 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 29.839 | 1832.285 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.228 | 1820.398 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.192 | 1836.590 | - | - | - | - | deadline exceeded |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.094 | 1400.234 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.092 | 1400.230 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.098 | 1750.195 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.100 | 1718.637 | - | - | - | - | deadline exceeded |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 9558194 vertices / 36746354 edges · 2 complete · 6 timeout · 16 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9558194 | 36746354 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.487 | 1571.605 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.506 | 1583.598 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.497 | 1572.867 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.087 | 1584.434 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.139 | 1514.648 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.121 | 1476.477 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.115 | 1515.906 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.141 | 1477.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.030 | 1571.734 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.134 | 1583.664 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.928 | 1572.695 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.406 | 1584.371 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.012 | 1303.180 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.649 | 1303.098 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.608 | 1303.113 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.603 | 1303.109 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.498 | 1303.055 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.675 | 1303.047 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.502 | 1302.973 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.746 | 1303.055 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 0 / 9558194 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 22.056 | 1303.105 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 9558194 | 0 / 14 | 0 / 13 | 0 / 2 | — / — | 21.429 | 1303.215 | odd | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.130 | 1442.457 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.136 | 1657.059 | - | - | - | - | deadline exceeded |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 13 | 0 / 13 | 0.000 / 13.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=branching-bisim.gm · 37636481 vertices / 120755185 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 37636481 | 120755185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.739 | 1531.379 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.731 | 1531.523 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.742 | 1531.453 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.082 | 1531.418 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 14.023 | 1531.355 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.061 | 1531.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.773 | 1531.414 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.604 | 1531.539 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 26.611 | 1531.520 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.229 | 1531.461 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.324 | 1531.395 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.234 | 1531.402 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 10.736 | 1531.281 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.660 | 1531.230 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.596 | 1531.363 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.726 | 1531.363 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 9.699 | 1531.301 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.682 | 1531.316 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.556 | 1531.402 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.515 | 1531.199 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 7.536 | 1531.543 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.776 | 1531.277 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.765 | 1531.543 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.755 | 1531.398 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=branching-sim.gm · 37636481 vertices / 120755185 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 37636481 | 120755185 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.608 | 1531.523 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 12.276 | 1531.523 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.610 | 1531.336 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.377 | 1531.402 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 11.362 | 1531.383 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.789 | 1531.402 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.946 | 1531.453 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.935 | 1531.434 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 10.854 | 1531.461 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.210 | 1531.562 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.199 | 1531.383 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.208 | 1531.418 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 9.403 | 1531.453 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.404 | 1531.211 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.393 | 1531.273 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.946 | 1531.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 8.946 | 1531.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.935 | 1531.387 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.623 | 1531.223 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.601 | 1531.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 8.612 | 1531.379 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.326 | 1531.266 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.335 | 1531.395 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.315 | 1531.266 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=2_capacity=1_windowsize=2)eq=weak-bisim.gm · 32926785 vertices / 167527601 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 32926785 | 167527601 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.407 | 1325.941 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.407 | 1325.852 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.405 | 1325.793 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.143 | 1325.879 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 7.194 | 1325.953 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.193 | 1325.945 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.642 | 1325.883 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.590 | 1325.906 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.590 | 1325.941 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.450 | 1326.027 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.450 | 1326.137 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.418 | 1325.969 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 7.050 | 1325.961 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.059 | 1326.082 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.059 | 1325.887 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.937 | 1325.891 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.917 | 1325.957 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.856 | 1326.082 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.806 | 1326.141 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.786 | 1326.082 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.892 | 1326.266 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.810 | 1326.129 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.853 | 1325.996 | - | - | - | - | 13307968:14: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.840 | 1326.141 | - | - | - | - | 13307968:14: failed to allocate the successor list |

</details>

<details>
<summary>equivchecking/games/SWP_SWP_(datasize=3_capacity=1_windowsize=2)eq=strong-bisim.gm · 14808231 vertices / 45377590 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14808231 | 45377590 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.882 | 1251.887 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.953 | 1251.898 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.880 | 1251.961 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.988 | 1251.891 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 4.843 | 1251.895 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.913 | 1251.953 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.924 | 1251.828 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.875 | 1251.898 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.913 | 1251.625 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.874 | 1251.762 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.843 | 1251.895 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.982 | 1252.023 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.893 | 1251.695 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.891 | 1251.934 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.867 | 1251.891 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.986 | 1251.969 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.890 | 1251.773 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.884 | 1251.969 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.880 | 1251.828 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.856 | 1251.898 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.761 | 1252.023 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.975 | 1251.840 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.955 | 1251.711 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.934 | 1251.750 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

