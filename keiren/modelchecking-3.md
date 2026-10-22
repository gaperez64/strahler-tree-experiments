# modelchecking, part 3

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/CCP_3.2._max_copies_per_region.gm · 6 vertices / 8 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6 | 8 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 72.199 | odd | - | - | false | - |
| lifting+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 72.199 | odd | - | - | false | - |
| lifting+iter | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 72.199 | odd | - | - | false | - |
| lifting+pre+iter | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 72.199 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 72.199 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 72.199 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 72.199 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 72.199 | odd | - | - | false | - |
| lifting-sym | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 72.199 | odd | - | - | false | - |
| lifting-sym+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 72.199 | odd | - | - | false | - |
| lifting-sym+iter | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 72.199 | odd | - | - | false | - |
| lifting-sym+pre+iter | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 72.199 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 6 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 72.199 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 72.199 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 6 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 72.199 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 72.199 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 6 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.407 | 72.199 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.406 | 72.199 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 6 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 72.199 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.406 | 72.199 | odd | - | - | false | - |
| zielonka | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 72.199 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 72.199 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 6 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.407 | 72.199 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 6 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 72.199 | odd | - | - | false | - |

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
<summary>modelchecking/games/Clobberwidth=4_height=4_black_has_winning_strategy.gm · 564914 vertices / 2185853 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 564914 | 2185853 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 217.598 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.368 | 217.535 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 217.590 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.353 | 217.777 | even | - | - | false | - |
| lifting-adaptive | complete | 351653 / 213261 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 3.076 | 217.660 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.513 | 217.727 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 351653 / 213261 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 3.247 | 217.594 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.511 | 217.598 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 217.703 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.444 | 217.461 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 217.539 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.410 | 217.449 | even | - | - | false | - |
| pm-strahler | complete | 351653 / 213261 | 15 / 2 | 14 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 11.199 | 217.539 | even | - | - | false | - |
| pm-strahler+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.617 | 217.590 | even | - | - | false | - |
| pm-strahler+iter | complete | 351653 / 213261 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.888 | 217.527 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.591 | 217.668 | even | - | - | false | - |
| pm-succinct | complete | 351653 / 213261 | 15 / 2 | 14 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 8.632 | 217.586 | even | - | - | false | - |
| pm-succinct+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.549 | 217.543 | even | - | - | false | - |
| pm-succinct+iter | complete | 351653 / 213261 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 2.185 | 217.672 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.571 | 217.668 | even | - | - | false | - |
| zielonka | complete | 351653 / 213261 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.496 | 217.586 | even | - | - | false | - |
| zielonka+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.448 | 217.594 | even | - | - | false | - |
| zielonka-sym | complete | 351653 / 213261 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 2.024 | 217.727 | even | - | - | false | - |
| zielonka-sym+pre | complete | 351653 / 213261 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.446 | 217.648 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 14 / 1 | 14 / 1 | 14.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 14 / 1 | 14 / 1 | 14.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Clobberwidth=4_height=4_white_has_winning_strategy.gm · 564914 vertices / 2185853 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 564914 | 2185853 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 217.727 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.403 | 217.535 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 217.590 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.374 | 217.707 | odd | false | true | false | - |
| lifting-adaptive | complete | 213262 / 351652 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 2.922 | 217.594 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.508 | 217.750 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 213262 / 351652 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 3.085 | 217.594 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.509 | 217.660 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 217.602 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.495 | 217.582 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 217.586 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.427 | 217.723 | odd | false | true | false | - |
| pm-strahler | complete | 213262 / 351652 | 14 / 2 | 13 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 8.564 | 217.551 | odd | false | true | false | - |
| pm-strahler+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.585 | 217.668 | odd | false | true | false | - |
| pm-strahler+iter | complete | 213262 / 351652 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.779 | 217.590 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.567 | 217.535 | odd | false | true | false | - |
| pm-succinct | complete | 213262 / 351652 | 14 / 2 | 13 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 6.614 | 217.375 | odd | false | true | false | - |
| pm-succinct+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.568 | 217.590 | odd | false | true | false | - |
| pm-succinct+iter | complete | 213262 / 351652 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 1.934 | 217.668 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.584 | 217.602 | odd | false | true | false | - |
| zielonka | complete | 213262 / 351652 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.476 | 217.449 | odd | false | true | false | - |
| zielonka+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.433 | 217.594 | odd | false | true | false | - |
| zielonka-sym | complete | 213262 / 351652 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.911 | 217.723 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 213262 / 351652 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.445 | 217.449 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 13 / 1 | 13 / 1 | 13.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 13 / 1 | 13 / 1 | 13.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Debug_spec_nodeadlock.gm · 2 vertices / 2 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2 | 2 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=1 / H=1, K=1, t=1 | 0.407 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=1 / H=1, K=1, t=1 | 0.406 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=1 / H=1, K=1, t=1 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=1 / H=1, K=1, t=1 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 73.324 | even | true | true | false | - |
| zielonka | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 2 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Domineeringwidth=4_height=4_player1_has_winning_strategy.gm · 2229 vertices / 7060 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2229 | 7060 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.699 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.697 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.369 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.450 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.387 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.880 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.895 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 1099 / 1130 | 11 / 2 | 10 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.403 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 1099 / 1130 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 1099 / 1130 | 11 / 2 | 10 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 1099 / 1130 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 73.324 | even | true | true | false | - |
| zielonka | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 1099 / 1130 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1099 / 1130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 10 / 1 | 10 / 1 | 10.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 10 / 1 | 10 / 1 | 10.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Domineeringwidth=4_height=4_player2_has_winning_strategy.gm · 2229 vertices / 7060 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2229 | 7060 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.717 | 73.324 | odd | false | true | false | - |
| lifting+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 73.324 | odd | false | true | false | - |
| lifting+iter | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.718 | 73.324 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 73.324 | odd | false | true | false | - |
| lifting-adaptive | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.369 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 73.324 | odd | false | true | false | - |
| lifting-sym | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.862 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 73.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.875 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 73.324 | odd | false | true | false | - |
| pm-strahler | complete | 1131 / 1098 | 9 / 2 | 8 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 73.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1131 / 1098 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-succinct | complete | 1131 / 1098 | 9 / 2 | 8 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 73.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1131 / 1098 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 73.324 | odd | false | true | false | - |
| zielonka | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.405 | 73.324 | odd | false | true | false | - |
| zielonka+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 73.324 | odd | false | true | false | - |
| zielonka-sym | complete | 1131 / 1098 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 73.324 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1131 / 1098 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 73.324 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 8 / 1 | 8 / 1 | 8.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 8 / 1 | 8 / 1 | 8.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=2_always_if_max_floor_requested_eventually_at_max_floor.gm · 13 vertices / 18 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13 | 18 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.410 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.410 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.409 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.402 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.402 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.402 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| zielonka | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=3_always_if_max_floor_requested_eventually_at_max_floor.gm · 25 vertices / 42 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 25 | 42 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.406 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.400 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.410 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.393 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.395 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 73.324 | even | true | true | false | - |
| zielonka | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=4_always_if_max_floor_requested_eventually_at_max_floor.gm · 43 vertices / 78 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 43 | 78 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.420 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.419 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.419 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.437 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.399 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.393 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.395 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 43 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| zielonka | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 43 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=5_always_if_max_floor_requested_eventually_at_max_floor.gm · 67 vertices / 126 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 67 | 126 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.416 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.416 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 67 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| zielonka | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 67 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=6_always_if_max_floor_requested_eventually_at_max_floor.gm · 97 vertices / 186 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 97 | 186 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.418 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.414 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.413 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.395 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.394 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.401 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.394 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 97 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.394 | 73.324 | even | true | true | false | - |
| zielonka | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 97 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=7_always_if_max_floor_requested_eventually_at_max_floor.gm · 133 vertices / 258 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 133 | 258 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.448 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.447 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.446 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.437 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.402 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 133 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 73.324 | even | true | true | false | - |
| zielonka | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 133 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=FIFO_storeys=8_always_if_max_floor_requested_eventually_at_max_floor.gm · 175 vertices / 342 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 175 | 342 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.468 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.468 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.467 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.455 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 175 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 73.324 | even | true | true | false | - |
| zielonka | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.396 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.396 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 175 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.396 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=LIFO_storeys=2_always_if_max_floor_requested_eventually_at_max_floor.gm · 13 vertices / 18 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13 | 18 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 73.324 | even | true | true | false | - |
| lifting+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 73.324 | even | true | true | false | - |
| lifting+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 73.324 | even | true | true | false | - |
| lifting+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 73.324 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 73.324 | even | true | true | false | - |
| lifting-sym | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 73.324 | even | true | true | false | - |
| lifting-sym+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 73.324 | even | true | true | false | - |
| lifting-sym+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 73.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 73.324 | even | true | true | false | - |
| pm-strahler | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct+pre | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.408 | 73.324 | even | true | true | false | - |
| pm-succinct+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 73.324 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.408 | 73.324 | even | true | true | false | - |
| zielonka | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 73.324 | even | true | true | false | - |
| zielonka+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka-sym | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 73.324 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 73.324 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=LIFO_storeys=3_always_if_max_floor_requested_eventually_at_max_floor.gm · 43 vertices / 85 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 43 | 85 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.405 | 73.324 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.405 | 73.324 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.404 | 73.324 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.406 | 73.324 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 73.324 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.404 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.406 | 73.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.407 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.407 | 73.324 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 43 | 0 / 18 | 0 / 11 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 43 | 0 / 18 | 0 / 11 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 73.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 43 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 43 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 73.324 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 43 | 0 / 20 | 0 / 11 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.407 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 43 | 0 / 20 | 0 / 11 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.407 | 73.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 43 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 43 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 73.324 | odd | false | true | false | - |
| zielonka | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 73.324 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 73.324 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 73.324 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 43 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 73.324 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 0 / 7 | 0 / 11 | 0 / 6 | 0.000 / 2.429 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 7 | 0 / 11 | 0 / 6 | 0.000 / 2.429 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 9 | 0 / 11 | 0 / 8 | 0.000 / 2.111 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 9 | 0 / 11 | 0 / 8 | 0.000 / 2.111 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=LIFO_storeys=4_always_if_max_floor_requested_eventually_at_max_floor.gm · 343 vertices / 957 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 343 | 957 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.457 | 73.324 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.457 | 73.324 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.457 | 73.324 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.447 | 73.324 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 73.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 73.324 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 343 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 343 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 73.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 343 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 343 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.396 | 73.324 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 343 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.395 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 343 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.395 | 73.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 343 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 343 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 73.324 | odd | false | true | false | - |
| zielonka | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 73.324 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 73.324 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 73.324 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 343 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 73.324 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=LIFO_storeys=5_always_if_max_floor_requested_eventually_at_max_floor.gm · 2395 vertices / 8767 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2395 | 8767 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.086 | 73.324 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.075 | 73.324 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.086 | 73.324 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.134 | 73.324 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 73.324 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 73.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 73.324 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2395 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.424 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2395 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.422 | 73.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2395 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.411 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2395 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.401 | 73.324 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2395 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2395 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.401 | 73.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2395 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2395 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 73.324 | odd | false | true | false | - |
| zielonka | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 73.324 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.412 | 73.324 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 73.324 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2395 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 73.324 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Elevatorpolicy=LIFO_storeys=6_always_if_max_floor_requested_eventually_at_max_floor.gm · 17773 vertices / 81348 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 17773 | 81348 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 73.324 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 73.324 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 73.324 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 73.324 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.456 | 73.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.455 | 73.324 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.724 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.666 | 73.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.209 | 73.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.245 | 73.324 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 17773 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.967 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 17773 | 0 / 17 | 0 / 10 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.989 | 73.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 17773 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.592 | 73.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 17773 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.607 | 73.324 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 17773 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.538 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 17773 | 0 / 16 | 0 / 9 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.547 | 73.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 17773 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.485 | 73.324 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 17773 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.475 | 73.324 | odd | false | true | false | - |
| zielonka | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.433 | 73.324 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.423 | 73.324 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.434 | 73.324 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 17773 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.423 | 73.324 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 7 | 0 / 10 | 0 / 6 | 0.000 / 2.286 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 9 | 0 / 6 | 0.000 / 2.143 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=10_eventually_done.gm · 59051 vertices / 177145 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 59051 | 177145 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=15 / H=1, K=1, t=15 | 23.745 | 74.500 | even | true | true | false | - |
| lifting+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 74.500 | even | true | true | false | - |
| lifting+iter | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=15 / H=1, K=1, t=15 | 23.754 | 74.500 | even | true | true | false | - |
| lifting+pre+iter | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 74.500 | even | true | true | false | - |
| lifting-adaptive | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 4.342 | 74.500 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.565 | 74.500 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 4.404 | 74.500 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.529 | 74.500 | even | true | true | false | - |
| lifting-sym | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=15 / H=1, K=1, t=15 | 16.030 | 74.500 | even | true | true | false | - |
| lifting-sym+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 74.500 | even | true | true | false | - |
| lifting-sym+iter | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=15 / H=1, K=1, t=15 | 11.622 | 74.500 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 74.500 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 74.500 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.485 | 74.500 | even | true | true | false | - |
| pm-strahler+iter | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.495 | 74.500 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.497 | 74.500 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 74.500 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.452 | 74.500 | even | true | true | false | - |
| pm-succinct+iter | complete | 59051 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.472 | 74.500 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.451 | 74.500 | even | true | true | false | - |
| zielonka | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.452 | 74.500 | even | true | true | false | - |
| zielonka+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.441 | 74.500 | even | true | true | false | - |
| zielonka-sym | complete | 59051 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.473 | 74.500 | even | true | true | false | - |
| zielonka-sym+pre | complete | 59051 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 74.500 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=11_eventually_done.gm · 177149 vertices / 531439 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 177149 | 531439 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 74.637 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 74.637 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 74.637 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.618 | 74.637 | even | true | true | false | - |
| lifting-adaptive | complete | 177149 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 25.731 | 74.637 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.686 | 74.637 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 177149 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 25.566 | 74.637 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 74.637 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 74.637 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.601 | 74.637 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 74.637 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.710 | 74.637 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 74.637 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.673 | 74.637 | even | true | true | false | - |
| pm-strahler+iter | complete | 177149 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.670 | 74.637 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.616 | 74.637 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 74.637 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.598 | 74.637 | even | true | true | false | - |
| pm-succinct+iter | complete | 177149 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.678 | 74.637 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.596 | 74.637 | even | true | true | false | - |
| zielonka | complete | 177149 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.599 | 74.637 | even | true | true | false | - |
| zielonka+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.573 | 74.637 | even | true | true | false | - |
| zielonka-sym | complete | 177149 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.667 | 74.637 | even | true | true | false | - |
| zielonka-sym+pre | complete | 177149 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.566 | 74.637 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=12_eventually_done.gm · 531443 vertices / 1594321 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 531443 | 1594321 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 197.410 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.089 | 197.266 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 197.473 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.054 | 197.539 | even | - | - | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 197.543 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.103 | 197.520 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 197.266 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.086 | 197.543 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 197.457 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.082 | 197.266 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 197.398 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.177 | 197.543 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 197.363 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.221 | 197.484 | even | - | - | false | - |
| pm-strahler+iter | complete | 531443 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.212 | 197.484 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.137 | 197.363 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 197.484 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.128 | 197.484 | even | - | - | false | - |
| pm-succinct+iter | complete | 531443 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 1.312 | 197.398 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.085 | 197.418 | even | - | - | false | - |
| zielonka | complete | 531443 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.101 | 197.477 | even | - | - | false | - |
| zielonka+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.997 | 197.402 | even | - | - | false | - |
| zielonka-sym | complete | 531443 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.338 | 197.246 | even | - | - | false | - |
| zielonka-sym+pre | complete | 531443 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.018 | 197.418 | even | - | - | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=13_eventually_done.gm · 1594325 vertices / 4782967 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1594325 | 4782967 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 591.789 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.537 | 591.996 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 591.992 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.527 | 591.938 | even | - | - | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.037 | 591.836 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.500 | 592.059 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.042 | 592.066 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.480 | 591.938 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.061 | 592.062 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.465 | 592.066 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 592.066 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.684 | 591.926 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 591.883 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 2.878 | 591.941 | even | - | - | false | - |
| pm-strahler+iter | complete | 1594325 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 2.918 | 592.008 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 2.665 | 592.012 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 591.867 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 2.667 | 591.926 | even | - | - | false | - |
| pm-succinct+iter | complete | 1594325 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 3.253 | 591.879 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 2.571 | 591.930 | even | - | - | false | - |
| zielonka | complete | 1594325 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 2.610 | 592.066 | even | - | - | false | - |
| zielonka+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.295 | 591.992 | even | - | - | false | - |
| zielonka-sym | complete | 1594325 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 3.265 | 591.926 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1594325 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.294 | 592.047 | even | - | - | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=8_eventually_done.gm · 6563 vertices / 19681 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6563 | 19681 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.642 | 75.238 | even | true | true | false | - |
| lifting+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 75.238 | even | true | true | false | - |
| lifting+iter | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.641 | 75.238 | even | true | true | false | - |
| lifting+pre+iter | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 75.238 | even | true | true | false | - |
| lifting-adaptive | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.494 | 75.238 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 75.238 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.485 | 75.238 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 75.238 | even | true | true | false | - |
| lifting-sym | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.556 | 75.238 | even | true | true | false | - |
| lifting-sym+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 75.238 | even | true | true | false | - |
| lifting-sym+iter | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.545 | 75.238 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 75.238 | even | true | true | false | - |
| pm-strahler | complete | 6563 / 0 | 259 / 0 | 258 / 0 | 2 / 0 | k=2, t=8, depth=1 / k=2, t=8, depth=1 | 2.170 | 75.238 | even | true | true | false | - |
| pm-strahler+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 75.238 | even | true | true | false | - |
| pm-strahler+iter | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.382 | 75.238 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.381 | 75.238 | even | true | true | false | - |
| pm-succinct | complete | 6563 / 0 | 259 / 0 | 258 / 0 | 2 / 0 | bits=8, depth=1 / bits=8, depth=1 | 1.767 | 75.238 | even | true | true | false | - |
| pm-succinct+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.369 | 75.238 | even | true | true | false | - |
| pm-succinct+iter | complete | 6563 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.379 | 75.238 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.380 | 75.238 | even | true | true | false | - |
| zielonka | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 75.238 | even | true | true | false | - |
| zielonka+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 75.238 | even | true | true | false | - |
| zielonka-sym | complete | 6563 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 75.238 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6563 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 75.238 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 258 / 0 | 258 / 0 | 258.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 258 / 0 | 258 / 0 | 258.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hanoindisks=9_eventually_done.gm · 19685 vertices / 59047 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19685 | 59047 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=14 / H=1, K=1, t=14 | 3.999 | 75.238 | even | true | true | false | - |
| lifting+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 75.238 | even | true | true | false | - |
| lifting+iter | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=14 / H=1, K=1, t=14 | 4.100 | 75.238 | even | true | true | false | - |
| lifting+pre+iter | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 75.238 | even | true | true | false | - |
| lifting-adaptive | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.064 | 75.238 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 75.238 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.039 | 75.238 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 75.238 | even | true | true | false | - |
| lifting-sym | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=14 / H=1, K=1, t=14 | 3.091 | 75.238 | even | true | true | false | - |
| lifting-sym+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 75.238 | even | true | true | false | - |
| lifting-sym+iter | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=14 / H=1, K=1, t=14 | 3.020 | 75.238 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 75.238 | even | true | true | false | - |
| pm-strahler | complete | 19685 / 0 | 515 / 0 | 514 / 0 | 2 / 0 | k=2, t=9, depth=1 / k=2, t=9, depth=1 | 11.507 | 75.238 | even | true | true | false | - |
| pm-strahler+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 75.238 | even | true | true | false | - |
| pm-strahler+iter | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 75.238 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 75.238 | even | true | true | false | - |
| pm-succinct | complete | 19685 / 0 | 515 / 0 | 514 / 0 | 2 / 0 | bits=9, depth=1 / bits=9, depth=1 | 8.758 | 75.238 | even | true | true | false | - |
| pm-succinct+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.390 | 75.238 | even | true | true | false | - |
| pm-succinct+iter | complete | 19685 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 75.238 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.391 | 75.238 | even | true | true | false | - |
| zielonka | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.390 | 75.238 | even | true | true | false | - |
| zielonka+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 75.238 | even | true | true | false | - |
| zielonka-sym | complete | 19685 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.400 | 75.238 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19685 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 75.238 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 514 / 0 | 514 / 0 | 514.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 514 / 0 | 514 / 0 | 514.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hesselinkdatasize=2_nodeadlock.gm · 540737 vertices / 1115713 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 540737 | 1115713 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 1.233 | 143.086 | even | - | - | false | - |
| lifting+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.945 | 142.938 | even | - | - | false | - |
| lifting+iter | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 1.263 | 143.004 | even | - | - | false | - |
| lifting+pre+iter | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.900 | 142.957 | even | - | - | false | - |
| lifting-adaptive | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.191 | 142.945 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.891 | 142.945 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.221 | 142.949 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.901 | 143.082 | even | - | - | false | - |
| lifting-sym | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 1.178 | 143.113 | even | - | - | false | - |
| lifting-sym+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.909 | 142.953 | even | - | - | false | - |
| lifting-sym+iter | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 1.189 | 142.949 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.900 | 143.086 | even | - | - | false | - |
| pm-strahler | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.316 | 142.828 | even | - | - | false | - |
| pm-strahler+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.046 | 142.953 | even | - | - | false | - |
| pm-strahler+iter | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.201 | 142.785 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.046 | 142.891 | even | - | - | false | - |
| pm-succinct | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.378 | 142.957 | even | - | - | false | - |
| pm-succinct+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.027 | 143.031 | even | - | - | false | - |
| pm-succinct+iter | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.215 | 142.902 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.039 | 142.906 | even | - | - | false | - |
| zielonka | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.944 | 142.898 | even | - | - | false | - |
| zielonka+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.912 | 142.957 | even | - | - | false | - |
| zielonka-sym | complete | 540737 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.056 | 142.953 | even | - | - | false | - |
| zielonka-sym+pre | complete | 540737 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.900 | 143.086 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hesselinkdatasize=2_property1.gm · 1081474 vertices / 2231426 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1081474 | 2231426 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 331.031 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.642 | 281.625 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 331.293 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.505 | 281.695 | odd | - | - | false | - |
| lifting-adaptive | complete | 238528 / 842946 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.559 | 281.633 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.724 | 281.625 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 238528 / 842946 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.944 | 281.629 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.752 | 281.754 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 331.422 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.702 | 281.754 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 331.547 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.609 | 281.738 | odd | - | - | false | - |
| pm-strahler | complete | 238528 / 842946 | 2 / 53 | 1 / 26 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.142 | 281.699 | odd | - | - | false | - |
| pm-strahler+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.959 | 281.699 | odd | - | - | false | - |
| pm-strahler+iter | complete | 238528 / 842946 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.526 | 281.430 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.939 | 281.617 | odd | - | - | false | - |
| pm-succinct | complete | 238528 / 842946 | 2 / 53 | 1 / 26 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 11.515 | 281.621 | odd | - | - | false | - |
| pm-succinct+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.970 | 281.578 | odd | - | - | false | - |
| pm-succinct+iter | complete | 238528 / 842946 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.696 | 281.566 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.926 | 281.500 | odd | - | - | false | - |
| zielonka | complete | 238528 / 842946 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.731 | 281.688 | odd | - | - | false | - |
| zielonka+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.515 | 281.754 | odd | - | - | false | - |
| zielonka-sym | complete | 238528 / 842946 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.340 | 281.625 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 238528 / 842946 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.510 | 281.570 | odd | - | - | false | - |

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
| pm-strahler | 1 / 27 | 1 / 26 | 1 / 26 | 1.000 / 1.926 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 27 | 1 / 26 | 1 / 26 | 1.000 / 1.926 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hesselinkdatasize=2_property2.gm · 1093761 vertices / 2246401 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1093761 | 2246401 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.124 | 284.680 | even | true | true | false | - |
| lifting+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.537 | 284.660 | even | true | true | false | - |
| lifting+iter | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.147 | 284.656 | even | true | true | false | - |
| lifting+pre+iter | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.394 | 284.449 | even | true | true | false | - |
| lifting-adaptive | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.060 | 284.719 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.448 | 284.699 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.092 | 284.656 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.428 | 284.699 | even | true | true | false | - |
| lifting-sym | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 1.969 | 284.723 | even | true | true | false | - |
| lifting-sym+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.472 | 284.656 | even | true | true | false | - |
| lifting-sym+iter | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.070 | 284.691 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.419 | 284.594 | even | true | true | false | - |
| pm-strahler | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.230 | 284.391 | even | true | true | false | - |
| pm-strahler+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.704 | 284.539 | even | true | true | false | - |
| pm-strahler+iter | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.093 | 284.598 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.720 | 284.602 | even | true | true | false | - |
| pm-succinct | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.457 | 284.352 | even | true | true | false | - |
| pm-succinct+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.701 | 284.668 | even | true | true | false | - |
| pm-succinct+iter | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.067 | 284.602 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.691 | 284.395 | even | true | true | false | - |
| zielonka | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.505 | 284.648 | even | true | true | false | - |
| zielonka+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.441 | 284.594 | even | true | true | false | - |
| zielonka-sym | complete | 1093761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.749 | 284.590 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1093761 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.450 | 284.535 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_nodeadlock.gm · 188570 vertices / 328544 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 188570 | 328544 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.677 | 75.590 | even | - | - | false | - |
| lifting+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.596 | 75.590 | even | - | - | false | - |
| lifting+iter | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.688 | 75.590 | even | - | - | false | - |
| lifting+pre+iter | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.574 | 75.590 | even | - | - | false | - |
| lifting-adaptive | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.644 | 75.590 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 75.590 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.662 | 75.590 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 75.590 | even | - | - | false | - |
| lifting-sym | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.640 | 75.590 | even | - | - | false | - |
| lifting-sym+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 75.590 | even | - | - | false | - |
| lifting-sym+iter | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.649 | 75.590 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 75.590 | even | - | - | false | - |
| pm-strahler | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.671 | 75.590 | even | - | - | false | - |
| pm-strahler+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.592 | 75.590 | even | - | - | false | - |
| pm-strahler+iter | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.640 | 75.590 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.588 | 75.590 | even | - | - | false | - |
| pm-succinct | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.691 | 75.590 | even | - | - | false | - |
| pm-succinct+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.588 | 75.590 | even | - | - | false | - |
| pm-succinct+iter | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.653 | 75.590 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.603 | 75.590 | even | - | - | false | - |
| zielonka | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.593 | 75.590 | even | - | - | false | - |
| zielonka+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.547 | 75.590 | even | - | - | false | - |
| zielonka-sym | complete | 188570 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.597 | 75.590 | even | - | - | false | - |
| zielonka-sym+pre | complete | 188570 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.555 | 75.590 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_property1.gm · 377113 vertices / 819008 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 377113 | 819008 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.974 | 107.801 | even | - | - | false | - |
| lifting+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.779 | 107.672 | even | - | - | false | - |
| lifting+iter | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.986 | 107.523 | even | - | - | false | - |
| lifting+pre+iter | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.744 | 107.609 | even | - | - | false | - |
| lifting-adaptive | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.953 | 107.445 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.743 | 107.730 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.962 | 107.656 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.744 | 107.527 | even | - | - | false | - |
| lifting-sym | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.919 | 107.781 | even | - | - | false | - |
| lifting-sym+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.745 | 107.797 | even | - | - | false | - |
| lifting-sym+iter | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.929 | 107.660 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.743 | 107.664 | even | - | - | false | - |
| pm-strahler | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.981 | 107.547 | even | - | - | false | - |
| pm-strahler+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.828 | 107.746 | even | - | - | false | - |
| pm-strahler+iter | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.920 | 107.680 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.848 | 107.617 | even | - | - | false | - |
| pm-succinct | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.013 | 107.746 | even | - | - | false | - |
| pm-succinct+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.819 | 107.602 | even | - | - | false | - |
| pm-succinct+iter | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.931 | 107.676 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.826 | 107.660 | even | - | - | false | - |
| zielonka | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.785 | 107.801 | even | - | - | false | - |
| zielonka+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.745 | 107.660 | even | - | - | false | - |
| zielonka-sym | complete | 377113 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.848 | 107.660 | even | - | - | false | - |
| zielonka-sym+pre | complete | 377113 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.745 | 107.730 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_property2.gm · 417016 vertices / 787653 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 417016 | 787653 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.016 | 113.770 | even | - | - | false | - |
| lifting+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.800 | 113.773 | even | - | - | false | - |
| lifting+iter | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.025 | 113.637 | even | - | - | false | - |
| lifting+pre+iter | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.765 | 113.777 | even | - | - | false | - |
| lifting-adaptive | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.002 | 113.715 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.776 | 113.711 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.012 | 113.625 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.775 | 113.645 | even | - | - | false | - |
| lifting-sym | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.951 | 113.648 | even | - | - | false | - |
| lifting-sym+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.785 | 113.703 | even | - | - | false | - |
| lifting-sym+iter | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 0.991 | 113.777 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.766 | 113.645 | even | - | - | false | - |
| pm-strahler | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.029 | 113.656 | even | - | - | false | - |
| pm-strahler+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.873 | 113.656 | even | - | - | false | - |
| pm-strahler+iter | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.986 | 113.641 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.858 | 113.723 | even | - | - | false | - |
| pm-succinct | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.076 | 113.719 | even | - | - | false | - |
| pm-succinct+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.860 | 113.578 | even | - | - | false | - |
| pm-succinct+iter | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.987 | 113.719 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.862 | 113.590 | even | - | - | false | - |
| zielonka | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.809 | 113.711 | even | - | - | false | - |
| zielonka+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.764 | 113.770 | even | - | - | false | - |
| zielonka-sym | complete | 417016 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.888 | 113.773 | even | - | - | false | - |
| zielonka-sym+pre | complete | 417016 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.775 | 113.773 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_property3.gm · 1285576 vertices / 2268975 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1285576 | 2268975 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.078 | 1177.211 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.815 | 344.789 | odd | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.119 | 1177.090 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre+iter | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.605 | 344.840 | odd | - | - | false | - |
| lifting-adaptive | complete | 395749 / 889827 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 7.753 | 344.801 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.715 | 344.859 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 395749 / 889827 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 7.884 | 344.793 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.722 | 344.859 | odd | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.006 | 1177.188 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.661 | 344.840 | odd | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.987 | 1177.047 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre+iter | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.703 | 344.859 | odd | - | - | false | - |
| pm-strahler | complete | 395749 / 889827 | 5 / 190 | 2 / 63 | 3 / 4 | k=3, t=4, depth=2 / k=3, t=4, depth=3 | 25.278 | 344.531 | odd | - | - | false | - |
| pm-strahler+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 2.023 | 344.508 | odd | - | - | false | - |
| pm-strahler+iter | complete | 395749 / 889827 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 2.313 | 344.746 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 1.910 | 344.738 | odd | - | - | false | - |
| pm-succinct | complete | 395749 / 889827 | 5 / 190 | 2 / 63 | 3 / 4 | bits=5, depth=2 / bits=5, depth=3 | 13.632 | 344.680 | odd | - | - | false | - |
| pm-succinct+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 1.920 | 344.805 | odd | - | - | false | - |
| pm-succinct+iter | complete | 395749 / 889827 | 5 / 10 | 2 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 2.425 | 344.809 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 1.873 | 344.676 | odd | - | - | false | - |
| zielonka | complete | 395749 / 889827 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 1.727 | 344.840 | odd | - | - | false | - |
| zielonka+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.558 | 344.859 | odd | - | - | false | - |
| zielonka-sym | complete | 395749 / 889827 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 2.384 | 344.723 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 395749 / 889827 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.648 | 344.645 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 3 / 127 | 2 / 63 | 2 / 63 | 1.333 / 1.488 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 3 / 127 | 2 / 63 | 2 / 63 | 1.333 / 1.488 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 7 | 2 / 3 | 2 / 3 | 1.333 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_property4.gm · 571378 vertices / 996970 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 571378 | 996970 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 171.051 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.954 | 152.832 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 170.984 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.897 | 152.898 | odd | - | - | false | - |
| lifting-adaptive | complete | 188569 / 382809 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.913 | 152.820 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.058 | 152.957 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 188569 / 382809 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.073 | 152.891 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.054 | 152.691 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 171.094 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.017 | 152.742 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 170.898 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.985 | 152.688 | odd | - | - | false | - |
| pm-strahler | complete | 188569 / 382809 | 2 / 123 | 1 / 61 | 2 / 3 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 16.013 | 152.836 | odd | - | - | false | - |
| pm-strahler+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.108 | 152.906 | odd | - | - | false | - |
| pm-strahler+iter | complete | 188569 / 382809 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.273 | 152.902 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.086 | 152.777 | odd | - | - | false | - |
| pm-succinct | complete | 188569 / 382809 | 2 / 123 | 1 / 61 | 2 / 3 | bits=5, depth=1 / bits=5, depth=2 | 8.279 | 152.902 | odd | - | - | false | - |
| pm-succinct+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.090 | 152.777 | odd | - | - | false | - |
| pm-succinct+iter | complete | 188569 / 382809 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.329 | 152.906 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.081 | 152.906 | odd | - | - | false | - |
| zielonka | complete | 188569 / 382809 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.037 | 152.938 | odd | - | - | false | - |
| zielonka+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.975 | 152.898 | odd | - | - | false | - |
| zielonka-sym | complete | 188569 / 382809 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.335 | 152.930 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 188569 / 382809 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.016 | 152.941 | odd | - | - | false | - |

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
| pm-strahler | 1 / 62 | 1 / 61 | 1 / 61 | 1.000 / 1.968 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 62 | 1 / 61 | 1 / 61 | 1.000 / 1.968 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/IEEE1394nparties=2_datasize=2_headersize=2_acksize=2_property5.gm · 1411274 vertices / 2454775 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1411274 | 2454775 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.530 | 375.137 | even | - | - | false | - |
| lifting+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.785 | 375.152 | even | - | - | false | - |
| lifting+iter | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.593 | 374.969 | even | - | - | false | - |
| lifting+pre+iter | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.626 | 375.016 | even | - | - | false | - |
| lifting-adaptive | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.446 | 375.027 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.670 | 375.152 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.486 | 375.152 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.645 | 375.023 | even | - | - | false | - |
| lifting-sym | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.323 | 375.086 | even | - | - | false | - |
| lifting-sym+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.680 | 374.965 | even | - | - | false | - |
| lifting-sym+iter | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 2.423 | 374.969 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.631 | 375.020 | even | - | - | false | - |
| pm-strahler | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.601 | 375.035 | even | - | - | false | - |
| pm-strahler+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.991 | 375.102 | even | - | - | false | - |
| pm-strahler+iter | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.429 | 374.824 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.003 | 375.027 | even | - | - | false | - |
| pm-succinct | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.755 | 374.957 | even | - | - | false | - |
| pm-succinct+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.985 | 374.973 | even | - | - | false | - |
| pm-succinct+iter | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.434 | 375.098 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.991 | 375.031 | even | - | - | false | - |
| zielonka | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.766 | 375.023 | even | - | - | false | - |
| zielonka+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.666 | 375.086 | even | - | - | false | - |
| zielonka-sym | complete | 1411274 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.076 | 375.016 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1411274 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.675 | 375.156 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Leadernparticipants=3_eventually-stable.gm · 5861 vertices / 14892 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5861 | 14892 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 75.859 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 75.859 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 75.859 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 75.859 | even | true | true | false | - |
| lifting-adaptive | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.433 | 75.859 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 75.859 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.453 | 75.859 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 75.859 | even | true | true | false | - |
| lifting-sym | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=12 / H=3, K=3, t=12 | 12.926 | 75.859 | even | true | true | false | - |
| lifting-sym+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 75.859 | even | true | true | false | - |
| lifting-sym+iter | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=12 / H=3, K=3, t=12 | 12.911 | 75.859 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 75.859 | even | true | true | false | - |
| pm-strahler | complete | 4663 / 1198 | 107 / 4 | 53 / 1 | 3 / 4 | k=3, t=5, depth=2 / k=3, t=5, depth=3 | 0.799 | 75.859 | even | true | true | false | - |
| pm-strahler+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.402 | 75.859 | even | true | true | false | - |
| pm-strahler+iter | complete | 4663 / 1198 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.414 | 75.859 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.402 | 75.859 | even | true | true | false | - |
| pm-succinct | complete | 4663 / 1198 | 107 / 4 | 53 / 1 | 3 / 4 | bits=5, depth=2 / bits=5, depth=3 | 0.525 | 75.859 | even | true | true | false | - |
| pm-succinct+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 0.405 | 75.859 | even | true | true | false | - |
| pm-succinct+iter | complete | 4663 / 1198 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.403 | 75.859 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 0.401 | 75.859 | even | true | true | false | - |
| zielonka | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.402 | 75.859 | even | true | true | false | - |
| zielonka+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 75.859 | even | true | true | false | - |
| zielonka-sym | complete | 4663 / 1198 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.393 | 75.859 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4663 / 1198 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 75.859 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 54 / 3 | 53 / 1 | 53 / 1 | 1.963 / 1.000 | 1 / 0 | 3 / 4 | 3.000 / 4.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 54 / 3 | 53 / 1 | 53 / 1 | 1.963 / 1.000 | 1 / 0 | 3 / 4 | 3.000 / 4.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Leadernparticipants=4_eventually-stable.gm · 2341446 vertices / 7935608 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2341446 | 7935608 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.171 | 1244.340 | - | - | - | - | Solver failed: failed to build the Even host U^3_{21,3} |
| lifting+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.934 | 827.812 | even | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.104 | 1244.105 | - | - | - | - | Solver failed: failed to build the Even host U^3_{21,3} |
| lifting+pre+iter | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.792 | 827.621 | even | - | - | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.030 | 827.938 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.863 | 827.867 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 827.766 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.827 | 827.918 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.197 | 1244.527 | - | - | - | - | Solver failed: failed to build the Even host U^3_{21,3} |
| lifting-sym+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.952 | 827.691 | even | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.177 | 1244.051 | - | - | - | - | Solver failed: failed to build the Even host U^3_{21,3} |
| lifting-sym+pre+iter | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.906 | 827.941 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.055 | 827.883 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 4.554 | 827.848 | even | - | - | false | - |
| pm-strahler+iter | complete | 1956907 / 384539 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 6.388 | 827.684 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 4.551 | 827.816 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 827.816 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 4.592 | 827.754 | even | - | - | false | - |
| pm-succinct+iter | complete | 1956907 / 384539 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 6.991 | 827.684 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=3 | 4.446 | 827.750 | even | - | - | false | - |
| zielonka | complete | 1956907 / 384539 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 4.187 | 827.922 | even | - | - | false | - |
| zielonka+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.739 | 827.812 | even | - | - | false | - |
| zielonka-sym | complete | 1956907 / 384539 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 5.540 | 827.703 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1956907 / 384539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.755 | 827.812 | even | - | - | false | - |

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
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_liveness_1_1.gm · 656 vertices / 1349 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 656 | 1349 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.540 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.538 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.506 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.508 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 656 / 0 | 15 / 0 | 14 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 656 / 0 | 15 / 0 | 14 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| zielonka | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 14 / 0 | 14 / 0 | 14.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 14 / 0 | 14 / 0 | 14.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_liveness_1_2.gm · 656 vertices / 1349 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 656 | 1349 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.537 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.547 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.505 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.505 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 656 / 0 | 15 / 0 | 14 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 656 / 0 | 15 / 0 | 14 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| zielonka | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 656 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 656 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 14 / 0 | 14 / 0 | 14.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 14 / 0 | 14 / 0 | 14.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_liveness_2_1.gm · 649 vertices / 1134 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 649 | 1134 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.538 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.538 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.484 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.487 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 649 / 0 | 23 / 0 | 22 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.402 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.401 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 649 / 0 | 23 / 0 | 22 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.403 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| zielonka | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 22 / 0 | 22 / 0 | 22.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 22 / 0 | 22 / 0 | 22.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_liveness_2_2.gm · 649 vertices / 1134 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 649 | 1134 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.540 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.538 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.484 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.484 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 649 / 0 | 23 / 0 | 22 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.403 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 649 / 0 | 23 / 0 | 22 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.412 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| zielonka | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 649 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 649 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 22 / 0 | 22 / 0 | 22.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 22 / 0 | 22 / 0 | 22.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_nodeadlock.gm · 328 vertices / 549 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 328 | 549 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.393 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.393 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.393 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.394 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.394 | 76.336 | even | true | true | false | - |
| zielonka | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 328 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 328 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_safety_1.gm · 308 vertices / 511 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 308 | 511 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.408 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.408 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.410 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.410 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 76.336 | even | true | true | false | - |
| zielonka | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 308 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 308 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_safety_2_1.gm · 227 vertices / 360 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 227 | 360 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.405 | 76.336 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 76.336 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 76.336 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.429 | 76.336 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.400 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.396 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 76.336 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 227 | 0 / 49 | 0 / 24 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 227 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 76.336 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 227 | 0 / 49 | 0 / 24 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 227 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | odd | false | true | false | - |

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
| pm-strahler | 0 / 25 | 0 / 24 | 0 / 24 | 0.000 / 1.920 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 25 | 0 / 24 | 0 / 24 | 0.000 / 1.920 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=2_safety_2_2.gm · 227 vertices / 360 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 227 | 360 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 76.336 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 76.336 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 76.336 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 76.336 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.396 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 76.336 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 227 | 0 / 49 | 0 / 24 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 76.336 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 227 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 227 | 0 / 49 | 0 / 24 | 0 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.395 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 76.336 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 227 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 76.336 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 76.336 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 227 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 227 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | odd | false | true | false | - |

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
| pm-strahler | 0 / 25 | 0 / 24 | 0 / 24 | 0.000 / 1.920 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 25 | 0 / 24 | 0 / 24 | 0.000 / 1.920 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_liveness_1_1.gm · 8626 vertices / 21275 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8626 | 21275 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 76.336 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 76.336 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 76.336 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.410 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 23.018 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 22.989 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 8626 / 0 | 22 / 0 | 21 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.544 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 8626 / 0 | 22 / 0 | 21 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.452 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| zielonka | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.400 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 21 / 0 | 21 / 0 | 21.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 21 / 0 | 21 / 0 | 21.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_liveness_1_2.gm · 8626 vertices / 21275 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8626 | 21275 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 76.336 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 76.336 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.410 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 23.050 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 22.992 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 8626 / 0 | 22 / 0 | 21 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.581 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.396 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 8626 / 0 | 22 / 0 | 21 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.452 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.390 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| zielonka | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.400 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 8626 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8626 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 21 / 0 | 21 / 0 | 21.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 21 / 0 | 21 / 0 | 21.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

