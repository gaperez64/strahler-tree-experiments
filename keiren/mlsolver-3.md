# mlsolver, part 3

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>mlsolver/games/MuCalcLimitClosurephi=p_n=0_compact.gm · 8 vertices / 11 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8 | 11 | 3 | 48 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=1.gm · 22 vertices / 26 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22 | 26 | 5 | 37 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=3, K=3, t=4 | 0.418 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=3, K=3, t=4 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=3, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=3, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=3, K=3, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.409 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=3, K=3, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 22 / 0 | 40 / 0 | 18 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=3 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 22 / 0 | 24 / 0 | 17 / 0 | 3 / 0 | k=3, t=3, depth=2 / k=3, t=3, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 22 / 0 | 37 / 0 | 17 / 0 | 4 / 0 | k=2, t=2, depth=3 / k=2, t=2, depth=3 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 22 / 0 | 20 / 0 | 17 / 0 | 3 / 0 | k=2, t=4, depth=2 / k=2, t=4, depth=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 22 / 0 | 30 / 0 | 18 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=3 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 22 / 0 | 21 / 0 | 17 / 0 | 3 / 0 | bits=3, depth=2 / bits=3, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 22 / 0 | 27 / 0 | 17 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=3 | 0.408 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 22 / 0 | 21 / 0 | 17 / 0 | 3 / 0 | bits=3, depth=2 / bits=3, depth=2 | 0.408 | 58.574 | even | true | true | false | - |
| zielonka | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 22 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 22 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 22 / 0 | 18 / 0 | 8 / 0 | 1.773 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 7 / 0 | 17 / 0 | 10 / 0 | 3.286 / 0.000 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 20 / 0 | 17 / 0 | 8 / 0 | 1.800 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 3 / 0 | 17 / 0 | 16 / 0 | 6.333 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 12 / 0 | 18 / 0 | 7 / 0 | 2.417 / 0.000 | 5 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 4 / 0 | 17 / 0 | 15 / 0 | 5.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 10 / 0 | 17 / 0 | 7 / 0 | 2.600 / 0.000 | 5 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 4 / 0 | 17 / 0 | 15 / 0 | 5.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=1_compact.gm · 12 vertices / 16 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12 | 16 | 4 | 36 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=3 / H=3, K=3, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=3 / H=3, K=3, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=3, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=3 / H=3, K=3, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=3 / H=3, K=3, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 12 / 0 | 11 / 0 | 6 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 12 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 12 / 0 | 11 / 0 | 6 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=3 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 12 / 0 | 11 / 0 | 6 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=3 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 12 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 12 / 0 | 7 / 0 | 3 / 0 | 3 / 0 | bits=1, depth=2 / bits=1, depth=3 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 12 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 5 / 0 | 6 / 0 | 4 / 0 | 2.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 5 / 0 | 6 / 0 | 4 / 0 | 2.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 5 / 0 | 6 / 0 | 4 / 0 | 2.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 4 / 0 | 3 / 0 | 3 / 0 | 1.500 / 0.000 | 1 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=2.gm · 365 vertices / 479 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 365 | 479 | 9 | 153 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 96.094 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 325 / 40 | 6 / 0 | 2 / 0 | 4 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 9.917 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 95.844 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 325 / 40 | 6 / 0 | 2 / 0 | 4 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 9.931 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 325 / 40 | 8 / 5 | 2 / 1 | 6 / 5 | H=6, K=2, t=1 / H=5, K=2, t=1 | 0.400 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 325 / 40 | 6 / 0 | 2 / 0 | 4 / 0 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.383 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 325 / 40 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=2, t=1 / H=5, K=2, t=1 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 325 / 40 | 3 / 0 | 1 / 0 | 3 / 0 | H=5, K=2, t=1 / H=4, K=2, t=1 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 325 / 40 | 8 / 5 | 2 / 1 | 6 / 5 | H=6, K=6, t=8 / H=5, K=5, t=8 | 1.511 | 113.074 | even | true | true | false | - |
| lifting-sym+pre | complete | 325 / 40 | 6 / 0 | 2 / 0 | 4 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 0.715 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 325 / 40 | 8 / 5 | 2 / 1 | 6 / 5 | H=6, K=6, t=8 / H=5, K=5, t=8 | 1.513 | 112.949 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 325 / 40 | 6 / 0 | 2 / 0 | 4 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 0.717 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 325 / 40 | 355 / 11 | 145 / 2 | 6 / 6 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 325 / 40 | 321 / 0 | 143 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.389 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 325 / 40 | 231 / 0 | 104 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.368 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 325 / 40 | 228 / 0 | 104 / 0 | 5 / 0 | k=3, t=4, depth=4 / k=3, t=4, depth=4 | 0.379 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 325 / 40 | 189 / 11 | 85 / 2 | 6 / 6 | bits=3, depth=5 / bits=3, depth=5 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 325 / 40 | 211 / 0 | 121 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 325 / 40 | 79 / 0 | 35 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=5 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 325 / 40 | 144 / 0 | 87 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 325 / 40 | 7 / 5 | 2 / 1 | 6 / 5 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 325 / 40 | 5 / 0 | 2 / 0 | 4 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 325 / 40 | 7 / 5 | 2 / 1 | 6 / 5 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 325 / 40 | 5 / 0 | 2 / 0 | 4 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-adaptive | 6 / 4 | 2 / 1 | 2 / 1 | 1.167 / 1.000 | 1 / 0 | 3 / 5 | 4.500 / 5.000 | 2 / 1 |
| lifting-adaptive+pre | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | 6 / 4 | 2 / 1 | 2 / 1 | 1.167 / 1.000 | 1 / 0 | 3 / 5 | 4.500 / 5.000 | 2 / 1 |
| lifting-sym+pre | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-sym+iter | 6 / 4 | 2 / 1 | 2 / 1 | 1.167 / 1.000 | 1 / 0 | 3 / 5 | 4.500 / 5.000 | 2 / 1 |
| lifting-sym+pre+iter | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| pm-strahler | 210 / 9 | 145 / 2 | 15 / 2 | 1.686 / 1.111 | 31 / 1 | 6 / 6 | 6.000 / 6.000 | 3 / 2 |
| pm-strahler+pre | 178 / 0 | 143 / 0 | 30 / 0 | 1.798 / 0.000 | 11 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 127 / 0 | 104 / 0 | 13 / 0 | 1.811 / 0.000 | 26 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 124 / 0 | 104 / 0 | 30 / 0 | 1.831 / 0.000 | 8 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct | 104 / 9 | 85 / 2 | 7 / 2 | 1.808 / 1.111 | 30 / 1 | 6 / 6 | 6.000 / 6.000 | 4 / 2 |
| pm-succinct+pre | 90 / 0 | 121 / 0 | 15 / 0 | 2.333 / 0.000 | 32 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 44 / 0 | 35 / 0 | 7 / 0 | 1.773 / 0.000 | 14 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 57 / 0 | 87 / 0 | 15 / 0 | 2.509 / 0.000 | 22 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 4 | 2 / 1 | 2 / 1 | 1.200 / 1.000 | 1 / 0 | 3 / 5 | 4.500 / 5.000 | 2 / 1 |
| zielonka+pre | 3 / 0 | 2 / 0 | 2 / 0 | 1.333 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| zielonka-sym | 5 / 4 | 2 / 1 | 2 / 1 | 1.200 / 1.000 | 1 / 0 | 3 / 5 | 4.500 / 5.000 | 2 / 1 |
| zielonka-sym+pre | 3 / 0 | 2 / 0 | 2 / 0 | 1.333 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=2_compact.gm · 191 vertices / 392 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 191 | 392 | 8 | 152 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | H=5, K=5, t=7 / H=5, K=5, t=7 | 3.585 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=4, t=7 / H=4, K=4, t=7 | 0.974 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | H=5, K=5, t=7 / H=5, K=5, t=7 | 3.585 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=4, t=7 / H=4, K=4, t=7 | 0.972 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=2, t=1 / H=4, K=2, t=1 | 0.371 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 168 / 23 | 2 / 0 | 1 / 0 | 2 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 168 / 23 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=2, t=1 / H=4, K=2, t=1 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | H=5, K=5, t=7 / H=5, K=5, t=7 | 0.535 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=4, t=7 / H=4, K=4, t=7 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | H=5, K=5, t=7 / H=5, K=5, t=7 | 0.537 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=4, t=7 / H=4, K=4, t=7 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 168 / 23 | 111 / 20 | 41 / 4 | 5 / 6 | k=3, t=2, depth=4 / k=3, t=2, depth=5 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 168 / 23 | 80 / 0 | 41 / 0 | 4 / 0 | k=3, t=2, depth=3 / k=3, t=2, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 168 / 23 | 98 / 0 | 35 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=5 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 168 / 23 | 68 / 0 | 35 / 0 | 4 / 0 | k=3, t=2, depth=3 / k=3, t=2, depth=4 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 168 / 23 | 82 / 20 | 33 / 4 | 5 / 6 | bits=3, depth=4 / bits=3, depth=5 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 168 / 23 | 54 / 0 | 28 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 168 / 23 | 63 / 0 | 26 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=5 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 168 / 23 | 44 / 0 | 23 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| zielonka | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 168 / 23 | 6 / 5 | 2 / 1 | 5 / 5 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 168 / 23 | 4 / 0 | 2 / 0 | 3 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| lifting+pre | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting+iter | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| lifting+pre+iter | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting-adaptive | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| lifting-adaptive+pre | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| lifting-sym+pre | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting-sym+iter | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| lifting-sym+pre+iter | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| pm-strahler | 70 / 16 | 41 / 4 | 10 / 3 | 1.571 / 1.188 | 11 / 2 | 5 / 6 | 5.000 / 6.000 | 3 / 2 |
| pm-strahler+pre | 39 / 0 | 41 / 0 | 10 / 0 | 2.026 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 63 / 0 | 35 / 0 | 9 / 0 | 1.540 / 0.000 | 10 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 33 / 0 | 35 / 0 | 9 / 0 | 2.030 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 49 / 16 | 33 / 4 | 8 / 3 | 1.653 / 1.188 | 15 / 2 | 5 / 6 | 5.000 / 6.000 | 3 / 2 |
| pm-succinct+pre | 26 / 0 | 28 / 0 | 8 / 0 | 2.038 / 0.000 | 10 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 37 / 0 | 26 / 0 | 6 / 0 | 1.676 / 0.000 | 12 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 21 / 0 | 23 / 0 | 6 / 0 | 2.048 / 0.000 | 8 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| zielonka | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| zielonka+pre | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| zielonka-sym | 4 / 4 | 2 / 1 | 2 / 1 | 1.250 / 1.000 | 1 / 0 | 2 / 5 | 3.500 / 5.000 | 2 / 1 |
| zielonka-sym+pre | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=3.gm · 3029 vertices / 4035 edges · 18 complete · 2 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3029 | 4035 | 12 | 349 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.519 | 1388.387 | - | true | - | - | Solver failed: failed to build the Even host U^8_{11,8} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 667.793 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.466 | 1388.449 | - | true | - | - | Solver failed: failed to build the Even host U^8_{11,8} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 667.859 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1993 / 1036 | 21 / 7 | 7 / 1 | 8 / 7 | H=8, K=2, t=1 / H=7, K=2, t=1 | 2.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1993 / 1036 | 14 / 0 | 6 / 0 | 5 / 0 | H=6, K=2, t=1 / H=5, K=2, t=1 | 1.116 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1993 / 1036 | 14 / 0 | 6 / 0 | 5 / 0 | H=8, K=2, t=1 / H=7, K=2, t=1 | 1.702 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1993 / 1036 | 14 / 0 | 6 / 0 | 5 / 0 | H=6, K=2, t=1 / H=5, K=2, t=1 | 1.124 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.340 | 1388.266 | - | true | - | - | Solver failed: failed to build the Even host U^8_{11,8} |
| lifting-sym+pre | complete | 1993 / 1036 | 14 / 0 | 5 / 0 | 5 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 29.377 | 790.418 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.350 | 1388.430 | - | true | - | - | Solver failed: failed to build the Even host U^8_{11,8} |
| lifting-sym+pre+iter | complete | 1993 / 1036 | 14 / 0 | 5 / 0 | 5 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 28.345 | 790.258 | even | true | true | false | - |
| pm-strahler | complete | 1993 / 1036 | 2536 / 15 | 834 / 2 | 8 / 8 | k=4, t=3, depth=7 / k=4, t=3, depth=7 | 1.088 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1993 / 1036 | 1523 / 0 | 793 / 0 | 6 / 0 | k=4, t=5, depth=5 / k=4, t=5, depth=5 | 1.808 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1993 / 1036 | 1955 / 0 | 672 / 0 | 8 / 0 | k=4, t=3, depth=7 / k=4, t=3, depth=7 | 0.440 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1993 / 1036 | 1171 / 0 | 638 / 0 | 6 / 0 | k=4, t=5, depth=5 / k=4, t=5, depth=5 | 1.207 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1993 / 1036 | 1715 / 15 | 613 / 2 | 8 / 8 | bits=4, depth=7 / bits=4, depth=7 | 0.543 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1993 / 1036 | 907 / 0 | 508 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.483 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1993 / 1036 | 1708 / 0 | 612 / 0 | 8 / 0 | bits=4, depth=7 / bits=4, depth=7 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1993 / 1036 | 101 / 0 | 64 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1993 / 1036 | 14 / 7 | 5 / 1 | 8 / 7 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1993 / 1036 | 10 / 0 | 4 / 0 | 5 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1993 / 1036 | 14 / 7 | 5 / 1 | 8 / 7 | — / — | 0.400 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1993 / 1036 | 10 / 0 | 4 / 0 | 5 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 14 / 6 | 6 / 1 | 5 / 1 | 1.429 / 1.000 | 3 / 0 | 3 / 7 | 4.714 / 7.000 | 2 / 1 |
| lifting-adaptive+pre | 8 / 0 | 5 / 0 | 5 / 0 | 1.625 / 0.000 | 2 / 0 | 3 / 0 | 4.167 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 8 / 0 | 5 / 0 | 5 / 0 | 1.625 / 0.000 | 2 / 0 | 3 / 0 | 4.167 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 8 / 0 | 5 / 0 | 5 / 0 | 1.625 / 0.000 | 2 / 0 | 3 / 0 | 4.167 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 9 / 0 | 4 / 0 | 3 / 0 | 1.444 / 0.000 | 3 / 0 | 3 / 0 | 4.400 / 0.000 | 2 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 9 / 0 | 4 / 0 | 3 / 0 | 1.444 / 0.000 | 3 / 0 | 3 / 0 | 4.400 / 0.000 | 2 / 0 |
| pm-strahler | 1702 / 13 | 834 / 2 | 16 / 2 | 1.489 / 1.077 | 182 / 1 | 8 / 8 | 8.000 / 8.000 | 4 / 2 |
| pm-strahler+pre | 730 / 0 | 793 / 0 | 26 / 0 | 2.085 / 0.000 | 125 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 1283 / 0 | 672 / 0 | 16 / 0 | 1.523 / 0.000 | 149 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 533 / 0 | 638 / 0 | 26 / 0 | 2.195 / 0.000 | 99 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct | 1102 / 13 | 613 / 2 | 29 / 2 | 1.555 / 1.077 | 237 / 1 | 8 / 8 | 8.000 / 8.000 | 5 / 2 |
| pm-succinct+pre | 399 / 0 | 508 / 0 | 29 / 0 | 2.271 / 0.000 | 128 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 1096 / 0 | 612 / 0 | 29 / 0 | 1.557 / 0.000 | 237 / 0 | 8 / 0 | 8.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 37 / 0 | 64 / 0 | 22 / 0 | 2.703 / 0.000 | 12 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka | 9 / 6 | 3 / 1 | 3 / 1 | 1.444 / 1.000 | 3 / 0 | 3 / 7 | 5.000 / 7.000 | 2 / 1 |
| zielonka+pre | 6 / 0 | 3 / 0 | 3 / 0 | 1.500 / 0.000 | 2 / 0 | 3 / 0 | 4.250 / 0.000 | 2 / 0 |
| zielonka-sym | 9 / 6 | 3 / 1 | 3 / 1 | 1.444 / 1.000 | 3 / 0 | 3 / 7 | 5.000 / 7.000 | 2 / 1 |
| zielonka-sym+pre | 6 / 0 | 3 / 0 | 3 / 0 | 1.500 / 0.000 | 2 / 0 | 3 / 0 | 4.250 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=3_compact.gm · 1562 vertices / 3401 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1562 | 3401 | 11 | 348 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.159 | 1774.980 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 223.062 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.157 | 1775.758 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 222.996 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1073 / 489 | 19 / 7 | 7 / 1 | 7 / 7 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.882 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1073 / 489 | 13 / 0 | 6 / 0 | 4 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.524 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1073 / 489 | 13 / 0 | 6 / 0 | 4 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.667 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1073 / 489 | 13 / 0 | 6 / 0 | 4 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.530 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.145 | 1775.695 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1073 / 489 | 12 / 0 | 5 / 0 | 4 / 0 | H=5, K=5, t=10 / H=5, K=5, t=10 | 12.440 | 422.309 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.138 | 1776.543 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1073 / 489 | 12 / 0 | 5 / 0 | 4 / 0 | H=5, K=5, t=10 / H=5, K=5, t=10 | 12.604 | 422.301 | even | true | true | false | - |
| pm-strahler | complete | 1073 / 489 | 617 / 28 | 167 / 4 | 7 / 8 | k=4, t=3, depth=6 / k=4, t=3, depth=7 | 0.596 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1073 / 489 | 442 / 0 | 195 / 0 | 5 / 0 | k=4, t=4, depth=4 / k=4, t=4, depth=5 | 0.543 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1073 / 489 | 94 / 0 | 21 / 0 | 7 / 0 | k=2, t=3, depth=6 / k=2, t=3, depth=7 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1073 / 489 | 314 / 0 | 144 / 0 | 5 / 0 | k=4, t=3, depth=4 / k=4, t=3, depth=5 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1073 / 489 | 483 / 28 | 137 / 4 | 7 / 8 | bits=4, depth=6 / bits=4, depth=7 | 0.431 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1073 / 489 | 293 / 0 | 136 / 0 | 5 / 0 | bits=4, depth=4 / bits=4, depth=5 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1073 / 489 | 434 / 0 | 126 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=7 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1073 / 489 | 262 / 0 | 125 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=5 | 0.380 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1073 / 489 | 13 / 7 | 5 / 1 | 7 / 7 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1073 / 489 | 9 / 0 | 4 / 0 | 4 / 0 | — / — | 0.397 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1073 / 489 | 13 / 7 | 5 / 1 | 7 / 7 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1073 / 489 | 9 / 0 | 4 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 12 / 6 | 6 / 1 | 6 / 1 | 1.500 / 1.000 | 2 / 0 | 2 / 7 | 3.714 / 7.000 | 2 / 1 |
| lifting-adaptive+pre | 7 / 0 | 5 / 0 | 5 / 0 | 1.714 / 0.000 | 2 / 0 | 2 / 0 | 3.167 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 7 / 0 | 5 / 0 | 5 / 0 | 1.714 / 0.000 | 2 / 0 | 2 / 0 | 3.167 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 7 / 0 | 5 / 0 | 5 / 0 | 1.714 / 0.000 | 2 / 0 | 2 / 0 | 3.167 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 7 / 0 | 4 / 0 | 4 / 0 | 1.571 / 0.000 | 2 / 0 | 2 / 0 | 3.400 / 0.000 | 2 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 7 / 0 | 4 / 0 | 4 / 0 | 1.571 / 0.000 | 2 / 0 | 2 / 0 | 3.400 / 0.000 | 2 / 0 |
| pm-strahler | 450 / 24 | 167 / 4 | 15 / 3 | 1.369 / 1.125 | 49 / 2 | 7 / 8 | 7.000 / 8.000 | 4 / 2 |
| pm-strahler+pre | 247 / 0 | 195 / 0 | 23 / 0 | 1.785 / 0.000 | 51 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 73 / 0 | 21 / 0 | 8 / 0 | 1.274 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 170 / 0 | 144 / 0 | 13 / 0 | 1.841 / 0.000 | 36 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct | 346 / 24 | 137 / 4 | 19 / 3 | 1.393 / 1.125 | 65 / 2 | 7 / 8 | 7.000 / 8.000 | 4 / 2 |
| pm-succinct+pre | 157 / 0 | 136 / 0 | 19 / 0 | 1.860 / 0.000 | 43 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 308 / 0 | 126 / 0 | 15 / 0 | 1.406 / 0.000 | 59 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 137 / 0 | 125 / 0 | 15 / 0 | 1.905 / 0.000 | 39 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| zielonka | 8 / 6 | 3 / 1 | 3 / 1 | 1.500 / 1.000 | 3 / 0 | 2 / 7 | 4.000 / 7.000 | 2 / 1 |
| zielonka+pre | 5 / 0 | 3 / 0 | 3 / 0 | 1.600 / 0.000 | 2 / 0 | 2 / 0 | 3.250 / 0.000 | 2 / 0 |
| zielonka-sym | 8 / 6 | 3 / 1 | 3 / 1 | 1.500 / 1.000 | 3 / 0 | 2 / 7 | 4.000 / 7.000 | 2 / 1 |
| zielonka-sym+pre | 5 / 0 | 3 / 0 | 3 / 0 | 1.600 / 0.000 | 2 / 0 | 2 / 0 | 3.250 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=4.gm · 14053 vertices / 18499 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14053 | 18499 | 14 | 625 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.224 | 1207.605 | - | true | - | - | Solver failed: failed to build the Even host U^9_{13,9} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.472 | 1372.922 | - | true | - | - | preprocess: residual=7867 shaved_even=1 shaved_odd=6185 single=0 loops=6186 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.119 | 1207.672 | - | true | - | - | Solver failed: failed to build the Even host U^9_{13,9} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.252 | 1373.559 | - | true | - | - | preprocess: residual=7867 shaved_even=1 shaved_odd=6185 single=0 loops=6186 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 7868 / 6185 | 12 / 0 | 4 / 0 | 6 / 0 | H=7, K=3, t=2 / H=6, K=3, t=2 | 28.421 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.958 | 1207.797 | - | true | - | - | Solver failed: failed to build the Even host U^9_{13,9} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.296 | 1373.008 | - | true | - | - | preprocess: residual=7867 shaved_even=1 shaved_odd=6185 single=0 loops=6186 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.061 | 1207.777 | - | true | - | - | Solver failed: failed to build the Even host U^9_{13,9} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.237 | 1373.691 | - | true | - | - | preprocess: residual=7867 shaved_even=1 shaved_odd=6185 single=0 loops=6186 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 7868 / 6185 | 5780 / 0 | 2413 / 0 | 7 / 0 | k=4, t=5, depth=6 / k=4, t=5, depth=6 | 11.959 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 7868 / 6185 | 7919 / 0 | 2300 / 0 | 9 / 0 | k=4, t=4, depth=8 / k=4, t=4, depth=8 | 2.465 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 7868 / 6185 | 4173 / 0 | 1875 / 0 | 7 / 0 | k=4, t=5, depth=6 / k=4, t=5, depth=6 | 7.217 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 7868 / 6185 | 5817 / 17 | 1955 / 2 | 9 / 9 | bits=5, depth=8 / bits=5, depth=8 | 4.605 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 7868 / 6185 | 3619 / 0 | 1914 / 0 | 7 / 0 | bits=5, depth=6 / bits=5, depth=6 | 1.035 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 7868 / 6185 | 5809 / 0 | 1954 / 0 | 9 / 0 | bits=5, depth=8 / bits=5, depth=8 | 0.667 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 7868 / 6185 | 3619 / 0 | 1914 / 0 | 7 / 0 | bits=5, depth=6 / bits=5, depth=6 | 0.647 | 58.574 | even | true | true | false | - |
| zielonka | complete | 7868 / 6185 | 26 / 8 | 10 / 1 | 9 / 8 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 7868 / 6185 | 21 / 0 | 9 / 0 | 6 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 7868 / 6185 | 26 / 8 | 10 / 1 | 9 / 8 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 7868 / 6185 | 21 / 0 | 9 / 0 | 6 / 0 | — / — | 0.442 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 8 / 0 | 3 / 0 | 3 / 0 | 1.375 / 0.000 | 2 / 0 | 3 / 0 | 4.750 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 3367 / 0 | 2413 / 0 | 46 / 0 | 1.716 / 0.000 | 324 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 5619 / 0 | 2300 / 0 | 33 / 0 | 1.409 / 0.000 | 439 / 0 | 9 / 0 | 9.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 2298 / 0 | 1875 / 0 | 46 / 0 | 1.815 / 0.000 | 270 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct | 3862 / 15 | 1955 / 2 | 51 / 2 | 1.506 / 1.067 | 777 / 1 | 9 / 9 | 9.000 / 9.000 | 5 / 2 |
| pm-succinct+pre | 1705 / 0 | 1914 / 0 | 41 / 0 | 2.122 / 0.000 | 506 / 0 | 7 / 0 | 7.000 / 0.000 | 6 / 0 |
| pm-succinct+iter | 3855 / 0 | 1954 / 0 | 51 / 0 | 1.507 / 0.000 | 777 / 0 | 9 / 0 | 9.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 1705 / 0 | 1914 / 0 | 41 / 0 | 2.122 / 0.000 | 506 / 0 | 7 / 0 | 7.000 / 0.000 | 6 / 0 |
| zielonka | 16 / 7 | 7 / 1 | 4 / 1 | 1.562 / 1.000 | 5 / 0 | 3 / 8 | 5.300 / 8.000 | 3 / 1 |
| zielonka+pre | 12 / 0 | 6 / 0 | 4 / 0 | 1.667 / 0.000 | 5 / 0 | 3 / 0 | 4.889 / 0.000 | 3 / 0 |
| zielonka-sym | 16 / 7 | 7 / 1 | 4 / 1 | 1.562 / 1.000 | 5 / 0 | 3 / 8 | 5.300 / 8.000 | 3 / 1 |
| zielonka-sym+pre | 12 / 0 | 6 / 0 | 4 / 0 | 1.667 / 0.000 | 5 / 0 | 3 / 0 | 4.889 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=4_compact.gm · 6817 vertices / 15208 edges · 15 complete · 5 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6817 | 15208 | 13 | 624 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.393 | 1372.676 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.112 | 1470.266 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.445 | 1372.438 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.109 | 1468.074 | - | true | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 3674 / 3143 | 30 / 0 | 12 / 0 | 5 / 0 | H=6, K=3, t=2 / H=6, K=3, t=2 | 17.585 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3674 / 3143 | 11 / 0 | 4 / 0 | 5 / 0 | H=8, K=3, t=2 / H=8, K=3, t=2 | 9.854 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3674 / 3143 | 11 / 0 | 4 / 0 | 5 / 0 | H=6, K=3, t=2 / H=6, K=3, t=2 | 4.753 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.210 | 1372.402 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.112 | 1469.957 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.223 | 1372.656 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.109 | 1468.391 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 3674 / 3143 | 2860 / 32 | 647 / 4 | 8 / 9 | k=4, t=3, depth=7 / k=4, t=3, depth=8 | 2.289 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3674 / 3143 | 1640 / 0 | 692 / 0 | 6 / 0 | k=5, t=3, depth=5 / k=5, t=3, depth=6 | 1.298 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3674 / 3143 | 2492 / 0 | 586 / 0 | 8 / 0 | k=4, t=3, depth=7 / k=4, t=3, depth=8 | 0.563 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3674 / 3143 | 1420 / 0 | 554 / 0 | 6 / 0 | k=4, t=3, depth=5 / k=4, t=3, depth=6 | 0.564 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3674 / 3143 | 2421 / 32 | 634 / 4 | 8 / 9 | bits=5, depth=7 / bits=5, depth=8 | 1.901 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3674 / 3143 | 1421 / 0 | 583 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=6 | 0.677 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3674 / 3143 | 354 / 0 | 78 / 0 | 8 / 0 | bits=4, depth=7 / bits=4, depth=8 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3674 / 3143 | 229 / 0 | 74 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.430 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3674 / 3143 | 25 / 8 | 10 / 1 | 8 / 8 | — / — | 0.410 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3674 / 3143 | 20 / 0 | 9 / 0 | 5 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3674 / 3143 | 25 / 8 | 10 / 1 | 8 / 8 | — / — | 0.483 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3674 / 3143 | 20 / 0 | 9 / 0 | 5 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 18 / 0 | 10 / 0 | 6 / 0 | 1.611 / 0.000 | 4 / 0 | 2 / 0 | 4.000 / 0.000 | 3 / 0 |
| lifting-adaptive+iter | 7 / 0 | 3 / 0 | 3 / 0 | 1.429 / 0.000 | 2 / 0 | 2 / 0 | 3.750 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 7 / 0 | 3 / 0 | 3 / 0 | 1.429 / 0.000 | 2 / 0 | 2 / 0 | 3.750 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 2213 / 28 | 647 / 4 | 27 / 3 | 1.292 / 1.107 | 161 / 2 | 8 / 9 | 8.000 / 9.000 | 4 / 2 |
| pm-strahler+pre | 948 / 0 | 692 / 0 | 27 / 0 | 1.729 / 0.000 | 212 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-strahler+iter | 1906 / 0 | 586 / 0 | 21 / 0 | 1.307 / 0.000 | 156 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 866 / 0 | 554 / 0 | 23 / 0 | 1.639 / 0.000 | 135 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct | 1787 / 28 | 634 / 4 | 38 / 3 | 1.354 / 1.107 | 319 / 2 | 8 / 9 | 8.000 / 9.000 | 5 / 2 |
| pm-succinct+pre | 838 / 0 | 583 / 0 | 38 / 0 | 1.695 / 0.000 | 216 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 276 / 0 | 78 / 0 | 13 / 0 | 1.279 / 0.000 | 43 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 155 / 0 | 74 / 0 | 13 / 0 | 1.471 / 0.000 | 33 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 15 / 7 | 7 / 1 | 4 / 1 | 1.600 / 1.000 | 5 / 0 | 2 / 8 | 4.300 / 8.000 | 3 / 1 |
| zielonka+pre | 11 / 0 | 6 / 0 | 4 / 0 | 1.727 / 0.000 | 5 / 0 | 2 / 0 | 3.889 / 0.000 | 3 / 0 |
| zielonka-sym | 15 / 7 | 7 / 1 | 4 / 1 | 1.600 / 1.000 | 5 / 0 | 2 / 8 | 4.300 / 8.000 | 3 / 1 |
| zielonka-sym+pre | 11 / 0 | 6 / 0 | 4 / 0 | 1.727 / 0.000 | 5 / 0 | 2 / 0 | 3.889 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=5.gm · 62707 vertices / 82920 edges · 6 complete · 10 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 62707 | 82920 | 16 | 981 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.424 | 1297.812 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.000 | 1084.219 | - | true | - | - | preprocess: residual=27416 shaved_even=1 shaved_odd=35290 single=0 loops=35291 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.372 | 1301.242 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.962 | 1084.215 | - | true | - | - | preprocess: residual=27416 shaved_even=1 shaved_odd=35290 single=0 loops=35291 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.336 | 1298.004 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.943 | 1084.285 | - | true | - | - | preprocess: residual=27416 shaved_even=1 shaved_odd=35290 single=0 loops=35291 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.390 | 1301.375 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.899 | 1084.176 | - | true | - | - | preprocess: residual=27416 shaved_even=1 shaved_odd=35290 single=0 loops=35291 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | complete | 27417 / 35290 | 22580 / 0 | 7178 / 0 | 10 / 0 | bits=7, depth=9 / bits=7, depth=9 | 26.001 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 27417 / 35290 | 17004 / 0 | 7922 / 0 | 8 / 0 | bits=7, depth=7 / bits=7, depth=7 | 16.855 | 58.574 | even | true | true | false | - |
| zielonka | complete | 27417 / 35290 | 53 / 9 | 21 / 1 | 10 / 9 | — / — | 0.832 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 27417 / 35290 | 47 / 0 | 20 / 0 | 7 / 0 | — / — | 0.452 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 27417 / 35290 | 53 / 9 | 21 / 1 | 10 / 9 | — / — | 2.471 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 27417 / 35290 | 47 / 0 | 20 / 0 | 7 / 0 | — / — | 0.678 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| pm-succinct+iter | 15402 / 0 | 7178 / 0 | 65 / 0 | 1.466 / 0.000 | 3027 / 0 | 10 / 0 | 10.000 / 0.000 | 6 / 0 |
| pm-succinct+pre+iter | 9082 / 0 | 7922 / 0 | 95 / 0 | 1.872 / 0.000 | 2352 / 0 | 8 / 0 | 8.000 / 0.000 | 6 / 0 |
| zielonka | 32 / 8 | 14 / 1 | 5 / 1 | 1.625 / 1.000 | 11 / 0 | 3 / 9 | 5.810 / 9.000 | 3 / 1 |
| zielonka+pre | 27 / 0 | 13 / 0 | 5 / 0 | 1.704 / 0.000 | 11 / 0 | 3 / 0 | 5.600 / 0.000 | 3 / 0 |
| zielonka-sym | 32 / 8 | 14 / 1 | 5 / 1 | 1.625 / 1.000 | 11 / 0 | 3 / 9 | 5.810 / 9.000 | 3 / 1 |
| zielonka-sym+pre | 27 / 0 | 13 / 0 | 5 / 0 | 1.704 / 0.000 | 11 / 0 | 3 / 0 | 5.600 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=5_compact.gm · 29335 vertices / 66905 edges · 10 complete · 6 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 29335 | 66905 | 15 | 980 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.000 | 1080.012 | - | true | - | - | Solver failed: failed to build the Even host U^9_{14,9} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.155 | 1209.582 | - | true | - | - | preprocess: residual=12679 shaved_even=15 shaved_odd=16641 single=0 loops=16656 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.925 | 1079.250 | - | true | - | - | Solver failed: failed to build the Even host U^9_{14,9} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.136 | 1209.488 | - | true | - | - | preprocess: residual=12679 shaved_even=15 shaved_odd=16641 single=0 loops=16656 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.822 | 1080.105 | - | true | - | - | Solver failed: failed to build the Even host U^9_{14,9} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.074 | 1209.645 | - | true | - | - | preprocess: residual=12679 shaved_even=15 shaved_odd=16641 single=0 loops=16656 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.000 | 1079.277 | - | true | - | - | Solver failed: failed to build the Even host U^9_{14,9} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.017 | 1209.586 | - | true | - | - | preprocess: residual=12679 shaved_even=15 shaved_odd=16641 single=0 loops=16656 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 12694 / 16641 | 6175 / 0 | 2228 / 0 | 7 / 0 | k=5, t=4, depth=6 / k=5, t=4, depth=7 | 21.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 12694 / 16641 | 1556 / 0 | 261 / 0 | 9 / 0 | k=4, t=4, depth=8 / k=4, t=4, depth=9 | 3.832 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 12694 / 16641 | 191 / 0 | 87 / 0 | 7 / 0 | k=5, t=4, depth=6 / k=5, t=4, depth=7 | 6.470 | 58.574 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 12694 / 16641 | 5791 / 0 | 2062 / 0 | 7 / 0 | bits=7, depth=6 / bits=7, depth=7 | 14.435 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 12694 / 16641 | 9248 / 0 | 2057 / 0 | 9 / 0 | bits=6, depth=8 / bits=6, depth=9 | 2.034 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 12694 / 16641 | 5747 / 0 | 2052 / 0 | 7 / 0 | bits=6, depth=6 / bits=6, depth=7 | 1.983 | 58.574 | even | true | true | false | - |
| zielonka | complete | 12694 / 16641 | 52 / 9 | 21 / 1 | 9 / 9 | — / — | 0.554 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 12694 / 16641 | 46 / 0 | 20 / 0 | 6 / 0 | — / — | 0.410 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 12694 / 16641 | 52 / 9 | 21 / 1 | 9 / 9 | — / — | 1.087 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 12694 / 16641 | 46 / 0 | 20 / 0 | 6 / 0 | — / — | 0.493 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 3947 / 0 | 2228 / 0 | 39 / 0 | 1.564 / 0.000 | 617 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-strahler+iter | 1295 / 0 | 261 / 0 | 21 / 0 | 1.201 / 0.000 | 75 / 0 | 9 / 0 | 9.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 104 / 0 | 87 / 0 | 12 / 0 | 1.827 / 0.000 | 24 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 3729 / 0 | 2062 / 0 | 73 / 0 | 1.553 / 0.000 | 785 / 0 | 7 / 0 | 7.000 / 0.000 | 6 / 0 |
| pm-succinct+iter | 7191 / 0 | 2057 / 0 | 69 / 0 | 1.286 / 0.000 | 1029 / 0 | 9 / 0 | 9.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 3695 / 0 | 2052 / 0 | 69 / 0 | 1.555 / 0.000 | 779 / 0 | 7 / 0 | 7.000 / 0.000 | 6 / 0 |
| zielonka | 31 / 8 | 14 / 1 | 5 / 1 | 1.645 / 1.000 | 11 / 0 | 2 / 9 | 4.810 / 9.000 | 3 / 1 |
| zielonka+pre | 26 / 0 | 13 / 0 | 5 / 0 | 1.731 / 0.000 | 11 / 0 | 2 / 0 | 4.600 / 0.000 | 3 / 0 |
| zielonka-sym | 31 / 8 | 14 / 1 | 5 / 1 | 1.645 / 1.000 | 11 / 0 | 2 / 9 | 4.810 / 9.000 | 3 / 1 |
| zielonka-sym+pre | 26 / 0 | 13 / 0 | 5 / 0 | 1.731 / 0.000 | 11 / 0 | 2 / 0 | 4.600 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=6.gm · 259455 vertices / 339108 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 259455 | 339108 | 18 | 1417 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.275 | 1126.914 | - | true | - | - | Solver failed: failed to build the Even host U^11_{17,11} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.844 | 1357.406 | - | true | - | - | preprocess: residual=105535 shaved_even=1 shaved_odd=153919 single=0 loops=153920 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.284 | 1127.840 | - | true | - | - | Solver failed: failed to build the Even host U^11_{17,11} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.859 | 1357.109 | - | true | - | - | preprocess: residual=105535 shaved_even=1 shaved_odd=153919 single=0 loops=153920 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 63.473 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 63.402 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 63.340 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 63.344 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.192 | 1127.141 | - | true | - | - | Solver failed: failed to build the Even host U^11_{17,11} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.858 | 1357.332 | - | true | - | - | preprocess: residual=105535 shaved_even=1 shaved_odd=153919 single=0 loops=153920 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.200 | 1127.949 | - | true | - | - | Solver failed: failed to build the Even host U^11_{17,11} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.786 | 1357.113 | - | true | - | - | preprocess: residual=105535 shaved_even=1 shaved_odd=153919 single=0 loops=153920 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.355 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.277 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.281 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.348 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.336 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.227 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.355 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 63.289 | - | true | - | - | deadline exceeded |
| zielonka | complete | 105536 / 153919 | 113 / 10 | 47 / 1 | 11 / 10 | — / — | 5.858 | 63.473 | even | true | true | false | - |
| zielonka+pre | complete | 105536 / 153919 | 106 / 0 | 46 / 0 | 8 / 0 | — / — | 0.931 | 63.410 | even | true | true | false | - |
| zielonka-sym | complete | 105536 / 153919 | 113 / 10 | 47 / 1 | 11 / 10 | — / — | 21.639 | 63.348 | even | true | true | false | - |
| zielonka-sym+pre | complete | 105536 / 153919 | 106 / 0 | 46 / 0 | 8 / 0 | — / — | 2.857 | 63.457 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 66 / 9 | 28 / 1 | 6 / 1 | 1.697 / 1.000 | 26 / 0 | 3 / 10 | 6.383 / 10.000 | 4 / 1 |
| zielonka+pre | 60 / 0 | 27 / 0 | 6 / 0 | 1.750 / 0.000 | 26 / 0 | 3 / 0 | 6.283 / 0.000 | 4 / 0 |
| zielonka-sym | 66 / 9 | 28 / 1 | 6 / 1 | 1.697 / 1.000 | 26 / 0 | 3 / 10 | 6.383 / 10.000 | 4 / 1 |
| zielonka-sym+pre | 60 / 0 | 27 / 0 | 6 / 0 | 1.750 / 0.000 | 26 / 0 | 3 / 0 | 6.283 / 0.000 | 4 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=6_compact.gm · 110328 vertices / 251339 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 110328 | 251339 | 17 | 1416 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.764 | 1342.867 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.495 | 1296.152 | - | true | - | - | preprocess: residual=42001 shaved_even=17 shaved_odd=68310 single=0 loops=68327 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.775 | 1342.879 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.390 | 1296.262 | - | true | - | - | preprocess: residual=42001 shaved_even=17 shaved_odd=68310 single=0 loops=68327 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.864 | 1343.016 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.626 | 1296.211 | - | true | - | - | preprocess: residual=42001 shaved_even=17 shaved_odd=68310 single=0 loops=68327 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.610 | 1343.012 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.408 | 1296.188 | - | true | - | - | preprocess: residual=42001 shaved_even=17 shaved_odd=68310 single=0 loops=68327 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| zielonka | complete | 42018 / 68310 | 112 / 10 | 47 / 1 | 10 / 10 | — / — | 1.899 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 42018 / 68310 | 105 / 0 | 46 / 0 | 7 / 0 | — / — | 0.566 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 42018 / 68310 | 112 / 10 | 47 / 1 | 10 / 10 | — / — | 7.002 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 42018 / 68310 | 105 / 0 | 46 / 0 | 7 / 0 | — / — | 1.218 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 65 / 9 | 28 / 1 | 6 / 1 | 1.708 / 1.000 | 26 / 0 | 2 / 10 | 5.383 / 10.000 | 4 / 1 |
| zielonka+pre | 59 / 0 | 27 / 0 | 6 / 0 | 1.763 / 0.000 | 26 / 0 | 2 / 0 | 5.283 / 0.000 | 4 / 0 |
| zielonka-sym | 65 / 9 | 28 / 1 | 6 / 1 | 1.708 / 1.000 | 26 / 0 | 2 / 10 | 5.383 / 10.000 | 4 / 1 |
| zielonka-sym+pre | 59 / 0 | 27 / 0 | 6 / 0 | 1.763 / 0.000 | 26 / 0 | 2 / 0 | 5.283 / 0.000 | 4 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=7.gm · 1021740 vertices / 1337584 edges · 2 complete · 14 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1021740 | 1337584 | 20 | 1933 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.818 | 1522.914 | - | - | - | - | Solver failed: failed to build the Even host U^12_{19,12} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.570 | 1425.777 | - | - | - | - | preprocess: residual=338196 shaved_even=1 shaved_odd=683543 single=0 loops=683544 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.756 | 1522.969 | - | - | - | - | Solver failed: failed to build the Even host U^12_{19,12} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.519 | 1425.777 | - | - | - | - | preprocess: residual=338196 shaved_even=1 shaved_odd=683543 single=0 loops=683544 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 245.277 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 245.406 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 245.277 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 245.383 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.660 | 1522.902 | - | - | - | - | Solver failed: failed to build the Even host U^12_{19,12} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.498 | 1425.773 | - | - | - | - | preprocess: residual=338196 shaved_even=1 shaved_odd=683543 single=0 loops=683544 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.643 | 1522.973 | - | - | - | - | Solver failed: failed to build the Even host U^12_{19,12} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.460 | 1425.777 | - | - | - | - | preprocess: residual=338196 shaved_even=1 shaved_odd=683543 single=0 loops=683544 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 245.074 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 245.285 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 245.207 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 245.289 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 245.352 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 245.285 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 245.281 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 245.215 | - | - | - | - | deadline exceeded |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 245.406 | - | - | - | - | deadline exceeded |
| zielonka+pre | complete | 338197 / 683543 | 244 / 0 | 105 / 0 | 9 / 0 | — / — | 3.265 | 245.273 | even | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 245.266 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | complete | 338197 / 683543 | 244 / 0 | 105 / 0 | 9 / 0 | — / — | 19.097 | 245.090 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 139 / 0 | 57 / 0 | 7 / 0 | 1.748 / 0.000 | 59 / 0 | 3 / 0 | 6.990 / 0.000 | 4 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 139 / 0 | 57 / 0 | 7 / 0 | 1.748 / 0.000 | 59 / 0 | 3 / 0 | 6.990 / 0.000 | 4 / 0 |

</details>

<details>
<summary>mlsolver/games/Nestern=7_compact.gm · 426185 vertices / 986070 edges · 3 complete · 13 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 426185 | 986070 | 19 | 1932 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.787 | 1383.801 | - | - | - | - | Solver failed: failed to build the Even host U^11_{18,11} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.539 | 1150.203 | - | - | - | - | preprocess: residual=134307 shaved_even=19 shaved_odd=291859 single=0 loops=291878 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.808 | 1383.750 | - | - | - | - | Solver failed: failed to build the Even host U^11_{18,11} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.480 | 1150.215 | - | - | - | - | preprocess: residual=134307 shaved_even=19 shaved_odd=291859 single=0 loops=291878 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 132.012 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 131.945 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 131.883 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 131.820 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.728 | 1383.746 | - | - | - | - | Solver failed: failed to build the Even host U^11_{18,11} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.525 | 1150.141 | - | - | - | - | preprocess: residual=134307 shaved_even=19 shaved_odd=291859 single=0 loops=291878 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.706 | 1383.621 | - | - | - | - | Solver failed: failed to build the Even host U^11_{18,11} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.526 | 1150.258 | - | - | - | - | preprocess: residual=134307 shaved_even=19 shaved_odd=291859 single=0 loops=291878 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 131.957 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 131.953 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 131.828 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 131.871 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 131.754 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 131.891 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 131.957 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 131.828 | - | - | - | - | deadline exceeded |
| zielonka | complete | 134326 / 291859 | 251 / 11 | 106 / 1 | 11 / 11 | — / — | 19.032 | 131.875 | even | - | - | false | - |
| zielonka+pre | complete | 134326 / 291859 | 243 / 0 | 105 / 0 | 8 / 0 | — / — | 1.377 | 131.992 | even | - | - | false | - |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 131.734 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | complete | 134326 / 291859 | 243 / 0 | 105 / 0 | 8 / 0 | — / — | 6.641 | 131.824 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| zielonka | 145 / 10 | 58 / 1 | 7 / 1 | 1.724 / 1.000 | 59 / 0 | 2 / 11 | 6.038 / 11.000 | 4 / 1 |
| zielonka+pre | 138 / 0 | 57 / 0 | 7 / 0 | 1.754 / 0.000 | 59 / 0 | 2 / 0 | 5.990 / 0.000 | 4 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 138 / 0 | 57 / 0 | 7 / 0 | 1.754 / 0.000 | 59 / 0 | 2 / 0 | 5.990 / 0.000 | 4 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=1.gm · 17 vertices / 22 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 17 | 22 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.419 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.417 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4 / 13 | 4 / 2 | 3 / 1 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4 / 13 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4 / 13 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4 / 13 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.409 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.409 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4 / 13 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4 / 13 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=1_compact.gm · 9 vertices / 15 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9 | 15 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 4 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4 / 5 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 4 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.405 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=2.gm · 203 vertices / 295 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 203 | 295 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.414 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 145 / 58 | 12 / 2 | 11 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 145 / 58 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.397 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 145 / 58 | 12 / 2 | 11 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.397 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.397 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 145 / 58 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 145 / 58 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 145 / 58 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/PDLBinaryCountern=2_compact.gm · 27 vertices / 51 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 27 | 51 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.408 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 18 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 18 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 18 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 18 / 9 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 18 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 18 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 18 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 18 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 18 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 18 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=3.gm · 1546 vertices / 2302 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1546 | 2302 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.754 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.754 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 1367 / 179 | 20 / 2 | 19 / 1 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1367 / 179 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 1367 / 179 | 20 / 2 | 19 / 1 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1367 / 179 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.395 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 1367 / 179 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1367 / 179 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 19 / 1 | 19 / 1 | 19.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 19 / 1 | 19 / 1 | 19.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=3_compact.gm · 105 vertices / 207 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 105 | 207 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.395 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 88 / 17 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 88 / 17 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 88 / 17 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 88 / 17 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 88 / 17 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 88 / 17 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 88 / 17 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 88 / 17 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.428 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 88 / 17 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.399 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 88 / 17 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.391 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=4.gm · 8691 vertices / 13051 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8691 | 13051 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 18.025 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 18.024 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.717 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 1.722 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 8207 / 484 | 28 / 2 | 27 / 1 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.420 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 8207 / 484 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 8207 / 484 | 28 / 2 | 27 / 1 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 8207 / 484 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.390 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 8207 / 484 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.390 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 8207 / 484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 27 / 1 | 27 / 1 | 27.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 27 / 1 | 27 / 1 | 27.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=4_compact.gm · 467 vertices / 931 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 467 | 931 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.436 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.436 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.448 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 434 / 33 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 434 / 33 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 434 / 33 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 434 / 33 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 434 / 33 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 434 / 33 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 434 / 33 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 434 / 33 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 434 / 33 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 434 / 33 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=5.gm · 44028 vertices / 66368 edges · 21 complete · 3 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 44028 | 66368 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 42807 / 1221 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.568 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 42807 / 1221 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.530 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 42807 / 1221 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=15 / H=1, K=1, t=15 | 20.581 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 42807 / 1221 | 36 / 2 | 35 / 1 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 0.691 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 42807 / 1221 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.465 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.465 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 42807 / 1221 | 36 / 2 | 35 / 1 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 0.732 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 42807 / 1221 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.497 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 42807 / 1221 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 42807 / 1221 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.506 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 42807 / 1221 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |

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
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 35 / 1 | 35 / 1 | 35.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 35 / 1 | 35 / 1 | 35.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=5_compact.gm · 2163 vertices / 4323 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2163 | 4323 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.986 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.382 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.974 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.371 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.526 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.547 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2098 / 65 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2098 / 65 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2098 / 65 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2098 / 65 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2098 / 65 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2098 / 65 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2098 / 65 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2098 / 65 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2098 / 65 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2098 / 65 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.383 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=6.gm · 214775 vertices / 324327 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 214775 | 324327 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.580 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.567 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 211825 / 2950 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.100 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.674 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 211825 / 2950 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.208 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.674 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.634 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 211825 / 2950 | 44 / 2 | 43 / 1 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 2.312 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.718 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 211825 / 2950 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.725 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.682 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 211825 / 2950 | 44 / 2 | 43 / 1 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 2.069 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.693 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 211825 / 2950 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.723 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.683 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 211825 / 2950 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.662 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 211825 / 2950 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.789 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 211825 / 2950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.615 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 43 / 1 | 43 / 1 | 43.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 43 / 1 | 43 / 1 | 43.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=6_compact.gm · 10183 vertices / 20363 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10183 | 20363 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 2.513 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 2.517 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10054 / 129 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10054 / 129 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10054 / 129 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10054 / 129 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10054 / 129 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10054 / 129 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10054 / 129 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10054 / 129 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10054 / 129 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10054 / 129 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.390 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=7.gm · 1031612 vertices / 1559132 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1031612 | 1559132 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 250.934 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.380 | 250.809 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 250.801 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.274 | 250.805 | odd | false | true | false | - |
| lifting-adaptive | complete | 1024693 / 6919 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 4.081 | 250.934 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.473 | 250.914 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1024693 / 6919 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 4.326 | 250.938 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.483 | 250.793 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 250.797 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.416 | 250.805 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 250.801 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.367 | 250.863 | odd | false | true | false | - |
| pm-strahler | complete | 1024693 / 6919 | 52 / 2 | 51 / 1 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 10.038 | 250.746 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.678 | 250.742 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1024693 / 6919 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.749 | 250.879 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.655 | 250.883 | odd | false | true | false | - |
| pm-succinct | complete | 1024693 / 6919 | 52 / 2 | 51 / 1 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 8.665 | 250.680 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.651 | 250.754 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1024693 / 6919 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 1.860 | 250.801 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.643 | 250.758 | odd | false | true | false | - |
| zielonka | complete | 1024693 / 6919 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.548 | 250.805 | odd | false | true | false | - |
| zielonka+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.414 | 250.934 | odd | false | true | false | - |
| zielonka-sym | complete | 1024693 / 6919 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 2.120 | 250.812 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1024693 / 6919 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.427 | 250.867 | odd | false | true | false | - |

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
| pm-strahler | 1 / 1 | 51 / 1 | 51 / 1 | 51.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 51 / 1 | 51 / 1 | 51.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=7_compact.gm · 48211 vertices / 96419 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 48211 | 96419 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.516 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.535 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 47954 / 257 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.540 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.517 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 47954 / 257 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.581 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.541 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.421 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 47954 / 257 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 1.126 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 47954 / 257 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 47954 / 257 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.478 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 47954 / 257 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.496 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 47954 / 257 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.835 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 47954 / 257 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.458 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 47954 / 257 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.507 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 47954 / 257 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 47954 / 257 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 47954 / 257 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.499 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 47954 / 257 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.485 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=8.gm · 4924413 vertices / 7445509 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4924413 | 7445509 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1316.793 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.441 | 1199.551 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.115 | 1317.395 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.007 | 1199.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 4908533 / 15880 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 20.774 | 1199.504 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.210 | 1199.430 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 4908533 / 15880 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 20.085 | 1199.441 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.191 | 1199.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.132 | 1316.684 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.210 | 1199.430 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.117 | 1317.391 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.528 | 1199.574 | odd | false | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.080 | 1199.453 | - | false | - | - | deadline exceeded |
| pm-strahler+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 6.906 | 1199.227 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4908533 / 15880 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 6.950 | 1199.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 6.545 | 1199.383 | odd | false | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.084 | 1199.453 | - | false | - | - | deadline exceeded |
| pm-succinct+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 6.538 | 1199.516 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4908533 / 15880 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 7.428 | 1199.316 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 6.548 | 1199.375 | odd | false | true | false | - |
| zielonka | complete | 4908533 / 15880 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 5.717 | 1199.574 | odd | false | true | false | - |
| zielonka+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.015 | 1199.574 | odd | false | true | false | - |
| zielonka-sym | complete | 4908533 / 15880 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 8.625 | 1199.301 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 4908533 / 15880 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.221 | 1199.309 | odd | false | true | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/PDLBinaryCountern=8_compact.gm · 228787 vertices / 457571 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 228787 | 457571 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 65.004 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 1.412 | 65.027 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 65.004 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 1.577 | 64.891 | odd | - | - | false | - |
| lifting-adaptive | complete | 228274 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.936 | 65.027 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.706 | 64.902 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 228274 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.965 | 64.965 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.699 | 65.031 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 65.031 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.655 | 65.027 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 64.898 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.652 | 65.027 | odd | - | - | false | - |
| pm-strahler | complete | 228274 / 513 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 7.960 | 64.777 | odd | - | - | false | - |
| pm-strahler+pre | complete | 228274 / 513 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.712 | 64.891 | odd | - | - | false | - |
| pm-strahler+iter | complete | 228274 / 513 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.681 | 64.699 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 228274 / 513 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.672 | 64.977 | odd | - | - | false | - |
| pm-succinct | complete | 228274 / 513 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 4.459 | 64.852 | odd | - | - | false | - |
| pm-succinct+pre | complete | 228274 / 513 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.672 | 64.836 | odd | - | - | false | - |
| pm-succinct+iter | complete | 228274 / 513 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.723 | 64.996 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 228274 / 513 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.673 | 64.832 | odd | - | - | false | - |
| zielonka | complete | 228274 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.641 | 64.898 | odd | - | - | false | - |
| zielonka+pre | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.623 | 64.902 | odd | - | - | false | - |
| zielonka-sym | complete | 228274 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.768 | 64.891 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 228274 / 513 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.653 | 65.012 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| pm-succinct+iter | 1 / 1 | 2 / 2 | 2 / 2 | 2.000 / 2.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 1 | 0 / 2 | 0 / 2 | 0.000 / 2.000 | 0 / 1 | 0 / 2 | 0.000 / 2.000 | 0 / 2 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=1.gm · 63 vertices / 80 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 63 | 80 | 6 | 127 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=5 / H=4, K=4, t=5 | 0.425 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=5 / H=4, K=4, t=5 | 0.426 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=5 / H=4, K=4, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=5 / H=4, K=4, t=5 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 63 / 0 | 54 / 0 | 23 / 0 | 5 / 0 | k=2, t=2, depth=4 / k=2, t=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 63 / 0 | 41 / 0 | 27 / 0 | 3 / 0 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 63 / 0 | 44 / 0 | 20 / 0 | 5 / 0 | k=2, t=2, depth=4 / k=2, t=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 63 / 0 | 41 / 0 | 27 / 0 | 3 / 0 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 63 / 0 | 40 / 0 | 19 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 63 / 0 | 21 / 0 | 17 / 0 | 3 / 0 | bits=3, depth=2 / bits=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 63 / 0 | 36 / 0 | 18 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 63 / 0 | 21 / 0 | 17 / 0 | 3 / 0 | bits=3, depth=2 / bits=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 63 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 63 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 31 / 0 | 23 / 0 | 8 / 0 | 1.710 / 0.000 | 4 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 14 / 0 | 27 / 0 | 15 / 0 | 2.857 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 24 / 0 | 20 / 0 | 8 / 0 | 1.792 / 0.000 | 4 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 14 / 0 | 27 / 0 | 15 / 0 | 2.857 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 21 / 0 | 19 / 0 | 5 / 0 | 1.857 / 0.000 | 7 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 4 / 0 | 17 / 0 | 15 / 0 | 5.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 18 / 0 | 18 / 0 | 5 / 0 | 1.944 / 0.000 | 7 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 4 / 0 | 17 / 0 | 15 / 0 | 5.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=1_compact.gm · 19 vertices / 27 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19 | 27 | 5 | 126 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.404 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.393 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 19 / 0 | 10 / 0 | 3 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 19 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | k=1, t=1, depth=3 / k=1, t=1, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 19 / 0 | 9 / 0 | 3 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 19 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 19 / 0 | 9 / 0 | 3 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 7 / 0 | 3 / 0 | 3 / 0 | 1.286 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct | 6 / 0 | 3 / 0 | 2 / 0 | 1.333 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 6 / 0 | 3 / 0 | 2 / 0 | 1.333 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=2.gm · 2497 vertices / 3341 edges · 18 complete · 2 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2497 | 3341 | 11 | 919 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.446 | 1385.789 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.035 | 667.840 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.506 | 1385.723 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 667.656 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 2497 / 0 | 9 / 0 | 2 / 0 | 7 / 0 | H=7, K=2, t=1 / H=6, K=2, t=1 | 0.608 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2497 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=7, K=2, t=1 / H=6, K=2, t=1 | 0.473 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.314 | 1385.734 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.552 | 790.441 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.320 | 1385.797 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.557 | 790.223 | even | true | true | false | - |
| pm-strahler | complete | 2497 / 0 | 907 / 0 | 310 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.463 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2497 / 0 | 805 / 0 | 326 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2497 / 0 | 615 / 0 | 222 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2497 / 0 | 308 / 0 | 125 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2497 / 0 | 349 / 0 | 126 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2497 / 0 | 219 / 0 | 103 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=5 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2497 / 0 | 182 / 0 | 66 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2497 / 0 | 128 / 0 | 60 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=5 | 0.401 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2497 / 0 | 8 / 0 | 2 / 0 | 7 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2497 / 0 | 8 / 0 | 2 / 0 | 7 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2497 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 7 / 0 | 2 / 0 | 2 / 0 | 1.143 / 0.000 | 1 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| pm-strahler | 597 / 0 | 310 / 0 | 15 / 0 | 1.518 / 0.000 | 46 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 479 / 0 | 326 / 0 | 24 / 0 | 1.678 / 0.000 | 41 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 393 / 0 | 222 / 0 | 15 / 0 | 1.562 / 0.000 | 36 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 183 / 0 | 125 / 0 | 24 / 0 | 1.678 / 0.000 | 16 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 223 / 0 | 126 / 0 | 8 / 0 | 1.561 / 0.000 | 53 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 116 / 0 | 103 / 0 | 8 / 0 | 1.879 / 0.000 | 36 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 116 / 0 | 66 / 0 | 8 / 0 | 1.560 / 0.000 | 28 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 68 / 0 | 60 / 0 | 8 / 0 | 1.868 / 0.000 | 21 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 2 / 0 | 2 / 0 | 1.167 / 0.000 | 1 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka+pre | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 2 / 0 | 2 / 0 | 1.167 / 0.000 | 1 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=2_compact.gm · 456 vertices / 1027 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 456 | 1027 | 9 | 918 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 101.820 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 2.274 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 101.691 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 2.254 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 456 / 0 | 7 / 0 | 2 / 0 | 6 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | 0.379 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 456 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 456 / 0 | 7 / 0 | 2 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.035 | 160.383 | even | true | true | false | - |
| lifting-sym+pre | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.520 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 456 / 0 | 7 / 0 | 2 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.004 | 160.512 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.523 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 456 / 0 | 33 / 0 | 7 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 456 / 0 | 19 / 0 | 7 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 456 / 0 | 33 / 0 | 7 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 456 / 0 | 19 / 0 | 7 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 456 / 0 | 28 / 0 | 6 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=6 | 0.373 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 456 / 0 | 16 / 0 | 6 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 456 / 0 | 15 / 0 | 3 / 0 | 6 / 0 | bits=1, depth=5 / bits=1, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 456 / 0 | 9 / 0 | 3 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 456 / 0 | 7 / 0 | 2 / 0 | 6 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 456 / 0 | 7 / 0 | 2 / 0 | 6 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 456 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 2 / 0 | 4.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 2 / 0 | 4.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 2 / 0 | 4.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 26 / 0 | 7 / 0 | 4 / 0 | 1.231 / 0.000 | 2 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 12 / 0 | 7 / 0 | 4 / 0 | 1.500 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 26 / 0 | 7 / 0 | 4 / 0 | 1.231 / 0.000 | 2 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 12 / 0 | 7 / 0 | 4 / 0 | 1.500 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct | 22 / 0 | 6 / 0 | 4 / 0 | 1.227 / 0.000 | 3 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 10 / 0 | 6 / 0 | 4 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 12 / 0 | 3 / 0 | 2 / 0 | 1.167 / 0.000 | 2 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 6 / 0 | 3 / 0 | 2 / 0 | 1.333 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| zielonka | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 2 / 0 | 4.000 / 0.000 | 2 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 2 / 0 | 4.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=3.gm · 33969 vertices / 44709 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 33969 | 44709 | 13 | 2401 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.392 | 1299.617 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.945 | 1081.078 | - | true | - | - | preprocess: residual=25857 shaved_even=8112 shaved_odd=0 single=0 loops=8112 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.390 | 1299.496 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.858 | 1081.070 | - | true | - | - | preprocess: residual=25857 shaved_even=8112 shaved_odd=0 single=0 loops=8112 wcwc=0 |
| lifting-adaptive | complete | 33969 / 0 | 28 / 0 | 9 / 0 | 8 / 0 | H=8, K=2, t=1 / H=7, K=2, t=1 | 11.637 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 33969 / 0 | 25 / 0 | 9 / 0 | 5 / 0 | H=7, K=2, t=1 / H=6, K=2, t=1 | 8.072 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 33969 / 0 | 21 / 0 | 8 / 0 | 5 / 0 | H=8, K=2, t=1 / H=7, K=2, t=1 | 8.227 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 33969 / 0 | 21 / 0 | 8 / 0 | 5 / 0 | H=7, K=2, t=1 / H=6, K=2, t=1 | 5.533 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.206 | 1299.562 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.835 | 1081.133 | - | true | - | - | preprocess: residual=25857 shaved_even=8112 shaved_odd=0 single=0 loops=8112 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.270 | 1299.633 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.832 | 1081.074 | - | true | - | - | preprocess: residual=25857 shaved_even=8112 shaved_odd=0 single=0 loops=8112 wcwc=0 |
| pm-strahler | complete | 33969 / 0 | 7059 / 0 | 2331 / 0 | 8 / 0 | k=4, t=3, depth=7 / k=4, t=3, depth=7 | 12.602 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 33969 / 0 | 6825 / 0 | 2624 / 0 | 7 / 0 | k=4, t=4, depth=6 / k=4, t=4, depth=6 | 3.650 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 33969 / 0 | 4691 / 0 | 1538 / 0 | 8 / 0 | k=4, t=3, depth=7 / k=4, t=3, depth=7 | 0.793 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 33969 / 0 | 717 / 0 | 348 / 0 | 7 / 0 | k=4, t=4, depth=6 / k=4, t=4, depth=6 | 1.089 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 33969 / 0 | 1019 / 0 | 353 / 0 | 8 / 0 | bits=3, depth=7 / bits=3, depth=7 | 1.067 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 33969 / 0 | 906 / 0 | 396 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.763 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 33969 / 0 | 788 / 0 | 277 / 0 | 8 / 0 | bits=3, depth=7 / bits=3, depth=7 | 0.671 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 33969 / 0 | 271 / 0 | 119 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.670 | 58.574 | even | true | true | false | - |
| zielonka | complete | 33969 / 0 | 14 / 0 | 5 / 0 | 8 / 0 | — / — | 0.464 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 33969 / 0 | 10 / 0 | 4 / 0 | 5 / 0 | — / — | 0.456 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 33969 / 0 | 14 / 0 | 5 / 0 | 8 / 0 | — / — | 0.569 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 33969 / 0 | 10 / 0 | 4 / 0 | 5 / 0 | — / — | 0.495 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 19 / 0 | 8 / 0 | 5 / 0 | 1.421 / 0.000 | 3 / 0 | 3 / 0 | 4.667 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 16 / 0 | 8 / 0 | 5 / 0 | 1.500 / 0.000 | 3 / 0 | 3 / 0 | 4.333 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 13 / 0 | 7 / 0 | 5 / 0 | 1.538 / 0.000 | 3 / 0 | 3 / 0 | 4.250 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 13 / 0 | 7 / 0 | 5 / 0 | 1.538 / 0.000 | 3 / 0 | 3 / 0 | 4.250 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 4728 / 0 | 2331 / 0 | 31 / 0 | 1.493 / 0.000 | 435 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-strahler+pre | 4201 / 0 | 2624 / 0 | 38 / 0 | 1.624 / 0.000 | 466 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 3153 / 0 | 1538 / 0 | 24 / 0 | 1.487 / 0.000 | 319 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 369 / 0 | 348 / 0 | 17 / 0 | 1.940 / 0.000 | 92 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct | 666 / 0 | 353 / 0 | 14 / 0 | 1.529 / 0.000 | 141 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 510 / 0 | 396 / 0 | 14 / 0 | 1.775 / 0.000 | 137 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 511 / 0 | 277 / 0 | 14 / 0 | 1.540 / 0.000 | 109 / 0 | 8 / 0 | 8.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 152 / 0 | 119 / 0 | 11 / 0 | 1.776 / 0.000 | 44 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| zielonka | 9 / 0 | 4 / 0 | 3 / 0 | 1.444 / 0.000 | 3 / 0 | 3 / 0 | 4.800 / 0.000 | 3 / 0 |
| zielonka+pre | 6 / 0 | 4 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 4.500 / 0.000 | 3 / 0 |
| zielonka-sym | 9 / 0 | 4 / 0 | 3 / 0 | 1.444 / 0.000 | 3 / 0 | 3 / 0 | 4.800 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 6 / 0 | 4 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 4.500 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=3_compact.gm · 6182 vertices / 24833 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6182 | 24833 | 11 | 2400 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.419 | 1373.137 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.068 | 906.723 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.347 | 1373.129 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.071 | 906.781 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 6182 / 0 | 19 / 0 | 7 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.122 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6182 / 0 | 15 / 0 | 6 / 0 | 4 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.708 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6182 / 0 | 15 / 0 | 6 / 0 | 4 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.892 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6182 / 0 | 15 / 0 | 6 / 0 | 4 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.604 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.203 | 1373.031 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.068 | 907.648 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.254 | 1373.145 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.071 | 907.668 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 6182 / 0 | 253 / 0 | 56 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=7 | 0.873 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 6182 / 0 | 140 / 0 | 53 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=5 | 0.840 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 6182 / 0 | 117 / 0 | 27 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=7 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6182 / 0 | 63 / 0 | 25 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=5 | 0.410 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 6182 / 0 | 115 / 0 | 23 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=7 | 0.635 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 6182 / 0 | 69 / 0 | 23 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=5 | 0.616 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 6182 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=2, depth=6 / bits=2, depth=7 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6182 / 0 | 14 / 0 | 4 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=5 | 0.432 | 58.574 | even | true | true | false | - |
| zielonka | complete | 6182 / 0 | 13 / 0 | 5 / 0 | 7 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 6182 / 0 | 9 / 0 | 4 / 0 | 4 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 6182 / 0 | 13 / 0 | 5 / 0 | 7 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6182 / 0 | 9 / 0 | 4 / 0 | 4 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 12 / 0 | 6 / 0 | 6 / 0 | 1.500 / 0.000 | 2 / 0 | 2 / 0 | 3.714 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 9 / 0 | 6 / 0 | 5 / 0 | 1.556 / 0.000 | 2 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 9 / 0 | 6 / 0 | 5 / 0 | 1.556 / 0.000 | 2 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 9 / 0 | 6 / 0 | 5 / 0 | 1.556 / 0.000 | 2 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 197 / 0 | 56 / 0 | 11 / 0 | 1.279 / 0.000 | 12 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 87 / 0 | 53 / 0 | 11 / 0 | 1.598 / 0.000 | 12 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 90 / 0 | 27 / 0 | 7 / 0 | 1.289 / 0.000 | 8 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 38 / 0 | 25 / 0 | 8 / 0 | 1.632 / 0.000 | 8 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct | 92 / 0 | 23 / 0 | 8 / 0 | 1.239 / 0.000 | 12 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 46 / 0 | 23 / 0 | 8 / 0 | 1.478 / 0.000 | 12 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 10 / 0 | 4 / 0 | 2 / 0 | 1.300 / 0.000 | 3 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka | 8 / 0 | 4 / 0 | 3 / 0 | 1.500 / 0.000 | 3 / 0 | 2 / 0 | 3.800 / 0.000 | 3 / 0 |
| zielonka+pre | 5 / 0 | 4 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 3.500 / 0.000 | 3 / 0 |
| zielonka-sym | 8 / 0 | 4 / 0 | 3 / 0 | 1.500 / 0.000 | 3 / 0 | 2 / 0 | 3.800 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 5 / 0 | 4 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 3.500 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=4.gm · 1042752 vertices / 1380194 edges · 7 complete · 9 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1042752 | 1380194 | 17 | 4705 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.767 | 1522.219 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.999 | 1522.430 | - | - | - | - | preprocess: residual=779822 shaved_even=262930 shaved_odd=0 single=0 loops=262930 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.767 | 1522.223 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.984 | 1522.504 | - | - | - | - | preprocess: residual=779822 shaved_even=262930 shaved_odd=0 single=0 loops=262930 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 249.844 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 249.840 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 249.973 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 249.848 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.679 | 1522.289 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.925 | 1522.418 | - | - | - | - | preprocess: residual=779822 shaved_even=262930 shaved_odd=0 single=0 loops=262930 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.684 | 1522.246 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.948 | 1522.445 | - | - | - | - | preprocess: residual=779822 shaved_even=262930 shaved_odd=0 single=0 loops=262930 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 249.785 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 249.715 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 249.789 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 249.715 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 249.918 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1042752 / 0 | 6578 / 0 | 2195 / 0 | 9 / 0 | bits=4, depth=8 / bits=4, depth=8 | 21.671 | 249.832 | even | - | - | false | - |
| pm-succinct+iter | complete | 1042752 / 0 | 6094 / 0 | 1724 / 0 | 10 / 0 | bits=4, depth=9 / bits=4, depth=9 | 27.079 | 249.832 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1042752 / 0 | 4741 / 0 | 1595 / 0 | 9 / 0 | bits=4, depth=8 / bits=4, depth=8 | 25.644 | 249.852 | even | - | - | false | - |
| zielonka | complete | 1042752 / 0 | 34 / 0 | 12 / 0 | 10 / 0 | — / — | 2.598 | 249.992 | even | - | - | false | - |
| zielonka+pre | complete | 1042752 / 0 | 30 / 0 | 12 / 0 | 6 / 0 | — / — | 2.159 | 249.828 | even | - | - | false | - |
| zielonka-sym | complete | 1042752 / 0 | 34 / 0 | 12 / 0 | 10 / 0 | — / — | 9.121 | 249.953 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1042752 / 0 | 30 / 0 | 12 / 0 | 6 / 0 | — / — | 5.212 | 249.969 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 4383 / 0 | 2195 / 0 | 29 / 0 | 1.501 / 0.000 | 864 / 0 | 9 / 0 | 9.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 4370 / 0 | 1724 / 0 | 29 / 0 | 1.394 / 0.000 | 734 / 0 | 10 / 0 | 10.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 3146 / 0 | 1595 / 0 | 29 / 0 | 1.507 / 0.000 | 628 / 0 | 9 / 0 | 9.000 / 0.000 | 5 / 0 |
| zielonka | 22 / 0 | 10 / 0 | 4 / 0 | 1.500 / 0.000 | 8 / 0 | 4 / 0 | 5.583 / 0.000 | 3 / 0 |
| zielonka+pre | 18 / 0 | 10 / 0 | 4 / 0 | 1.611 / 0.000 | 8 / 0 | 4 / 0 | 5.250 / 0.000 | 3 / 0 |
| zielonka-sym | 22 / 0 | 10 / 0 | 4 / 0 | 1.500 / 0.000 | 8 / 0 | 4 / 0 | 5.583 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 18 / 0 | 10 / 0 | 4 / 0 | 1.611 / 0.000 | 8 / 0 | 4 / 0 | 5.250 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/ParityAndBuechin=4_compact.gm · 183781 vertices / 1506551 edges · 6 complete · 10 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 183781 | 1506551 | 14 | 4704 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.349 | 1156.246 | - | - | - | - | Solver failed: failed to build the Even host U^9_{17,9} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.410 | 1156.422 | - | - | - | - | preprocess: residual=183771 shaved_even=10 shaved_odd=0 single=0 loops=10 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.391 | 1156.434 | - | - | - | - | Solver failed: failed to build the Even host U^9_{17,9} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.359 | 1156.344 | - | - | - | - | preprocess: residual=183771 shaved_even=10 shaved_odd=0 single=0 loops=10 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 127.402 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 127.461 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 127.441 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 127.332 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.295 | 1156.309 | - | - | - | - | Solver failed: failed to build the Even host U^9_{17,9} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.393 | 1156.434 | - | - | - | - | preprocess: residual=183771 shaved_even=10 shaved_odd=0 single=0 loops=10 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.369 | 1156.293 | - | - | - | - | Solver failed: failed to build the Even host U^9_{17,9} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.312 | 1156.348 | - | - | - | - | preprocess: residual=183771 shaved_even=10 shaved_odd=0 single=0 loops=10 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 127.324 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 127.344 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 127.270 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 127.207 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 127.270 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 127.340 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 183781 / 0 | 149 / 0 | 21 / 0 | 9 / 0 | bits=3, depth=8 / bits=3, depth=9 | 27.845 | 127.324 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 183781 / 0 | 86 / 0 | 21 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 27.837 | 127.281 | even | - | - | false | - |
| zielonka | complete | 183781 / 0 | 33 / 0 | 12 / 0 | 9 / 0 | — / — | 0.812 | 127.391 | even | - | - | false | - |
| zielonka+pre | complete | 183781 / 0 | 29 / 0 | 12 / 0 | 5 / 0 | — / — | 0.874 | 127.398 | even | - | - | false | - |
| zielonka-sym | complete | 183781 / 0 | 33 / 0 | 12 / 0 | 9 / 0 | — / — | 1.381 | 127.320 | even | - | - | false | - |
| zielonka-sym+pre | complete | 183781 / 0 | 29 / 0 | 12 / 0 | 5 / 0 | — / — | 1.400 | 127.320 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| pm-succinct+iter | 128 / 0 | 21 / 0 | 8 / 0 | 1.156 / 0.000 | 11 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 65 / 0 | 21 / 0 | 8 / 0 | 1.308 / 0.000 | 11 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka | 21 / 0 | 10 / 0 | 4 / 0 | 1.524 / 0.000 | 8 / 0 | 3 / 0 | 4.583 / 0.000 | 3 / 0 |
| zielonka+pre | 17 / 0 | 10 / 0 | 4 / 0 | 1.647 / 0.000 | 8 / 0 | 3 / 0 | 4.250 / 0.000 | 3 / 0 |
| zielonka-sym | 21 / 0 | 10 / 0 | 4 / 0 | 1.524 / 0.000 | 8 / 0 | 3 / 0 | 4.583 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 17 / 0 | 10 / 0 | 4 / 0 | 1.647 / 0.000 | 8 / 0 | 3 / 0 | 4.250 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=1.gm · 105 vertices / 118 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 105 | 118 | 6 | 411 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=6 / H=4, K=4, t=6 | 0.550 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.403 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=6 / H=4, K=4, t=6 | 0.549 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=6 / H=4, K=4, t=6 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=6 / H=4, K=4, t=6 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=6 / H=2, K=2, t=6 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 105 / 0 | 128 / 0 | 52 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=4 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 105 / 0 | 83 / 0 | 69 / 0 | 3 / 0 | k=3, t=4, depth=2 / k=3, t=4, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 105 / 0 | 109 / 0 | 42 / 0 | 5 / 0 | k=2, t=2, depth=4 / k=2, t=2, depth=4 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 105 / 0 | 67 / 0 | 45 / 0 | 3 / 0 | k=2, t=4, depth=2 / k=2, t=4, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 105 / 0 | 86 / 0 | 40 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=4 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 105 / 0 | 86 / 0 | 71 / 0 | 3 / 0 | bits=4, depth=2 / bits=4, depth=2 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 105 / 0 | 75 / 0 | 37 / 0 | 5 / 0 | bits=2, depth=4 / bits=2, depth=4 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 105 / 0 | 43 / 0 | 37 / 0 | 3 / 0 | bits=4, depth=2 / bits=4, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 105 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 105 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 76 / 0 | 52 / 0 | 15 / 0 | 1.671 / 0.000 | 7 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 14 / 0 | 69 / 0 | 28 / 0 | 5.857 / 0.000 | 8 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 67 / 0 | 42 / 0 | 15 / 0 | 1.612 / 0.000 | 4 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 22 / 0 | 45 / 0 | 25 / 0 | 3.000 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 46 / 0 | 40 / 0 | 7 / 0 | 1.848 / 0.000 | 14 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 15 / 0 | 71 / 0 | 31 / 0 | 5.667 / 0.000 | 8 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 38 / 0 | 37 / 0 | 7 / 0 | 1.947 / 0.000 | 13 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 6 / 0 | 37 / 0 | 31 / 0 | 7.000 / 0.000 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=1_compact.gm · 34 vertices / 46 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 34 | 46 | 5 | 410 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 34 / 0 | 20 / 0 | 8 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 34 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 34 / 0 | 20 / 0 | 8 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 34 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 34 / 0 | 19 / 0 | 8 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 34 / 0 | 9 / 0 | 8 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 34 / 0 | 16 / 0 | 7 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 34 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 34 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 34 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 12 / 0 | 8 / 0 | 4 / 0 | 1.583 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 12 / 0 | 8 / 0 | 4 / 0 | 1.583 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 11 / 0 | 8 / 0 | 4 / 0 | 1.636 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 8 / 0 | 8 / 0 | 8.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 9 / 0 | 7 / 0 | 3 / 0 | 1.667 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=2.gm · 200 vertices / 224 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 200 | 224 | 6 | 681 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=7 / H=4, K=4, t=7 | 1.296 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.465 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=7 / H=4, K=4, t=7 | 1.284 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.461 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=7 / H=4, K=4, t=7 | 0.484 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=7 / H=4, K=4, t=7 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 200 / 0 | 275 / 0 | 129 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 200 / 0 | 145 / 0 | 140 / 0 | 3 / 0 | k=3, t=6, depth=2 / k=3, t=6, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 200 / 0 | 248 / 0 | 119 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 200 / 0 | 108 / 0 | 81 / 0 | 3 / 0 | k=2, t=5, depth=2 / k=2, t=5, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 200 / 0 | 192 / 0 | 108 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 200 / 0 | 111 / 0 | 98 / 0 | 3 / 0 | bits=5, depth=2 / bits=5, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 200 / 0 | 110 / 0 | 69 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 200 / 0 | 75 / 0 | 69 / 0 | 3 / 0 | bits=5, depth=2 / bits=5, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.397 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 200 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 200 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 146 / 0 | 129 / 0 | 15 / 0 | 1.877 / 0.000 | 22 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 5 / 0 | 140 / 0 | 68 / 0 | 28.800 / 0.000 | 4 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 129 / 0 | 119 / 0 | 15 / 0 | 1.915 / 0.000 | 20 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 27 / 0 | 81 / 0 | 56 / 0 | 3.963 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 84 / 0 | 108 / 0 | 15 / 0 | 2.274 / 0.000 | 29 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 13 / 0 | 98 / 0 | 63 / 0 | 8.462 / 0.000 | 6 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 41 / 0 | 69 / 0 | 15 / 0 | 2.659 / 0.000 | 16 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 6 / 0 | 69 / 0 | 63 / 0 | 12.333 / 0.000 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=2_compact.gm · 47 vertices / 63 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 47 | 63 | 5 | 680 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.425 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.414 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=5 / H=4, K=4, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 47 / 0 | 27 / 0 | 12 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 47 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 47 / 0 | 27 / 0 | 12 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 47 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 47 / 0 | 25 / 0 | 12 / 0 | 4 / 0 | bits=2, depth=3 / bits=2, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 47 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 47 / 0 | 16 / 0 | 7 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 47 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 47 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 47 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 15 / 0 | 12 / 0 | 7 / 0 | 1.733 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 15 / 0 | 12 / 0 | 7 / 0 | 1.733 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 13 / 0 | 12 / 0 | 4 / 0 | 1.846 / 0.000 | 5 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 9 / 0 | 7 / 0 | 3 / 0 | 1.667 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=3.gm · 330 vertices / 369 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 330 | 369 | 6 | 971 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 4.185 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.843 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 4.194 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.838 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 0.707 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=5, K=5, t=8 / H=4, K=4, t=8 | 0.751 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 330 / 0 | 268 / 0 | 129 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=4 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 330 / 0 | 250 / 0 | 245 / 0 | 3 / 0 | k=3, t=7, depth=2 / k=3, t=7, depth=2 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 330 / 0 | 251 / 0 | 124 / 0 | 5 / 0 | k=3, t=2, depth=4 / k=3, t=2, depth=4 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 330 / 0 | 158 / 0 | 139 / 0 | 3 / 0 | k=2, t=6, depth=2 / k=2, t=6, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 330 / 0 | 285 / 0 | 158 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 330 / 0 | 204 / 0 | 188 / 0 | 3 / 0 | bits=6, depth=2 / bits=6, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 330 / 0 | 191 / 0 | 113 / 0 | 5 / 0 | bits=3, depth=4 / bits=3, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 330 / 0 | 116 / 0 | 113 / 0 | 3 / 0 | bits=6, depth=2 / bits=6, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 330 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 330 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 139 / 0 | 129 / 0 | 15 / 0 | 1.921 / 0.000 | 23 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 5 / 0 | 245 / 0 | 112 / 0 | 49.800 / 0.000 | 4 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 127 / 0 | 124 / 0 | 15 / 0 | 1.969 / 0.000 | 22 / 0 | 5 / 0 | 5.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 19 / 0 | 139 / 0 | 122 / 0 | 8.263 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 127 / 0 | 158 / 0 | 15 / 0 | 2.236 / 0.000 | 44 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 16 / 0 | 188 / 0 | 112 / 0 | 12.688 / 0.000 | 9 / 0 | 3 / 0 | 3.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 113 / 0 | 15 / 0 | 2.436 / 0.000 | 29 / 0 | 5 / 0 | 5.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 3 / 0 | 113 / 0 | 112 / 0 | 38.333 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Petrin=3_compact.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.127 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | true | - | - | exit 3: 62:1: unexpected keyword |

</details>

