# modelchecking, part 7

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_infinitely_often_read_write.gm · 2977 vertices / 6497 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2977 | 6497 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.585 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.555 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.490 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.494 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.411 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.093 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.108 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.100 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.092 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.394 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.395 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2977 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 88.344 | even | true | true | false | - |
| zielonka | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.402 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.402 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.402 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2977 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_infinitely_often_receive_d1.gm · 1490 vertices / 5010 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1490 | 5010 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.197 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 3.197 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.373 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.390 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.413 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 1490 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.425 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 1490 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.424 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 1490 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 1490 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 88.344 | even | true | true | false | - |
| zielonka | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 1490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 88.344 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_infinitely_often_receive_for_all_d.gm · 5958 vertices / 20041 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5958 | 20041 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 88.344 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 88.344 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 88.344 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 88.344 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.699 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.698 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.696 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.476 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.475 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.455 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.444 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5958 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 88.344 | even | true | true | false | - |
| zielonka | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5958 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 88.344 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_invariantly_infinitely_many_reachable_taus.gm · 4033 vertices / 12417 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4033 | 12417 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.843 | 88.344 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.843 | 88.344 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.843 | 88.344 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.850 | 88.344 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 88.344 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 88.344 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.475 | 88.344 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 4033 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 4033 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.412 | 88.344 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 4033 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 4033 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 88.344 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 4033 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.414 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 4033 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 88.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 4033 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 4033 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 4033 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 88.344 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_no_duplication_of_messages.gm · 6866 vertices / 24674 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6866 | 24674 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 11.350 | 88.344 | odd | false | true | false | - |
| lifting+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 88.344 | odd | false | true | false | - |
| lifting+iter | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 11.378 | 88.344 | odd | false | true | false | - |
| lifting+pre+iter | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 88.344 | odd | false | true | false | - |
| lifting-adaptive | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 88.344 | odd | false | true | false | - |
| lifting-sym | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 4.116 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| lifting-sym+iter | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 4.135 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 88.344 | odd | false | true | false | - |
| pm-strahler | complete | 5256 / 1610 | 2 / 39 | 1 / 19 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.617 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 88.344 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5256 / 1610 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 88.344 | odd | false | true | false | - |
| pm-succinct | complete | 5256 / 1610 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.558 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 88.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5256 / 1610 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.404 | 88.344 | odd | false | true | false | - |
| zielonka+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym | complete | 5256 / 1610 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.394 | 88.344 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5256 / 1610 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | odd | false | true | false | - |

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
| pm-strahler | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_no_generation_of_messages.gm · 3344 vertices / 11922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3344 | 11922 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.413 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.414 | 88.344 | even | true | true | false | - |
| zielonka | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_nodeadlock.gm · 1345 vertices / 4865 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1345 | 4865 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.407 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.407 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.415 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.406 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.415 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.436 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.395 | 88.344 | even | true | true | false | - |
| zielonka | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_read_then_eventually_send.gm · 7897 vertices / 26073 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7897 | 26073 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.767 | 88.344 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.772 | 88.344 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 88.344 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.688 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7897 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.411 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 88.344 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7897 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 88.344 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7897 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 88.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7897 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 88.344 | odd | false | true | false | - |
| zielonka | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 88.344 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | odd | false | true | false | - |

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
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_read_then_eventually_send_if_fair.gm · 2690 vertices / 7322 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2690 | 7322 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.131 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.130 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.732 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.754 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 2690 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.400 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.380 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.382 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.383 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 2690 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.397 | 88.344 | even | true | true | false | - |
| zielonka | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.397 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 88.344 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 2245634 vertices / 6978309 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2245634 | 6978309 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.067 | 782.574 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 782.531 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.068 | 782.719 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 782.715 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 8.488 | 782.578 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 8.489 | 782.715 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 9.099 | 782.656 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 9.150 | 782.578 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 782.578 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 782.695 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 782.590 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 782.445 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 782.652 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 782.508 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 0 / 2245634 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 15.750 | 782.590 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 2245634 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 15.819 | 782.535 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 2245634 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 14.729 | 782.387 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 2245634 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 14.699 | 782.594 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 2245634 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.700 | 782.590 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 2245634 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.554 | 782.422 | odd | - | - | false | - |
| zielonka | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.690 | 782.715 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.859 | 782.699 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 4.793 | 782.695 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 4.804 | 782.578 | odd | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_lost.gm · 512018 vertices / 2504114 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 512018 | 2504114 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.145 | 1457.387 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.404 | 222.211 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.143 | 1457.383 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.295 | 221.863 | even | - | - | false | - |
| lifting-adaptive | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 2.735 | 222.078 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.317 | 222.211 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 3.088 | 222.082 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.528 | 222.145 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1459.184 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.207 | 222.098 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1462.375 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.420 | 222.211 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 222.086 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 1.476 | 221.961 | even | - | - | false | - |
| pm-strahler+iter | complete | 362945 / 149073 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 4.106 | 222.027 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 1.531 | 222.094 | even | - | - | false | - |
| pm-succinct | complete | 362945 / 149073 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 25.146 | 222.027 | even | - | - | false | - |
| pm-succinct+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.350 | 222.020 | even | - | - | false | - |
| pm-succinct+iter | complete | 362945 / 149073 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 3.507 | 221.953 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.385 | 222.074 | even | - | - | false | - |
| zielonka | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 1.405 | 221.914 | even | - | - | false | - |
| zielonka+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.260 | 222.207 | even | - | - | false | - |
| zielonka-sym | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 1.793 | 222.191 | even | - | - | false | - |
| zielonka-sym+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.279 | 222.141 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 5 / 0 | 4 / 0 | 1.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 3 | 3 / 2 | 2 / 2 | 1.667 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_read_write.gm · 353089 vertices / 800769 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 353089 | 800769 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 113.055 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 113.059 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 112.852 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 113.059 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 10.849 | 108.797 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 10.787 | 109.055 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 11.242 | 108.941 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 11.294 | 108.711 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 112.789 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 112.914 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 113.062 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 112.922 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.456 | 109.016 | even | - | - | false | - |
| pm-strahler+pre | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.438 | 109.016 | even | - | - | false | - |
| pm-strahler+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.445 | 108.781 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.493 | 108.891 | even | - | - | false | - |
| pm-succinct | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.326 | 108.742 | even | - | - | false | - |
| pm-succinct+pre | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.380 | 109.016 | even | - | - | false | - |
| pm-succinct+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.602 | 108.945 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.651 | 109.016 | even | - | - | false | - |
| zielonka | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.947 | 108.949 | even | - | - | false | - |
| zielonka+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.940 | 108.938 | even | - | - | false | - |
| zielonka-sym | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 1.313 | 109.055 | even | - | - | false | - |
| zielonka-sym+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 1.294 | 108.883 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_receive_d1.gm · 163394 vertices / 611074 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 163394 | 611074 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 89.137 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.643 | 89.137 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 89.137 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.639 | 89.137 | even | true | true | false | - |
| lifting-adaptive | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.994 | 89.137 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.748 | 89.137 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.107 | 89.137 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.757 | 89.137 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 89.137 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.688 | 89.137 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 89.137 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.684 | 89.137 | even | true | true | false | - |
| pm-strahler | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.107 | 89.137 | even | true | true | false | - |
| pm-strahler+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.735 | 89.137 | even | true | true | false | - |
| pm-strahler+iter | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.991 | 89.137 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.727 | 89.137 | even | true | true | false | - |
| pm-succinct | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.429 | 89.137 | even | true | true | false | - |
| pm-succinct+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.727 | 89.137 | even | true | true | false | - |
| pm-succinct+iter | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.429 | 89.137 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.726 | 89.137 | even | true | true | false | - |
| zielonka | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.695 | 89.137 | even | true | true | false | - |
| zielonka+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 89.137 | even | true | true | false | - |
| zielonka-sym | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.767 | 89.137 | even | true | true | false | - |
| zielonka-sym+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.695 | 89.137 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_receive_for_all_d.gm · 653574 vertices / 2444297 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 653574 | 2444297 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 255.418 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.484 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.426 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.492 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.673 | 255.422 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.674 | 255.422 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.833 | 255.414 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.833 | 255.422 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 255.430 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 255.422 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 255.414 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 255.422 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 16.203 | 255.406 | even | - | - | false | - |
| pm-strahler+pre | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.814 | 255.402 | even | - | - | false | - |
| pm-strahler+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 10.214 | 255.371 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.857 | 255.496 | even | - | - | false | - |
| pm-succinct | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.093 | 255.223 | even | - | - | false | - |
| pm-succinct+pre | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.138 | 255.355 | even | - | - | false | - |
| pm-succinct+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.737 | 255.355 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.801 | 255.500 | even | - | - | false | - |
| zielonka | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.385 | 255.344 | even | - | - | false | - |
| zielonka+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.441 | 255.531 | even | - | - | false | - |
| zielonka-sym | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.652 | 255.430 | even | - | - | false | - |
| zielonka-sym+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.623 | 255.551 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_invariantly_infinitely_many_reachable_taus.gm · 421057 vertices / 1456769 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 421057 | 1456769 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 154.871 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 154.969 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 155.105 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 154.840 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.468 | 155.055 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.478 | 155.105 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.502 | 154.969 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.563 | 154.828 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 155.105 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 154.961 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 155.160 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 155.031 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.062 | 154.926 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.259 | 154.922 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 421057 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.422 | 154.980 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 421057 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.427 | 154.918 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 2.905 | 154.984 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 2.959 | 154.922 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 421057 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.792 | 154.965 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 421057 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.803 | 155.047 | odd | false | true | false | - |
| zielonka | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.128 | 154.965 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.213 | 155.035 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.333 | 154.980 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.336 | 154.961 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_no_duplication_of_messages.gm · 858114 vertices / 3433490 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 858114 | 3433490 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 340.547 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.694 | 340.656 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 340.547 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.695 | 340.648 | odd | - | - | false | - |
| lifting-adaptive | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.602 | 340.551 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.859 | 340.539 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.835 | 340.547 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.848 | 340.488 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 340.680 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.775 | 340.547 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 340.555 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.754 | 340.547 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 340.559 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.906 | 340.543 | odd | - | - | false | - |
| pm-strahler+iter | complete | 494528 / 363586 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.315 | 340.480 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.892 | 340.555 | odd | - | - | false | - |
| pm-succinct | complete | 494528 / 363586 | 2 / 43 | 1 / 21 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 26.934 | 340.496 | odd | - | - | false | - |
| pm-succinct+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.755 | 340.539 | odd | - | - | false | - |
| pm-succinct+iter | complete | 494528 / 363586 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.365 | 340.543 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.784 | 340.539 | odd | - | - | false | - |
| zielonka | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.706 | 340.555 | odd | - | - | false | - |
| zielonka+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.612 | 340.680 | odd | - | - | false | - |
| zielonka-sym | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.203 | 340.676 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.601 | 340.680 | odd | - | - | false | - |

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
| pm-succinct | 1 / 22 | 1 / 21 | 1 / 21 | 1.000 / 1.909 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_no_generation_of_messages.gm · 211955 vertices / 876954 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 211955 | 876954 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.811 | 89.574 | even | true | true | false | - |
| lifting+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.696 | 89.574 | even | true | true | false | - |
| lifting+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.828 | 89.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| lifting-adaptive | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.793 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 89.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.795 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 89.574 | even | true | true | false | - |
| lifting-sym | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.774 | 89.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.793 | 89.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| pm-strahler | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.837 | 89.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.714 | 89.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.797 | 89.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.724 | 89.574 | even | true | true | false | - |
| pm-succinct | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.971 | 89.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.711 | 89.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.797 | 89.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.717 | 89.574 | even | true | true | false | - |
| zielonka | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.686 | 89.574 | even | true | true | false | - |
| zielonka+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 89.574 | even | true | true | false | - |
| zielonka-sym | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.746 | 89.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.683 | 89.574 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_nodeadlock.gm · 140353 vertices / 588033 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 140353 | 588033 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.663 | 89.574 | even | true | true | false | - |
| lifting+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.589 | 89.574 | even | true | true | false | - |
| lifting+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.672 | 89.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 89.574 | even | true | true | false | - |
| lifting-adaptive | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.661 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 89.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.662 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.579 | 89.574 | even | true | true | false | - |
| lifting-sym | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.649 | 89.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.580 | 89.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.665 | 89.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 89.574 | even | true | true | false | - |
| pm-strahler | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.683 | 89.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.609 | 89.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.651 | 89.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.609 | 89.574 | even | true | true | false | - |
| pm-succinct | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.774 | 89.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.600 | 89.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.651 | 89.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.600 | 89.574 | even | true | true | false | - |
| zielonka | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.589 | 89.574 | even | true | true | false | - |
| zielonka+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 89.574 | even | true | true | false | - |
| zielonka-sym | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.607 | 89.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.566 | 89.574 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_read_then_eventually_send.gm · 869569 vertices / 3200129 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 869569 | 3200129 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 333.828 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.746 | 333.699 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 333.832 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.725 | 333.762 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.980 | 333.812 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.891 | 333.766 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.156 | 333.832 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.865 | 333.836 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 333.707 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.819 | 333.773 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 333.766 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.786 | 333.559 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 869569 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.704 | 333.777 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.120 | 333.777 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 869569 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.516 | 333.578 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.043 | 333.711 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 869569 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 5.463 | 333.648 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.054 | 333.777 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 869569 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.686 | 333.777 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.000 | 333.645 | odd | - | - | false | - |
| zielonka | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.886 | 333.582 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.779 | 333.766 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.219 | 333.793 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.747 | 333.836 | odd | - | - | false | - |

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
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_read_then_eventually_send_if_fair.gm · 388418 vertices / 1125698 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 388418 | 1125698 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 129.062 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.882 | 129.062 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 128.922 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.866 | 128.879 | even | - | - | false | - |
| lifting-adaptive | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.746 | 129.062 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.998 | 129.062 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.841 | 129.047 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.987 | 128.941 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 129.043 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.934 | 128.938 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 128.926 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.919 | 129.062 | even | - | - | false | - |
| pm-strahler | complete | 388418 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 12.227 | 129.012 | even | - | - | false | - |
| pm-strahler+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.023 | 128.734 | even | - | - | false | - |
| pm-strahler+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.275 | 128.871 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.012 | 129.008 | even | - | - | false | - |
| pm-succinct | complete | 388418 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.581 | 129.008 | even | - | - | false | - |
| pm-succinct+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.016 | 128.738 | even | - | - | false | - |
| pm-succinct+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.437 | 128.945 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.033 | 128.879 | even | - | - | false | - |
| zielonka | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.952 | 128.992 | even | - | - | false | - |
| zielonka+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.910 | 128.992 | even | - | - | false | - |
| zielonka-sym | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.195 | 128.938 | even | - | - | false | - |
| zielonka-sym+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.947 | 128.996 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_infinitely_often_read_write.gm · 19550209 vertices / 45106177 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19550209 | 45106177 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.660 | 1508.547 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.670 | 1508.578 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.625 | 1508.484 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 17.381 | 1485.297 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 17.307 | 1486.480 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 17.213 | 1489.164 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.710 | 1508.609 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.616 | 1508.523 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.575 | 1508.516 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.989 | 1508.535 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.009 | 1508.465 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.010 | 1508.523 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.984 | 1508.473 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.974 | 1508.336 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.943 | 1508.363 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.100 | 1508.402 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.014 | 1508.340 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.056 | 1508.555 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.155 | 1508.555 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.103 | 1508.422 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.863 | 1508.590 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.493 | 1508.539 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.309 | 1508.473 | - | - | - | - | 6249392:13: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.369 | 1508.609 | - | - | - | - | 6249392:13: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_infinitely_often_receive_d1.gm · 8835074 vertices / 34391042 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8835074 | 34391042 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.465 | 1735.664 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.455 | 1735.840 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.433 | 1735.605 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.447 | 1736.082 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 19.416 | 1736.172 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 19.386 | 1736.297 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.769 | 1712.859 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.830 | 1710.730 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 13.780 | 1713.297 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 23.257 | 1736.047 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 23.216 | 1736.227 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 23.175 | 1736.422 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 23.693 | 1736.242 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 23.719 | 1736.047 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 23.702 | 1736.223 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.561 | 1736.055 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 28.549 | 1736.180 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.533 | 1735.973 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.665 | 1735.098 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.697 | 1734.430 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 22.838 | 1734.598 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 22.072 | 1736.227 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 22.092 | 1735.961 | - | - | - | - | 5859377:31: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 21.950 | 1736.359 | - | - | - | - | 5859377:31: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_invariantly_infinitely_many_reachable_taus.gm · 22288897 vertices / 80830465 edges · 6 timeout · 18 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22288897 | 80830465 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.787 | 1782.031 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.784 | 1779.359 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.784 | 1771.469 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.120 | 1320.086 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.121 | 1319.852 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.119 | 1311.859 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.734 | 1804.977 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.755 | 1797.344 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.953 | 1781.484 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.124 | 1374.363 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1389.109 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.113 | 1485.457 | - | - | - | - | deadline exceeded |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 15.802 | 1422.367 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 15.799 | 1407.363 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 15.589 | 1425.492 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 20.279 | 1696.973 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 20.301 | 1720.055 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 20.255 | 1740.281 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.945 | 1587.973 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.088 | 1559.984 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 26.357 | 1455.352 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 24.218 | 1539.984 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 24.087 | 1532.859 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 23.507 | 1556.477 | - | - | - | - | 4194304:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_no_generation_of_messages.gm · 6690605 vertices / 29413398 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6690605 | 29413398 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.859 | 1613.172 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.879 | 1613.039 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.868 | 1612.961 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.733 | 1612.711 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 14.732 | 1612.980 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.703 | 1613.047 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.459 | 1613.215 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.382 | 1613.215 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.411 | 1612.977 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.473 | 1613.105 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.383 | 1613.098 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.386 | 1613.109 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.958 | 1613.172 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.922 | 1613.098 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.881 | 1612.902 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.015 | 1612.988 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.983 | 1612.906 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.979 | 1613.172 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.507 | 1613.098 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.528 | 1613.180 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 6.360 | 1613.215 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.499 | 1613.215 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.567 | 1612.961 | - | - | - | - | 5178827:67: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.565 | 1613.234 | - | - | - | - | 5178827:67: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_nodeadlock.gm · 7429633 vertices / 32985601 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7429633 | 32985601 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.762 | 1635.328 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.796 | 1635.457 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.794 | 1635.527 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.930 | 1626.215 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 11.867 | 1631.098 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.885 | 1631.086 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.259 | 1619.484 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.270 | 1605.789 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 16.299 | 1608.598 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.695 | 1635.387 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.624 | 1635.406 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.624 | 1635.293 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 11.411 | 1635.156 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.374 | 1635.348 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.396 | 1635.348 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.252 | 1635.234 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 10.270 | 1635.238 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.268 | 1635.555 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.624 | 1635.238 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.603 | 1635.238 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 16.418 | 1635.344 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.855 | 1635.336 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.680 | 1635.523 | - | - | - | - | 4960968:13: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.648 | 1635.605 | - | - | - | - | 4960968:13: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_read_then_eventually_send_if_fair.gm · 24565250 vertices / 73675010 edges · 11 timeout · 13 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 24565250 | 73675010 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.037 | 1776.504 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.145 | 1741.043 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.142 | 1762.273 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.157 | 1675.422 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.178 | 1722.336 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.182 | 1709.855 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.453 | 1668.145 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.191 | 1693.031 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 16.207 | 1683.469 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 17.308 | 1683.090 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 17.288 | 1684.785 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 17.234 | 1676.078 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.179 | 1752.488 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.181 | 1730.055 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.170 | 1749.789 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 34.063 | 1794.410 | - | - | - | - | deadline exceeded |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 34.060 | 1792.789 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 34.011 | 1783.164 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 33.973 | 1793.738 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 33.973 | 1781.980 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 33.973 | 1780.898 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.220 | 812.547 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 814.594 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.177 | 808.660 | - | - | - | - | deadline exceeded |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_enabled_then_infinitely_often_taken.gm · 147458 vertices / 406665 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 147458 | 406665 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.837 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.847 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.857 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.868 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 147458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.470 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 147458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.732 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 147458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.353 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 147458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.352 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 147458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.333 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 147458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.334 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 147458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.885 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 147458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.897 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.675 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.676 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.749 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.740 | 90.051 | odd | false | true | false | - |

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
| pm-succinct | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_lost.gm · 12818 vertices / 49890 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12818 | 49890 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.464 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 9393 / 3425 | 26 / 5 | 13 / 2 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 1.229 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.412 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 9393 / 3425 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.463 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.423 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 9393 / 3425 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.711 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.435 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 9393 / 3425 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.474 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.444 | 90.051 | even | true | true | false | - |
| zielonka | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.454 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.455 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 5 / 0 | 4 / 0 | 1.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 3 | 3 / 2 | 2 / 2 | 1.667 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_read_write.gm · 10369 vertices / 22849 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10369 | 22849 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.454 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.464 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.452 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.473 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.475 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.473 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.422 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.421 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| zielonka | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.390 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.411 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_receive_d1.gm · 4898 vertices / 17378 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4898 | 17378 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.667 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.666 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.430 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.369 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.420 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| zielonka | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |

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
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_receive_for_all_d.gm · 39178 vertices / 139025 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39178 | 139025 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.506 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.506 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.514 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.504 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.933 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.104 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.221 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.006 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.018 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.936 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.906 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.854 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.874 | 90.051 | even | true | true | false | - |
| zielonka | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.531 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.530 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.550 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.550 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_invariantly_infinitely_many_reachable_taus.gm · 13825 vertices / 43393 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13825 | 43393 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.040 | 90.051 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.083 | 90.051 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.009 | 90.051 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.956 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 90.051 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.597 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.578 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.567 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.433 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.433 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 13825 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.412 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 13825 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.445 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.443 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 13825 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.427 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 13825 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.425 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.414 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 5 | 0 / 4 | 0 / 4 | 0.000 / 1.600 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_no_duplication_of_messages.gm · 41762 vertices / 154498 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 41762 | 154498 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.579 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.643 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.541 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 36624 / 5138 | 2 / 39 | 1 / 19 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.184 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.495 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 36624 / 5138 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.508 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.487 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 36624 / 5138 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.642 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.478 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 36624 / 5138 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.497 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.509 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.496 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_no_generation_of_messages.gm · 28964 vertices / 106938 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 28964 | 106938 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.447 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.446 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.448 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.443 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.444 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.443 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.444 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.433 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.443 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.434 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.454 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.434 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.444 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.433 | 90.051 | even | true | true | false | - |
| zielonka | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.432 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_nodeadlock.gm · 4609 vertices / 17089 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4609 | 17089 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.409 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.418 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.414 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| zielonka | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_read_then_eventually_send.gm · 45937 vertices / 160561 edges · 21 complete · 3 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 45937 | 160561 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 90.051 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.601 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.550 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.509 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 21.321 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 45937 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.641 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.548 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 45937 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.571 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.528 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 45937 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.621 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.506 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 45937 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.526 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.508 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.506 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.516 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_read_then_eventually_send_if_fair.gm · 9986 vertices / 26994 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9986 | 26994 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.520 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.481 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 9986 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.485 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 9986 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.431 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 90.051 | even | true | true | false | - |
| zielonka | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Snakewidth=4_height=4_black_has_winning_strategy.gm · 4860 vertices / 6922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4860 | 6922 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.147 | 90.051 | odd | false | true | false | - |
| lifting+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 90.051 | odd | false | true | false | - |
| lifting+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.156 | 90.051 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-sym | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 2.356 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 2.407 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 1886 / 2974 | 12 / 2 | 11 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.403 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.379 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1886 / 2974 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.380 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 1886 / 2974 | 12 / 2 | 11 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.391 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1886 / 2974 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.382 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.401 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 11 / 1 | 11 / 1 | 11.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 11 / 1 | 11 / 1 | 11.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Snakewidth=4_height=4_white_has_winning_strategy.gm · 4860 vertices / 6922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4860 | 6922 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.463 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.453 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.379 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 1.674 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 1.712 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 2975 / 1885 | 14 / 2 | 13 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 2975 / 1885 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 2975 / 1885 | 14 / 2 | 13 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.413 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 2975 / 1885 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.401 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 90.051 | even | true | true | false | - |
| zielonka | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |

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

