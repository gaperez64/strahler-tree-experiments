# modelchecking, part 1

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/ABP(BW)datasize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 778 vertices / 1079 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 778 | 1079 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.917 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.917 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.916 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.908 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.405 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 778 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 778 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 778 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 778 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 778 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 778 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 778 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 778 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 778 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.371 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=2_infinitely_often_read_write.gm · 114 vertices / 139 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 114 | 139 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.408 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.414 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.402 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 114 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.396 | 64.938 | even | true | true | false | - |
| zielonka | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 114 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=2_infinitely_often_receive_d1.gm · 102 vertices / 127 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 102 | 127 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.415 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.414 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 102 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 102 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 102 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 102 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=2_infinitely_often_receive_for_all_d.gm · 204 vertices / 255 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 204 | 255 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.448 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.448 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.448 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.435 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 204 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.408 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 204 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.396 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=2_invariantly_infinitely_many_reachable_taus.gm · 292 vertices / 439 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 292 | 439 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.407 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 292 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 292 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 292 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 292 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 292 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 292 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 292 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.418 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 292 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.418 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.418 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.407 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.407 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 292 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=2_no_duplication_of_messages.gm · 292 vertices / 367 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 292 | 367 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.408 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.398 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 292 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 292 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=2_no_generation_of_messages.gm · 102 vertices / 125 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 102 | 125 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.408 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.408 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 64.938 | even | true | true | false | - |
| zielonka | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 102 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 102 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=2_nodeadlock.gm · 98 vertices / 123 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 98 | 123 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 98 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 98 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=2_read_then_eventually_send.gm · 302 vertices / 383 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 302 | 383 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.415 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 302 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 302 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 302 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 302 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 302 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 302 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 3058 vertices / 4285 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3058 | 4285 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.886 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.806 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.818 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.824 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.472 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3058 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3058 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.390 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3058 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3058 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3058 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3058 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3058 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3058 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3058 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=4_infinitely_often_read_write.gm · 222 vertices / 275 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 222 | 275 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.436 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.436 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.414 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.424 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.424 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.424 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 222 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 222 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=4_infinitely_often_receive_d1.gm · 196 vertices / 249 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 196 | 249 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.436 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.446 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 196 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 196 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 196 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 196 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.449 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 196 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 196 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=4_infinitely_often_receive_for_all_d.gm · 782 vertices / 997 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 782 | 997 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.997 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.997 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.999 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.998 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 782 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 782 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=4_invariantly_infinitely_many_reachable_taus.gm · 574 vertices / 871 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 574 | 871 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.459 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.459 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.459 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.445 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 574 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 574 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 574 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 574 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 574 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 574 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.395 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 574 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.395 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 574 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 574 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=4_no_duplication_of_messages.gm · 956 vertices / 1221 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 956 | 1221 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| zielonka | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 956 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 956 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=4_no_generation_of_messages.gm · 578 vertices / 737 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 578 | 737 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| zielonka | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 578 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 578 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=4_nodeadlock.gm · 192 vertices / 245 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 192 | 245 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| zielonka | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 192 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=4_read_then_eventually_send.gm · 976 vertices / 1253 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 976 | 1253 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.488 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.487 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 976 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 976 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 976 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 976 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 976 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=8_infinitely_often_enabled_then_infinitely_often_taken.gm · 12130 vertices / 17081 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12130 | 17081 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 64.938 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.578 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.545 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.565 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.586 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 12130 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 12130 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.453 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 12130 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.434 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 12130 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 12130 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 12130 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 12130 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 12130 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.425 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.400 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 12130 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.390 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=8_infinitely_often_read_write.gm · 438 vertices / 547 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 438 | 547 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.497 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.485 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.443 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.445 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.444 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.447 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 438 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| zielonka | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 438 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.382 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=8_infinitely_often_receive_d1.gm · 384 vertices / 493 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 384 | 493 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.538 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.538 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 384 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 384 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 384 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 384 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| zielonka | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 384 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 384 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=8_infinitely_often_receive_for_all_d.gm · 3066 vertices / 3945 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3066 | 3945 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.042 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.019 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.041 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.041 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3066 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| zielonka | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3066 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABP(BW)datasize=8_invariantly_infinitely_many_reachable_taus.gm · 1138 vertices / 1735 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1138 | 1735 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.588 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.588 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.589 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.578 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1138 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1138 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1138 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1138 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1138 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1138 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1138 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1138 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=8_no_duplication_of_messages.gm · 3412 vertices / 4393 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3412 | 4393 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.449 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 3412 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3412 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=8_no_generation_of_messages.gm · 2658 vertices / 3425 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2658 | 3425 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.401 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| zielonka | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 2658 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=8_nodeadlock.gm · 380 vertices / 489 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 380 | 489 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.408 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.398 | 64.938 | even | true | true | false | - |
| zielonka | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.398 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 380 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 380 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABP(BW)datasize=8_read_then_eventually_send.gm · 3452 vertices / 4457 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3452 | 4457 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.750 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.750 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.485 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3452 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3452 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3452 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3452 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3452 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 594 vertices / 819 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 594 | 819 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.795 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.794 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.794 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.793 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.405 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 594 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 594 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 594 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.397 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 594 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.396 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 594 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.449 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 594 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 594 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 594 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 594 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.370 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_infinitely_often_lost.gm · 120 vertices / 150 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 120 | 150 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.416 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 111 / 9 | 33 / 3 | 19 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.415 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 111 / 9 | 33 / 0 | 19 / 0 | 3 / 0 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 111 / 9 | 33 / 3 | 19 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.404 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 111 / 9 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| zielonka | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 111 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 111 / 9 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 14 / 2 | 19 / 1 | 13 / 1 | 2.286 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 14 / 0 | 19 / 0 | 13 / 0 | 2.286 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 14 / 2 | 19 / 1 | 13 / 1 | 2.286 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 5 / 0 | 10 / 0 | 7 / 0 | 2.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_infinitely_often_read_write.gm · 89 vertices / 107 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 89 | 107 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.416 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.395 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.395 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.413 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 89 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 89 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_infinitely_often_receive_d1.gm · 78 vertices / 96 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 78 | 96 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.415 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 78 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 78 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 78 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 78 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_infinitely_often_receive_for_all_d.gm · 156 vertices / 193 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 156 | 193 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.439 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.439 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.438 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.425 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 156 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| zielonka | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.396 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 156 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_invariantly_infinitely_many_reachable_taus.gm · 223 vertices / 333 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 223 | 333 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.416 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 223 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 223 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 223 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 223 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 223 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 223 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 223 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.396 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 223 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.395 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 223 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.394 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=2_no_duplication_of_messages.gm · 223 vertices / 277 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 223 | 277 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 223 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 223 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=2_no_generation_of_messages.gm · 78 vertices / 95 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 78 | 95 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 78 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 78 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=2_nodeadlock.gm · 75 vertices / 93 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 75 | 93 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.408 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| zielonka | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 75 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 75 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=2_read_then_eventually_send.gm · 231 vertices / 289 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 231 | 289 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.468 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.414 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.405 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 231 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 231 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 231 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 231 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 231 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 231 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=2_read_then_eventually_send_if_fair.gm · 132 vertices / 162 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 132 | 162 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.417 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 132 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| zielonka | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 132 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 132 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 2338 vertices / 3253 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2338 | 3253 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 6.738 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 6.738 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 6.737 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 6.819 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.383 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2338 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2338 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2338 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2338 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2338 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2338 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2338 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2338 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2338 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 64.938 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 19 | 0 / 15 | 0.000 / 4.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_infinitely_often_lost.gm · 236 vertices / 298 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 236 | 298 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.476 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.475 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.412 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 219 / 17 | 33 / 3 | 19 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.401 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 219 / 17 | 33 / 0 | 19 / 0 | 3 / 0 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 219 / 17 | 33 / 3 | 19 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 219 / 17 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| zielonka | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 219 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 219 / 17 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 14 / 2 | 19 / 1 | 13 / 1 | 2.286 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 14 / 0 | 19 / 0 | 13 / 0 | 2.286 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 14 / 2 | 19 / 1 | 13 / 1 | 2.286 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 5 / 0 | 10 / 0 | 7 / 0 | 2.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_infinitely_often_read_write.gm · 173 vertices / 211 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 173 | 211 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.427 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.416 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.396 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 173 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| zielonka | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.395 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 173 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_infinitely_often_receive_d1.gm · 150 vertices / 188 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 150 | 188 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.424 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 150 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 150 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 150 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 150 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| zielonka | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 150 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 150 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_infinitely_often_receive_for_all_d.gm · 598 vertices / 753 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 598 | 753 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.856 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.855 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.853 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.853 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.384 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 598 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| zielonka | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 598 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 64.938 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/ABPdatasize=4_invariantly_infinitely_many_reachable_taus.gm · 439 vertices / 661 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 439 | 661 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.427 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.427 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.426 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 439 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 439 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 439 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 439 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 439 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 439 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 439 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 439 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 439 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=4_no_duplication_of_messages.gm · 731 vertices / 921 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 731 | 921 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.416 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.416 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.404 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.394 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.393 | 64.938 | even | true | true | false | - |
| zielonka | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 731 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 731 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |

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

