# mlsolver, part 5

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>mlsolver/games/StarNesterk=3_n=2_compact.gm · 15 vertices / 35 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15 | 35 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 15 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 15 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
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
<summary>mlsolver/games/StarNesterk=3_n=3.gm · 140 vertices / 210 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 140 | 210 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 140 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 140 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=3_compact.gm · 21 vertices / 63 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 21 | 63 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 21 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 21 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=4.gm · 225 vertices / 342 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 225 | 342 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.409 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.419 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.419 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.419 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 225 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.408 | 58.574 | even | true | true | false | - |
| zielonka | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.417 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 225 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.417 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=4_compact.gm · 27 vertices / 99 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 27 | 99 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.438 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.397 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 27 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 27 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=5.gm · 330 vertices / 506 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 330 | 506 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.419 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.418 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.429 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.428 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.429 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 330 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=5_compact.gm · 33 vertices / 143 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 33 | 143 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 33 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| zielonka | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 33 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=6.gm · 455 vertices / 702 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 455 | 702 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.416 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 455 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 455 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=6_compact.gm · 39 vertices / 195 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39 | 195 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.408 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 39 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.408 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.408 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 39 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=7.gm · 600 vertices / 930 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 600 | 930 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.396 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.414 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 600 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 600 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=7_compact.gm · 45 vertices / 255 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 45 | 255 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.396 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 45 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 45 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
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
<summary>mlsolver/games/StarNesterk=3_n=8.gm · 765 vertices / 1190 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 765 | 1190 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.396 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 765 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 765 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/StarNesterk=3_n=8_compact.gm · 51 vertices / 323 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 51 | 323 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 51 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 51 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
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

