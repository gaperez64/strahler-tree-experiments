# modelchecking, part 4

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

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

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_liveness_2_1.gm · 6359 vertices / 13357 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6359 | 13357 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 13.862 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 13.818 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.389 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.306 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.273 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 6359 / 0 | 42 / 0 | 41 / 0 | 2 / 0 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.484 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 6359 / 0 | 42 / 0 | 41 / 0 | 2 / 0 | bits=5, depth=1 / bits=5, depth=2 | 0.443 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.390 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| zielonka | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 76.336 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 41 / 0 | 41 / 0 | 41.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 41 / 0 | 41 / 0 | 41.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_liveness_2_2.gm · 6359 vertices / 13357 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6359 | 13357 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 13.760 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 13.813 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.288 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 7.256 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 6359 / 0 | 42 / 0 | 41 / 0 | 2 / 0 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.473 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 6359 / 0 | 42 / 0 | 41 / 0 | 2 / 0 | bits=5, depth=1 / bits=5, depth=2 | 0.433 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 76.336 | even | true | true | false | - |
| zielonka | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 6359 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6359 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 76.336 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 41 / 0 | 41 / 0 | 41.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 41 / 0 | 41 / 0 | 41.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_nodeadlock.gm · 4313 vertices / 9919 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4313 | 9919 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.417 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.417 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.427 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.426 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.427 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.429 | 76.336 | even | true | true | false | - |
| zielonka | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.429 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 4313 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4313 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 76.336 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Correct)nlifts=3_safety_1.gm · 4021 vertices / 9267 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4021 | 9267 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.418 | 76.336 | even | true | true | false | - |
| lifting+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 76.336 | even | true | true | false | - |
| lifting+iter | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.418 | 76.336 | even | true | true | false | - |
| lifting+pre+iter | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 76.336 | even | true | true | false | - |
| lifting-adaptive | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 76.336 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 76.336 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 76.336 | even | true | true | false | - |
| lifting-sym | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 76.336 | even | true | true | false | - |
| lifting-sym+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 76.336 | even | true | true | false | - |
| lifting-sym+iter | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 76.336 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 76.336 | even | true | true | false | - |
| pm-strahler+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+iter | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-succinct | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| pm-succinct+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.415 | 76.336 | even | true | true | false | - |
| pm-succinct+iter | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.415 | 76.336 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 76.336 | even | true | true | false | - |
| zielonka | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 76.336 | even | true | true | false | - |
| zielonka+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 76.336 | even | true | true | false | - |
| zielonka-sym | complete | 4021 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 76.336 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4021 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Correct)nlifts=3_safety_2_1.gm · 2126 vertices / 4462 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2126 | 4462 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.083 | 76.336 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.082 | 76.336 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 76.336 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 76.336 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2126 | 0 / 87 | 0 / 43 | 0 / 3 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.422 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 76.336 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2126 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2126 | 0 / 87 | 0 / 43 | 0 / 3 | bits=5, depth=1 / bits=5, depth=2 | 0.411 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 76.336 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2126 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 76.336 | odd | false | true | false | - |
| zielonka | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 76.336 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 76.336 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 76.336 | odd | false | true | false | - |

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
| pm-strahler | 0 / 44 | 0 / 43 | 0 / 43 | 0.000 / 1.955 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 44 | 0 / 43 | 0 / 43 | 0.000 / 1.955 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=3_safety_2_2.gm · 2126 vertices / 4462 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2126 | 4462 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.082 | 76.336 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 76.336 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.082 | 76.336 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 76.336 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 76.336 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 76.336 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 76.336 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 76.336 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 76.336 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2126 | 0 / 87 | 0 / 43 | 0 / 3 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.413 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 76.336 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2126 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 76.336 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 76.336 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2126 | 0 / 87 | 0 / 43 | 0 / 3 | bits=5, depth=1 / bits=5, depth=2 | 0.413 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 76.336 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2126 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 76.336 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 76.336 | odd | false | true | false | - |
| zielonka | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 76.336 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 76.336 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2126 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 76.336 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2126 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 76.336 | odd | false | true | false | - |

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
| pm-strahler | 0 / 44 | 0 / 43 | 0 / 43 | 0.000 / 1.955 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 44 | 0 / 43 | 0 / 43 | 0.000 / 1.955 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_liveness_1_1.gm · 107276 vertices / 298842 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 107276 | 298842 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 77.520 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.515 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.985 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.601 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.051 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.602 | 77.520 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.559 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 107276 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 4.087 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.558 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.662 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.590 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 107276 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 2.025 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.591 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.654 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.590 | 77.520 | even | true | true | false | - |
| zielonka | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.578 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.568 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.640 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.568 | 77.520 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_liveness_1_2.gm · 107276 vertices / 298842 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 107276 | 298842 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 77.520 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.515 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.984 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.614 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.062 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.624 | 77.520 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.550 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.561 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 107276 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 4.047 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.558 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.651 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.589 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 107276 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 2.015 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.579 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.662 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.579 | 77.520 | even | true | true | false | - |
| zielonka | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.577 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.559 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 107276 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.612 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 107276 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.570 | 77.520 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_liveness_2_1.gm · 44773 vertices / 107216 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 44773 | 107216 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 77.520 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.777 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.529 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.860 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.540 | 77.520 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 44773 / 0 | 70 / 0 | 69 / 0 | 2 / 0 | k=2, t=6, depth=1 / k=3, t=6, depth=2 | 2.013 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.530 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.517 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.497 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 44773 / 0 | 70 / 0 | 69 / 0 | 2 / 0 | bits=6, depth=1 / bits=6, depth=2 | 1.275 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.496 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.527 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.498 | 77.520 | even | true | true | false | - |
| zielonka | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.486 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.507 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 77.520 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 69 / 0 | 69 / 0 | 69.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 69 / 0 | 69 / 0 | 69.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_liveness_2_2.gm · 44773 vertices / 107216 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 44773 | 107216 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 77.520 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.804 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.540 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.885 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.530 | 77.520 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 77.520 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.499 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 44773 / 0 | 70 / 0 | 69 / 0 | 2 / 0 | k=2, t=6, depth=1 / k=3, t=6, depth=2 | 2.144 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.559 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.524 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.499 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 44773 / 0 | 70 / 0 | 69 / 0 | 2 / 0 | bits=6, depth=1 / bits=6, depth=2 | 1.291 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.501 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.524 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.507 | 77.520 | even | true | true | false | - |
| zielonka | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.489 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 44773 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.528 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 44773 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 77.520 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 69 / 0 | 69 / 0 | 69.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 69 / 0 | 69 / 0 | 69.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_nodeadlock.gm · 53638 vertices / 154793 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 53638 | 154793 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.499 | 77.520 | even | true | true | false | - |
| lifting+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.458 | 77.520 | even | true | true | false | - |
| lifting+iter | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.499 | 77.520 | even | true | true | false | - |
| lifting+pre+iter | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.458 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.487 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.457 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.497 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 77.520 | even | true | true | false | - |
| lifting-sym | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.468 | 77.520 | even | true | true | false | - |
| lifting-sym+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.477 | 77.520 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.497 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.476 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.487 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.466 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.506 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.456 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.513 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.456 | 77.520 | even | true | true | false | - |
| zielonka | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.470 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 53638 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.496 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 53638 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 77.520 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Correct)nlifts=4_safety_1.gm · 51220 vertices / 148411 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 51220 | 148411 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.490 | 77.520 | even | true | true | false | - |
| lifting+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.458 | 77.520 | even | true | true | false | - |
| lifting+iter | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.489 | 77.520 | even | true | true | false | - |
| lifting+pre+iter | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.476 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.485 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 77.520 | even | true | true | false | - |
| lifting-sym | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.474 | 77.520 | even | true | true | false | - |
| lifting-sym+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.475 | 77.520 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.477 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.455 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.467 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.457 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.487 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.455 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.477 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.468 | 77.520 | even | true | true | false | - |
| zielonka | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.467 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 51220 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.470 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 51220 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.439 | 77.520 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Correct)nlifts=4_safety_2_1.gm · 18625 vertices / 47653 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 18625 | 47653 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 77.520 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.539 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.618 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.562 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.250 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.109 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 18625 | 0 / 137 | 0 / 68 | 0 / 3 | k=2, t=6, depth=1 / k=3, t=6, depth=2 | 0.856 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 18625 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.425 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 18625 | 0 / 137 | 0 / 68 | 0 / 3 | bits=6, depth=1 / bits=6, depth=2 | 0.678 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.404 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 18625 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.425 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.412 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 77.520 | odd | false | true | false | - |

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
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 69 | 0 / 68 | 0 / 68 | 0.000 / 1.971 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 69 | 0 / 68 | 0 / 68 | 0.000 / 1.971 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Correct)nlifts=4_safety_2_2.gm · 18625 vertices / 47653 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 18625 | 47653 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 77.520 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 77.520 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.482 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.594 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.523 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.686 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.540 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.186 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.276 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 18625 | 0 / 137 | 0 / 68 | 0 / 3 | k=2, t=6, depth=1 / k=3, t=6, depth=2 | 0.927 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.422 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 18625 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.593 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.671 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 18625 | 0 / 137 | 0 / 68 | 0 / 3 | bits=6, depth=1 / bits=6, depth=2 | 0.899 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.579 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 18625 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.839 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.635 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.598 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.501 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 18625 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.799 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 18625 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.788 | 77.520 | odd | false | true | false | - |

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
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 69 | 0 / 68 | 0 / 68 | 0.000 / 1.971 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 69 | 0 / 68 | 0 / 68 | 0.000 / 1.971 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_liveness_1_1.gm · 1691 vertices / 4825 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1691 | 4825 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 10.989 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.618 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 10.987 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.490 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.610 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.541 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.681 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.618 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 1.653 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.629 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 1.632 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.732 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 792 / 899 | 25 / 34 | 12 / 11 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.546 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.606 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 792 / 899 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.624 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 792 / 899 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.664 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 792 / 899 | 25 / 34 | 12 / 11 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.594 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.514 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 792 / 899 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.702 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.528 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.584 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.578 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.586 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.503 | 77.520 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 13 / 23 | 12 / 11 | 12 / 11 | 1.846 / 1.435 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 13 / 23 | 12 / 11 | 12 / 11 | 1.846 / 1.435 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_liveness_1_2.gm · 1691 vertices / 4825 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1691 | 4825 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 10.407 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.561 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 10.832 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.746 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.641 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.525 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.486 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.579 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 1.540 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.689 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=10 / H=3, K=3, t=10 | 1.741 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.694 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 792 / 899 | 25 / 34 | 12 / 11 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.726 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.497 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 792 / 899 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.699 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 792 / 899 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.747 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 792 / 899 | 25 / 34 | 12 / 11 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.520 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.609 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 792 / 899 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.547 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 792 / 899 | 3 / 7 | 1 / 2 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.559 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.578 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.733 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 792 / 899 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.650 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 792 / 899 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.488 | 77.520 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 13 / 23 | 12 / 11 | 12 / 11 | 1.846 / 1.435 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 13 / 23 | 12 / 11 | 12 / 11 | 1.846 / 1.435 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 5 | 1 / 2 | 1 / 2 | 1.000 / 1.200 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_liveness_2_1.gm · 882 vertices / 1939 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 882 | 1939 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 2.526 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.634 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 2.443 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.533 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.594 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.416 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.439 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.417 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 0.606 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.462 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 0.595 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.479 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 597 / 285 | 21 / 52 | 10 / 17 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 0.437 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.440 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 597 / 285 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.448 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 597 / 285 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.440 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 597 / 285 | 21 / 52 | 10 / 17 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 0.442 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.420 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 597 / 285 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.450 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.438 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.450 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.418 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.405 | 77.520 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 11 / 35 | 10 / 17 | 10 / 17 | 1.818 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 11 / 35 | 10 / 17 | 10 / 17 | 1.818 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_liveness_2_2.gm · 882 vertices / 1939 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 882 | 1939 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 2.079 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.434 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 2.076 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.441 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.369 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.370 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.393 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.402 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 0.556 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.434 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=3, t=9 / H=3, K=3, t=9 | 0.557 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=8 / H=3, K=3, t=8 | 0.433 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 597 / 285 | 21 / 52 | 10 / 17 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.398 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 597 / 285 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 597 / 285 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.394 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 597 / 285 | 21 / 52 | 10 / 17 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.393 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 597 / 285 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.402 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 597 / 285 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.396 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.392 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.394 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 597 / 285 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.392 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 597 / 285 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.381 | 77.520 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 11 / 35 | 10 / 17 | 10 / 17 | 1.818 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 11 / 35 | 10 / 17 | 10 / 17 | 1.818 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_nodeadlock.gm · 846 vertices / 2172 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 846 | 2172 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.572 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.570 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.416 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.439 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.450 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 198 / 648 | 2 / 31 | 1 / 15 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.415 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 198 / 648 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 198 / 648 | 2 / 31 | 1 / 15 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 198 / 648 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.393 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 198 / 648 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.383 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 198 / 648 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 77.520 | odd | false | true | false | - |

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
| pm-strahler | 1 / 16 | 1 / 15 | 1 / 15 | 1.000 / 1.875 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 16 | 1 / 15 | 1 / 15 | 1.000 / 1.875 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_safety_1.gm · 763 vertices / 1903 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 763 | 1903 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.421 | 77.520 | even | true | true | false | - |
| lifting+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 77.520 | even | true | true | false | - |
| lifting+iter | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.429 | 77.520 | even | true | true | false | - |
| lifting+pre+iter | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 77.520 | even | true | true | false | - |
| lifting-adaptive | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.438 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 77.520 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 77.520 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 77.520 | even | true | true | false | - |
| lifting-sym | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.413 | 77.520 | even | true | true | false | - |
| lifting-sym+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 77.520 | even | true | true | false | - |
| lifting-sym+iter | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.403 | 77.520 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 77.520 | even | true | true | false | - |
| pm-strahler | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 77.520 | even | true | true | false | - |
| pm-strahler+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.393 | 77.520 | even | true | true | false | - |
| pm-strahler+iter | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 77.520 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.401 | 77.520 | even | true | true | false | - |
| pm-succinct | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 77.520 | even | true | true | false | - |
| pm-succinct+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 77.520 | even | true | true | false | - |
| pm-succinct+iter | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 77.520 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.392 | 77.520 | even | true | true | false | - |
| zielonka | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 77.520 | even | true | true | false | - |
| zielonka+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 77.520 | even | true | true | false | - |
| zielonka-sym | complete | 763 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 77.520 | even | true | true | false | - |
| zielonka-sym+pre | complete | 763 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 77.520 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_safety_2_1.gm · 486 vertices / 1126 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 486 | 1126 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.457 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.456 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.408 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 202 / 284 | 2 / 45 | 1 / 22 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.397 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 202 / 284 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 202 / 284 | 2 / 45 | 1 / 22 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 202 / 284 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.404 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.401 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 77.520 | odd | false | true | false | - |

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
| pm-strahler | 1 / 23 | 1 / 22 | 1 / 22 | 1.000 / 1.913 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 23 | 1 / 22 | 1 / 22 | 1.000 / 1.913 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=2_safety_2_2.gm · 486 vertices / 1126 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 486 | 1126 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.462 | 77.520 | odd | false | true | false | - |
| lifting+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 77.520 | odd | false | true | false | - |
| lifting+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.462 | 77.520 | odd | false | true | false | - |
| lifting+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.420 | 77.520 | odd | false | true | false | - |
| lifting-adaptive | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.408 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.427 | 77.520 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 77.520 | odd | false | true | false | - |
| lifting-sym | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.440 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.439 | 77.520 | odd | false | true | false | - |
| lifting-sym+iter | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.472 | 77.520 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.428 | 77.520 | odd | false | true | false | - |
| pm-strahler | complete | 202 / 284 | 2 / 45 | 1 / 22 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.444 | 77.520 | odd | false | true | false | - |
| pm-strahler+iter | complete | 202 / 284 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.450 | 77.520 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.439 | 77.520 | odd | false | true | false | - |
| pm-succinct | complete | 202 / 284 | 2 / 45 | 1 / 22 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.417 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.450 | 77.520 | odd | false | true | false | - |
| pm-succinct+iter | complete | 202 / 284 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.441 | 77.520 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.439 | 77.520 | odd | false | true | false | - |
| zielonka | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.429 | 77.520 | odd | false | true | false | - |
| zielonka+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.441 | 77.520 | odd | false | true | false | - |
| zielonka-sym | complete | 202 / 284 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.461 | 77.520 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 202 / 284 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 77.520 | odd | false | true | false | - |

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
| pm-strahler | 1 / 23 | 1 / 22 | 1 / 22 | 1.000 / 1.913 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 23 | 1 / 22 | 1 / 22 | 1.000 / 1.913 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_liveness_1_1.gm · 63907 vertices / 240612 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 63907 | 240612 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 172.473 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 85.055 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 172.199 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 85.062 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.743 | 79.094 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.516 | 79.094 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.777 | 79.094 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.541 | 79.094 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 172.961 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 85.113 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 175.465 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 92.527 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 39736 / 24171 | 31 / 40 | 15 / 13 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.949 | 79.094 | odd | false | true | false | - |
| pm-strahler+pre | complete | 39736 / 24171 | 3 / 31 | 1 / 10 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.633 | 79.094 | odd | false | true | false | - |
| pm-strahler+iter | complete | 39736 / 24171 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.582 | 79.094 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 39736 / 24171 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.658 | 79.094 | odd | false | true | false | - |
| pm-succinct | complete | 39736 / 24171 | 31 / 40 | 15 / 13 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 1.364 | 79.094 | odd | false | true | false | - |
| pm-succinct+pre | complete | 39736 / 24171 | 3 / 31 | 1 / 10 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.760 | 79.094 | odd | false | true | false | - |
| pm-succinct+iter | complete | 39736 / 24171 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.697 | 79.094 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 39736 / 24171 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.644 | 79.094 | odd | false | true | false | - |
| zielonka | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.668 | 79.094 | odd | false | true | false | - |
| zielonka+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.670 | 79.094 | odd | false | true | false | - |
| zielonka-sym | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.760 | 79.094 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.691 | 79.094 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 16 / 27 | 15 / 13 | 15 / 13 | 1.875 / 1.444 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 21 | 1 / 10 | 1 / 10 | 1.000 / 1.429 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 16 / 27 | 15 / 13 | 15 / 13 | 1.875 / 1.444 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 21 | 1 / 10 | 1 / 10 | 1.000 / 1.429 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_liveness_1_2.gm · 63907 vertices / 240612 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 63907 | 240612 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 173.102 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 84.992 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 173.094 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 85.133 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.741 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.550 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.749 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.506 | 79.188 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 173.539 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 86.148 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 175.891 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 92.445 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 39736 / 24171 | 31 / 40 | 15 / 13 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.948 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 39736 / 24171 | 3 / 31 | 1 / 10 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.627 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 39736 / 24171 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.578 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 39736 / 24171 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.580 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 39736 / 24171 | 31 / 40 | 15 / 13 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 1.211 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 39736 / 24171 | 3 / 31 | 1 / 10 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.758 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 39736 / 24171 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.707 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 39736 / 24171 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.635 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.666 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.667 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 39736 / 24171 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.737 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 39736 / 24171 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.686 | 79.188 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 16 / 27 | 15 / 13 | 15 / 13 | 1.875 / 1.444 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 21 | 1 / 10 | 1 / 10 | 1.000 / 1.429 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 16 / 27 | 15 / 13 | 15 / 13 | 1.875 / 1.444 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 21 | 1 / 10 | 1 / 10 | 1.000 / 1.429 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_liveness_2_1.gm · 13222 vertices / 32797 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13222 | 32797 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 17.655 | 79.188 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 15.145 | 79.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.455 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.403 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.452 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.411 | 79.188 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 81.188 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 9.800 | 79.188 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 83.301 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 10.203 | 79.188 | odd | false | true | false | - |
| pm-strahler | complete | 8059 / 5163 | 41 / 52 | 20 / 17 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 0.567 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 8059 / 5163 | 3 / 28 | 1 / 9 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.443 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 8059 / 5163 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.423 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 8059 / 5163 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.434 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 8059 / 5163 | 41 / 52 | 20 / 17 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 0.558 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 8059 / 5163 | 3 / 28 | 1 / 9 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.496 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 8059 / 5163 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.507 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 8059 / 5163 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.529 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.540 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.540 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.521 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.519 | 79.188 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 21 / 35 | 20 / 17 | 20 / 17 | 1.905 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 19 | 1 / 9 | 1 / 9 | 1.000 / 1.421 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 21 / 35 | 20 / 17 | 20 / 17 | 1.905 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 19 | 1 / 9 | 1 / 9 | 1.000 / 1.421 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_liveness_2_2.gm · 13222 vertices / 32797 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13222 | 32797 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 17.636 | 79.188 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 14.934 | 79.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.454 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.403 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.450 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.412 | 79.188 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 80.812 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 9.613 | 79.188 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 83.250 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=3, t=12 / H=3, K=3, t=12 | 10.252 | 79.188 | odd | false | true | false | - |
| pm-strahler | complete | 8059 / 5163 | 41 / 52 | 20 / 17 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 0.557 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 8059 / 5163 | 3 / 28 | 1 / 9 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 0.433 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 8059 / 5163 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.433 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 8059 / 5163 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.422 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 8059 / 5163 | 41 / 52 | 20 / 17 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 0.546 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 8059 / 5163 | 3 / 28 | 1 / 9 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 0.496 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 8059 / 5163 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.509 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 8059 / 5163 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.530 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.530 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.551 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 8059 / 5163 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.529 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 8059 / 5163 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.510 | 79.188 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| pm-strahler | 21 / 35 | 20 / 17 | 20 / 17 | 1.905 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 19 | 1 / 9 | 1 / 9 | 1.000 / 1.421 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 21 / 35 | 20 / 17 | 20 / 17 | 1.905 / 1.457 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 19 | 1 / 9 | 1 / 9 | 1.000 / 1.421 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_nodeadlock.gm · 31954 vertices / 121625 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 31954 | 121625 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 79.188 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 79.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 11214 / 20740 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.548 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 11214 / 20740 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.611 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.530 | 79.188 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 79.188 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 79.188 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 79.188 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 79.188 | odd | false | true | false | - |
| pm-strahler | complete | 11214 / 20740 | 2 / 35 | 1 / 17 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.277 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.502 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 11214 / 20740 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.464 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.487 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 11214 / 20740 | 2 / 35 | 1 / 17 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.031 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.444 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 11214 / 20740 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.497 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.466 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 11214 / 20740 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.476 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 11214 / 20740 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.496 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 11214 / 20740 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 79.188 | odd | false | true | false | - |

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
| pm-strahler | 1 / 18 | 1 / 17 | 1 / 17 | 1.000 / 1.889 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 18 | 1 / 17 | 1 / 17 | 1.000 / 1.889 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_safety_1.gm · 26996 vertices / 99348 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 26996 | 99348 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.451 | 79.188 | even | true | true | false | - |
| lifting+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 79.188 | even | true | true | false | - |
| lifting+iter | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.450 | 79.188 | even | true | true | false | - |
| lifting+pre+iter | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 79.188 | even | true | true | false | - |
| lifting-adaptive | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.444 | 79.188 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 79.188 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.443 | 79.188 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 79.188 | even | true | true | false | - |
| lifting-sym | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.434 | 79.188 | even | true | true | false | - |
| lifting-sym+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 79.188 | even | true | true | false | - |
| lifting-sym+iter | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.443 | 79.188 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 79.188 | even | true | true | false | - |
| pm-strahler | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.445 | 79.188 | even | true | true | false | - |
| pm-strahler+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.432 | 79.188 | even | true | true | false | - |
| pm-strahler+iter | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.443 | 79.188 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.434 | 79.188 | even | true | true | false | - |
| pm-succinct | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.464 | 79.188 | even | true | true | false | - |
| pm-succinct+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.435 | 79.188 | even | true | true | false | - |
| pm-succinct+iter | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.444 | 79.188 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.435 | 79.188 | even | true | true | false | - |
| zielonka | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 79.188 | even | true | true | false | - |
| zielonka+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 79.188 | even | true | true | false | - |
| zielonka-sym | complete | 26996 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.435 | 79.188 | even | true | true | false | - |
| zielonka-sym+pre | complete | 26996 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 79.188 | even | true | true | false | - |

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
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_safety_2_1.gm · 11977 vertices / 39577 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11977 | 39577 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 79.188 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 79.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.431 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.432 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 79.188 | odd | false | true | false | - |
| lifting-sym | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 10.364 | 79.188 | odd | false | true | false | - |
| lifting-sym+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 79.188 | odd | false | true | false | - |
| lifting-sym+iter | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 10.377 | 79.188 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 79.188 | odd | false | true | false | - |
| pm-strahler | complete | 6475 / 5502 | 2 / 75 | 1 / 37 | 2 / 3 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 1.272 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.412 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 6475 / 5502 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.412 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 6475 / 5502 | 2 / 75 | 1 / 37 | 2 / 3 | bits=5, depth=1 / bits=5, depth=2 | 0.834 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.411 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 6475 / 5502 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.421 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.401 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 79.188 | odd | false | true | false | - |

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
| pm-strahler | 1 / 38 | 1 / 37 | 1 / 37 | 1.000 / 1.947 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 38 | 1 / 37 | 1 / 37 | 1.000 / 1.947 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=3_safety_2_2.gm · 11977 vertices / 39577 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11977 | 39577 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 79.188 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 79.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 79.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.486 | 79.188 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 79.188 | odd | false | true | false | - |
| lifting-sym | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 10.356 | 79.188 | odd | false | true | false | - |
| lifting-sym+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 79.188 | odd | false | true | false | - |
| lifting-sym+iter | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 10.383 | 79.188 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 79.188 | odd | false | true | false | - |
| pm-strahler | complete | 6475 / 5502 | 2 / 75 | 1 / 37 | 2 / 3 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 1.262 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 79.188 | odd | false | true | false | - |
| pm-strahler+iter | complete | 6475 / 5502 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 79.188 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.400 | 79.188 | odd | false | true | false | - |
| pm-succinct | complete | 6475 / 5502 | 2 / 75 | 1 / 37 | 2 / 3 | bits=5, depth=1 / bits=5, depth=2 | 0.822 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.413 | 79.188 | odd | false | true | false | - |
| pm-succinct+iter | complete | 6475 / 5502 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.411 | 79.188 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.414 | 79.188 | odd | false | true | false | - |
| zielonka | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 79.188 | odd | false | true | false | - |
| zielonka+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 79.188 | odd | false | true | false | - |
| zielonka-sym | complete | 6475 / 5502 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.402 | 79.188 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 6475 / 5502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 79.188 | odd | false | true | false | - |

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
| pm-strahler | 1 / 38 | 1 / 37 | 1 / 37 | 1.000 / 1.947 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 38 | 1 / 37 | 1 / 37 | 1.000 / 1.947 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_liveness_1_1.gm · 1997579 vertices / 9752561 edges · 14 complete · 6 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1997579 | 9752561 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.658 | 1443.281 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.166 | 1637.035 | - | - | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.698 | 1443.031 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.137 | 1638.082 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 19.118 | 894.012 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 6.395 | 893.980 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 17.608 | 894.012 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 5.757 | 894.031 | odd | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.205 | 1443.406 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.139 | 1637.656 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.070 | 1443.270 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.141 | 1639.285 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.053 | 893.984 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1324996 / 672583 | 3 / 40 | 1 / 13 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 12.248 | 893.926 | odd | - | - | false | - |
| pm-strahler+iter | complete | 1324996 / 672583 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 6.665 | 893.984 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 1324996 / 672583 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 5.213 | 893.914 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 894.027 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1324996 / 672583 | 3 / 40 | 1 / 13 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 11.314 | 893.980 | odd | - | - | false | - |
| pm-succinct+iter | complete | 1324996 / 672583 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 8.680 | 893.922 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 1324996 / 672583 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 4.892 | 893.969 | odd | - | - | false | - |
| zielonka | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 4.719 | 894.105 | odd | - | - | false | - |
| zielonka+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 4.217 | 894.102 | odd | - | - | false | - |
| zielonka-sym | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 6.565 | 894.102 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 4.572 | 894.074 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 2 / 27 | 1 / 13 | 1 / 13 | 1.000 / 1.444 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 2 / 27 | 1 / 13 | 1 / 13 | 1.000 / 1.444 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_liveness_1_2.gm · 1997579 vertices / 9752561 edges · 14 complete · 6 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1997579 | 9752561 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.585 | 1443.086 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.164 | 1637.211 | - | - | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.647 | 1443.160 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.161 | 1638.156 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 18.017 | 894.086 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 6.747 | 894.105 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 17.589 | 894.043 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 5.917 | 893.980 | odd | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.263 | 1443.336 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.144 | 1637.523 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.081 | 1443.332 | - | - | - | - | Solver failed: failed to build the Even host U^3_{20,3} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.131 | 1639.168 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.054 | 893.875 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1324996 / 672583 | 3 / 40 | 1 / 13 | 3 / 4 | k=2, t=2, depth=2 / k=2, t=2, depth=3 | 12.372 | 893.914 | odd | - | - | false | - |
| pm-strahler+iter | complete | 1324996 / 672583 | 3 / 0 | 1 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 6.779 | 893.980 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 1324996 / 672583 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 5.255 | 893.852 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.054 | 893.980 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1324996 / 672583 | 3 / 40 | 1 / 13 | 3 / 4 | bits=3, depth=2 / bits=3, depth=3 | 11.417 | 894.051 | odd | - | - | false | - |
| pm-succinct+iter | complete | 1324996 / 672583 | 3 / 0 | 1 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 8.650 | 893.965 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 1324996 / 672583 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 4.863 | 893.969 | odd | - | - | false | - |
| zielonka | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 4.789 | 894.102 | odd | - | - | false | - |
| zielonka+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 4.204 | 894.086 | odd | - | - | false | - |
| zielonka-sym | complete | 1324996 / 672583 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 6.614 | 893.965 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 1324996 / 672583 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 4.620 | 894.031 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 2 / 27 | 1 / 13 | 1 / 13 | 1.000 / 1.444 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 2 / 27 | 1 / 13 | 1 / 13 | 1.000 / 1.444 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_liveness_2_1.gm · 134162 vertices / 372852 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 134162 | 372852 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.067 | 680.355 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 177.918 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.067 | 680.367 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 177.914 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 1.247 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.672 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 1.258 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.673 | 80.391 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 681.000 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 178.555 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.061 | 681.480 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 179.742 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 75580 / 58582 | 69 / 64 | 34 / 21 | 3 / 4 | k=3, t=5, depth=2 / k=3, t=5, depth=3 | 10.401 | 80.391 | odd | - | - | false | - |
| pm-strahler+pre | complete | 75580 / 58582 | 3 / 55 | 1 / 18 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 1.897 | 80.391 | odd | - | - | false | - |
| pm-strahler+iter | complete | 75580 / 58582 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.844 | 80.391 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 75580 / 58582 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.857 | 80.391 | odd | - | - | false | - |
| pm-succinct | complete | 75580 / 58582 | 69 / 64 | 34 / 21 | 3 / 4 | bits=5, depth=2 / bits=5, depth=3 | 4.001 | 80.391 | odd | - | - | false | - |
| pm-succinct+pre | complete | 75580 / 58582 | 3 / 55 | 1 / 18 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 1.567 | 80.391 | odd | - | - | false | - |
| pm-succinct+iter | complete | 75580 / 58582 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.852 | 80.391 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 75580 / 58582 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.794 | 80.391 | odd | - | - | false | - |
| zielonka | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.731 | 80.391 | odd | - | - | false | - |
| zielonka+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.747 | 80.391 | odd | - | - | false | - |
| zielonka-sym | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.827 | 80.391 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.770 | 80.391 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 35 / 43 | 34 / 21 | 34 / 21 | 1.943 / 1.465 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 37 | 1 / 18 | 1 / 18 | 1.000 / 1.459 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 35 / 43 | 34 / 21 | 34 / 21 | 1.943 / 1.465 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 37 | 1 / 18 | 1 / 18 | 1.000 / 1.459 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_liveness_2_2.gm · 134162 vertices / 372852 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 134162 | 372852 | 4 | 4 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 680.625 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 178.426 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 680.754 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 178.051 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 1.262 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.673 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | H=3, K=1, t=0 / H=3, K=1, t=0 | 1.299 | 80.391 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.682 | 80.391 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.060 | 680.684 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 178.488 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 681.629 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 180.238 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 75580 / 58582 | 69 / 64 | 34 / 21 | 3 / 4 | k=3, t=5, depth=2 / k=3, t=5, depth=3 | 10.409 | 80.391 | odd | - | - | false | - |
| pm-strahler+pre | complete | 75580 / 58582 | 3 / 55 | 1 / 18 | 3 / 4 | k=2, t=3, depth=2 / k=2, t=3, depth=3 | 1.930 | 80.391 | odd | - | - | false | - |
| pm-strahler+iter | complete | 75580 / 58582 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.872 | 80.391 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 75580 / 58582 | 3 / 4 | 1 / 1 | 3 / 4 | k=1, t=1, depth=2 / k=1, t=1, depth=3 | 0.862 | 80.391 | odd | - | - | false | - |
| pm-succinct | complete | 75580 / 58582 | 69 / 64 | 34 / 21 | 3 / 4 | bits=5, depth=2 / bits=5, depth=3 | 4.027 | 80.391 | odd | - | - | false | - |
| pm-succinct+pre | complete | 75580 / 58582 | 3 / 55 | 1 / 18 | 3 / 4 | bits=4, depth=2 / bits=4, depth=3 | 1.585 | 80.391 | odd | - | - | false | - |
| pm-succinct+iter | complete | 75580 / 58582 | 7 / 10 | 3 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.867 | 80.391 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 75580 / 58582 | 3 / 10 | 1 / 3 | 3 / 4 | bits=1, depth=2 / bits=1, depth=3 | 0.801 | 80.391 | odd | - | - | false | - |
| zielonka | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.730 | 80.391 | odd | - | - | false | - |
| zielonka+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.729 | 80.391 | odd | - | - | false | - |
| zielonka-sym | complete | 75580 / 58582 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.822 | 80.391 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 75580 / 58582 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.759 | 80.391 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 35 / 43 | 34 / 21 | 34 / 21 | 1.943 / 1.465 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-strahler+pre | 2 / 37 | 1 / 18 | 1 / 18 | 1.000 / 1.459 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-strahler+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-strahler+pre+iter | 2 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 4 | 3.000 / 4.000 | 1 / 1 |
| pm-succinct | 35 / 43 | 34 / 21 | 34 / 21 | 1.943 / 1.465 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre | 2 / 37 | 1 / 18 | 1 / 18 | 1.000 / 1.459 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| pm-succinct+iter | 4 / 7 | 3 / 3 | 3 / 3 | 1.500 / 1.286 | 1 / 1 | 3 / 4 | 3.000 / 4.000 | 2 / 2 |
| pm-succinct+pre+iter | 2 / 7 | 1 / 3 | 1 / 3 | 1.000 / 1.286 | 0 / 1 | 3 / 4 | 3.000 / 4.000 | 1 / 2 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_nodeadlock.gm · 998790 vertices / 5412890 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 998790 | 5412890 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 476.027 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.458 | 475.922 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.035 | 475.914 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.533 | 475.777 | odd | - | - | false | - |
| lifting-adaptive | complete | 356230 / 642560 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 6.752 | 476.047 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.676 | 476.102 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 356230 / 642560 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 7.077 | 475.918 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.741 | 475.801 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 475.918 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.494 | 476.027 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 475.910 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.534 | 475.922 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.035 | 476.020 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.730 | 475.789 | odd | - | - | false | - |
| pm-strahler+iter | complete | 356230 / 642560 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.330 | 475.855 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.585 | 475.871 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.045 | 475.855 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.683 | 475.797 | odd | - | - | false | - |
| pm-succinct+iter | complete | 356230 / 642560 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 3.884 | 475.910 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.677 | 475.906 | odd | - | - | false | - |
| zielonka | complete | 356230 / 642560 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.480 | 475.926 | odd | - | - | false | - |
| zielonka+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.263 | 475.988 | odd | - | - | false | - |
| zielonka-sym | complete | 356230 / 642560 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 3.358 | 475.859 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 356230 / 642560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.357 | 475.988 | odd | - | - | false | - |

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
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_safety_1.gm · 788879 vertices / 4146139 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 788879 | 4146139 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 2.361 | 369.301 | even | - | - | false | - |
| lifting+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.839 | 369.305 | even | - | - | false | - |
| lifting+iter | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 2.377 | 369.309 | even | - | - | false | - |
| lifting+pre+iter | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.728 | 369.371 | even | - | - | false | - |
| lifting-adaptive | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.290 | 369.309 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.756 | 369.293 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 2.339 | 369.434 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.729 | 369.434 | even | - | - | false | - |
| lifting-sym | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 2.203 | 369.164 | even | - | - | false | - |
| lifting-sym+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.726 | 369.367 | even | - | - | false | - |
| lifting-sym+iter | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=19 / H=1, K=1, t=19 | 2.284 | 369.375 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.727 | 369.230 | even | - | - | false | - |
| pm-strahler | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.643 | 369.379 | even | - | - | false | - |
| pm-strahler+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.001 | 369.254 | even | - | - | false | - |
| pm-strahler+iter | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.332 | 369.383 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 2.004 | 369.379 | even | - | - | false | - |
| pm-succinct | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 3.702 | 369.297 | even | - | - | false | - |
| pm-succinct+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.977 | 369.238 | even | - | - | false | - |
| pm-succinct+iter | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.406 | 369.289 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.960 | 369.258 | even | - | - | false | - |
| zielonka | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.777 | 369.438 | even | - | - | false | - |
| zielonka+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.724 | 369.434 | even | - | - | false | - |
| zielonka-sym | complete | 788879 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.022 | 369.367 | even | - | - | false | - |
| zielonka-sym+pre | complete | 788879 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.687 | 369.309 | even | - | - | false | - |

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
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_safety_2_1.gm · 267378 vertices / 1257302 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 267378 | 1257302 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 116.898 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.874 | 116.676 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 116.883 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.874 | 116.703 | odd | - | - | false | - |
| lifting-adaptive | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.865 | 116.828 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.976 | 116.641 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.959 | 116.812 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.970 | 116.695 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 116.953 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.924 | 116.828 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 116.836 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.930 | 116.812 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 116.648 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.972 | 116.633 | odd | - | - | false | - |
| pm-strahler+iter | complete | 139086 / 128292 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.106 | 116.691 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.961 | 116.695 | odd | - | - | false | - |
| pm-succinct | complete | 139086 / 128292 | 2 / 115 | 1 / 57 | 2 / 3 | bits=5, depth=1 / bits=5, depth=2 | 25.371 | 116.648 | odd | - | - | false | - |
| pm-succinct+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.864 | 116.645 | odd | - | - | false | - |
| pm-succinct+iter | complete | 139086 / 128292 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.091 | 116.695 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.930 | 116.637 | odd | - | - | false | - |
| zielonka | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.879 | 116.695 | odd | - | - | false | - |
| zielonka+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.833 | 116.688 | odd | - | - | false | - |
| zielonka-sym | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.037 | 116.812 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.823 | 116.832 | odd | - | - | false | - |

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
| pm-succinct | 1 / 58 | 1 / 57 | 1 / 57 | 1.000 / 1.966 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Lift_(Incorrect)nlifts=4_safety_2_2.gm · 267378 vertices / 1257302 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 267378 | 1257302 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 117.004 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.870 | 116.812 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 117.004 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.849 | 116.695 | odd | - | - | false | - |
| lifting-adaptive | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.850 | 116.645 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.984 | 116.559 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.963 | 116.832 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.978 | 116.703 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 116.895 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.918 | 116.828 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 116.820 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.910 | 116.699 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 116.711 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.972 | 116.773 | odd | - | - | false | - |
| pm-strahler+iter | complete | 139086 / 128292 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.096 | 116.715 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.960 | 116.691 | odd | - | - | false | - |
| pm-succinct | complete | 139086 / 128292 | 2 / 115 | 1 / 57 | 2 / 3 | bits=5, depth=1 / bits=5, depth=2 | 25.350 | 116.773 | odd | - | - | false | - |
| pm-succinct+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.864 | 116.504 | odd | - | - | false | - |
| pm-succinct+iter | complete | 139086 / 128292 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.082 | 116.574 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.897 | 116.707 | odd | - | - | false | - |
| zielonka | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.866 | 116.688 | odd | - | - | false | - |
| zielonka+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.835 | 116.809 | odd | - | - | false | - |
| zielonka-sym | complete | 139086 / 128292 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.034 | 116.691 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 139086 / 128292 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.815 | 116.641 | odd | - | - | false | - |

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
| pm-succinct | 1 / 58 | 1 / 57 | 1 / 57 | 1.000 / 1.966 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 655362 vertices / 2541187 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 655362 | 2541187 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 256.473 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 256.199 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 256.332 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 256.348 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.870 | 256.340 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.891 | 256.469 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.046 | 256.344 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.068 | 256.453 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 256.195 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 256.398 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 256.449 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 256.336 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 655362 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 17.777 | 256.414 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 655362 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 16.738 | 256.355 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 655362 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 6.460 | 256.348 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 655362 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 6.151 | 256.418 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 655362 | 0 / 21 | 0 / 14 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 5.698 | 256.141 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 655362 | 0 / 21 | 0 / 14 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 5.830 | 256.414 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 655362 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.929 | 256.141 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 655362 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.919 | 256.418 | odd | - | - | false | - |
| zielonka | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.533 | 256.469 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.542 | 256.473 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.785 | 256.449 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 655362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.795 | 256.469 | odd | - | - | false | - |

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
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 7 | 0 / 14 | 0 / 7 | 0.000 / 2.857 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 14 | 0 / 7 | 0.000 / 2.857 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=2_infinitely_often_read_write.gm · 170753 vertices / 556993 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 170753 | 556993 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 81.113 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 81.113 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.113 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 2.103 | 81.113 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 2.132 | 81.113 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 2.229 | 81.113 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 2.243 | 81.113 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 81.113 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.467 | 81.113 | even | true | true | false | - |
| pm-strahler+pre | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.579 | 81.113 | even | true | true | false | - |
| pm-strahler+iter | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.203 | 81.113 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.188 | 81.113 | even | true | true | false | - |
| pm-succinct | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.357 | 81.113 | even | true | true | false | - |
| pm-succinct+pre | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.367 | 81.113 | even | true | true | false | - |
| pm-succinct+iter | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.345 | 81.113 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 170753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.339 | 81.113 | even | true | true | false | - |
| zielonka | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.750 | 81.113 | even | true | true | false | - |
| zielonka+pre | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.716 | 81.113 | even | true | true | false | - |
| zielonka-sym | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.891 | 81.113 | even | true | true | false | - |
| zielonka-sym+pre | complete | 170753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.860 | 81.113 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=2_infinitely_often_receive_d1.gm · 88834 vertices / 475074 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 88834 | 475074 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 81.113 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.548 | 81.113 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 81.113 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.555 | 81.113 | even | true | true | false | - |
| lifting-adaptive | complete | 88834 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.778 | 81.113 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.654 | 81.113 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 88834 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.858 | 81.113 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.655 | 81.113 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.601 | 81.113 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 81.113 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 81.113 | even | true | true | false | - |
| pm-strahler | complete | 88834 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 3.692 | 81.113 | even | true | true | false | - |
| pm-strahler+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.624 | 81.113 | even | true | true | false | - |
| pm-strahler+iter | complete | 88834 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.629 | 81.113 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.631 | 81.113 | even | true | true | false | - |
| pm-succinct | complete | 88834 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.219 | 81.113 | even | true | true | false | - |
| pm-succinct+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.631 | 81.113 | even | true | true | false | - |
| pm-succinct+iter | complete | 88834 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.195 | 81.113 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.621 | 81.113 | even | true | true | false | - |
| zielonka | complete | 88834 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.610 | 81.113 | even | true | true | false | - |
| zielonka+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.599 | 81.113 | even | true | true | false | - |
| zielonka-sym | complete | 88834 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.663 | 81.113 | even | true | true | false | - |
| zielonka-sym+pre | complete | 88834 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.599 | 81.113 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=2_infinitely_often_receive_for_all_d.gm · 177668 vertices / 950149 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 177668 | 950149 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 83.473 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 83.609 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 83.602 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 83.680 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.086 | 83.551 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.097 | 83.539 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.130 | 83.680 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.120 | 83.410 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 83.617 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 83.621 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 83.617 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 83.684 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.160 | 83.629 | even | true | true | false | - |
| pm-strahler+pre | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.352 | 83.488 | even | true | true | false | - |
| pm-strahler+iter | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.297 | 83.559 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 5.253 | 83.711 | even | true | true | false | - |
| pm-succinct | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.276 | 83.559 | even | true | true | false | - |
| pm-succinct+pre | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.869 | 83.566 | even | true | true | false | - |
| pm-succinct+iter | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.665 | 83.562 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 177668 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.645 | 83.496 | even | true | true | false | - |
| zielonka | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.713 | 83.590 | even | true | true | false | - |
| zielonka+pre | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.722 | 83.492 | even | true | true | false | - |
| zielonka-sym | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.823 | 83.680 | even | true | true | false | - |
| zielonka-sym+pre | complete | 177668 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.813 | 83.406 | even | true | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=2_invariantly_infinitely_many_reachable_taus.gm · 245761 vertices / 1376833 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 245761 | 1376833 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 120.789 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 120.727 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 120.672 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 120.863 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.106 | 120.730 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.127 | 120.859 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.105 | 120.797 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.125 | 120.859 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 120.840 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 120.734 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 120.789 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 120.801 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.296 | 120.805 | even | - | - | false | - |
| pm-strahler+pre | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.507 | 120.805 | even | - | - | false | - |
| pm-strahler+iter | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.707 | 120.672 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.668 | 120.672 | even | - | - | false | - |
| pm-succinct | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.482 | 120.609 | even | - | - | false | - |
| pm-succinct+pre | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.503 | 120.531 | even | - | - | false | - |
| pm-succinct+iter | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.323 | 120.805 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 245761 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.323 | 120.805 | even | - | - | false | - |
| zielonka | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.970 | 120.859 | even | - | - | false | - |
| zielonka+pre | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.992 | 120.734 | even | - | - | false | - |
| zielonka-sym | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.073 | 120.723 | even | - | - | false | - |
| zielonka-sym+pre | complete | 245761 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.082 | 120.844 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=2_message_can_be_lost_infinitely_often.gm · 153985 vertices / 870977 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 153985 | 870977 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.496 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.676 | 81.496 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.496 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.678 | 81.496 | even | true | true | false | - |
| lifting-adaptive | complete | 153985 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.012 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.777 | 81.496 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 153985 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.088 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.778 | 81.496 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 81.496 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.716 | 81.496 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 81.496 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.714 | 81.496 | even | true | true | false | - |
| pm-strahler | complete | 153985 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 2.953 | 81.496 | even | true | true | false | - |
| pm-strahler+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.789 | 81.496 | even | true | true | false | - |
| pm-strahler+iter | complete | 153985 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.815 | 81.496 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.754 | 81.496 | even | true | true | false | - |
| pm-succinct | complete | 153985 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=1 | 2.337 | 81.496 | even | true | true | false | - |
| pm-succinct+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.754 | 81.496 | even | true | true | false | - |
| pm-succinct+iter | complete | 153985 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.930 | 81.496 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.764 | 81.496 | even | true | true | false | - |
| zielonka | complete | 153985 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.764 | 81.496 | even | true | true | false | - |
| zielonka+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.725 | 81.496 | even | true | true | false | - |
| zielonka-sym | complete | 153985 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.853 | 81.496 | even | true | true | false | - |
| zielonka-sym+pre | complete | 153985 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.730 | 81.496 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

