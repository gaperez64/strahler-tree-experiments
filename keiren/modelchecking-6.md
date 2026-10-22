# modelchecking, part 6

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/Pardatasize=8_nodeadlock.gm · 356 vertices / 473 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 356 | 473 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.397 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.398 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| zielonka | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=8_read_then_eventually_send.gm · 3228 vertices / 4249 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3228 | 4249 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.648 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.656 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.476 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.475 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3228 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3228 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3228 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3228 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3228 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3228 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_infinitely_often_enabled_then_infinitely_often_taken.gm · 3458 vertices / 9195 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3458 | 9195 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.454 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.476 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.472 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.496 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.400 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.472 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.412 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.412 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.371 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_infinitely_often_lost.gm · 1046 vertices / 3714 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1046 | 3714 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=10 / H=2, K=2, t=10 | 3.779 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.373 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=10 / H=2, K=2, t=10 | 3.767 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.767 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=10 / H=2, K=2, t=10 | 0.786 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 765 / 281 | 26 / 5 | 13 / 2 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.447 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 765 / 281 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 765 / 281 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.413 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 765 / 281 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.414 | 82.871 | even | true | true | false | - |
| zielonka | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.414 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 765 / 281 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.384 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 765 / 281 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_infinitely_often_read_write.gm · 937 vertices / 2017 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 937 | 2017 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.039 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.038 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.038 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.023 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.382 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.607 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.607 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.608 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.628 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.414 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 937 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| zielonka | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.450 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.398 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 937 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.383 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_infinitely_often_receive_d1.gm · 506 vertices / 1586 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 506 | 1586 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.631 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.630 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 506 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 506 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 506 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 506 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.401 | 82.871 | even | true | true | false | - |
| zielonka | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_infinitely_often_receive_for_all_d.gm · 1012 vertices / 3173 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1012 | 3173 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.365 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.365 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.365 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.371 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.401 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.400 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.413 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1012 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| zielonka | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1012 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_invariantly_infinitely_many_reachable_taus.gm · 1297 vertices / 3889 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1297 | 3889 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.631 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.631 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.630 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.629 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.422 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1297 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1297 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1297 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1297 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1297 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1297 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1297 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1297 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1297 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.380 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_no_duplication_of_messages.gm · 1370 vertices / 4714 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1370 | 4714 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.949 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.948 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.557 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.556 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 804 / 566 | 2 / 39 | 1 / 19 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.434 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.438 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 804 / 566 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.397 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 804 / 566 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.423 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 804 / 566 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 804 / 566 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.385 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 804 / 566 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_no_generation_of_messages.gm · 326 vertices / 1086 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 326 | 1086 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.410 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.398 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.397 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| zielonka | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 326 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 326 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_nodeadlock.gm · 433 vertices / 1513 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 433 | 1513 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| zielonka | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_read_then_eventually_send.gm · 1621 vertices / 5005 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1621 | 5005 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.692 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.692 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1621 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1621 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1621 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1621 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1621 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1621 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=1_read_then_eventually_send_if_fair.gm · 770 vertices / 2118 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 770 | 2118 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.598 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.590 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.495 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.495 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 770 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.388 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.398 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.456 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 770 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.395 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| zielonka | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 770 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 770 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 112514 vertices / 345315 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 112514 | 345315 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.734 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.734 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.763 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.753 | 86.012 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 112514 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.082 | 86.012 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 112514 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.281 | 86.012 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 112514 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.237 | 86.012 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 112514 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.239 | 86.012 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 112514 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.127 | 86.012 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 112514 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.125 | 86.012 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 112514 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.810 | 86.012 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 112514 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.812 | 86.012 | odd | false | true | false | - |
| zielonka | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.635 | 86.012 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.637 | 86.012 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.685 | 86.012 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 112514 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.684 | 86.012 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_infinitely_often_lost.gm · 42618 vertices / 196506 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 42618 | 196506 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 171.184 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 86.012 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 171.188 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 86.012 | even | true | true | false | - |
| lifting-adaptive | complete | 30929 / 11689 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.568 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 86.012 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 30929 / 11689 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.597 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 86.012 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 171.996 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.540 | 86.012 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 180.812 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.516 | 86.012 | even | true | true | false | - |
| pm-strahler | complete | 30929 / 11689 | 26 / 5 | 13 / 2 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 5.126 | 86.012 | even | true | true | false | - |
| pm-strahler+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.464 | 86.012 | even | true | true | false | - |
| pm-strahler+iter | complete | 30929 / 11689 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.661 | 86.012 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.495 | 86.012 | even | true | true | false | - |
| pm-succinct | complete | 30929 / 11689 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 1.946 | 86.012 | even | true | true | false | - |
| pm-succinct+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.517 | 86.012 | even | true | true | false | - |
| pm-succinct+iter | complete | 30929 / 11689 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.651 | 86.012 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.505 | 86.012 | even | true | true | false | - |
| zielonka | complete | 30929 / 11689 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.518 | 86.012 | even | true | true | false | - |
| zielonka+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 86.012 | even | true | true | false | - |
| zielonka-sym | complete | 30929 / 11689 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.560 | 86.012 | even | true | true | false | - |
| zielonka-sym+pre | complete | 30929 / 11689 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 86.012 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_infinitely_often_read_write.gm · 34673 vertices / 77633 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 34673 | 77633 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.196 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.199 | 86.012 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.250 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 1.258 | 86.012 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.793 | 86.012 | even | true | true | false | - |
| pm-strahler+pre | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.868 | 86.012 | even | true | true | false | - |
| pm-strahler+iter | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.674 | 86.012 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.675 | 86.012 | even | true | true | false | - |
| pm-succinct | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.749 | 86.012 | even | true | true | false | - |
| pm-succinct+pre | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.757 | 86.012 | even | true | true | false | - |
| pm-succinct+iter | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.582 | 86.012 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 34673 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.582 | 86.012 | even | true | true | false | - |
| zielonka | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.520 | 86.012 | even | true | true | false | - |
| zielonka+pre | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.520 | 86.012 | even | true | true | false | - |
| zielonka-sym | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.585 | 86.012 | even | true | true | false | - |
| zielonka-sym+pre | complete | 34673 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.560 | 86.012 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_infinitely_often_receive_d1.gm · 17810 vertices / 60770 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 17810 | 60770 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 86.012 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 86.012 | even | true | true | false | - |
| lifting-adaptive | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.474 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 86.012 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.539 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 86.012 | even | true | true | false | - |
| lifting-sym | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.499 | 86.012 | even | true | true | false | - |
| lifting-sym+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 86.012 | even | true | true | false | - |
| lifting-sym+iter | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.142 | 86.012 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 86.012 | even | true | true | false | - |
| pm-strahler | complete | 17810 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.649 | 86.012 | even | true | true | false | - |
| pm-strahler+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.421 | 86.012 | even | true | true | false | - |
| pm-strahler+iter | complete | 17810 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.577 | 86.012 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.423 | 86.012 | even | true | true | false | - |
| pm-succinct | complete | 17810 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.545 | 86.012 | even | true | true | false | - |
| pm-succinct+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.426 | 86.012 | even | true | true | false | - |
| pm-succinct+iter | complete | 17810 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.546 | 86.012 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.421 | 86.012 | even | true | true | false | - |
| zielonka | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 86.012 | even | true | true | false | - |
| zielonka+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 86.012 | even | true | true | false | - |
| zielonka-sym | complete | 17810 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.430 | 86.012 | even | true | true | false | - |
| zielonka-sym+pre | complete | 17810 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 86.012 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_infinitely_often_receive_for_all_d.gm · 35620 vertices / 121541 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 35620 | 121541 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.485 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.486 | 86.012 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.493 | 86.012 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.504 | 86.012 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.996 | 86.012 | even | true | true | false | - |
| pm-strahler | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.987 | 86.012 | even | true | true | false | - |
| pm-strahler+pre | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.089 | 86.012 | even | true | true | false | - |
| pm-strahler+iter | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.936 | 86.012 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.966 | 86.012 | even | true | true | false | - |
| pm-succinct | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.881 | 86.012 | even | true | true | false | - |
| pm-succinct+pre | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.892 | 86.012 | even | true | true | false | - |
| pm-succinct+iter | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.841 | 86.012 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 35620 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.840 | 86.012 | even | true | true | false | - |
| zielonka | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.540 | 86.012 | even | true | true | false | - |
| zielonka+pre | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.530 | 86.012 | even | true | true | false | - |
| zielonka-sym | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.542 | 86.012 | even | true | true | false | - |
| zielonka-sym+pre | complete | 35620 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.554 | 86.012 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_invariantly_infinitely_many_reachable_taus.gm · 42193 vertices / 142177 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 42193 | 142177 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.496 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.496 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.506 | 86.012 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.505 | 86.012 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.012 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 86.012 | - | false | - | - | metrics: deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.645 | 86.012 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 42193 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.536 | 86.012 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 42193 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.578 | 86.012 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 42193 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.548 | 86.012 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 42193 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.572 | 86.012 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 42193 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.694 | 86.012 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 42193 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.705 | 86.012 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 42193 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.591 | 86.012 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 42193 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.592 | 86.012 | odd | false | true | false | - |
| zielonka | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.529 | 86.012 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.542 | 86.012 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.552 | 86.012 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 42193 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.551 | 86.012 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_no_duplication_of_messages.gm · 54322 vertices / 203914 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 54322 | 203914 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.500 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 86.500 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.500 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 86.500 | odd | false | true | false | - |
| lifting-adaptive | complete | 19856 / 34466 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.644 | 86.500 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.548 | 86.500 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 19856 / 34466 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.704 | 86.500 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.570 | 86.500 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.500 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.512 | 86.500 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.500 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.516 | 86.500 | odd | false | true | false | - |
| pm-strahler | complete | 19856 / 34466 | 2 / 39 | 1 / 19 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.332 | 86.500 | odd | false | true | false | - |
| pm-strahler+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.517 | 86.500 | odd | false | true | false | - |
| pm-strahler+iter | complete | 19856 / 34466 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.547 | 86.500 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.517 | 86.500 | odd | false | true | false | - |
| pm-succinct | complete | 19856 / 34466 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.775 | 86.500 | odd | false | true | false | - |
| pm-succinct+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.506 | 86.500 | odd | false | true | false | - |
| pm-succinct+iter | complete | 19856 / 34466 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.547 | 86.500 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.527 | 86.500 | odd | false | true | false | - |
| zielonka | complete | 19856 / 34466 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.527 | 86.500 | odd | false | true | false | - |
| zielonka+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 86.500 | odd | false | true | false | - |
| zielonka-sym | complete | 19856 / 34466 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.559 | 86.500 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 19856 / 34466 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 86.500 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_no_generation_of_messages.gm · 3949 vertices / 15256 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3949 | 15256 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 86.500 | even | true | true | false | - |
| lifting+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 86.500 | even | true | true | false | - |
| lifting+iter | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.415 | 86.500 | even | true | true | false | - |
| lifting+pre+iter | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 86.500 | even | true | true | false | - |
| lifting-adaptive | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 86.500 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 86.500 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 86.500 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 86.500 | even | true | true | false | - |
| lifting-sym | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 86.500 | even | true | true | false | - |
| lifting-sym+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 86.500 | even | true | true | false | - |
| lifting-sym+iter | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.415 | 86.500 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 86.500 | even | true | true | false | - |
| pm-strahler | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 86.500 | even | true | true | false | - |
| pm-strahler+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 86.500 | even | true | true | false | - |
| pm-strahler+iter | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 86.500 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 86.500 | even | true | true | false | - |
| pm-succinct | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.414 | 86.500 | even | true | true | false | - |
| pm-succinct+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.414 | 86.500 | even | true | true | false | - |
| pm-succinct+iter | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 86.500 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.415 | 86.500 | even | true | true | false | - |
| zielonka | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 86.500 | even | true | true | false | - |
| zielonka+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 86.500 | even | true | true | false | - |
| zielonka-sym | complete | 3949 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 86.500 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3949 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 86.500 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_nodeadlock.gm · 14065 vertices / 57025 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14065 | 57025 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.427 | 86.500 | even | true | true | false | - |
| lifting+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 86.500 | even | true | true | false | - |
| lifting+iter | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.436 | 86.500 | even | true | true | false | - |
| lifting+pre+iter | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 86.500 | even | true | true | false | - |
| lifting-adaptive | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.413 | 86.500 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 86.500 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.433 | 86.500 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 86.500 | even | true | true | false | - |
| lifting-sym | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.414 | 86.500 | even | true | true | false | - |
| lifting-sym+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 86.500 | even | true | true | false | - |
| lifting-sym+iter | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.423 | 86.500 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 86.500 | even | true | true | false | - |
| pm-strahler | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.435 | 86.500 | even | true | true | false | - |
| pm-strahler+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.414 | 86.500 | even | true | true | false | - |
| pm-strahler+iter | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.426 | 86.500 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.413 | 86.500 | even | true | true | false | - |
| pm-succinct | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.432 | 86.500 | even | true | true | false | - |
| pm-succinct+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.411 | 86.500 | even | true | true | false | - |
| pm-succinct+iter | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.433 | 86.500 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.424 | 86.500 | even | true | true | false | - |
| zielonka | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.414 | 86.500 | even | true | true | false | - |
| zielonka+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 86.500 | even | true | true | false | - |
| zielonka-sym | complete | 14065 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 86.500 | even | true | true | false | - |
| zielonka-sym+pre | complete | 14065 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 86.500 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_read_then_eventually_send.gm · 56241 vertices / 192609 edges · 21 complete · 3 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 56241 | 192609 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 86.867 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 86.867 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.867 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 86.867 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 56241 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.578 | 86.867 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.548 | 86.867 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 56241 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.650 | 86.867 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.618 | 86.867 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 86.867 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 86.867 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 56241 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 21.541 | 86.867 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.527 | 86.867 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 56241 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.766 | 86.867 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.572 | 86.867 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 56241 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.602 | 86.867 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.538 | 86.867 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 56241 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.723 | 86.867 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.517 | 86.867 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 56241 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.568 | 86.867 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.527 | 86.867 | odd | false | true | false | - |
| zielonka | complete | 0 / 56241 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.518 | 86.867 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 86.867 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 56241 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.547 | 86.867 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 56241 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 86.867 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=2_read_then_eventually_send_if_fair.gm · 32402 vertices / 95314 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 32402 | 95314 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.867 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 86.867 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.867 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 86.867 | even | true | true | false | - |
| lifting-adaptive | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.525 | 86.867 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.509 | 86.867 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.591 | 86.867 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.529 | 86.867 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.867 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 86.867 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 86.867 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 86.867 | even | true | true | false | - |
| pm-strahler | complete | 32402 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.216 | 86.867 | even | true | true | false | - |
| pm-strahler+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.464 | 86.867 | even | true | true | false | - |
| pm-strahler+iter | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.453 | 86.867 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.442 | 86.867 | even | true | true | false | - |
| pm-succinct | complete | 32402 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.689 | 86.867 | even | true | true | false | - |
| pm-succinct+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.455 | 86.867 | even | true | true | false | - |
| pm-succinct+iter | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.484 | 86.867 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.454 | 86.867 | even | true | true | false | - |
| zielonka | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.457 | 86.867 | even | true | true | false | - |
| zielonka+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 86.867 | even | true | true | false | - |
| zielonka-sym | complete | 32402 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.485 | 86.867 | even | true | true | false | - |
| zielonka-sym+pre | complete | 32402 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 86.867 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_infinitely_often_enabled_then_infinitely_often_taken.gm · 1787138 vertices / 5852835 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1787138 | 5852835 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.055 | 633.461 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.055 | 633.449 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.056 | 633.523 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.053 | 633.570 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 6.510 | 633.438 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 6.540 | 633.449 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 7.196 | 633.570 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 7.144 | 633.453 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 633.570 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.055 | 633.316 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.052 | 633.445 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.051 | 633.449 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.045 | 633.531 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.043 | 633.465 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 0 / 1787138 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 12.920 | 633.531 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 1787138 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 12.919 | 633.398 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 1787138 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 11.346 | 633.465 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 1787138 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 11.367 | 633.328 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 1787138 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.171 | 633.449 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 1787138 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 6.280 | 633.262 | odd | - | - | false | - |
| zielonka | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.212 | 633.523 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.243 | 633.586 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.996 | 633.586 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 1787138 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.985 | 633.457 | odd | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_infinitely_often_lost.gm · 742970 vertices / 3925130 edges · 18 complete · 2 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 742970 | 3925130 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.120 | 1579.680 | - | - | - | - | Solver failed: failed to build the Even host U^3_{19,3} |
| lifting+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.923 | 354.844 | even | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.120 | 1579.762 | - | - | - | - | Solver failed: failed to build the Even host U^3_{19,3} |
| lifting+pre+iter | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.877 | 354.824 | even | - | - | false | - |
| lifting-adaptive | complete | 535009 / 207961 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 3.985 | 354.637 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.868 | 354.844 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 535009 / 207961 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 4.161 | 354.777 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.849 | 354.844 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.968 | 1579.578 | - | - | - | - | Solver failed: failed to build the Even host U^3_{19,3} |
| lifting-sym+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.824 | 354.777 | even | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.968 | 1579.797 | - | - | - | - | Solver failed: failed to build the Even host U^3_{19,3} |
| lifting-sym+pre+iter | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.874 | 354.770 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 354.656 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 2.090 | 354.516 | even | - | - | false | - |
| pm-strahler+iter | complete | 535009 / 207961 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 6.326 | 354.664 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 1.911 | 354.590 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 354.703 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.921 | 354.703 | even | - | - | false | - |
| pm-succinct+iter | complete | 535009 / 207961 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 5.313 | 354.660 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.921 | 354.785 | even | - | - | false | - |
| zielonka | complete | 535009 / 207961 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 1.938 | 354.707 | even | - | - | false | - |
| zielonka+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.746 | 354.820 | even | - | - | false | - |
| zielonka-sym | complete | 535009 / 207961 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 2.641 | 354.715 | even | - | - | false | - |
| zielonka-sym+pre | complete | 535009 / 207961 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.734 | 354.715 | even | - | - | false | - |

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
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 3 | 3 / 2 | 2 / 2 | 1.667 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_infinitely_often_read_write.gm · 576385 vertices / 1317505 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 576385 | 1317505 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 173.766 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 173.762 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 173.770 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 174.348 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 22.936 | 173.152 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 22.935 | 173.082 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 23.442 | 173.148 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 23.442 | 173.027 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 174.090 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 173.770 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 173.770 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 174.273 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 24.757 | 173.082 | even | - | - | false | - |
| pm-strahler+pre | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 24.706 | 173.086 | even | - | - | false | - |
| pm-strahler+iter | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.690 | 172.941 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.959 | 173.027 | even | - | - | false | - |
| pm-succinct | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 13.554 | 173.094 | even | - | - | false | - |
| pm-succinct+pre | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 13.616 | 172.820 | even | - | - | false | - |
| pm-succinct+iter | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 5.431 | 173.027 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 576385 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 5.545 | 173.094 | even | - | - | false | - |
| zielonka | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | — / — | 1.243 | 173.148 | even | - | - | false | - |
| zielonka+pre | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | — / — | 1.253 | 173.008 | even | - | - | false | - |
| zielonka-sym | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | — / — | 1.917 | 173.020 | even | - | - | false | - |
| zielonka-sym+pre | complete | 576385 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | — / — | 1.929 | 173.148 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_infinitely_often_receive_d1.gm · 294434 vertices / 1035554 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 294434 | 1035554 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 107.652 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.851 | 107.586 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 107.496 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.835 | 107.699 | even | - | - | false | - |
| lifting-adaptive | complete | 294434 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.398 | 107.734 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.964 | 107.578 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 294434 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.471 | 107.645 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.968 | 107.699 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 107.531 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.915 | 107.676 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 107.445 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.889 | 107.590 | even | - | - | false | - |
| pm-strahler | complete | 294434 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 7.088 | 107.461 | even | - | - | false | - |
| pm-strahler+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.975 | 107.660 | even | - | - | false | - |
| pm-strahler+iter | complete | 294434 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.849 | 107.582 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.962 | 107.664 | even | - | - | false | - |
| pm-succinct | complete | 294434 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.108 | 107.598 | even | - | - | false | - |
| pm-succinct+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.965 | 107.664 | even | - | - | false | - |
| pm-succinct+iter | complete | 294434 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 3.950 | 107.535 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.963 | 107.660 | even | - | - | false | - |
| zielonka | complete | 294434 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.879 | 107.652 | even | - | - | false | - |
| zielonka+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.881 | 107.578 | even | - | - | false | - |
| zielonka-sym | complete | 294434 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.017 | 107.715 | even | - | - | false | - |
| zielonka-sym+pre | complete | 294434 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.868 | 107.715 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_infinitely_often_receive_for_all_d.gm · 588868 vertices / 2071109 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 588868 | 2071109 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 214.000 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 213.824 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 213.957 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 214.016 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.218 | 213.848 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.260 | 213.871 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.310 | 213.883 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.342 | 213.957 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 213.742 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 213.891 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 213.879 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 213.934 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 14.327 | 213.668 | even | - | - | false | - |
| pm-strahler+pre | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 14.494 | 213.883 | even | - | - | false | - |
| pm-strahler+iter | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.803 | 213.922 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.558 | 213.832 | even | - | - | false | - |
| pm-succinct | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.029 | 213.883 | even | - | - | false | - |
| pm-succinct+pre | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.143 | 213.762 | even | - | - | false | - |
| pm-succinct+iter | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.881 | 213.965 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 588868 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 6.819 | 213.832 | even | - | - | false | - |
| zielonka | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.275 | 213.891 | even | - | - | false | - |
| zielonka+pre | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.278 | 213.996 | even | - | - | false | - |
| zielonka-sym | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.476 | 213.949 | even | - | - | false | - |
| zielonka-sym+pre | complete | 588868 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.465 | 213.879 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_invariantly_infinitely_many_reachable_taus.gm · 670177 vertices / 2375809 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 670177 | 2375809 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 245.051 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 245.176 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 245.195 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 245.195 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.152 | 244.922 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.173 | 245.008 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.254 | 245.062 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.282 | 245.062 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 245.066 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 245.070 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 245.199 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 245.176 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 670177 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 3.223 | 245.074 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 670177 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 3.480 | 245.074 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 670177 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.039 | 245.082 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 670177 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.055 | 244.941 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 670177 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 4.683 | 245.016 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 670177 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 4.716 | 245.141 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 670177 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.735 | 244.875 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 670177 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.745 | 245.008 | odd | - | - | false | - |
| zielonka | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.473 | 245.125 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.506 | 245.195 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.791 | 245.066 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 670177 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.810 | 245.199 | odd | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_no_duplication_of_messages.gm · 944090 vertices / 3685946 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 944090 | 3685946 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 367.566 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.888 | 367.504 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 367.430 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.852 | 367.492 | odd | - | - | false | - |
| lifting-adaptive | complete | 220872 / 723218 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.695 | 367.430 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.009 | 367.562 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 220872 / 723218 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.981 | 367.504 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.011 | 367.543 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 367.543 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.941 | 367.434 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 367.438 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.930 | 367.426 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 367.438 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.098 | 367.512 | odd | - | - | false | - |
| pm-strahler+iter | complete | 220872 / 723218 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.633 | 367.359 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.063 | 367.238 | odd | - | - | false | - |
| pm-succinct | complete | 220872 / 723218 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 22.714 | 367.438 | odd | - | - | false | - |
| pm-succinct+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.958 | 367.445 | odd | - | - | false | - |
| pm-succinct+iter | complete | 220872 / 723218 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.957 | 367.441 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.938 | 367.508 | odd | - | - | false | - |
| zielonka | complete | 220872 / 723218 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.906 | 367.438 | odd | - | - | false | - |
| zielonka+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.739 | 367.289 | odd | - | - | false | - |
| zielonka-sym | complete | 220872 / 723218 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.579 | 367.352 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 220872 / 723218 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.770 | 367.430 | odd | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_no_generation_of_messages.gm · 22873 vertices / 94230 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22873 | 94230 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.446 | 87.828 | even | true | true | false | - |
| lifting+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.428 | 87.828 | even | true | true | false | - |
| lifting+iter | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.439 | 87.828 | even | true | true | false | - |
| lifting+pre+iter | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 87.828 | even | true | true | false | - |
| lifting-adaptive | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.434 | 87.828 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 87.828 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.433 | 87.828 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 87.828 | even | true | true | false | - |
| lifting-sym | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.443 | 87.828 | even | true | true | false | - |
| lifting-sym+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 87.828 | even | true | true | false | - |
| lifting-sym+iter | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.445 | 87.828 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 87.828 | even | true | true | false | - |
| pm-strahler | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.445 | 87.828 | even | true | true | false | - |
| pm-strahler+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.424 | 87.828 | even | true | true | false | - |
| pm-strahler+iter | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.433 | 87.828 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.423 | 87.828 | even | true | true | false | - |
| pm-succinct | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.454 | 87.828 | even | true | true | false | - |
| pm-succinct+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.422 | 87.828 | even | true | true | false | - |
| pm-succinct+iter | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.445 | 87.828 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.424 | 87.828 | even | true | true | false | - |
| zielonka | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 87.828 | even | true | true | false | - |
| zielonka+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 87.828 | even | true | true | false | - |
| zielonka-sym | complete | 22873 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.432 | 87.828 | even | true | true | false | - |
| zielonka-sym+pre | complete | 22873 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 87.828 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_nodeadlock.gm · 223393 vertices / 964513 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 223393 | 964513 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.851 | 90.629 | even | true | true | false | - |
| lifting+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.715 | 90.832 | even | true | true | false | - |
| lifting+iter | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.850 | 90.812 | even | true | true | false | - |
| lifting+pre+iter | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.694 | 90.902 | even | true | true | false | - |
| lifting-adaptive | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.825 | 90.969 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.701 | 90.766 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.826 | 90.883 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.695 | 90.773 | even | true | true | false | - |
| lifting-sym | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.797 | 90.719 | even | true | true | false | - |
| lifting-sym+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 90.777 | even | true | true | false | - |
| lifting-sym+iter | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.826 | 90.773 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 90.875 | even | true | true | false | - |
| pm-strahler | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.858 | 90.930 | even | true | true | false | - |
| pm-strahler+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.751 | 90.848 | even | true | true | false | - |
| pm-strahler+iter | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.815 | 90.766 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.734 | 90.848 | even | true | true | false | - |
| pm-succinct | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.034 | 90.848 | even | true | true | false | - |
| pm-succinct+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.744 | 90.848 | even | true | true | false | - |
| pm-succinct+iter | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.824 | 90.785 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.741 | 90.777 | even | true | true | false | - |
| zielonka | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.710 | 90.633 | even | true | true | false | - |
| zielonka+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 90.832 | even | true | true | false | - |
| zielonka-sym | complete | 223393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.765 | 90.770 | even | true | true | false | - |
| zielonka-sym+pre | complete | 223393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 90.902 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_read_then_eventually_send.gm · 917713 vertices / 3283153 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 917713 | 3283153 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 341.223 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.788 | 341.223 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 341.285 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.771 | 341.289 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 917713 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.182 | 341.102 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.919 | 341.160 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 917713 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.413 | 341.160 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.930 | 341.156 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 341.266 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.854 | 341.270 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 341.102 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.845 | 341.223 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 917713 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.730 | 341.148 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.187 | 341.160 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 917713 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.642 | 341.086 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.102 | 341.105 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 917713 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 6.464 | 341.230 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.087 | 341.152 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 917713 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.986 | 341.098 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.087 | 341.230 | odd | false | true | false | - |
| zielonka | complete | 0 / 917713 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.964 | 341.148 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.850 | 341.289 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 917713 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.349 | 341.012 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 917713 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.771 | 341.285 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=3_read_then_eventually_send_if_fair.gm · 586658 vertices / 1782434 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 586658 | 1782434 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 204.422 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.194 | 203.516 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 204.453 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.147 | 203.348 | even | - | - | false | - |
| lifting-adaptive | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.713 | 203.520 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.283 | 203.410 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.958 | 203.535 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.313 | 203.406 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 204.273 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.277 | 203.465 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 204.340 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.210 | 203.402 | even | - | - | false | - |
| pm-strahler | complete | 586658 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 20.027 | 203.480 | even | - | - | false | - |
| pm-strahler+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.345 | 203.480 | even | - | - | false | - |
| pm-strahler+iter | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.843 | 203.414 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.395 | 203.359 | even | - | - | false | - |
| pm-succinct | complete | 586658 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.133 | 203.129 | even | - | - | false | - |
| pm-succinct+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.399 | 203.348 | even | - | - | false | - |
| pm-succinct+iter | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 2.056 | 203.398 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.376 | 203.418 | even | - | - | false | - |
| zielonka | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.256 | 203.262 | even | - | - | false | - |
| zielonka+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.215 | 203.535 | even | - | - | false | - |
| zielonka-sym | complete | 586658 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.655 | 203.539 | even | - | - | false | - |
| zielonka-sym+pre | complete | 586658 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.239 | 203.535 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 20712450 vertices / 70290691 edges · 6 timeout · 18 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20712450 | 70290691 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.769 | 1708.984 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.768 | 1701.844 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.769 | 1704.605 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.090 | 362.359 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.296 | 356.602 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.332 | 360.598 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.727 | 1743.234 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.511 | 1741.980 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 16.300 | 1744.723 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.135 | 682.730 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.092 | 678.602 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.055 | 685.090 | - | - | - | - | deadline exceeded |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 10.826 | 1406.180 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.633 | 1410.223 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.696 | 1392.973 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.464 | 1679.164 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 7.434 | 1679.797 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.320 | 1679.738 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.586 | 1707.230 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.584 | 1706.680 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 25.484 | 1713.691 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 24.025 | 1758.301 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 23.996 | 1760.211 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 23.975 | 1755.355 | - | - | - | - | 4194304:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_lost.gm · 8964338 vertices / 51952370 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8964338 | 51952370 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.572 | 1504.844 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.653 | 1504.500 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.681 | 1504.754 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.335 | 1504.734 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 9.254 | 1504.598 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.225 | 1504.520 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.571 | 1504.859 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.559 | 1504.586 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.528 | 1504.723 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.479 | 1504.840 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.511 | 1504.727 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.518 | 1504.672 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.809 | 1504.598 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.759 | 1504.734 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.696 | 1504.805 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.649 | 1504.609 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.607 | 1504.734 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.596 | 1504.742 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.773 | 1504.723 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.763 | 1504.805 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.584 | 1504.797 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.399 | 1504.719 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.426 | 1504.859 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.436 | 1504.859 | - | - | - | - | 4194304:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_read_write.gm · 6823297 vertices / 15799809 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6823297 | 15799809 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.467 | 1620.141 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.599 | 1620.363 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.588 | 1620.035 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.241 | 1620.238 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 5.305 | 1620.176 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.285 | 1620.234 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.239 | 1620.246 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.303 | 1620.230 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.323 | 1620.238 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.145 | 1620.312 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.290 | 1620.258 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.260 | 1620.301 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 5.033 | 1620.168 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.279 | 1620.113 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.279 | 1620.180 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.966 | 1620.250 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.183 | 1620.246 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.195 | 1620.184 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.806 | 1620.188 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.055 | 1620.184 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.032 | 1620.293 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.563 | 1620.207 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.807 | 1620.090 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.847 | 1620.289 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_receive_d1.gm · 3487362 vertices / 12463874 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3487362 | 12463874 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.086 | 1289.895 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.763 | 1289.832 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.088 | 1289.609 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.998 | 1289.895 | even | - | - | false | - |
| lifting-adaptive | complete | 3487362 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 13.517 | 1289.777 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.418 | 1289.773 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 3487362 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 12.758 | 1289.660 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.479 | 1289.785 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1289.852 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.299 | 1289.898 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.076 | 1289.855 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.866 | 1289.918 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 1289.793 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 8.142 | 1289.672 | even | - | - | false | - |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.064 | 1289.816 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 7.437 | 1289.863 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 1289.734 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 7.388 | 1289.789 | even | - | - | false | - |
| pm-succinct+iter | complete | 3487362 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 29.049 | 1289.746 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 7.522 | 1289.660 | even | - | - | false | - |
| zielonka | complete | 3487362 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 6.010 | 1289.895 | even | - | - | false | - |
| zielonka+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.321 | 1289.789 | even | - | - | false | - |
| zielonka-sym | complete | 3487362 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.222 | 1289.918 | even | - | - | false | - |
| zielonka-sym+pre | complete | 3487362 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.076 | 1289.785 | even | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_receive_for_all_d.gm · 6974724 vertices / 24927749 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6974724 | 24927749 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.978 | 1690.715 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.957 | 1690.594 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.926 | 1690.594 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.142 | 1690.484 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 13.109 | 1690.523 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.088 | 1690.473 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.182 | 1690.734 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.182 | 1690.609 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.149 | 1690.480 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.681 | 1690.254 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.641 | 1690.527 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.628 | 1690.383 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.255 | 1690.359 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.407 | 1690.492 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.254 | 1690.359 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.059 | 1689.469 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 10.977 | 1689.734 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.865 | 1689.801 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.554 | 1690.297 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.564 | 1689.914 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 7.409 | 1690.484 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.955 | 1690.480 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.882 | 1690.578 | - | - | - | - | 6604441:13: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.830 | 1690.344 | - | - | - | - | 6604441:13: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_invariantly_infinitely_many_reachable_taus.gm · 7767169 vertices / 28309249 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7767169 | 28309249 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.181 | 1720.633 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.201 | 1720.883 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.211 | 1720.586 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 23.392 | 1720.727 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 23.363 | 1720.742 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 23.334 | 1720.723 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.226 | 1720.602 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.186 | 1720.664 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.199 | 1720.672 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.471 | 1695.465 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.428 | 1694.480 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.377 | 1696.648 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.995 | 1720.867 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.974 | 1720.797 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.954 | 1720.922 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 17.191 | 1720.730 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 17.160 | 1720.719 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 18.062 | 1720.605 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.745 | 1720.805 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.725 | 1720.859 | - | - | - | - | 6530113:31: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 25.863 | 1720.672 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 21.000 | 1717.035 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 21.020 | 1717.609 | - | - | - | - | 6529269:13: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 21.047 | 1717.855 | - | - | - | - | 6529269:13: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_no_duplication_of_messages.gm · 11488274 vertices / 45840722 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11488274 | 45840722 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.774 | 1509.043 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.637 | 1508.961 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.802 | 1508.977 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 15.891 | 1508.980 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 15.779 | 1508.922 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 15.664 | 1508.844 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.309 | 1509.047 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.278 | 1509.047 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.243 | 1509.109 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.410 | 1509.102 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.358 | 1509.109 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.380 | 1509.039 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 5.521 | 1508.855 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.488 | 1508.848 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.488 | 1508.973 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.796 | 1509.055 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.796 | 1508.762 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.795 | 1509.055 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.850 | 1508.973 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.850 | 1508.930 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 5.808 | 1508.852 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.159 | 1509.164 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.138 | 1509.109 | - | - | - | - | 4194304:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.117 | 1509.109 | - | - | - | - | 4194304:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_no_generation_of_messages.gm · 94710 vertices / 404736 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 94710 | 404736 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.602 | 88.344 | even | - | - | false | - |
| lifting+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.540 | 88.344 | even | - | - | false | - |
| lifting+iter | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.603 | 88.344 | even | - | - | false | - |
| lifting+pre+iter | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 88.344 | even | - | - | false | - |
| lifting-adaptive | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.571 | 88.344 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 88.344 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.591 | 88.344 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.528 | 88.344 | even | - | - | false | - |
| lifting-sym | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.569 | 88.344 | even | - | - | false | - |
| lifting-sym+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 88.344 | even | - | - | false | - |
| lifting-sym+iter | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.579 | 88.344 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 88.344 | even | - | - | false | - |
| pm-strahler | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.682 | 88.344 | even | - | - | false | - |
| pm-strahler+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.546 | 88.344 | even | - | - | false | - |
| pm-strahler+iter | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.566 | 88.344 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.538 | 88.344 | even | - | - | false | - |
| pm-succinct | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.649 | 88.344 | even | - | - | false | - |
| pm-succinct+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.536 | 88.344 | even | - | - | false | - |
| pm-succinct+iter | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.567 | 88.344 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.536 | 88.344 | even | - | - | false | - |
| zielonka | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.527 | 88.344 | even | - | - | false | - |
| zielonka+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.516 | 88.344 | even | - | - | false | - |
| zielonka-sym | complete | 94710 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.558 | 88.344 | even | - | - | false | - |
| zielonka-sym+pre | complete | 94710 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 88.344 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_nodeadlock.gm · 2589057 vertices / 11565569 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2589057 | 11565569 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=21 / H=1, K=1, t=21 | 6.308 | 1076.148 | even | - | - | false | - |
| lifting+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.690 | 1076.438 | even | - | - | false | - |
| lifting+iter | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=21 / H=1, K=1, t=21 | 6.533 | 1076.430 | even | - | - | false | - |
| lifting+pre+iter | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.200 | 1076.305 | even | - | - | false | - |
| lifting-adaptive | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 5.981 | 1076.520 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.225 | 1076.570 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 6.161 | 1076.590 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.240 | 1076.453 | even | - | - | false | - |
| lifting-sym | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=21 / H=1, K=1, t=21 | 5.803 | 1076.465 | even | - | - | false | - |
| lifting-sym+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.290 | 1076.586 | even | - | - | false | - |
| lifting-sym+iter | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=21 / H=1, K=1, t=21 | 6.058 | 1076.590 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.285 | 1076.355 | even | - | - | false | - |
| pm-strahler | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 6.978 | 1076.430 | even | - | - | false | - |
| pm-strahler+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 5.270 | 1076.336 | even | - | - | false | - |
| pm-strahler+iter | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 6.334 | 1076.531 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 5.187 | 1076.535 | even | - | - | false | - |
| pm-succinct | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 9.104 | 1076.449 | even | - | - | false | - |
| pm-succinct+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 5.137 | 1076.531 | even | - | - | false | - |
| pm-succinct+iter | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 6.279 | 1076.531 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 5.130 | 1076.398 | even | - | - | false | - |
| zielonka | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 4.425 | 1076.352 | even | - | - | false | - |
| zielonka+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.243 | 1076.461 | even | - | - | false | - |
| zielonka-sym | complete | 2589057 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.253 | 1076.344 | even | - | - | false | - |
| zielonka-sym+pre | complete | 2589057 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.272 | 1076.465 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_read_then_eventually_send.gm · 10782593 vertices / 39508737 edges · 3 timeout · 21 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10782593 | 39508737 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.447 | 1749.289 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.389 | 1759.797 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.467 | 1740.422 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.559 | 224.598 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 229.219 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.853 | 228.730 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 12.431 | 1644.984 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 12.000 | 1670.984 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.515 | 1714.594 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 30.220 | 1788.855 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 30.158 | 1803.473 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 30.107 | 1807.480 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 22.505 | 1764.414 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 22.504 | 1782.234 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.503 | 1814.180 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.326 | 1797.922 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 28.326 | 1793.152 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.325 | 1796.117 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.862 | 1774.234 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.769 | 1787.422 | - | - | - | - | 6608594:13: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 28.831 | 1787.105 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 25.265 | 1782.691 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 25.203 | 1781.984 | - | - | - | - | 6607807:31: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 25.172 | 1770.109 | - | - | - | - | 6607807:31: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_read_then_eventually_send_if_fair.gm · 7310722 vertices / 22667778 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7310722 | 22667778 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.329 | 1667.297 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.237 | 1665.230 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.278 | 1667.359 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 22.833 | 1685.219 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 22.763 | 1685.219 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 22.711 | 1685.102 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.348 | 1684.594 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.343 | 1684.727 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 11.318 | 1684.770 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 26.680 | 1663.543 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.706 | 1663.973 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 25.696 | 1662.609 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 16.497 | 1685.484 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 16.475 | 1685.430 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 16.477 | 1685.305 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.297 | 1685.430 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 13.316 | 1685.348 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.327 | 1685.297 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.029 | 1685.422 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.028 | 1685.363 | - | - | - | - | 6771801:31: failed to allocate the successor list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 12.926 | 1685.234 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.261 | 1685.223 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.189 | 1685.102 | - | - | - | - | 6770377:13: failed to allocate the successor list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.168 | 1685.105 | - | - | - | - | 6770377:13: failed to allocate the successor list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_infinitely_often_enabled_then_infinitely_often_taken.gm · 21506 vertices / 58405 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 21506 | 58405 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 88.344 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 88.344 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 88.344 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 88.344 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.458 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.453 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.453 | 88.344 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.576 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.543 | 88.344 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.033 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.093 | 88.344 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 21506 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.654 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 21506 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.627 | 88.344 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 21506 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.495 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 21506 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.494 | 88.344 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 21506 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.484 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 21506 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.483 | 88.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 21506 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.442 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 21506 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.443 | 88.344 | odd | false | true | false | - |
| zielonka | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.422 | 88.344 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.421 | 88.344 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.431 | 88.344 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 21506 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.411 | 88.344 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_infinitely_often_lost.gm · 3530 vertices / 13266 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3530 | 13266 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 25.108 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 25.128 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 2.597 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 2.616 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 2585 / 945 | 26 / 5 | 13 / 2 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.577 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.427 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 2585 / 945 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.409 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.392 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 2585 / 945 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.445 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.372 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 2585 / 945 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.393 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.371 | 88.344 | even | true | true | false | - |
| zielonka | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.382 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 2585 / 945 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.383 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2585 / 945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | even | true | true | false | - |

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

