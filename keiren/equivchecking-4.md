# equivchecking, part 4

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

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

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 1095 vertices / 2052 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1095 | 2052 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.853 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.853 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.852 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.894 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.411 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.411 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.405 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.402 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.407 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.399 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1095 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 1095 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
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

<details>
<summary>equivchecking/games/Buffer_Par_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 11 vertices / 18 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11 | 18 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.417 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.396 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 11 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 11 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 11 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 11 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.406 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.411 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 2410 vertices / 5666 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2410 | 5666 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.769 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.758 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.400 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2410 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.390 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2410 | 0 / 41 | 0 / 20 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.381 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2410 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.370 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.382 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2410 | 0 / 41 | 0 / 20 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2410 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.373 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.370 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2410 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.369 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2410 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=2_windowsize=1)eq=branching-sim.gm · 3697 vertices / 9561 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3697 | 9561 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.078 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.079 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 18.994 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 19.033 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.473 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.472 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.464 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.462 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3697 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.411 | 124.797 | even | true | true | false | - |
| zielonka | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3697 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=2_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/Buffer_SWP_(datasize=2_capacity=2_windowsize=1)eq=weak-bisim.gm · 3985 vertices / 10665 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3985 | 10665 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 17.998 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 18.038 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 18.067 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 18.112 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.472 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.425 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.425 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.421 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.421 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3985 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.384 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3985 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 6722 vertices / 16466 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6722 | 16466 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.441 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 6722 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.387 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.689 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.685 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 6722 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.421 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 6722 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.390 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 6722 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 6722 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 6722 vertices / 16466 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6722 | 16466 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.441 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 6722 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 6722 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.421 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 6722 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 6722 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.421 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.390 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 6722 | 0 / 3 | 0 / 1 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 6722 | 0 / 3 | 0 / 2 | 0 / 2 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 6722 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 124.797 | odd | false | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=2_windowsize=1)eq=branching-bisim.gm · 13409 vertices / 36625 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13409 | 36625 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.431 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.431 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.432 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.569 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.601 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.583 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.615 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.740 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.730 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.546 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.535 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.570 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.523 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.476 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.475 | 124.797 | even | true | true | false | - |
| zielonka | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=2_windowsize=1)eq=branching-sim.gm · 13409 vertices / 36625 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13409 | 36625 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.600 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.580 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.582 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.592 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.730 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.721 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.537 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.537 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.526 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.525 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13409 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.467 | 124.797 | even | true | true | false | - |
| zielonka | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13409 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Buffer_SWP_(datasize=4_capacity=2_windowsize=1)eq=weak-bisim.gm · 14177 vertices / 40049 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14177 | 40049 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.436 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.583 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.581 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.680 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.689 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.526 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.529 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.504 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.504 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 14177 / 0 | 11 / 0 | 10 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.473 | 124.797 | even | true | true | false | - |
| zielonka | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 14177 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 10 / 0 | 10 / 0 | 10.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>equivchecking/games/CABP_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 7626354 vertices / 30467442 edges · 3 timeout · 21 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7626354 | 30467442 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.744 | 1622.332 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.546 | 1643.219 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.887 | 1616.715 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.881 | 1686.598 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 19.714 | 1686.672 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 19.540 | 1686.695 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 880.230 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 870.168 | - | - | - | - | deadline exceeded |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.084 | 896.641 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.259 | 1686.734 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.155 | 1686.730 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.143 | 1686.840 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 28.758 | 1590.680 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.902 | 1578.047 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.747 | 1593.039 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.309 | 1686.609 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 10.237 | 1686.430 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.124 | 1686.406 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.912 | 1637.113 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.903 | 1634.551 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 11.746 | 1637.609 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 12.474 | 1683.574 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 12.298 | 1685.727 | - | - | - | - | 5882992:31: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 12.224 | 1685.957 | - | - | - | - | 5882992:31: failed to allocate the successor list |

</details>

<details>
<summary>equivchecking/games/CABP_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 74039 vertices / 191547 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 74039 | 191547 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.583 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.582 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.589 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.590 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.357 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.519 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.967 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.967 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.277 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 74039 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.300 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.780 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 74039 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.792 | 124.797 | even | true | true | false | - |
| zielonka | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.607 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 74039 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.602 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/CABP_Par_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.407 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
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

<details>
<summary>equivchecking/games/CABP_Par_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 65131 vertices / 221717 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 65131 | 221717 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.557 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.548 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.555 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.556 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 65131 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.758 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 65131 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.045 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 65131 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.988 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 65131 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.978 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 65131 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.152 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 65131 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 1.153 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 65131 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.823 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 65131 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.824 | 124.797 | even | true | true | false | - |
| zielonka | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.561 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.572 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.592 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 65131 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.594 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/CABP_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 167247 vertices / 434239 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 167247 | 434239 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.818 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.847 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.827 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.837 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.074 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.330 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.640 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.640 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.492 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.446 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.241 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.243 | 124.797 | even | true | true | false | - |
| zielonka | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.687 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.708 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.769 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.771 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/CABP_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 167247 vertices / 434239 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 167247 | 434239 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.820 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.829 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.828 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.846 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.069 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.378 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.701 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.656 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.444 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 167247 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.444 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.229 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 167247 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.232 | 124.797 | even | true | true | false | - |
| zielonka | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.687 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.689 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.749 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 167247 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.763 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/CABP_Par_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.406 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.395 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.446 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.401 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 124.797 | odd | false | true | false | - |
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
<summary>equivchecking/games/CABP_Par_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 147323 vertices / 500573 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 147323 | 500573 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.746 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.756 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.758 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.766 | 124.797 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 124.797 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 147323 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.057 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 147323 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.262 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 147323 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.684 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 147323 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.665 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 147323 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.167 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 147323 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.160 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 147323 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.303 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 147323 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.301 | 124.797 | even | true | true | false | - |
| zielonka | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.688 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.687 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.740 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 147323 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.743 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/CABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-bisim.gm · 276225 vertices / 869985 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 276225 | 869985 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 21.447 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 21.452 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 276225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.071 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 276225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.107 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.046 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.073 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 276225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.789 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 276225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.784 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 7.051 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 7.010 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 276225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.717 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 276225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.759 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.153 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.153 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.694 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.694 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 276225 vertices / 869985 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 276225 | 869985 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 21.419 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 21.429 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 276225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.225 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 276225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.214 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.170 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.269 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 276225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.784 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 276225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.788 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 6.969 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 276225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 6.970 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 276225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.715 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 276225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.741 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.151 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.163 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.726 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 276225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.698 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 38502 vertices / 115446 edges · 21 complete · 3 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 38502 | 115446 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.491 | 124.797 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.480 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 38502 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.752 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.524 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 38502 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.658 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.567 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 38502 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 21.492 | 124.797 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.541 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 38502 | 0 / 45 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.120 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.540 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 38502 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.571 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.497 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 38502 | 0 / 45 | 0 / 22 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.902 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.486 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 38502 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.537 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.506 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 38502 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.509 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 38502 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.527 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 38502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |

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
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
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
<summary>equivchecking/games/CABP_SWP_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 245697 vertices / 1211969 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 245697 | 1211969 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.797 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 19.656 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 19.812 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 245697 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 9.054 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 245697 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 8.970 | 124.797 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 124.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 245697 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 10.875 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 245697 | 0 / 53 | 0 / 26 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 10.933 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 245697 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.988 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 245697 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.988 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 245697 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 11.739 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 245697 | 0 / 53 | 0 / 26 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 11.686 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 245697 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 4.113 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 245697 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 4.027 | 124.797 | odd | false | true | false | - |
| zielonka | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.190 | 124.797 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.215 | 124.797 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.711 | 124.797 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 245697 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 1.659 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 27 | 0 / 26 | 0 / 26 | 0.000 / 1.926 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 788225 vertices / 2505729 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 788225 | 2505729 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 267.898 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 267.898 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 268.172 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 268.152 | - | false | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 268.172 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 268.051 | - | false | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 0 / 788225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 25.929 | 268.039 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 788225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 25.929 | 268.047 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 268.176 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 268.051 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 268.039 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 268.172 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 19.543 | 267.953 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 19.552 | 267.988 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 788225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.463 | 267.996 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 788225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.466 | 268.059 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 18.189 | 267.922 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 18.308 | 268.121 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 788225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.418 | 267.977 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 788225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.297 | 267.844 | odd | false | true | false | - |
| zielonka | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.225 | 268.102 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.299 | 268.047 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 3.635 | 268.047 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 3.547 | 268.039 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 788225 vertices / 2505729 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 788225 | 2505729 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 268.109 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 268.152 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 268.047 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 267.902 | - | false | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 268.113 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 268.090 | - | false | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 0 / 788225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 26.486 | 268.176 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 788225 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 26.404 | 268.023 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 267.902 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 268.109 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 268.043 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 268.035 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 19.425 | 268.117 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 19.451 | 267.844 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 788225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.427 | 267.996 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 788225 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.439 | 267.980 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 18.171 | 268.035 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 788225 | 0 / 47 | 0 / 23 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 18.282 | 267.992 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 788225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.408 | 268.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 788225 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.297 | 267.996 | odd | false | true | false | - |
| zielonka | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.229 | 268.047 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.290 | 268.047 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 3.647 | 268.156 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 788225 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 3.542 | 268.172 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 24 | 0 / 23 | 0 / 23 | 0.000 / 1.917 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/CABP_SWP_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 700289 vertices / 3449345 edges · 10 complete · 14 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 700289 | 3449345 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 315.949 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 315.828 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 316.016 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 315.945 | - | false | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 315.887 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 315.938 | - | false | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 0 / 700289 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 24.944 | 315.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 700289 | 0 / 4 | 0 / 3 | 0 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 25.079 | 315.949 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 315.742 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 316.016 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 315.828 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 316.016 | - | false | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 315.832 | - | false | - | - | metrics: deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 315.891 | - | false | - | - | metrics: deadline exceeded |
| pm-strahler+iter | complete | 0 / 700289 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.776 | 315.715 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 700289 | 0 / 3 | 0 / 1 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.630 | 315.836 | odd | false | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 315.824 | - | false | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 315.961 | - | false | - | - | deadline exceeded |
| pm-succinct+iter | complete | 0 / 700289 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 10.092 | 315.965 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 700289 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 9.839 | 315.879 | odd | false | true | false | - |
| zielonka | complete | 0 / 700289 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.547 | 315.883 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 700289 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 2.581 | 315.887 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 700289 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 4.174 | 315.953 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 700289 | 0 / 15 | 0 / 14 | 0 / 2 | — / — | 4.168 | 316.020 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka-sym+pre | 0 / 1 | 0 / 14 | 0 / 14 | 0.000 / 14.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |

</details>

<details>
<summary>equivchecking/games/Onebit_SWP_(datasize=3_capacity=1_windowsize=1)eq=strong-bisim.gm · 19026506 vertices / 78220622 edges · 12 timeout · 12 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19026506 | 78220622 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 16.167 | 1648.965 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 16.648 | 1614.719 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.445 | 1619.098 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 770.598 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.189 | 780.734 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 784.730 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 20.759 | 1697.840 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 20.343 | 1710.234 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 19.830 | 1716.859 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 428.340 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 453.734 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 452.734 | - | - | - | - | deadline exceeded |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 19.242 | 1673.930 | - | - | - | - | 4057131:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 18.871 | 1679.105 | - | - | - | - | 4057131:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 18.813 | 1684.680 | - | - | - | - | 4057131:13: failed to allocate the successor list |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.030 | 246.801 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 240.805 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.040 | 244.676 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 20.075 | 1822.055 | - | - | - | - | 4057131:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.884 | 1862.238 | - | - | - | - | 4057131:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 20.067 | 1832.234 | - | - | - | - | 4056315:13: failed to allocate the successor list |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 33.137 | 1688.984 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 33.002 | 1714.711 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 32.175 | 1674.598 | - | - | - | - | deadline exceeded |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 10927074 vertices / 30319218 edges · 3 timeout · 21 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10927074 | 30319218 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.824 | 1674.293 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.659 | 1690.277 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.782 | 1717.395 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 29.254 | 1762.234 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 29.203 | 1726.727 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 29.077 | 1757.109 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 170.820 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.160 | 172.844 | - | - | - | - | deadline exceeded |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.313 | 176.734 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 17.231 | 1717.734 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 17.180 | 1716.355 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.642 | 1710.797 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 31.014 | 1743.797 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 30.448 | 1749.805 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 30.705 | 1743.781 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.287 | 1728.797 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 28.338 | 1733.805 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.295 | 1738.430 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 31.191 | 1854.242 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 31.326 | 1853.305 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 31.283 | 1853.773 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 29.894 | 1722.711 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 29.297 | 1737.984 | - | - | - | - | 8388608:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 29.429 | 1730.609 | - | - | - | - | 8388608:1: failed to allocate the declaration list |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.471 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.450 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.480 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.405 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.545 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.514 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.513 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.417 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.416 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.414 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.425 | 124.797 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | odd | - | - | false | - |

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
<summary>equivchecking/games/Par_Onebit_(datasize=2_capacity=1_windowsize=1)eq=weak-bisim.gm · 9558194 vertices / 36746354 edges · 6 timeout · 18 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9558194 | 36746354 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.112 | 1689.270 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.440 | 1689.105 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.412 | 1685.719 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.418 | 160.711 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 157.641 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.473 | 164.797 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.500 | 1730.859 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.107 | 1729.984 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 14.021 | 1725.461 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.281 | 300.672 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.066 | 308.734 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.037 | 304.609 | - | - | - | - | deadline exceeded |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 9.719 | 1587.805 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.614 | 1580.914 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.440 | 1599.848 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.686 | 1717.223 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 28.459 | 1717.480 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.491 | 1716.551 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.919 | 1587.789 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.787 | 1613.793 | - | - | - | - | 5696694:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 22.775 | 1598.785 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 18.212 | 1672.590 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 18.129 | 1661.598 | - | - | - | - | 5695821:66: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 18.088 | 1654.734 | - | - | - | - | 5695821:66: failed to allocate the successor list |

</details>

<details>
<summary>equivchecking/games/Par_Onebit_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 3 vertices / 3 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3 | 3 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.428 | 124.797 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.592 | 124.797 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 124.797 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.395 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.412 | 124.797 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 124.797 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.488 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.445 | 124.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 3 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 124.797 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.415 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 3 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 124.797 | odd | - | - | false | - |
| zielonka | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 124.797 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 124.797 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.401 | 124.797 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 124.797 | odd | - | - | false | - |

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
<summary>equivchecking/games/Par_Par_(datasize=2_capacity=1_windowsize=1)eq=branching-sim.gm · 9507 vertices / 19696 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9507 | 19696 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.464 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.442 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.459 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.577 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.607 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.562 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.596 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.527 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.527 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.447 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.438 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9507 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.454 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.429 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9507 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.427 | 124.797 | even | true | true | false | - |
| zielonka | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9507 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Par_Par_(datasize=2_capacity=1_windowsize=1)eq=strong-bisim.gm · 2375 vertices / 4368 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2375 | 4368 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.248 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.388 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.229 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.599 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.588 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 326 / 2049 | 2 / 29 | 1 / 14 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.408 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 326 / 2049 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.415 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 326 / 2049 | 2 / 29 | 1 / 14 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 326 / 2049 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 326 / 2049 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.405 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 326 / 2049 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 15 | 1 / 14 | 1 / 14 | 1.000 / 1.867 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 15 | 1 / 14 | 1 / 14 | 1.000 / 1.867 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Par_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-bisim.gm · 19423 vertices / 40348 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19423 | 40348 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.438 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.468 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.482 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.243 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.442 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.444 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.666 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.656 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.487 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.514 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.514 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.476 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.493 | 124.797 | even | true | true | false | - |
| zielonka | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.488 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.468 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.429 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Par_Par_(datasize=4_capacity=1_windowsize=1)eq=branching-sim.gm · 19423 vertices / 40348 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19423 | 40348 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.459 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.481 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.921 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 7.001 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.205 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.239 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.628 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.640 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.478 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.506 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 19423 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.505 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.455 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19423 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.464 | 124.797 | even | true | true | false | - |
| zielonka | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19423 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.421 | 124.797 | even | true | true | false | - |

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
<summary>equivchecking/games/Par_Par_(datasize=4_capacity=1_windowsize=1)eq=strong-bisim.gm · 4743 vertices / 8732 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4743 | 8732 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.835 | 124.797 | even | true | true | false | - |
| lifting+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| lifting+iter | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.803 | 124.797 | even | true | true | false | - |
| lifting+pre+iter | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 124.797 | even | true | true | false | - |
| lifting-adaptive | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 1.125 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 1.127 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 646 / 4097 | 2 / 29 | 1 / 14 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.390 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.379 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 646 / 4097 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.380 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.380 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 646 / 4097 | 2 / 29 | 1 / 14 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.390 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.380 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 646 / 4097 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 124.797 | even | true | true | false | - |
| zielonka | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 646 / 4097 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.392 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 646 / 4097 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 1 / 15 | 1 / 14 | 1 / 14 | 1.000 / 1.867 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 15 | 1 / 14 | 1 / 14 | 1.000 / 1.867 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>equivchecking/games/Par_Par_(datasize=4_capacity=1_windowsize=1)eq=weak-bisim.gm · 16162 vertices / 39527 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16162 | 39527 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.426 | 124.797 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.428 | 124.797 | even | true | true | false | - |
| lifting-sym | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.583 | 124.797 | even | true | true | false | - |
| lifting-sym+pre | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.595 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 124.797 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.572 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 16162 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.556 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 16162 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.567 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 16162 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16162 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.431 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 16162 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.474 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 16162 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.472 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 16162 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16162 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.422 | 124.797 | even | true | true | false | - |
| zielonka | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka+pre | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16162 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |

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

