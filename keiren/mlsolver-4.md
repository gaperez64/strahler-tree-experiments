# mlsolver, part 4

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>mlsolver/games/Petrin=4.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.127 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 497:1: unexpected keyword |

</details>

<details>
<summary>mlsolver/games/Petrin=4_compact.gm · 71 vertices / 95 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 71 | 95 | 5 | 1280 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.476 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.476 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 71 / 0 | 44 / 0 | 20 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 71 / 0 | 21 / 0 | 20 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 71 / 0 | 36 / 0 | 15 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 71 / 0 | 16 / 0 | 15 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 71 / 0 | 35 / 0 | 20 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 71 / 0 | 21 / 0 | 20 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 71 / 0 | 35 / 0 | 20 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 71 / 0 | 16 / 0 | 15 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 71 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 71 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 24 / 0 | 20 / 0 | 8 / 0 | 1.792 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 20 / 0 | 20 / 0 | 20.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 21 / 0 | 15 / 0 | 7 / 0 | 1.667 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 15 / 0 | 15 / 0 | 15.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 15 / 0 | 20 / 0 | 7 / 0 | 2.267 / 0.000 | 6 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 20 / 0 | 20 / 0 | 20.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 15 / 0 | 20 / 0 | 7 / 0 | 2.267 / 0.000 | 6 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 15 / 0 | 15 / 0 | 15.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=5.gm · 692 vertices / 773 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 692 | 773 | 6 | 1611 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 22.005 | 80.078 | even | true | true | false | - |
| lifting+pre | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 4.442 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 23.034 | 80.215 | even | true | true | false | - |
| lifting+pre+iter | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 4.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 1.867 | 85.172 | even | true | true | false | - |
| lifting-sym+pre | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.410 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 1.869 | 85.305 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 692 / 0 | 555 / 0 | 314 / 0 | 5 / 0 | k=4, t=3, depth=4 / k=4, t=3, depth=4 | 0.382 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 692 / 0 | 550 / 0 | 545 / 0 | 3 / 0 | k=3, t=8, depth=2 / k=3, t=8, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 692 / 0 | 415 / 0 | 237 / 0 | 5 / 0 | k=4, t=3, depth=4 / k=4, t=3, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 692 / 0 | 240 / 0 | 237 / 0 | 3 / 0 | k=2, t=8, depth=2 / k=2, t=8, depth=2 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 692 / 0 | 470 / 0 | 305 / 0 | 5 / 0 | bits=4, depth=4 / bits=4, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 692 / 0 | 306 / 0 | 294 / 0 | 3 / 0 | bits=7, depth=2 / bits=7, depth=2 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 692 / 0 | 336 / 0 | 237 / 0 | 5 / 0 | bits=4, depth=4 / bits=4, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 692 / 0 | 240 / 0 | 237 / 0 | 3 / 0 | bits=7, depth=2 / bits=7, depth=2 | 0.371 | 58.574 | even | true | true | false | - |
| zielonka | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 692 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 692 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 241 / 0 | 314 / 0 | 31 / 0 | 2.299 / 0.000 | 44 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-strahler+pre | 5 / 0 | 545 / 0 | 236 / 0 | 109.800 / 0.000 | 4 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 178 / 0 | 237 / 0 | 31 / 0 | 2.326 / 0.000 | 29 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 3 / 0 | 237 / 0 | 236 / 0 | 79.667 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 165 / 0 | 305 / 0 | 31 / 0 | 2.842 / 0.000 | 62 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 12 / 0 | 294 / 0 | 236 / 0 | 25.417 / 0.000 | 7 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 99 / 0 | 237 / 0 | 31 / 0 | 3.384 / 0.000 | 41 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 3 / 0 | 237 / 0 | 236 / 0 | 79.667 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=5_compact.gm · 83 vertices / 111 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 83 | 111 | 5 | 1610 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.498 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.498 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 83 / 0 | 51 / 0 | 24 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 83 / 0 | 25 / 0 | 24 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 83 / 0 | 51 / 0 | 24 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 83 / 0 | 25 / 0 | 24 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 83 / 0 | 41 / 0 | 24 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.395 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 83 / 0 | 25 / 0 | 24 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 83 / 0 | 41 / 0 | 24 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 83 / 0 | 25 / 0 | 24 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 83 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 83 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 27 / 0 | 24 / 0 | 11 / 0 | 1.852 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 27 / 0 | 24 / 0 | 11 / 0 | 1.852 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 17 / 0 | 24 / 0 | 7 / 0 | 2.353 / 0.000 | 7 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 17 / 0 | 24 / 0 | 7 / 0 | 2.353 / 0.000 | 7 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=6.gm · 924 vertices / 1032 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 924 | 1032 | 6 | 1961 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 80.215 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 7.651 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 80.160 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 7.898 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.373 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 1.900 | 85.320 | even | true | true | false | - |
| lifting-sym+pre | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=9 / H=4, K=4, t=9 | 1.887 | 85.324 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.410 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 924 / 0 | 663 / 0 | 354 / 0 | 5 / 0 | k=3, t=3, depth=4 / k=3, t=3, depth=4 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 924 / 0 | 522 / 0 | 518 / 0 | 3 / 0 | k=3, t=8, depth=2 / k=3, t=8, depth=2 | 0.400 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 924 / 0 | 588 / 0 | 317 / 0 | 5 / 0 | k=3, t=3, depth=4 / k=3, t=3, depth=4 | 0.371 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 924 / 0 | 320 / 0 | 317 / 0 | 3 / 0 | k=2, t=8, depth=2 / k=2, t=8, depth=2 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 924 / 0 | 602 / 0 | 390 / 0 | 5 / 0 | bits=4, depth=4 / bits=4, depth=4 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 924 / 0 | 394 / 0 | 381 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 924 / 0 | 456 / 0 | 317 / 0 | 5 / 0 | bits=4, depth=4 / bits=4, depth=4 | 0.381 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 924 / 0 | 320 / 0 | 317 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.382 | 58.574 | even | true | true | false | - |
| zielonka | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 924 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 309 / 0 | 354 / 0 | 31 / 0 | 2.142 / 0.000 | 46 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 4 / 0 | 518 / 0 | 360 / 0 | 130.250 / 0.000 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 271 / 0 | 317 / 0 | 31 / 0 | 2.166 / 0.000 | 41 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 3 / 0 | 317 / 0 | 316 / 0 | 106.333 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 212 / 0 | 390 / 0 | 31 / 0 | 2.835 / 0.000 | 79 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 13 / 0 | 381 / 0 | 316 / 0 | 30.231 / 0.000 | 7 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 139 / 0 | 317 / 0 | 31 / 0 | 3.273 / 0.000 | 57 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 3 / 0 | 317 / 0 | 316 / 0 | 106.333 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=6_compact.gm · 95 vertices / 127 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 95 | 127 | 5 | 1960 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.508 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.506 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 95 / 0 | 59 / 0 | 28 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 95 / 0 | 29 / 0 | 28 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 95 / 0 | 59 / 0 | 28 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 95 / 0 | 29 / 0 | 28 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 95 / 0 | 50 / 0 | 28 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 95 / 0 | 29 / 0 | 28 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 95 / 0 | 50 / 0 | 28 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 95 / 0 | 29 / 0 | 28 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 95 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 95 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 31 / 0 | 28 / 0 | 15 / 0 | 1.871 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 28 / 0 | 28 / 0 | 28.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 31 / 0 | 28 / 0 | 15 / 0 | 1.871 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 28 / 0 | 28 / 0 | 28.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 22 / 0 | 28 / 0 | 7 / 0 | 2.227 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 28 / 0 | 28 / 0 | 28.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 22 / 0 | 28 / 0 | 7 / 0 | 2.227 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 28 / 0 | 28 / 0 | 28.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=7.gm · 1190 vertices / 1329 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1190 | 1329 | 6 | 2331 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 180.629 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 24.615 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 180.680 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 24.752 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=10 / H=4, K=4, t=10 | 7.283 | 249.754 | even | true | true | false | - |
| lifting-sym+pre | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.554 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=10 / H=4, K=4, t=10 | 7.353 | 249.809 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.553 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1190 / 0 | 904 / 0 | 530 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1190 / 0 | 970 / 0 | 965 / 0 | 3 / 0 | k=3, t=9, depth=2 / k=3, t=9, depth=2 | 0.453 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1190 / 0 | 880 / 0 | 521 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1190 / 0 | 412 / 0 | 409 / 0 | 3 / 0 | k=2, t=9, depth=2 / k=2, t=9, depth=2 | 0.435 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1190 / 0 | 754 / 0 | 490 / 0 | 5 / 0 | bits=5, depth=4 / bits=5, depth=4 | 0.421 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1190 / 0 | 496 / 0 | 480 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1190 / 0 | 591 / 0 | 409 / 0 | 5 / 0 | bits=5, depth=4 / bits=5, depth=4 | 0.382 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1190 / 0 | 412 / 0 | 409 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1190 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1190 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 374 / 0 | 530 / 0 | 63 / 0 | 2.414 / 0.000 | 56 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 5 / 0 | 965 / 0 | 408 / 0 | 193.800 / 0.000 | 4 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 359 / 0 | 521 / 0 | 63 / 0 | 2.448 / 0.000 | 53 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 3 / 0 | 409 / 0 | 408 / 0 | 137.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 264 / 0 | 490 / 0 | 32 / 0 | 2.852 / 0.000 | 99 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 16 / 0 | 480 / 0 | 408 / 0 | 30.938 / 0.000 | 9 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 182 / 0 | 409 / 0 | 32 / 0 | 3.242 / 0.000 | 75 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 3 / 0 | 409 / 0 | 408 / 0 | 137.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=7_compact.gm · 107 vertices / 143 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 107 | 143 | 5 | 2330 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.518 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.517 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 107 / 0 | 71 / 0 | 32 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 107 / 0 | 33 / 0 | 32 / 0 | 2 / 0 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 107 / 0 | 71 / 0 | 32 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 107 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 107 / 0 | 59 / 0 | 32 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 107 / 0 | 33 / 0 | 32 / 0 | 2 / 0 | bits=5, depth=1 / bits=5, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 107 / 0 | 56 / 0 | 31 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 107 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 107 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.383 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 107 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 39 / 0 | 32 / 0 | 15 / 0 | 1.795 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 32 / 0 | 32 / 0 | 32.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 39 / 0 | 32 / 0 | 15 / 0 | 1.795 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 27 / 0 | 32 / 0 | 8 / 0 | 2.148 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 32 / 0 | 32 / 0 | 32.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 25 / 0 | 31 / 0 | 7 / 0 | 2.200 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=8.gm · 1490 vertices / 1664 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1490 | 1664 | 6 | 2721 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 180.715 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 180.828 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=10 / H=4, K=4, t=10 | 7.359 | 249.711 | even | true | true | false | - |
| lifting-sym+pre | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.574 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=10 / H=4, K=4, t=10 | 7.332 | 249.879 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.554 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1490 / 0 | 1372 / 0 | 790 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.464 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1490 / 0 | 518 / 0 | 513 / 0 | 3 / 0 | k=3, t=8, depth=2 / k=3, t=8, depth=2 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1490 / 0 | 862 / 0 | 513 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1490 / 0 | 516 / 0 | 513 / 0 | 3 / 0 | k=2, t=9, depth=2 / k=2, t=9, depth=2 | 0.462 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1490 / 0 | 935 / 0 | 641 / 0 | 5 / 0 | bits=5, depth=4 / bits=5, depth=4 | 0.430 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1490 / 0 | 694 / 0 | 668 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1490 / 0 | 711 / 0 | 513 / 0 | 5 / 0 | bits=5, depth=4 / bits=5, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1490 / 0 | 517 / 0 | 513 / 0 | 3 / 0 | bits=8, depth=2 / bits=8, depth=2 | 0.401 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1490 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1490 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 582 / 0 | 790 / 0 | 63 / 0 | 2.356 / 0.000 | 75 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 5 / 0 | 513 / 0 | 508 / 0 | 103.400 / 0.000 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 349 / 0 | 513 / 0 | 63 / 0 | 2.467 / 0.000 | 52 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 3 / 0 | 513 / 0 | 512 / 0 | 171.667 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 294 / 0 | 641 / 0 | 32 / 0 | 3.177 / 0.000 | 115 / 0 | 5 / 0 | 5.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 26 / 0 | 668 / 0 | 511 / 0 | 26.654 / 0.000 | 13 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 198 / 0 | 513 / 0 | 32 / 0 | 3.586 / 0.000 | 83 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 4 / 0 | 513 / 0 | 511 / 0 | 129.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=8_compact.gm · 119 vertices / 159 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 119 | 159 | 5 | 2720 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.517 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.403 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.517 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.445 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=6 / H=4, K=4, t=6 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 119 / 0 | 71 / 0 | 36 / 0 | 4 / 0 | k=3, t=2, depth=3 / k=3, t=2, depth=4 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 119 / 0 | 37 / 0 | 36 / 0 | 2 / 0 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 0.395 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 119 / 0 | 80 / 0 | 35 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 119 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 119 / 0 | 65 / 0 | 36 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 119 / 0 | 37 / 0 | 36 / 0 | 2 / 0 | bits=5, depth=1 / bits=5, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 119 / 0 | 56 / 0 | 31 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 119 / 0 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 119 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 119 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 35 / 0 | 36 / 0 | 15 / 0 | 2.000 / 0.000 | 6 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 1 / 0 | 36 / 0 | 36 / 0 | 36.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 45 / 0 | 35 / 0 | 15 / 0 | 1.756 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 29 / 0 | 36 / 0 | 8 / 0 | 2.207 / 0.000 | 11 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 36 / 0 | 36 / 0 | 36.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 25 / 0 | 31 / 0 | 7 / 0 | 2.200 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/StarNesterk=1_n=1.gm · 76 vertices / 95 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 76 | 95 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 76 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| zielonka | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.408 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 76 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=1_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=2.gm · 336 vertices / 394 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 336 | 394 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.414 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 336 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 336 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=2_compact.gm · 15 vertices / 35 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15 | 35 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| zielonka | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=3.gm · 912 vertices / 1029 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 912 | 1029 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.398 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 912 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.396 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 912 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=3_compact.gm · 21 vertices / 63 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 21 | 63 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| zielonka | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.419 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.419 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=4.gm · 1924 vertices / 2120 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1924 | 2120 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.428 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.427 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.426 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.427 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.427 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.427 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.416 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.416 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.416 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1924 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.396 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1924 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=4_compact.gm · 27 vertices / 99 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 27 | 99 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=5.gm · 3492 vertices / 3787 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3492 | 3787 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.456 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.456 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.435 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.436 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3492 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.416 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.416 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3492 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=5_compact.gm · 33 vertices / 143 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 33 | 143 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.398 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.397 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.445 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=6.gm · 5736 vertices / 6150 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5736 | 6150 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.559 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.568 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.548 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.560 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.545 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.536 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.547 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=12 / H=1, K=1, t=12 | 0.559 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5736 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5736 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=6_compact.gm · 39 vertices / 195 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39 | 195 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=7.gm · 8776 vertices / 9329 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8776 | 9329 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.008 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.007 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.018 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.987 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.999 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.995 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.977 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.989 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.400 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8776 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8776 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=7_compact.gm · 45 vertices / 255 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 45 | 255 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.408 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=8.gm · 12732 vertices / 13444 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12732 | 13444 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.011 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.015 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.046 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.986 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.996 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.996 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 0.993 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.000 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12732 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12732 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=1_n=8_compact.gm · 51 vertices / 323 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 51 | 323 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=1.gm · 61 vertices / 74 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 61 | 74 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 61 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 61 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=1_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.410 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=2.gm · 160 vertices / 179 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 160 | 179 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 160 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| zielonka | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 160 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=2_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.409 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.409 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.409 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=3.gm · 319 vertices / 344 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 319 | 344 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 319 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 319 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=3_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=4.gm · 538 vertices / 569 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 538 | 569 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 538 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 538 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=4_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=5.gm · 817 vertices / 854 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 817 | 854 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.398 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.397 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.396 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 817 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 817 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=5_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.408 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.408 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=6.gm · 1156 vertices / 1199 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1156 | 1199 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.414 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.414 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1156 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1156 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=6_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=7.gm · 1555 vertices / 1604 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1555 | 1604 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.413 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1555 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1555 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=7_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.411 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.400 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.397 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=8.gm · 2014 vertices / 2069 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2014 | 2069 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.415 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.416 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2014 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2014 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=2_n=8_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=3_n=1.gm · 30 vertices / 42 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30 | 42 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 30 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 30 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=3_n=1_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
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
<summary>mlsolver/games/StarNesterk=3_n=2.gm · 75 vertices / 110 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 75 | 110 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.400 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.441 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.398 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 75 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 75 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

