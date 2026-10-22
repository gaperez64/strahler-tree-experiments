# modelchecking, part 2

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/ABPdatasize=4_no_generation_of_messages.gm · 442 vertices / 557 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 442 | 557 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.407 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 64.938 | even | true | true | false | - |
| zielonka | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 442 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 442 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=4_nodeadlock.gm · 147 vertices / 185 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 147 | 185 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.397 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.441 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.391 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 64.938 | even | true | true | false | - |
| zielonka | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 147 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 147 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=4_read_then_eventually_send.gm · 747 vertices / 945 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 747 | 945 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.467 | 64.938 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 64.938 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.467 | 64.938 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.401 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 747 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 747 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 747 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.390 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 747 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 747 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.394 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 747 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=4_read_then_eventually_send_if_fair.gm · 260 vertices / 322 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 260 | 322 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.436 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.414 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.434 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 260 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 64.938 | even | true | true | false | - |
| zielonka | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| zielonka+pre | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| zielonka-sym | complete | 260 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| zielonka-sym+pre | complete | 260 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_infinitely_often_enabled_then_infinitely_often_taken.gm · 9282 vertices / 12969 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9282 | 12969 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 64.938 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 64.938 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 64.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.414 | 64.938 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.558 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.556 | 64.938 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.539 | 64.938 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.574 | 64.938 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 9282 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.434 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 9282 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.442 | 64.938 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 9282 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.430 | 64.938 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 9282 | 0 / 25 | 0 / 19 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.432 | 64.938 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 9282 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.410 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 9282 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 64.938 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 9282 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 64.938 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 9282 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.423 | 64.938 | odd | false | true | false | - |
| zielonka | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.400 | 64.938 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 9282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 64.938 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_infinitely_often_lost.gm · 468 vertices / 594 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 468 | 594 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.701 | 64.938 | even | true | true | false | - |
| lifting+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 64.938 | even | true | true | false | - |
| lifting+iter | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.701 | 64.938 | even | true | true | false | - |
| lifting+pre+iter | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 64.938 | even | true | true | false | - |
| lifting-adaptive | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 64.938 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 64.938 | even | true | true | false | - |
| lifting-sym | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.423 | 64.938 | even | true | true | false | - |
| lifting-sym+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| lifting-sym+iter | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.423 | 64.938 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler | complete | 435 / 33 | 33 / 3 | 19 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-strahler+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+iter | complete | 435 / 33 | 33 / 0 | 19 / 0 | 3 / 0 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.393 | 64.938 | even | true | true | false | - |
| pm-succinct | complete | 435 / 33 | 33 / 3 | 19 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.403 | 64.938 | even | true | true | false | - |
| pm-succinct+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.414 | 64.938 | even | true | true | false | - |
| pm-succinct+iter | complete | 435 / 33 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.392 | 64.938 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.405 | 64.941 | even | true | true | false | - |
| zielonka | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.405 | 64.941 | even | true | true | false | - |
| zielonka+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 64.941 | even | true | true | false | - |
| zielonka-sym | complete | 435 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.382 | 64.941 | even | true | true | false | - |
| zielonka-sym+pre | complete | 435 / 33 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 64.941 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_infinitely_often_read_write.gm · 341 vertices / 419 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 341 | 419 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.478 | 64.941 | even | true | true | false | - |
| lifting+pre | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.480 | 64.941 | even | true | true | false | - |
| lifting+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.479 | 64.941 | even | true | true | false | - |
| lifting+pre+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.464 | 64.941 | even | true | true | false | - |
| lifting-adaptive | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 64.941 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.391 | 64.941 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 64.941 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 64.941 | even | true | true | false | - |
| lifting-sym | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.433 | 64.941 | even | true | true | false | - |
| lifting-sym+pre | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.434 | 64.941 | even | true | true | false | - |
| lifting-sym+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.432 | 64.941 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.422 | 64.941 | even | true | true | false | - |
| pm-strahler | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 64.941 | even | true | true | false | - |
| pm-strahler+pre | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-strahler+iter | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-succinct | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 64.941 | even | true | true | false | - |
| pm-succinct+pre | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-succinct+iter | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 64.941 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 341 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| zielonka | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 64.941 | even | true | true | false | - |
| zielonka+pre | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 64.941 | even | true | true | false | - |
| zielonka-sym | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.394 | 64.941 | even | true | true | false | - |
| zielonka-sym+pre | complete | 341 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.381 | 64.941 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_infinitely_often_receive_d1.gm · 294 vertices / 372 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 294 | 372 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 64.941 | even | true | true | false | - |
| lifting+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 64.941 | even | true | true | false | - |
| lifting+iter | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.497 | 64.941 | even | true | true | false | - |
| lifting+pre+iter | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.941 | even | true | true | false | - |
| lifting-adaptive | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 64.941 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 64.941 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 64.941 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.941 | even | true | true | false | - |
| lifting-sym | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.403 | 64.941 | even | true | true | false | - |
| lifting-sym+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 64.941 | even | true | true | false | - |
| lifting-sym+iter | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 64.941 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.941 | even | true | true | false | - |
| pm-strahler | complete | 294 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 64.941 | even | true | true | false | - |
| pm-strahler+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-strahler+iter | complete | 294 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 64.941 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 64.941 | even | true | true | false | - |
| pm-succinct | complete | 294 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-succinct+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 64.941 | even | true | true | false | - |
| pm-succinct+iter | complete | 294 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 64.941 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 64.941 | even | true | true | false | - |
| zielonka | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 64.941 | even | true | true | false | - |
| zielonka+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 64.941 | even | true | true | false | - |
| zielonka-sym | complete | 294 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.384 | 64.941 | even | true | true | false | - |
| zielonka-sym+pre | complete | 294 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 64.941 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_infinitely_often_receive_for_all_d.gm · 2346 vertices / 2977 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2346 | 2977 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 7.711 | 65.066 | even | true | true | false | - |
| lifting+pre | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 7.690 | 65.066 | even | true | true | false | - |
| lifting+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 7.666 | 65.066 | even | true | true | false | - |
| lifting+pre+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 7.717 | 65.066 | even | true | true | false | - |
| lifting-adaptive | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 65.066 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 65.066 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 65.066 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 65.066 | even | true | true | false | - |
| lifting-sym | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 65.066 | even | true | true | false | - |
| lifting-sym+pre | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.466 | 65.066 | even | true | true | false | - |
| lifting-sym+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 65.066 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 65.066 | even | true | true | false | - |
| pm-strahler | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 65.066 | even | true | true | false | - |
| pm-strahler+pre | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 65.066 | even | true | true | false | - |
| pm-strahler+iter | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 65.066 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 65.066 | even | true | true | false | - |
| pm-succinct | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 65.066 | even | true | true | false | - |
| pm-succinct+pre | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.390 | 65.066 | even | true | true | false | - |
| pm-succinct+iter | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.382 | 65.066 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2346 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.383 | 65.066 | even | true | true | false | - |
| zielonka | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 65.066 | even | true | true | false | - |
| zielonka+pre | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 65.066 | even | true | true | false | - |
| zielonka-sym | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 65.066 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2346 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 65.066 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_invariantly_infinitely_many_reachable_taus.gm · 871 vertices / 1317 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 871 | 1317 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.479 | 65.066 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.479 | 65.191 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.479 | 65.066 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.467 | 65.191 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 65.191 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 65.191 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 65.191 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 65.191 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 65.191 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.412 | 65.191 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.404 | 65.191 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 65.191 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 871 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.401 | 65.191 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 871 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 65.191 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 871 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 65.191 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 871 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 65.191 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 871 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 65.191 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 871 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 65.191 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 871 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 65.191 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 871 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 65.191 | odd | false | true | false | - |
| zielonka | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 65.191 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 65.191 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 65.191 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 871 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 65.191 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_no_duplication_of_messages.gm · 2611 vertices / 3313 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2611 | 3313 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 65.191 | even | true | true | false | - |
| lifting+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 65.191 | even | true | true | false | - |
| lifting+iter | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 65.191 | even | true | true | false | - |
| lifting+pre+iter | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 65.191 | even | true | true | false | - |
| lifting-adaptive | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 65.191 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 65.191 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.414 | 65.191 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 65.191 | even | true | true | false | - |
| lifting-sym | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.394 | 65.191 | even | true | true | false | - |
| lifting-sym+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 65.191 | even | true | true | false | - |
| lifting-sym+iter | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 65.191 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 65.191 | even | true | true | false | - |
| pm-strahler | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.418 | 65.191 | even | true | true | false | - |
| pm-strahler+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 65.191 | even | true | true | false | - |
| pm-strahler+iter | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 65.191 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 65.191 | even | true | true | false | - |
| pm-succinct | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.414 | 65.191 | even | true | true | false | - |
| pm-succinct+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.394 | 65.191 | even | true | true | false | - |
| pm-succinct+iter | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.413 | 65.191 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.402 | 65.191 | even | true | true | false | - |
| zielonka | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 65.191 | even | true | true | false | - |
| zielonka+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 65.191 | even | true | true | false | - |
| zielonka-sym | complete | 2611 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 65.191 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2611 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 65.191 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_no_generation_of_messages.gm · 2034 vertices / 2585 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2034 | 2585 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.406 | 65.316 | even | true | true | false | - |
| lifting+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 65.316 | even | true | true | false | - |
| lifting+iter | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.405 | 65.316 | even | true | true | false | - |
| lifting+pre+iter | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 65.316 | even | true | true | false | - |
| lifting-adaptive | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 65.316 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 65.316 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 65.316 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 65.316 | even | true | true | false | - |
| lifting-sym | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.391 | 65.316 | even | true | true | false | - |
| lifting-sym+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 65.316 | even | true | true | false | - |
| lifting-sym+iter | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.391 | 65.316 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 65.316 | even | true | true | false | - |
| pm-strahler | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 65.316 | even | true | true | false | - |
| pm-strahler+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 65.316 | even | true | true | false | - |
| pm-strahler+iter | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 65.316 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 65.441 | even | true | true | false | - |
| pm-succinct | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.403 | 65.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 65.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.402 | 65.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 65.441 | even | true | true | false | - |
| zielonka | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 65.441 | even | true | true | false | - |
| zielonka+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 65.441 | even | true | true | false | - |
| zielonka-sym | complete | 2034 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 65.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2034 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 65.441 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_nodeadlock.gm · 291 vertices / 369 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 291 | 369 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 65.441 | even | true | true | false | - |
| lifting+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 65.441 | even | true | true | false | - |
| lifting+iter | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 65.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 65.441 | even | true | true | false | - |
| lifting-adaptive | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 65.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 65.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 65.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 65.441 | even | true | true | false | - |
| lifting-sym | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 65.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 65.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 65.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 65.441 | even | true | true | false | - |
| pm-strahler | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-succinct | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 65.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.408 | 65.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.408 | 65.441 | even | true | true | false | - |
| zielonka | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 65.441 | even | true | true | false | - |
| zielonka+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 65.441 | even | true | true | false | - |
| zielonka-sym | complete | 291 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 65.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 291 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 65.441 | even | true | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_read_then_eventually_send.gm · 2643 vertices / 3361 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2643 | 3361 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.431 | 65.441 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 65.441 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.439 | 65.441 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 65.441 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 65.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 65.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 65.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 65.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.474 | 65.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 65.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.476 | 65.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 65.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2643 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.401 | 65.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 65.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2643 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 65.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 65.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2643 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 65.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 65.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2643 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 65.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 65.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 65.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 65.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2643 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 65.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2643 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 65.441 | odd | false | true | false | - |

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
<summary>modelchecking/games/ABPdatasize=8_read_then_eventually_send_if_fair.gm · 516 vertices / 642 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 516 | 642 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.578 | 65.441 | even | true | true | false | - |
| lifting+pre | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.464 | 65.441 | even | true | true | false | - |
| lifting+iter | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.570 | 65.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.474 | 65.441 | even | true | true | false | - |
| lifting-adaptive | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 65.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 65.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 65.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 65.441 | even | true | true | false | - |
| lifting-sym | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.443 | 65.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 65.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.442 | 65.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.393 | 65.441 | even | true | true | false | - |
| pm-strahler | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 65.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 65.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.391 | 65.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 65.441 | even | true | true | false | - |
| pm-succinct | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 65.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 65.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 65.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 516 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 65.441 | even | true | true | false | - |
| zielonka | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 65.441 | even | true | true | false | - |
| zielonka+pre | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 65.441 | even | true | true | false | - |
| zielonka-sym | complete | 516 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 65.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 516 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 65.441 | even | true | true | false | - |

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
<summary>modelchecking/games/BRPdatasize=2_counting.gm · 2177202 vertices / 2532590 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2177202 | 2532590 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 628.684 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.558 | 517.574 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 628.938 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.222 | 517.574 | even | - | - | false | - |
| lifting-adaptive | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 11.607 | 517.465 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.676 | 517.406 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 11.912 | 517.461 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.445 | 517.457 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 628.809 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.385 | 517.574 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 628.938 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.287 | 517.461 | even | - | - | false | - |
| pm-strahler | complete | 2177202 / 0 | 45 / 0 | 44 / 0 | 2 / 0 | k=2, t=5, depth=1 / k=3, t=5, depth=2 | 29.618 | 537.586 | even | - | - | false | - |
| pm-strahler+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.225 | 517.543 | even | - | - | false | - |
| pm-strahler+iter | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 3.979 | 517.410 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.115 | 517.402 | even | - | - | false | - |
| pm-succinct | complete | 2177202 / 0 | 45 / 0 | 44 / 0 | 2 / 0 | bits=5, depth=1 / bits=5, depth=2 | 17.584 | 517.414 | even | - | - | false | - |
| pm-succinct+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.158 | 517.473 | even | - | - | false | - |
| pm-succinct+iter | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 4.175 | 517.539 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.028 | 517.543 | even | - | - | false | - |
| zielonka | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 2.848 | 517.445 | even | - | - | false | - |
| zielonka+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.345 | 517.453 | even | - | - | false | - |
| zielonka-sym | complete | 2177202 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 4.629 | 517.461 | even | - | - | false | - |
| zielonka-sym+pre | complete | 2177202 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.432 | 517.324 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 44 / 0 | 44 / 0 | 44.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 44 / 0 | 44 / 0 | 44.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/BRPdatasize=2_nodeadlock.gm · 9101 vertices / 10445 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9101 | 10445 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.417 | 70.441 | even | - | - | false | - |
| lifting+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | - | - | false | - |
| lifting+iter | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.416 | 70.441 | even | - | - | false | - |
| lifting+pre+iter | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | - | - | false | - |
| lifting-adaptive | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 70.441 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 70.441 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 70.441 | even | - | - | false | - |
| lifting-sym | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.415 | 70.441 | even | - | - | false | - |
| lifting-sym+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | - | - | false | - |
| lifting-sym+iter | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=13 / H=1, K=1, t=13 | 0.415 | 70.441 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 70.441 | even | - | - | false | - |
| pm-strahler | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 70.441 | even | - | - | false | - |
| pm-strahler+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 70.441 | even | - | - | false | - |
| pm-strahler+iter | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 70.441 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 70.441 | even | - | - | false | - |
| pm-succinct | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 70.441 | even | - | - | false | - |
| pm-succinct+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 70.441 | even | - | - | false | - |
| pm-succinct+iter | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 70.441 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 70.441 | even | - | - | false | - |
| zielonka | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 70.441 | even | - | - | false | - |
| zielonka+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 70.441 | even | - | - | false | - |
| zielonka-sym | complete | 9101 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 70.441 | even | - | - | false | - |
| zielonka-sym+pre | complete | 9101 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 70.441 | even | - | - | false | - |

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
<summary>modelchecking/games/BRPdatasize=4_nodeadlock.gm · 48861 vertices / 56113 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 48861 | 56113 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.457 | 70.441 | even | - | - | false | - |
| lifting+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 70.441 | even | - | - | false | - |
| lifting+iter | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.456 | 70.441 | even | - | - | false | - |
| lifting+pre+iter | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 70.441 | even | - | - | false | - |
| lifting-adaptive | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.457 | 70.441 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 70.441 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.455 | 70.441 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 70.441 | even | - | - | false | - |
| lifting-sym | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.443 | 70.441 | even | - | - | false | - |
| lifting-sym+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 70.441 | even | - | - | false | - |
| lifting-sym+iter | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.465 | 70.441 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 70.441 | even | - | - | false | - |
| pm-strahler | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.454 | 70.441 | even | - | - | false | - |
| pm-strahler+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.434 | 70.441 | even | - | - | false | - |
| pm-strahler+iter | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.445 | 70.441 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.435 | 70.441 | even | - | - | false | - |
| pm-succinct | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.454 | 70.441 | even | - | - | false | - |
| pm-succinct+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.433 | 70.441 | even | - | - | false | - |
| pm-succinct+iter | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.443 | 70.441 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.433 | 70.441 | even | - | - | false | - |
| zielonka | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.433 | 70.441 | even | - | - | false | - |
| zielonka+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 70.441 | even | - | - | false | - |
| zielonka-sym | complete | 48861 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.444 | 70.441 | even | - | - | false | - |
| zielonka-sym+pre | complete | 48861 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 70.441 | even | - | - | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 3714 vertices / 9699 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3714 | 9699 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.587 | 70.441 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.586 | 70.441 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.586 | 70.441 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.656 | 70.441 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.462 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.462 | 70.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.494 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 70.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 70.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3714 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3714 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.468 | 70.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3714 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3714 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.400 | 70.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3714 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3714 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3714 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3714 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 70.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 70.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 70.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 70.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3714 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 70.441 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/CABPdatasize=2_infinitely_often_read_write.gm · 691 vertices / 1859 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 691 | 1859 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.743 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.743 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.742 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.732 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.401 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.390 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.577 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.586 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.567 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.579 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.382 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.395 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 691 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 70.441 | even | true | true | false | - |
| zielonka | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.383 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 691 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.371 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_infinitely_often_receive_d1.gm · 514 vertices / 1682 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 514 | 1682 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.951 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.375 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.950 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.414 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 514 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 514 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 514 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 514 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 70.441 | even | true | true | false | - |
| zielonka | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 514 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 514 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_infinitely_often_receive_for_all_d.gm · 1028 vertices / 3365 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1028 | 3365 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.607 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.624 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.617 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.646 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.382 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.401 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.402 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.395 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1028 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| zielonka | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1028 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_invariantly_infinitely_many_reachable_taus.gm · 1393 vertices / 4193 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1393 | 4193 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.652 | 70.441 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.651 | 70.441 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.651 | 70.441 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.641 | 70.441 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.412 | 70.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 70.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.413 | 70.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1393 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.413 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1393 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.414 | 70.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1393 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1393 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 70.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1393 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1393 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 70.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1393 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1393 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 70.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 70.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 70.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 70.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1393 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 70.441 | odd | false | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_no_duplication_of_messages.gm · 1393 vertices / 4897 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1393 | 4897 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.415 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.404 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.414 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.393 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.416 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.418 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.396 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.394 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.394 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.402 | 70.441 | even | true | true | false | - |
| zielonka | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 1393 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1393 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_no_generation_of_messages.gm · 450 vertices / 1523 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 450 | 1523 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.408 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| zielonka | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 450 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 450 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_nodeadlock.gm · 465 vertices / 1633 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 465 | 1633 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.407 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.404 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.396 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.440 | 70.441 | even | true | true | false | - |
| zielonka | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 465 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 465 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=2_read_then_eventually_send.gm · 1553 vertices / 5153 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1553 | 5153 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.691 | 70.441 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 70.441 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.691 | 70.441 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 70.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.426 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 70.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1553 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1553 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 70.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1553 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 70.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1553 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 70.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 70.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1553 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 70.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1553 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 70.441 | odd | false | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 16642 vertices / 44933 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16642 | 44933 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 70.441 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 70.441 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 70.441 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 70.441 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.445 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 70.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.589 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.608 | 70.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.833 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.834 | 70.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 16642 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.741 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 16642 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.741 | 70.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 16642 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.464 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 16642 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.463 | 70.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 16642 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.495 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 16642 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.495 | 70.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 16642 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.422 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 16642 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.423 | 70.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 70.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 70.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.423 | 70.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 16642 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 70.441 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/CABPdatasize=4_infinitely_often_read_write.gm · 1619 vertices / 4387 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1619 | 4387 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.973 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.978 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.977 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.987 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.395 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.199 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.198 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.210 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.209 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.380 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.369 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.391 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.401 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1619 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| zielonka | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1619 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.391 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_infinitely_often_receive_d1.gm · 1122 vertices / 3890 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1122 | 3890 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.795 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 2.804 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.400 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.424 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 1122 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 1122 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.414 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 1122 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 1122 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 70.441 | even | true | true | false | - |
| zielonka | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 1122 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.390 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1122 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_infinitely_often_receive_for_all_d.gm · 4486 vertices / 15561 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4486 | 15561 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 70.441 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 70.441 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 70.441 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 70.441 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.679 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.678 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.678 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.678 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.443 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.444 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.436 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.432 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.421 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4486 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.412 | 70.441 | even | true | true | false | - |
| zielonka | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.401 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4486 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_invariantly_infinitely_many_reachable_taus.gm · 3121 vertices / 9697 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3121 | 9697 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.518 | 70.441 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.518 | 70.441 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.518 | 70.441 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.521 | 70.441 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 70.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 70.441 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.473 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.464 | 70.441 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.473 | 70.441 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.473 | 70.441 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 3121 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 3121 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 3121 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 70.441 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 3121 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 70.441 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 3121 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.401 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 3121 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 70.441 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 3121 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 3121 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 70.441 | odd | false | true | false | - |
| zielonka | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 70.441 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 70.441 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 70.441 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 3121 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 70.441 | odd | false | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_no_duplication_of_messages.gm · 5201 vertices / 19041 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5201 | 19041 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.418 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.417 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 70.441 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| lifting-sym | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 70.441 | even | true | true | false | - |
| lifting-sym+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |
| lifting-sym+iter | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.402 | 70.441 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |
| pm-strahler | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 70.441 | even | true | true | false | - |
| pm-strahler+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.401 | 70.441 | even | true | true | false | - |
| pm-strahler+iter | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.441 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.402 | 70.441 | even | true | true | false | - |
| pm-succinct+iter | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.403 | 70.441 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 70.441 | even | true | true | false | - |
| zielonka | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |
| zielonka+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.441 | even | true | true | false | - |
| zielonka-sym | complete | 5201 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 70.441 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5201 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 70.441 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_no_generation_of_messages.gm · 2946 vertices / 10597 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2946 | 10597 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.419 | 70.441 | even | true | true | false | - |
| lifting+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 70.441 | even | true | true | false | - |
| lifting+iter | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.419 | 70.441 | even | true | true | false | - |
| lifting+pre+iter | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 70.441 | even | true | true | false | - |
| lifting-adaptive | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 70.531 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 70.441 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 70.531 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 70.531 | even | true | true | false | - |
| lifting-sym | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.414 | 70.531 | even | true | true | false | - |
| lifting-sym+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.531 | even | true | true | false | - |
| lifting-sym+iter | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.403 | 70.531 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.531 | even | true | true | false | - |
| pm-strahler | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.531 | even | true | true | false | - |
| pm-strahler+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.531 | even | true | true | false | - |
| pm-strahler+iter | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.531 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 70.531 | even | true | true | false | - |
| pm-succinct | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 70.531 | even | true | true | false | - |
| pm-succinct+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 70.531 | even | true | true | false | - |
| pm-succinct+iter | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 70.531 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 70.531 | even | true | true | false | - |
| zielonka | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 70.531 | even | true | true | false | - |
| zielonka+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 70.656 | even | true | true | false | - |
| zielonka-sym | complete | 2946 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 70.656 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2946 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 70.656 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_nodeadlock.gm · 1041 vertices / 3809 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1041 | 3809 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.418 | 70.656 | even | true | true | false | - |
| lifting+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 70.656 | even | true | true | false | - |
| lifting+iter | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.417 | 70.656 | even | true | true | false | - |
| lifting+pre+iter | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 70.656 | even | true | true | false | - |
| lifting-adaptive | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 70.656 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 70.656 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.418 | 70.656 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 70.656 | even | true | true | false | - |
| lifting-sym | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.417 | 70.656 | even | true | true | false | - |
| lifting-sym+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.656 | even | true | true | false | - |
| lifting-sym+iter | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.403 | 70.656 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 70.656 | even | true | true | false | - |
| pm-strahler | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 70.656 | even | true | true | false | - |
| pm-strahler+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.393 | 70.656 | even | true | true | false | - |
| pm-strahler+iter | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.656 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 70.656 | even | true | true | false | - |
| pm-succinct | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 70.656 | even | true | true | false | - |
| pm-succinct+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.393 | 70.656 | even | true | true | false | - |
| pm-succinct+iter | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.392 | 70.656 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.393 | 70.656 | even | true | true | false | - |
| zielonka | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 70.656 | even | true | true | false | - |
| zielonka+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 70.656 | even | true | true | false | - |
| zielonka-sym | complete | 1041 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 70.656 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1041 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 70.656 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=4_read_then_eventually_send.gm · 5649 vertices / 19809 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5649 | 19809 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 5.043 | 70.656 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 70.656 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 5.040 | 70.656 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 70.656 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 70.656 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 70.656 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.379 | 70.656 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 70.656 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.665 | 70.656 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 70.656 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.677 | 70.656 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 70.656 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 5649 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.390 | 70.656 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 70.656 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 5649 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 70.656 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 70.656 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 5649 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.422 | 70.656 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 70.656 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 5649 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 70.656 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 70.656 | odd | false | true | false | - |
| zielonka | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 70.656 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 70.656 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 5649 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 70.656 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 5649 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 70.656 | odd | false | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_infinitely_often_enabled_then_infinitely_often_taken.gm · 82434 vertices / 231945 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 82434 | 231945 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 71.906 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 71.906 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 71.906 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 71.906 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.643 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.641 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.661 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.659 | 71.906 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 71.906 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 71.906 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 71.906 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 71.906 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 82434 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.796 | 71.906 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 82434 | 0 / 23 | 0 / 17 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.945 | 71.906 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 82434 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.901 | 71.906 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 82434 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.903 | 71.906 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 82434 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.195 | 71.906 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 82434 | 0 / 23 | 0 / 15 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 1.195 | 71.906 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 82434 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.675 | 71.906 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 82434 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.680 | 71.906 | odd | false | true | false | - |
| zielonka | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.571 | 71.906 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.576 | 71.906 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.633 | 71.906 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 82434 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.613 | 71.906 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 8 | 0 / 15 | 0 / 7 | 0.000 / 2.750 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/CABPdatasize=8_infinitely_often_read_write.gm · 4243 vertices / 11555 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4243 | 11555 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 17.342 | 71.906 | even | true | true | false | - |
| lifting+pre | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 17.301 | 71.906 | even | true | true | false | - |
| lifting+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 17.323 | 71.906 | even | true | true | false | - |
| lifting+pre+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 17.400 | 71.906 | even | true | true | false | - |
| lifting-adaptive | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.412 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.413 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 8.648 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 8.595 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 8.616 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 8.595 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.379 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.413 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4243 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 71.906 | even | true | true | false | - |
| zielonka | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4243 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.381 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_infinitely_often_receive_d1.gm · 2722 vertices / 10034 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2722 | 10034 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 12.260 | 71.906 | even | true | true | false | - |
| lifting+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 71.906 | even | true | true | false | - |
| lifting+iter | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 12.249 | 71.906 | even | true | true | false | - |
| lifting+pre+iter | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 71.906 | even | true | true | false | - |
| lifting-adaptive | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.451 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.451 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 2722 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.412 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 2722 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.400 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 2722 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.390 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 2722 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 71.906 | even | true | true | false | - |
| zielonka | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 2722 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.386 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_infinitely_often_receive_for_all_d.gm · 21770 vertices / 80273 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 21770 | 80273 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 71.906 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 71.906 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 71.906 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 71.906 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.455 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.467 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.951 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.992 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.145 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=14 / H=2, K=2, t=14 | 6.081 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.773 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.773 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.659 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.659 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.609 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.608 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.597 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 21770 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.587 | 71.906 | even | true | true | false | - |
| zielonka | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.435 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 21770 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.434 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_invariantly_infinitely_many_reachable_taus.gm · 7729 vertices / 24929 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7729 | 24929 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.034 | 71.906 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.057 | 71.906 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.020 | 71.906 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.050 | 71.906 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.401 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 71.906 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 71.906 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.687 | 71.906 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 71.906 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.708 | 71.906 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.697 | 71.906 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7729 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.412 | 71.906 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7729 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.411 | 71.906 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7729 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 71.906 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7729 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.401 | 71.906 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7729 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 71.906 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7729 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.422 | 71.906 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7729 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 71.906 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7729 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 71.906 | odd | false | true | false | - |
| zielonka | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 71.906 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 71.906 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 71.906 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7729 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.391 | 71.906 | odd | false | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_no_duplication_of_messages.gm · 23185 vertices / 88993 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 23185 | 88993 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.447 | 71.906 | even | true | true | false | - |
| lifting+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 71.906 | even | true | true | false | - |
| lifting+iter | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.447 | 71.906 | even | true | true | false | - |
| lifting+pre+iter | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| lifting-adaptive | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.435 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.434 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.434 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.435 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.433 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.422 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.432 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.423 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.444 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.424 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.433 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.422 | 71.906 | even | true | true | false | - |
| zielonka | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 23185 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.424 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 23185 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_no_generation_of_messages.gm · 17154 vertices / 65225 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 17154 | 65225 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.435 | 71.906 | even | true | true | false | - |
| lifting+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |
| lifting+iter | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.435 | 71.906 | even | true | true | false | - |
| lifting+pre+iter | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |
| lifting-adaptive | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.425 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.423 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.423 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.424 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.423 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.414 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.423 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.423 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.433 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.412 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.423 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.412 | 71.906 | even | true | true | false | - |
| zielonka | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.412 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 17154 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.459 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 17154 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_nodeadlock.gm · 2577 vertices / 9889 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2577 | 9889 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 71.906 | even | true | true | false | - |
| lifting+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 71.906 | even | true | true | false | - |
| lifting+iter | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 71.906 | even | true | true | false | - |
| lifting+pre+iter | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| lifting-adaptive | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.417 | 71.906 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 71.906 | even | true | true | false | - |
| lifting-sym | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.415 | 71.906 | even | true | true | false | - |
| lifting-sym+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| lifting-sym+iter | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 71.906 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| pm-strahler | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 71.906 | even | true | true | false | - |
| pm-strahler+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 71.906 | even | true | true | false | - |
| pm-strahler+iter | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.415 | 71.906 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 71.906 | even | true | true | false | - |
| pm-succinct | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 71.906 | even | true | true | false | - |
| pm-succinct+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 71.906 | even | true | true | false | - |
| pm-succinct+iter | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 71.906 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 71.906 | even | true | true | false | - |
| zielonka | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| zielonka+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 71.906 | even | true | true | false | - |
| zielonka-sym | complete | 2577 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2577 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 71.906 | even | true | true | false | - |

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
<summary>modelchecking/games/CABPdatasize=8_read_then_eventually_send.gm · 24593 vertices / 91553 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 24593 | 91553 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 72.074 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 72.199 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 72.199 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 72.199 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.484 | 72.199 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 72.199 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.529 | 72.199 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 72.199 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.117 | 72.199 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 72.199 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=14 / H=2, K=2, t=14 | 5.094 | 72.199 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 72.199 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 24593 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.474 | 72.199 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.422 | 72.199 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 24593 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.434 | 72.199 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.433 | 72.199 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 24593 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.474 | 72.199 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.423 | 72.199 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 24593 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.432 | 72.199 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.432 | 72.199 | odd | false | true | false | - |
| zielonka | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.422 | 72.199 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 72.199 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 24593 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.432 | 72.199 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 24593 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 72.199 | odd | false | true | false | - |

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

