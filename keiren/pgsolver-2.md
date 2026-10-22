# pgsolver, part 2

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=11.gm · 1000 vertices / 10424 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10424 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.297 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.434 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.561 | 436.027 | even | true | true | false | - |
| lifting-sym+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.485 | 436.148 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 501 / 499 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 501 / 499 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.377 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 501 / 499 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.371 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 501 / 499 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.371 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 21 | 4 / 4 | 4 / 4 | 1.176 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=12.gm · 1000 vertices / 10378 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10378 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.301 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.289 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.632 | 436.016 | even | true | true | false | - |
| lifting-sym+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.553 | 436.008 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 512 / 488 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 512 / 488 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 512 / 488 | 28 / 46 | 6 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 512 / 488 | 23 / 40 | 5 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 512 / 488 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 512 / 488 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 37 | 6 / 9 | 4 / 4 | 1.227 / 1.216 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 32 | 5 / 8 | 3 / 3 | 1.222 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=13.gm · 1000 vertices / 10461 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10461 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.223 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.434 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.596 | 436.023 | odd | false | true | false | - |
| lifting-sym+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.573 | 436.012 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 469 / 531 | 21 / 36 | 4 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 469 / 531 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 469 / 531 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 469 / 531 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.372 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.372 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 30 | 4 / 6 | 4 / 5 | 1.176 / 1.167 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 21 / 27 | 6 / 6 | 3 / 3 | 1.238 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 27 | 6 / 6 | 3 / 3 | 1.238 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=14.gm · 1000 vertices / 10496 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10496 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.160 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.309 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.663 | 496.414 | even | true | true | false | - |
| lifting-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.527 | 534.156 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 487 / 513 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 487 / 513 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 487 / 513 | 23 / 37 | 5 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 487 / 513 | 23 / 31 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.371 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 487 / 513 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.373 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 18 / 30 | 5 / 7 | 3 / 4 | 1.222 / 1.200 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 25 | 5 / 6 | 3 / 3 | 1.222 / 1.200 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=15.gm · 1000 vertices / 10733 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10733 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.305 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.312 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.648 | 435.832 | odd | false | true | false | - |
| lifting-sym+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.646 | 436.156 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 489 / 511 | 25 / 25 | 5 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.382 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.371 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 489 / 511 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 489 / 511 | 28 / 33 | 7 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.381 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 489 / 511 | 28 / 33 | 7 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.372 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 489 / 511 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 21 | 5 / 4 | 4 / 4 | 1.200 / 1.143 | 2 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 21 / 27 | 7 / 6 | 3 / 3 | 1.286 / 1.185 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 27 | 7 / 6 | 3 / 3 | 1.286 / 1.185 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=16.gm · 1000 vertices / 10641 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10641 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.418 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.199 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.526 | 436.027 | even | true | true | false | - |
| lifting-sym+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.480 | 435.902 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 469 / 531 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 469 / 531 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 469 / 531 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.375 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 469 / 531 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 469 / 531 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 469 / 531 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 34 | 7 / 8 | 4 / 4 | 1.240 / 1.206 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=17.gm · 1000 vertices / 10755 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10755 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.371 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 275.047 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.894 | 436.012 | even | true | true | false | - |
| lifting-sym+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.782 | 435.957 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 484 / 516 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 484 / 516 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 484 / 516 | 28 / 44 | 6 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 484 / 516 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| zielonka | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 484 / 516 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 36 | 6 / 8 | 4 / 4 | 1.227 / 1.194 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=18.gm · 1000 vertices / 10595 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10595 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.391 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.301 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.629 | 436.008 | odd | false | true | false | - |
| lifting-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.582 | 436.023 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 490 / 510 | 26 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 490 / 510 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 490 / 510 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.371 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 490 / 510 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.371 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 21 / 30 | 5 / 6 | 5 / 5 | 1.190 / 1.167 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 34 | 7 / 8 | 4 / 4 | 1.240 / 1.206 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=19.gm · 1000 vertices / 10548 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10548 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.289 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.418 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.569 | 436.012 | even | true | true | false | - |
| lifting-sym+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.581 | 435.926 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 532 / 468 | 25 / 25 | 5 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 532 / 468 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 532 / 468 | 26 / 39 | 6 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 532 / 468 | 26 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 532 / 468 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 532 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 21 | 5 / 4 | 4 / 4 | 1.200 / 1.143 | 2 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 20 / 32 | 6 / 7 | 3 / 4 | 1.250 / 1.188 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 20 / 27 | 6 / 6 | 3 / 3 | 1.250 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=2.gm · 1000 vertices / 10499 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10499 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.293 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.434 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.555 | 534.227 | even | true | true | false | - |
| lifting-sym+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.581 | 435.965 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 463 / 537 | 27 / 25 | 6 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 463 / 537 | 8 / 0 | 2 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 463 / 537 | 30 / 28 | 7 / 5 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 463 / 537 | 25 / 28 | 6 / 5 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 463 / 537 | 4 / 2 | 1 / 1 | 4 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 21 / 21 | 6 / 4 | 4 / 4 | 1.238 / 1.143 | 3 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 6 / 0 | 2 / 0 | 2 / 0 | 1.167 / 0.000 | 1 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 23 / 23 | 7 / 5 | 4 / 3 | 1.261 / 1.174 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19 / 23 | 6 / 5 | 3 / 3 | 1.263 / 1.174 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=20.gm · 1000 vertices / 10704 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10704 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.305 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.422 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.830 | 436.027 | odd | false | true | false | - |
| lifting-sym+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.803 | 435.906 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 483 / 517 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 483 / 517 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.387 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 483 / 517 | 23 / 39 | 5 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 483 / 517 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 483 / 517 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 17 / 21 | 4 / 4 | 4 / 4 | 1.176 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 18 / 32 | 5 / 7 | 3 / 4 | 1.222 / 1.188 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=21.gm · 1000 vertices / 10657 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10657 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 323.270 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 275.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.716 | 435.832 | odd | false | true | false | - |
| lifting-sym+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.601 | 435.965 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 523 / 477 | 16 / 25 | 3 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 523 / 477 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 523 / 477 | 20 / 39 | 4 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 523 / 477 | 20 / 33 | 4 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 523 / 477 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 523 / 477 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 13 / 21 | 3 / 4 | 3 / 4 | 1.154 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 16 / 32 | 4 / 7 | 3 / 4 | 1.188 / 1.188 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 16 / 27 | 4 / 6 | 3 / 3 | 1.188 / 1.185 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=22.gm · 1000 vertices / 10750 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10750 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.223 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.371 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.603 | 435.969 | even | true | true | false | - |
| lifting-sym+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.687 | 436.027 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 492 / 508 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 492 / 508 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 492 / 508 | 25 / 36 | 5 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.371 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 492 / 508 | 20 / 36 | 4 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 492 / 508 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 492 / 508 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 20 / 29 | 5 / 7 | 4 / 3 | 1.200 / 1.207 | 2 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 16 / 29 | 4 / 7 | 3 / 3 | 1.188 / 1.207 | 2 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=23.gm · 1000 vertices / 10499 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10499 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.438 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.418 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.644 | 436.027 | even | true | true | false | - |
| lifting-sym+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.696 | 435.758 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 510 / 490 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 510 / 490 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 510 / 490 | 28 / 36 | 6 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 510 / 490 | 23 / 36 | 5 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 510 / 490 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 510 / 490 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 29 | 6 / 7 | 4 / 3 | 1.227 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 29 | 5 / 7 | 3 / 3 | 1.222 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=24.gm · 1000 vertices / 10368 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10368 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.312 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.301 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.546 | 436.133 | odd | false | true | false | - |
| lifting-sym+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.517 | 435.691 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 502 / 498 | 29 / 30 | 6 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 502 / 498 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 502 / 498 | 35 / 37 | 8 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 502 / 498 | 23 / 31 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.381 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.379 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 502 / 498 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 502 / 498 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 23 / 25 | 6 / 5 | 4 / 4 | 1.217 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 27 / 30 | 8 / 7 | 4 / 4 | 1.259 / 1.200 | 5 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 25 | 5 / 6 | 3 / 3 | 1.222 / 1.200 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=3.gm · 1000 vertices / 10826 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10826 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.250 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.227 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.599 | 436.090 | even | true | true | false | - |
| lifting-sym+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.620 | 436.016 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 533 / 467 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 533 / 467 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.372 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 533 / 467 | 32 / 39 | 7 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 533 / 467 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 533 / 467 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 21 | 4 / 4 | 4 / 4 | 1.176 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 32 | 7 / 7 | 4 / 4 | 1.240 / 1.188 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 27 | 6 / 6 | 3 / 3 | 1.238 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=4.gm · 1000 vertices / 10809 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10809 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.402 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.371 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.651 | 435.848 | odd | false | true | false | - |
| lifting-sym+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.522 | 435.895 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 493 / 507 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 493 / 507 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 493 / 507 | 20 / 33 | 4 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 493 / 507 | 20 / 33 | 4 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.371 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 493 / 507 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 493 / 507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 21 | 4 / 4 | 4 / 4 | 1.176 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 16 / 27 | 4 / 6 | 3 / 3 | 1.188 / 1.185 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 16 / 27 | 4 / 6 | 3 / 3 | 1.188 / 1.185 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=5.gm · 1000 vertices / 10723 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10723 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 323.375 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.246 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.761 | 435.832 | even | true | true | false | - |
| lifting-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.507 | 435.895 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 500 / 500 | 16 / 37 | 3 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 500 / 500 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 500 / 500 | 20 / 39 | 4 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 500 / 500 | 20 / 33 | 4 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 500 / 500 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 13 / 31 | 3 / 6 | 3 / 6 | 1.154 / 1.161 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 16 / 32 | 4 / 7 | 3 / 4 | 1.188 / 1.188 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 16 / 27 | 4 / 6 | 3 / 3 | 1.188 / 1.185 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=6.gm · 1000 vertices / 10343 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10343 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 275.105 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.414 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.661 | 435.945 | even | true | true | false | - |
| lifting-sym+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.503 | 435.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 505 / 495 | 25 / 25 | 5 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 505 / 495 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 505 / 495 | 23 / 39 | 5 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 505 / 495 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.372 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 505 / 495 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 505 / 495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 21 | 5 / 4 | 4 / 4 | 1.200 / 1.143 | 2 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 18 / 32 | 5 / 7 | 3 / 4 | 1.222 / 1.188 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=7.gm · 1000 vertices / 10251 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10251 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.367 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.309 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.562 | 436.000 | even | true | true | false | - |
| lifting-sym+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.629 | 435.898 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 516 / 484 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.382 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 516 / 484 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 516 / 484 | 25 / 28 | 5 / 5 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 516 / 484 | 20 / 28 | 4 / 5 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 516 / 484 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 516 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 20 / 23 | 5 / 5 | 4 / 3 | 1.200 / 1.174 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 16 / 23 | 4 / 5 | 3 / 3 | 1.188 / 1.174 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=8.gm · 1000 vertices / 10682 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10682 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.363 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.312 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.490 | 436.082 | odd | false | true | false | - |
| lifting-sym+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.609 | 484.215 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 497 / 503 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 497 / 503 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 497 / 503 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 497 / 503 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 497 / 503 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 497 / 503 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 21 | 4 / 4 | 4 / 4 | 1.176 / 1.143 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=9.gm · 1000 vertices / 10351 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10351 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 323.363 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 323.297 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.628 | 436.008 | even | true | true | false | - |
| lifting-sym+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.663 | 436.137 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 501 / 499 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 501 / 499 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 501 / 499 | 29 / 37 | 7 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.382 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 501 / 499 | 29 / 31 | 7 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 501 / 499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 501 / 499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 30 | 7 / 7 | 3 / 4 | 1.273 / 1.200 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 25 | 7 / 6 | 3 / 3 | 1.273 / 1.200 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=0.gm · 10000 vertices / 104720 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104720 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.154 | 1212.684 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.133 | 1212.746 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5003 / 4997 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.549 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5003 / 4997 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.549 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.078 | 1212.535 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.088 | 1212.789 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5003 / 4997 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.537 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5003 / 4997 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5003 / 4997 | 32 / 46 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.580 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5003 / 4997 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.473 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5003 / 4997 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5003 / 4997 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 34 | 5 / 7 | 4 / 5 | 1.200 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 37 | 7 / 9 | 4 / 4 | 1.240 / 1.216 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=1.gm · 10000 vertices / 105013 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105013 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.154 | 1212.832 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.153 | 1212.770 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5037 / 4963 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.559 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5037 / 4963 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.556 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.093 | 1212.895 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.096 | 1212.848 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5037 / 4963 | 25 / 47 | 5 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.548 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.443 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5037 / 4963 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.456 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5037 / 4963 | 35 / 59 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5037 / 4963 | 30 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5037 / 4963 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5037 / 4963 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5037 / 4963 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 39 | 5 / 8 | 4 / 6 | 1.200 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 27 / 48 | 8 / 11 | 4 / 6 | 1.259 / 1.208 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 29 | 7 / 7 | 3 / 3 | 1.261 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=10.gm · 10000 vertices / 105089 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105089 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.101 | 1212.906 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.173 | 1212.766 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4971 / 5029 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.558 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4971 / 5029 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.087 | 1212.949 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.168 | 1212.883 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4971 / 5029 | 34 / 30 | 7 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.558 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4971 / 5029 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4971 / 5029 | 39 / 48 | 9 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.569 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4971 / 5029 | 30 / 37 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.468 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.437 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4971 / 5029 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4971 / 5029 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4971 / 5029 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 27 / 25 | 7 / 5 | 5 / 4 | 1.222 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 30 / 39 | 9 / 9 | 4 / 4 | 1.267 / 1.205 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 30 | 7 / 7 | 3 / 3 | 1.261 / 1.200 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=11.gm · 10000 vertices / 105602 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105602 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.154 | 1212.859 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.091 | 1212.680 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4850 / 5150 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.539 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4850 / 5150 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.086 | 1212.734 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.159 | 1212.867 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4850 / 5150 | 25 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.548 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4850 / 5150 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.436 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4850 / 5150 | 35 / 47 | 8 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4850 / 5150 | 30 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.477 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4850 / 5150 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4850 / 5150 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4850 / 5150 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 30 | 5 / 6 | 4 / 5 | 1.200 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 27 / 38 | 8 / 9 | 4 / 4 | 1.259 / 1.211 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 29 | 7 / 7 | 3 / 3 | 1.261 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=12.gm · 10000 vertices / 104653 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104653 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.151 | 1212.777 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.140 | 1212.820 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4928 / 5072 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.558 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4928 / 5072 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.096 | 1212.633 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.169 | 1212.770 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4928 / 5072 | 21 / 41 | 4 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.550 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4928 / 5072 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4928 / 5072 | 32 / 49 | 7 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.570 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4928 / 5072 | 27 / 38 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4928 / 5072 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4928 / 5072 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4928 / 5072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 34 | 4 / 7 | 4 / 5 | 1.176 / 1.176 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 39 | 7 / 10 | 4 / 4 | 1.240 / 1.231 | 3 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 30 | 6 / 8 | 3 / 3 | 1.238 / 1.233 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=13.gm · 10000 vertices / 106357 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 106357 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.130 | 1212.941 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.170 | 1212.938 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5050 / 4950 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5050 / 4950 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.538 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.095 | 1212.945 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.149 | 1212.871 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5050 / 4950 | 26 / 35 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.557 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5050 / 4950 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5050 / 4950 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.576 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5050 / 4950 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5050 / 4950 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.431 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5050 / 4950 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 21 / 29 | 5 / 6 | 5 / 4 | 1.190 / 1.172 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 34 | 7 / 8 | 4 / 4 | 1.240 / 1.206 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=14.gm · 10000 vertices / 105236 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105236 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.182 | 1212.863 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.139 | 1212.934 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.085 | 1212.809 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.076 | 1212.930 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4957 / 5043 | 25 / 46 | 5 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.546 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4957 / 5043 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4957 / 5043 | 32 / 60 | 7 / 13 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.424 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4957 / 5043 | 27 / 42 | 6 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 38 | 5 / 8 | 4 / 5 | 1.200 / 1.184 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 47 | 7 / 13 | 4 / 4 | 1.240 / 1.255 | 3 / 8 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 33 | 6 / 9 | 3 / 3 | 1.238 / 1.242 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=15.gm · 10000 vertices / 104944 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104944 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.132 | 1212.688 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.122 | 1212.836 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5084 / 4916 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5084 / 4916 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.549 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.100 | 1212.852 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.126 | 1212.723 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5084 / 4916 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.557 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.445 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5084 / 4916 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5084 / 4916 | 37 / 47 | 9 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5084 / 4916 | 32 / 36 | 8 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5084 / 4916 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.431 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5084 / 4916 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5084 / 4916 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 38 | 9 / 9 | 4 / 4 | 1.286 / 1.211 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 29 | 8 / 7 | 3 / 3 | 1.292 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=16.gm · 10000 vertices / 104207 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104207 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.125 | 1212.801 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.185 | 1212.586 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5104 / 4896 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.559 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5104 / 4896 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.131 | 1212.801 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.077 | 1212.738 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.437 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5104 / 4896 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.556 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5104 / 4896 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.463 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.443 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5104 / 4896 | 41 / 50 | 10 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.579 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5104 / 4896 | 29 / 39 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5104 / 4896 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5104 / 4896 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5104 / 4896 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 27 / 34 | 7 / 7 | 5 / 5 | 1.222 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 31 / 40 | 10 / 10 | 4 / 4 | 1.290 / 1.225 | 6 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 31 | 7 / 8 | 3 / 3 | 1.273 / 1.226 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=17.gm · 10000 vertices / 103997 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 103997 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.155 | 1212.703 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.143 | 1212.691 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5066 / 4934 | 1 / 5 | 1 / 1 | 1 / 5 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5066 / 4934 | 1 / 5 | 1 / 1 | 1 / 5 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.095 | 1212.844 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.125 | 1212.719 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5066 / 4934 | 29 / 30 | 6 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.537 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5066 / 4934 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.452 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5066 / 4934 | 32 / 47 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.566 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.424 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5066 / 4934 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5066 / 4934 | 1 / 5 | 1 / 1 | 1 / 5 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5066 / 4934 | 1 / 5 | 1 / 1 | 1 / 5 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5066 / 4934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 4 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 5 | 1.000 / 5.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 4 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 5 | 1.000 / 5.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 23 / 25 | 6 / 5 | 4 / 4 | 1.217 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 38 | 7 / 9 | 4 / 4 | 1.240 / 1.211 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 4 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 5 | 1.000 / 5.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 4 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 5 | 1.000 / 5.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=18.gm · 10000 vertices / 105120 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105120 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.123 | 1212.633 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.154 | 1212.840 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4954 / 5046 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.563 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4954 / 5046 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.098 | 1212.824 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.138 | 1212.777 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4954 / 5046 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.558 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4954 / 5046 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4954 / 5046 | 34 / 42 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.580 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4954 / 5046 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4954 / 5046 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4954 / 5046 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 34 | 8 / 8 | 4 / 4 | 1.269 / 1.206 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=19.gm · 10000 vertices / 105547 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105547 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.176 | 1212.641 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.102 | 1212.656 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.445 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5025 / 4975 | 6 / 4 | 1 / 2 | 6 / 3 | H=6, K=2, t=1 / H=6, K=2, t=1 | 1.794 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.436 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5025 / 4975 | 0 / 3 | 0 / 1 | 0 / 3 | H=6, K=2, t=1 / H=6, K=2, t=1 | 0.560 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.086 | 1212.828 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.088 | 1212.828 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5025 / 4975 | 29 / 45 | 6 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.548 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5025 / 4975 | 0 / 11 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5025 / 4975 | 0 / 11 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.465 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5025 / 4975 | 0 / 11 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.443 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5025 / 4975 | 38 / 45 | 9 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5025 / 4975 | 0 / 11 | 0 / 2 | 0 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5025 / 4975 | 29 / 33 | 7 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5025 / 4975 | 0 / 11 | 0 / 2 | 0 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5025 / 4975 | 6 / 4 | 1 / 2 | 6 / 3 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5025 / 4975 | 6 / 4 | 1 / 2 | 6 / 3 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5025 / 4975 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.415 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 5 / 2 | 1 / 2 | 1 / 2 | 1.000 / 1.500 | 0 / 1 | 6 / 2 | 6.000 / 2.500 | 1 / 2 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 23 / 37 | 6 / 8 | 4 / 5 | 1.217 / 1.189 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 2 | 0 / 2 | 0.000 / 1.111 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-strahler+iter | 0 / 9 | 0 / 2 | 0 / 2 | 0.000 / 1.111 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 2 | 0 / 2 | 0.000 / 1.111 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-succinct | 29 / 37 | 9 / 8 | 4 / 5 | 1.276 / 1.189 | 5 / 3 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 9 | 0 / 2 | 0 / 2 | 0.000 / 1.111 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-succinct+iter | 22 / 27 | 7 / 6 | 3 / 3 | 1.273 / 1.185 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 9 | 0 / 2 | 0 / 2 | 0.000 / 1.111 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| zielonka | 5 / 2 | 1 / 2 | 1 / 2 | 1.000 / 1.500 | 0 / 1 | 6 / 2 | 6.000 / 2.500 | 1 / 2 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 5 / 2 | 1 / 2 | 1 / 2 | 1.000 / 1.500 | 0 / 1 | 6 / 2 | 6.000 / 2.500 | 1 / 2 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=2.gm · 10000 vertices / 104191 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104191 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.162 | 1212.648 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.152 | 1212.562 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5034 / 4966 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.538 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5034 / 4966 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.537 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.096 | 1212.586 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.107 | 1212.645 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5034 / 4966 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.549 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5034 / 4966 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.456 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.443 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5034 / 4966 | 36 / 42 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.567 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.431 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5034 / 4966 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5034 / 4966 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5034 / 4966 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5034 / 4966 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 34 | 8 / 8 | 4 / 4 | 1.250 / 1.206 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=20.gm · 10000 vertices / 105305 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105305 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.151 | 1212.773 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.161 | 1212.898 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5099 / 4901 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5099 / 4901 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.085 | 1212.773 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.093 | 1212.852 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5099 / 4901 | 25 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.546 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5099 / 4901 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.453 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5099 / 4901 | 34 / 46 | 8 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5099 / 4901 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.474 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.443 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5099 / 4901 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5099 / 4901 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5099 / 4901 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 30 | 5 / 6 | 4 / 5 | 1.200 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 37 | 8 / 9 | 4 / 4 | 1.269 / 1.216 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=21.gm · 10000 vertices / 105345 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105345 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.164 | 1212.730 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.153 | 1212.824 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4999 / 5001 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.550 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4999 / 5001 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.549 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.110 | 1212.855 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.098 | 1212.723 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4999 / 5001 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.539 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.436 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4999 / 5001 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4999 / 5001 | 36 / 42 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4999 / 5001 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.425 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4999 / 5001 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.457 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.440 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4999 / 5001 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.454 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4999 / 5001 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 24 / 34 | 6 / 7 | 5 / 5 | 1.208 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 34 | 8 / 8 | 4 / 4 | 1.250 / 1.206 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=22.gm · 10000 vertices / 104788 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104788 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.162 | 1212.703 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.171 | 1212.848 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5009 / 4991 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5009 / 4991 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.168 | 1212.750 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.105 | 1212.738 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5009 / 4991 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.556 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5009 / 4991 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5009 / 4991 | 36 / 39 | 8 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.579 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5009 / 4991 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5009 / 4991 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5009 / 4991 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5009 / 4991 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 32 | 8 / 7 | 4 / 4 | 1.250 / 1.188 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 27 | 6 / 6 | 3 / 3 | 1.238 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=23.gm · 10000 vertices / 105795 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105795 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.130 | 1212.727 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.109 | 1212.832 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5013 / 4987 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5013 / 4987 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.537 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.097 | 1212.730 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.108 | 1212.855 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.437 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5013 / 4987 | 30 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.537 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5013 / 4987 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.436 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5013 / 4987 | 32 / 51 | 7 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5013 / 4987 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.472 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.435 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5013 / 4987 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5013 / 4987 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 30 | 6 / 6 | 5 / 5 | 1.208 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 41 | 7 / 10 | 4 / 4 | 1.240 / 1.220 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=24.gm · 10000 vertices / 106168 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 106168 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.181 | 1212.871 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.078 | 1212.762 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.559 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.546 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.120 | 1212.766 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.158 | 1212.824 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4957 / 5043 | 29 / 30 | 6 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.539 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.436 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4957 / 5043 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.465 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4957 / 5043 | 38 / 47 | 9 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4957 / 5043 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.473 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4957 / 5043 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.449 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4957 / 5043 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 23 / 25 | 6 / 5 | 4 / 4 | 1.217 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 29 / 38 | 9 / 9 | 4 / 4 | 1.276 / 1.211 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=3.gm · 10000 vertices / 104188 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104188 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.133 | 1212.738 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.132 | 1212.863 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4966 / 5034 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4966 / 5034 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.108 | 1212.746 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.431 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.074 | 1212.801 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4966 / 5034 | 29 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.538 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4966 / 5034 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.442 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4966 / 5034 | 34 / 42 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.568 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4966 / 5034 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.424 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4966 / 5034 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4966 / 5034 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 23 / 30 | 6 / 6 | 4 / 5 | 1.217 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 34 | 8 / 8 | 4 / 4 | 1.269 / 1.206 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=4.gm · 10000 vertices / 105286 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105286 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.121 | 1212.980 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.110 | 1212.895 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4988 / 5012 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.557 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4988 / 5012 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.139 | 1212.793 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.097 | 1212.793 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4988 / 5012 | 30 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.568 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4988 / 5012 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4988 / 5012 | 35 / 48 | 8 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4988 / 5012 | 30 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.474 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4988 / 5012 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4988 / 5012 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4988 / 5012 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 30 | 6 / 6 | 5 / 5 | 1.208 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 27 / 39 | 8 / 9 | 4 / 5 | 1.259 / 1.205 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 29 | 7 / 7 | 3 / 3 | 1.261 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=5.gm · 10000 vertices / 106096 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 106096 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.124 | 1212.895 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.133 | 1212.824 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5045 / 4955 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.550 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5045 / 4955 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.110 | 1212.836 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.112 | 1212.832 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5045 / 4955 | 25 / 40 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.540 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5045 / 4955 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5045 / 4955 | 36 / 55 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5045 / 4955 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.473 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5045 / 4955 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.442 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5045 / 4955 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5045 / 4955 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 33 | 5 / 7 | 4 / 4 | 1.200 / 1.182 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 44 | 8 / 11 | 4 / 4 | 1.250 / 1.227 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=6.gm · 10000 vertices / 104527 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104527 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.175 | 1212.609 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.102 | 1212.746 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4973 / 5027 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.558 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4973 / 5027 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.546 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.084 | 1212.797 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.077 | 1212.809 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4973 / 5027 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.558 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4973 / 5027 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.436 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4973 / 5027 | 37 / 53 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4973 / 5027 | 32 / 42 | 8 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4973 / 5027 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4973 / 5027 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4973 / 5027 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 34 | 6 / 7 | 5 / 5 | 1.208 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 42 | 9 / 11 | 4 / 4 | 1.286 / 1.238 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 33 | 8 / 9 | 3 / 3 | 1.292 / 1.242 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=7.gm · 10000 vertices / 104392 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104392 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.134 | 1212.789 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.458 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.154 | 1212.648 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 4880 / 5120 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.559 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4880 / 5120 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.548 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.099 | 1212.652 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.090 | 1212.719 | - | true | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 4880 / 5120 | 39 / 41 | 8 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.559 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 4880 / 5120 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.455 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.444 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 4880 / 5120 | 51 / 47 | 12 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 4880 / 5120 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| zielonka | complete | 4880 / 5120 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 4880 / 5120 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4880 / 5120 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 31 / 34 | 8 / 7 | 6 / 5 | 1.226 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39 / 38 | 12 / 9 | 6 / 4 | 1.282 / 1.211 | 6 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

