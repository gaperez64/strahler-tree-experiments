# pgsolver, part 4

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=24.gm · 5000 vertices / 52699 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52699 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.494 | 2002.668 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.523 | 2002.414 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2524 / 2476 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2524 / 2476 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.474 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.260 | 2002.688 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.427 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.028 | 2002.500 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2524 / 2476 | 30 / 35 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.506 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.471 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2524 / 2476 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.417 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2524 / 2476 | 32 / 51 | 7 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.478 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2524 / 2476 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.414 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2524 / 2476 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2524 / 2476 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.422 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2524 / 2476 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 29 | 6 / 6 | 5 / 4 | 1.208 / 1.172 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 41 | 7 / 10 | 4 / 4 | 1.240 / 1.220 | 3 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=3.gm · 5000 vertices / 51966 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 51966 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.622 | 2002.441 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.621 | 2002.547 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2513 / 2487 | 5 / 2 | 1 / 1 | 5 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.488 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2513 / 2487 | 5 / 2 | 1 / 1 | 5 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.465 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.302 | 2002.551 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.044 | 2002.605 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2513 / 2487 | 25 / 35 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.486 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.448 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2513 / 2487 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2513 / 2487 | 38 / 42 | 9 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.464 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2513 / 2487 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2513 / 2487 | 5 / 2 | 1 / 1 | 5 / 2 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2513 / 2487 | 5 / 2 | 1 / 1 | 5 / 2 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 4 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 2 | 5.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 4 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 2 | 5.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 20 / 29 | 5 / 6 | 4 / 4 | 1.200 / 1.172 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 29 / 34 | 9 / 8 | 4 / 4 | 1.276 / 1.206 | 5 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 4 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 2 | 5.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 4 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 2 | 5.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=4.gm · 5000 vertices / 52862 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52862 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.573 | 2002.691 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.552 | 2002.598 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2505 / 2495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2505 / 2495 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.210 | 2002.551 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.003 | 2002.688 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2505 / 2495 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.488 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2505 / 2495 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.456 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2505 / 2495 | 32 / 47 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2505 / 2495 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2505 / 2495 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.422 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2505 / 2495 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2505 / 2495 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 25 | 4 / 5 | 4 / 4 | 1.176 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 38 | 7 / 9 | 4 / 4 | 1.240 / 1.211 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=5.gm · 5000 vertices / 52235 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52235 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.538 | 2002.574 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.578 | 2002.582 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2499 / 2501 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2499 / 2501 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.464 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.189 | 2002.703 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.236 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.788 | 2002.570 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.449 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2499 / 2501 | 34 / 40 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.655 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.421 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2499 / 2501 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2499 / 2501 | 39 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2499 / 2501 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2499 / 2501 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2499 / 2501 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2499 / 2501 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 27 / 33 | 7 / 7 | 5 / 4 | 1.222 / 1.182 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 30 / 41 | 9 / 10 | 5 / 4 | 1.267 / 1.220 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=6.gm · 5000 vertices / 52862 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52862 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.570 | 2002.734 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.559 | 2002.730 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2520 / 2480 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2520 / 2480 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.223 | 2002.789 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.047 | 2002.621 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2520 / 2480 | 21 / 52 | 4 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.498 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.458 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2520 / 2480 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.446 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2520 / 2480 | 32 / 64 | 7 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2520 / 2480 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2520 / 2480 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2520 / 2480 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2520 / 2480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 43 | 4 / 9 | 4 / 6 | 1.176 / 1.186 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 52 | 7 / 12 | 4 / 6 | 1.240 / 1.212 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=7.gm · 5000 vertices / 52521 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52521 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.609 | 2002.539 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.598 | 2002.477 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2491 / 2509 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2491 / 2509 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.273 | 2002.547 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.019 | 2002.609 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2491 / 2509 | 21 / 36 | 4 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.488 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.448 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2491 / 2509 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2491 / 2509 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.473 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2491 / 2509 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2491 / 2509 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2491 / 2509 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 30 | 4 / 6 | 4 / 5 | 1.176 / 1.167 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=8.gm · 5000 vertices / 52823 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52823 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.577 | 2002.410 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.576 | 2002.684 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2433 / 2567 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.489 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.427 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2433 / 2567 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.213 | 2002.684 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.037 | 2002.809 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2433 / 2567 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.498 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.459 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2433 / 2567 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2433 / 2567 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2433 / 2567 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2433 / 2567 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2433 / 2567 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2433 / 2567 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | odd | false | true | false | - |

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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=9.gm · 5000 vertices / 52067 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52067 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.480 | 2002.555 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.614 | 2002.688 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2513 / 2487 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2513 / 2487 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.223 | 2002.422 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.099 | 2002.641 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.410 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2513 / 2487 | 21 / 35 | 4 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.447 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2513 / 2487 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.468 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2513 / 2487 | 32 / 51 | 7 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2513 / 2487 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.422 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2513 / 2487 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2513 / 2487 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.431 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2513 / 2487 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 29 | 4 / 6 | 4 / 4 | 1.176 / 1.172 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
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
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=0.gm · 50000 vertices / 525759 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525759 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.586 | 1327.445 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.585 | 1327.359 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24994 / 25006 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.434 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24994 / 25006 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.426 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.526 | 1327.441 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.463 | 1327.410 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24994 / 25006 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.660 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24994 / 25006 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.794 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24994 / 25006 | 46 / 51 | 11 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.796 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.681 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24994 / 25006 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.986 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.659 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24994 / 25006 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.639 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24994 / 25006 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.730 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 35 / 41 | 11 / 10 | 5 / 4 | 1.286 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=1.gm · 50000 vertices / 526588 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526588 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.563 | 1327.379 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.552 | 1327.434 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 24981 / 25019 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.350 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.654 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24981 / 25019 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.354 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.461 | 1327.387 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.487 | 1327.301 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.629 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 24981 / 25019 | 34 / 50 | 7 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.652 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24981 / 25019 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.803 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24981 / 25019 | 49 / 61 | 12 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.762 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.660 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24981 / 25019 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.968 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24981 / 25019 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.640 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24981 / 25019 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.712 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24981 / 25019 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.575 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 27 / 41 | 7 / 9 | 5 / 5 | 1.222 / 1.195 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 37 / 49 | 12 / 12 | 5 / 5 | 1.297 / 1.224 | 6 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=10.gm · 50000 vertices / 526563 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526563 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.540 | 1327.273 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.634 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.540 | 1327.336 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.641 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25268 / 24732 | 2 / 2 | 1 / 1 | 2 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.368 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25268 / 24732 | 2 / 2 | 1 / 1 | 2 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.462 | 1327.297 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.453 | 1327.270 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.630 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25268 / 24732 | 30 / 47 | 6 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.660 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25268 / 24732 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.794 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.660 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25268 / 24732 | 43 / 63 | 10 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.752 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.668 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25268 / 24732 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.989 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25268 / 24732 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.650 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25268 / 24732 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.742 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25268 / 24732 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 39 | 6 / 8 | 5 / 6 | 1.208 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 33 / 51 | 10 / 12 | 5 / 6 | 1.273 / 1.216 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=11.gm · 50000 vertices / 522281 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 522281 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.488 | 1327.238 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.540 | 1327.098 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.629 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24870 / 25130 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.331 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24870 / 25130 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.327 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.502 | 1327.238 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.440 | 1326.930 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24870 / 25130 | 34 / 47 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.358 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24870 / 25130 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24870 / 25130 | 46 / 67 | 11 / 13 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.750 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24870 / 25130 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.959 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24870 / 25130 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.640 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.599 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24870 / 25130 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.720 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24870 / 25130 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.566 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 27 / 39 | 7 / 8 | 5 / 6 | 1.222 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 35 / 54 | 11 / 13 | 5 / 6 | 1.286 / 1.222 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=12.gm · 50000 vertices / 527772 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 527772 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.739 | 1327.465 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.624 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.480 | 1327.371 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 24963 / 25037 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.302 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.630 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24963 / 25037 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.303 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.469 | 1327.469 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.463 | 1327.305 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.618 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 24963 / 25037 | 30 / 46 | 6 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.398 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24963 / 25037 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.776 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.660 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24963 / 25037 | 43 / 56 | 10 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.734 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24963 / 25037 | 29 / 39 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.981 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24963 / 25037 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.654 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.614 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24963 / 25037 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.727 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24963 / 25037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 38 | 6 / 8 | 5 / 5 | 1.208 / 1.184 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 33 / 45 | 10 / 11 | 5 / 5 | 1.273 / 1.222 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 31 | 7 / 8 | 3 / 3 | 1.273 / 1.226 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=13.gm · 50000 vertices / 525003 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525003 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.462 | 1327.312 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.637 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.545 | 1327.191 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25136 / 24864 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.312 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.598 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25136 / 24864 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.310 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.606 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.442 | 1327.293 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.518 | 1327.059 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.618 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25136 / 24864 | 34 / 47 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.391 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.653 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25136 / 24864 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.775 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25136 / 24864 | 46 / 72 | 11 / 14 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.754 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25136 / 24864 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.981 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25136 / 24864 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.641 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25136 / 24864 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.720 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25136 / 24864 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.586 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 27 / 39 | 7 / 8 | 5 / 6 | 1.222 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 35 / 58 | 11 / 14 | 5 / 6 | 1.286 / 1.224 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=14.gm · 50000 vertices / 526968 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526968 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.554 | 1327.395 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.542 | 1327.359 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25061 / 24939 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.337 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25061 / 24939 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.362 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.452 | 1327.137 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.606 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.463 | 1327.113 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25061 / 24939 | 34 / 47 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.380 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25061 / 24939 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25061 / 24939 | 46 / 63 | 11 / 13 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.757 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25061 / 24939 | 32 / 42 | 8 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.982 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.653 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25061 / 24939 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.638 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.606 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25061 / 24939 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.721 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25061 / 24939 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 27 / 39 | 7 / 8 | 5 / 6 | 1.222 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 35 / 50 | 11 / 13 | 5 / 5 | 1.286 / 1.240 | 5 / 7 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 33 | 8 / 9 | 3 / 3 | 1.292 / 1.242 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=15.gm · 50000 vertices / 525568 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525568 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.533 | 1327.336 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.543 | 1327.340 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.350 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.352 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.570 | 1327.316 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.447 | 1327.172 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24962 / 25038 | 34 / 52 | 7 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.372 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24962 / 25038 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.787 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24962 / 25038 | 42 / 58 | 10 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.740 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.659 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24962 / 25038 | 32 / 43 | 8 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.988 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.649 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.722 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 27 / 43 | 7 / 9 | 5 / 6 | 1.222 / 1.186 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 32 / 46 | 10 / 12 | 5 / 4 | 1.281 / 1.239 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 34 | 8 / 9 | 3 / 3 | 1.292 / 1.235 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=16.gm · 50000 vertices / 524594 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 524594 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.551 | 1327.035 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.643 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.561 | 1327.176 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 24919 / 25081 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.358 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24919 / 25081 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.356 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.457 | 1327.242 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.602 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.445 | 1327.172 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 24919 / 25081 | 34 / 47 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.389 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24919 / 25081 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.796 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24919 / 25081 | 47 / 59 | 11 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.741 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.669 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24919 / 25081 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.977 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.648 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24919 / 25081 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.650 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24919 / 25081 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.721 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24919 / 25081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.566 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 27 / 39 | 7 / 8 | 5 / 6 | 1.222 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 36 / 48 | 11 / 11 | 5 / 6 | 1.278 / 1.208 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=17.gm · 50000 vertices / 527400 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 527400 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.529 | 1327.516 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.636 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.498 | 1327.441 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.645 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.372 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.378 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.615 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.509 | 1327.402 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.642 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.486 | 1327.488 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.628 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 24962 / 25038 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24962 / 25038 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.659 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24962 / 25038 | 41 / 62 | 10 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.742 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.659 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24962 / 25038 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.979 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.641 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.600 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24962 / 25038 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.720 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24962 / 25038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 31 / 50 | 10 / 12 | 4 / 5 | 1.290 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=18.gm · 50000 vertices / 526864 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526864 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.573 | 1327.305 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.582 | 1327.223 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.631 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24867 / 25133 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.329 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24867 / 25133 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.347 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.466 | 1327.297 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.472 | 1327.281 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24867 / 25133 | 30 / 52 | 6 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.367 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.655 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24867 / 25133 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.801 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.659 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24867 / 25133 | 43 / 62 | 10 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.744 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.660 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24867 / 25133 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.991 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.671 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24867 / 25133 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.649 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24867 / 25133 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.773 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24867 / 25133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 43 | 6 / 9 | 5 / 6 | 1.208 / 1.186 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 33 / 50 | 10 / 12 | 5 / 5 | 1.273 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=19.gm · 50000 vertices / 525539 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525539 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.544 | 1327.316 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.625 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.492 | 1327.160 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.630 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25098 / 24902 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25098 / 24902 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.396 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.469 | 1327.301 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.488 | 1327.301 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25098 / 24902 | 44 / 41 | 9 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25098 / 24902 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.772 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25098 / 24902 | 52 / 54 | 12 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.754 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.652 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25098 / 24902 | 29 / 43 | 7 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.981 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25098 / 24902 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.649 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25098 / 24902 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.722 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25098 / 24902 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 35 / 34 | 9 / 7 | 7 / 5 | 1.229 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 40 / 43 | 12 / 11 | 6 / 4 | 1.275 / 1.233 | 6 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 34 | 7 / 9 | 3 / 3 | 1.273 / 1.235 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=2.gm · 50000 vertices / 524507 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 524507 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.560 | 1327.184 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.634 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.560 | 1327.316 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25147 / 24853 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.296 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.613 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25147 / 24853 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.313 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.613 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.443 | 1327.316 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.464 | 1327.316 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25147 / 24853 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.378 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25147 / 24853 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.784 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25147 / 24853 | 44 / 51 | 10 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.734 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25147 / 24853 | 30 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.971 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.659 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25147 / 24853 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.686 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25147 / 24853 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.714 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25147 / 24853 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.565 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 34 / 41 | 10 / 10 | 5 / 4 | 1.265 / 1.220 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 32 | 7 / 8 | 3 / 3 | 1.261 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=20.gm · 50000 vertices / 523291 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 523291 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.539 | 1327.191 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.497 | 1327.242 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25087 / 24913 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.357 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.600 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25087 / 24913 | 4 / 2 | 1 / 1 | 4 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.601 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.445 | 1327.312 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.521 | 1327.312 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25087 / 24913 | 39 / 52 | 8 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.388 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.653 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25087 / 24913 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.767 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.652 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25087 / 24913 | 51 / 64 | 12 / 14 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.742 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25087 / 24913 | 32 / 43 | 8 / 10 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.991 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25087 / 24913 | 4 / 2 | 1 / 1 | 4 / 2 | — / — | 0.648 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25087 / 24913 | 4 / 2 | 1 / 1 | 4 / 2 | — / — | 0.741 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25087 / 24913 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | even | true | true | false | - |

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
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 31 / 43 | 8 / 9 | 6 / 6 | 1.226 / 1.186 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39 / 50 | 12 / 14 | 6 / 5 | 1.282 / 1.260 | 5 / 8 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 33 | 8 / 10 | 3 / 3 | 1.292 / 1.273 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 3 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 4 / 2 | 4.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=21.gm · 50000 vertices / 526826 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526826 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.551 | 1327.254 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.624 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.518 | 1327.305 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25032 / 24968 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.314 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25032 / 24968 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.309 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.487 | 1327.438 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.455 | 1327.180 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25032 / 24968 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.391 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.651 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25032 / 24968 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.796 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.660 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25032 / 24968 | 48 / 57 | 12 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.748 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.659 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25032 / 24968 | 34 / 42 | 9 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.973 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.653 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25032 / 24968 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.650 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25032 / 24968 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.741 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25032 / 24968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 27 / 34 | 7 / 7 | 5 / 5 | 1.222 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 36 / 45 | 12 / 12 | 5 / 4 | 1.306 / 1.244 | 5 / 7 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 25 / 33 | 9 / 9 | 3 / 3 | 1.320 / 1.242 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=22.gm · 50000 vertices / 526732 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526732 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.550 | 1327.395 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.634 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.530 | 1327.477 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25075 / 24925 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.326 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25075 / 24925 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.320 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.491 | 1327.410 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.483 | 1327.348 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.629 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25075 / 24925 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25075 / 24925 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.673 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25075 / 24925 | 42 / 51 | 10 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.725 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25075 / 24925 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.960 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25075 / 24925 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.641 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25075 / 24925 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.723 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25075 / 24925 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 32 / 41 | 10 / 10 | 5 / 4 | 1.281 / 1.220 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=23.gm · 50000 vertices / 525611 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525611 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.511 | 1327.352 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.625 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.541 | 1327.230 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.631 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25005 / 24995 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.367 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.599 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25005 / 24995 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.372 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.599 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.443 | 1327.375 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.506 | 1327.387 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25005 / 24995 | 39 / 41 | 8 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.378 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25005 / 24995 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.775 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.657 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25005 / 24995 | 46 / 55 | 11 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.758 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.668 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25005 / 24995 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.998 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25005 / 24995 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.640 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25005 / 24995 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.720 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25005 / 24995 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.575 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 35 / 44 | 11 / 11 | 5 / 4 | 1.286 / 1.227 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=24.gm · 50000 vertices / 524843 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 524843 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.552 | 1327.312 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.643 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.553 | 1327.195 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25006 / 24994 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.400 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25006 / 24994 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.395 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.493 | 1327.172 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.481 | 1327.125 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25006 / 24994 | 30 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.368 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25006 / 24994 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.783 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.649 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25006 / 24994 | 37 / 57 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.734 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.660 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25006 / 24994 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.982 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25006 / 24994 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.638 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.598 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25006 / 24994 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.742 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25006 / 24994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.576 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 30 | 6 / 6 | 5 / 5 | 1.208 / 1.167 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 46 | 9 / 11 | 4 / 5 | 1.286 / 1.217 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=3.gm · 50000 vertices / 525193 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525193 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.532 | 1327.211 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.623 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.542 | 1327.207 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25141 / 24859 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.337 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25141 / 24859 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.333 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.463 | 1327.168 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.444 | 1327.270 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25141 / 24859 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.669 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25141 / 24859 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.788 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25141 / 24859 | 46 / 67 | 11 / 14 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.760 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25141 / 24859 | 32 / 45 | 8 / 10 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.970 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.662 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25141 / 24859 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.639 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25141 / 24859 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.712 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25141 / 24859 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 35 / 53 | 11 / 14 | 5 / 5 | 1.286 / 1.245 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 35 | 8 / 10 | 3 / 3 | 1.292 / 1.257 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=4.gm · 50000 vertices / 525345 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525345 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.566 | 1327.367 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.637 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.566 | 1327.328 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25085 / 24915 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.452 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25085 / 24915 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.455 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.473 | 1327.234 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.505 | 1327.344 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25085 / 24915 | 44 / 47 | 9 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.389 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.650 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25085 / 24915 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.774 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25085 / 24915 | 53 / 57 | 13 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.724 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.670 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25085 / 24915 | 34 / 40 | 9 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.992 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.652 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25085 / 24915 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.651 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25085 / 24915 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.714 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25085 / 24915 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.586 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 35 / 39 | 9 / 8 | 7 / 6 | 1.229 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 40 / 46 | 13 / 11 | 6 / 5 | 1.300 / 1.217 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 25 / 32 | 9 / 8 | 3 / 3 | 1.320 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=5.gm · 50000 vertices / 525412 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525412 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.521 | 1327.348 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.625 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.541 | 1327.266 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.631 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24904 / 25096 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.357 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24904 / 25096 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.352 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.464 | 1327.355 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.509 | 1327.215 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24904 / 25096 | 35 / 46 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.376 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.658 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24904 / 25096 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.795 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.682 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24904 / 25096 | 46 / 57 | 11 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.742 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24904 / 25096 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.970 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.652 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24904 / 25096 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.639 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24904 / 25096 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.720 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24904 / 25096 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.567 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 28 / 38 | 7 / 8 | 6 / 5 | 1.214 / 1.184 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 35 / 46 | 11 / 11 | 5 / 5 | 1.286 / 1.217 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=6.gm · 50000 vertices / 525810 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525810 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.523 | 1327.355 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.624 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.594 | 1327.191 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25170 / 24830 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.319 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.609 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25170 / 24830 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.320 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.600 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.486 | 1327.289 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.498 | 1327.254 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25170 / 24830 | 39 / 47 | 8 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.371 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25170 / 24830 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.786 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25170 / 24830 | 46 / 57 | 11 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.748 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.661 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25170 / 24830 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.974 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.656 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25170 / 24830 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.650 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.607 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25170 / 24830 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.722 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25170 / 24830 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.575 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 31 / 39 | 8 / 8 | 6 / 6 | 1.226 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 35 / 46 | 11 / 11 | 5 / 5 | 1.286 / 1.217 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=7.gm · 50000 vertices / 526107 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 526107 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.561 | 1327.262 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.624 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.560 | 1327.336 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.642 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 24983 / 25017 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.346 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.612 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 24983 / 25017 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.355 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.613 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.506 | 1327.246 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.476 | 1327.086 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 24983 / 25017 | 39 / 47 | 8 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24983 / 25017 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 24983 / 25017 | 41 / 59 | 10 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.735 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24983 / 25017 | 32 / 42 | 8 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.981 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.651 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 24983 / 25017 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.640 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 24983 / 25017 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.722 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 24983 / 25017 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 31 / 39 | 8 / 8 | 6 / 6 | 1.226 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 31 / 47 | 10 / 12 | 4 / 5 | 1.290 / 1.234 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 33 | 8 / 9 | 3 / 3 | 1.292 / 1.242 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=8.gm · 50000 vertices / 525548 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525548 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.517 | 1327.312 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.625 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.568 | 1327.340 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.630 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 25066 / 24934 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.353 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.611 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 25066 / 24934 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.345 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.601 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.435 | 1327.188 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.610 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.537 | 1327.156 | - | false | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 25066 / 24934 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.661 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25066 / 24934 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.788 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.642 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 25066 / 24934 | 46 / 66 | 12 / 14 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.742 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.671 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25066 / 24934 | 34 / 45 | 9 / 10 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.982 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 25066 / 24934 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.648 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 25066 / 24934 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.721 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 25066 / 24934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 34 / 52 | 12 / 14 | 4 / 5 | 1.324 / 1.250 | 6 / 7 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 25 / 35 | 9 / 10 | 3 / 3 | 1.320 / 1.257 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(50000,_10,_1,_20)id=9.gm · 50000 vertices / 525378 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 525378 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.533 | 1327.320 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.636 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.533 | 1327.207 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting+pre+iter | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 25035 / 24965 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.383 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.605 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 25035 / 24965 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 1.355 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.631 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.493 | 1327.320 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.620 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.467 | 1327.348 | - | true | - | - | Solver failed: failed to build the Even host U^6_{15,6} |
| lifting-sym+pre+iter | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.619 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 25035 / 24965 | 34 / 47 | 7 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 1.399 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.653 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 25035 / 24965 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.785 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.649 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 25035 / 24965 | 50 / 57 | 12 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 1.731 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.669 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 25035 / 24965 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.979 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.650 | 58.574 | even | true | true | false | - |
| zielonka | complete | 25035 / 24965 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.651 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.618 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 25035 / 24965 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.722 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 25035 / 24965 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.575 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 27 / 39 | 7 / 8 | 5 / 6 | 1.222 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 38 / 46 | 12 / 11 | 5 / 5 | 1.289 / 1.217 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/recursiveladder(100).gm · 500 vertices / 1097 edges · 8 complete · 8 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 500 | 1097 | 302 | 302 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.624 | 1386.805 | - | - | - | - | Solver failed: failed to build the Even host U^9_{8,152} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.625 | 1386.984 | - | - | - | - | preprocess: residual=500 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.573 | 1386.996 | - | - | - | - | Solver failed: failed to build the Even host U^9_{8,152} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.296 | 1386.926 | - | - | - | - | preprocess: residual=500 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.308 | 1386.988 | - | - | - | - | Solver failed: failed to build the Even host U^9_{8,152} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.366 | 1387.113 | - | - | - | - | preprocess: residual=500 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.394 | 1386.879 | - | - | - | - | Solver failed: failed to build the Even host U^9_{8,152} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.310 | 1387.113 | - | - | - | - | preprocess: residual=500 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| pm-strahler | complete | 0 / 500 | 0 / 26755 | 0 / 301 | 0 / 153 | k=3, t=2, depth=151 / k=3, t=2, depth=152 | 8.081 | 58.574 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 500 | 0 / 26454 | 0 / 301 | 0 / 152 | k=3, t=2, depth=150 / k=3, t=2, depth=151 | 8.032 | 58.574 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 500 | 0 / 25125 | 0 / 289 | 0 / 153 | k=3, t=2, depth=151 / k=3, t=2, depth=152 | 7.841 | 58.574 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 500 | 0 / 24836 | 0 / 289 | 0 / 152 | k=3, t=2, depth=150 / k=3, t=2, depth=151 | 7.811 | 58.574 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 500 | 0 / 22229 | 0 / 251 | 0 / 153 | bits=2, depth=151 / bits=2, depth=152 | 1.021 | 58.574 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 500 | 0 / 21978 | 0 / 251 | 0 / 152 | bits=2, depth=150 / bits=2, depth=151 | 1.037 | 58.574 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 500 | 0 / 183 | 0 / 6 | 0 / 153 | bits=1, depth=151 / bits=1, depth=152 | 0.565 | 58.574 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 500 | 0 / 177 | 0 / 6 | 0 / 152 | bits=1, depth=150 / bits=1, depth=151 | 0.566 | 58.574 | odd | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler | 0 / 26454 | 0 / 301 | 0 / 6 | 0.000 / 1.011 | 0 / 166 | 0 / 153 | 0.000 / 153.000 | 0 / 3 |
| pm-strahler+pre | 0 / 26153 | 0 / 301 | 0 / 6 | 0.000 / 1.011 | 0 / 166 | 0 / 152 | 0.000 / 152.000 | 0 / 3 |
| pm-strahler+iter | 0 / 24836 | 0 / 289 | 0 / 4 | 0.000 / 1.012 | 0 / 160 | 0 / 153 | 0.000 / 153.000 | 0 / 3 |
| pm-strahler+pre+iter | 0 / 24547 | 0 / 289 | 0 / 4 | 0.000 / 1.012 | 0 / 160 | 0 / 152 | 0.000 / 152.000 | 0 / 3 |
| pm-succinct | 0 / 21978 | 0 / 251 | 0 / 4 | 0.000 / 1.011 | 0 / 246 | 0 / 153 | 0.000 / 153.000 | 0 / 3 |
| pm-succinct+pre | 0 / 21727 | 0 / 251 | 0 / 4 | 0.000 / 1.012 | 0 / 246 | 0 / 152 | 0.000 / 152.000 | 0 / 3 |
| pm-succinct+iter | 0 / 177 | 0 / 6 | 0 / 2 | 0.000 / 1.028 | 0 / 5 | 0 / 153 | 0.000 / 153.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 171 | 0 / 6 | 0 / 2 | 0.000 / 1.029 | 0 / 5 | 0 / 152 | 0.000 / 152.000 | 0 / 2 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/recursiveladder(200).gm · 1000 vertices / 2197 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 2197 | 602 | 602 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.364 | 1305.781 | - | - | - | - | Solver failed: failed to build the Even host U^10_{9,302} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.343 | 1305.820 | - | - | - | - | preprocess: residual=1000 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.364 | 1305.570 | - | - | - | - | Solver failed: failed to build the Even host U^10_{9,302} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.144 | 1305.699 | - | - | - | - | preprocess: residual=1000 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 109.184 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 108.254 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 109.172 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 108.328 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.152 | 1305.844 | - | - | - | - | Solver failed: failed to build the Even host U^10_{9,302} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.212 | 1305.824 | - | - | - | - | preprocess: residual=1000 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.182 | 1305.844 | - | - | - | - | Solver failed: failed to build the Even host U^10_{9,302} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.138 | 1305.828 | - | - | - | - | preprocess: residual=1000 shaved_even=0 shaved_odd=0 single=0 loops=0 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.000 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct | complete | 0 / 1000 | 0 / 86954 | 0 / 501 | 0 / 303 | bits=2, depth=301 / bits=2, depth=302 | 5.102 | 74.398 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 1000 | 0 / 86453 | 0 / 501 | 0 / 302 | bits=2, depth=300 / bits=2, depth=301 | 5.155 | 74.059 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 1000 | 0 / 333 | 0 / 6 | 0 / 303 | bits=1, depth=301 / bits=1, depth=302 | 1.677 | 58.574 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 1000 | 0 / 327 | 0 / 6 | 0 / 302 | bits=1, depth=300 / bits=1, depth=301 | 1.678 | 58.574 | odd | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-succinct | 0 / 86453 | 0 / 501 | 0 / 4 | 0.000 / 1.006 | 0 / 496 | 0 / 303 | 0.000 / 303.000 | 0 / 3 |
| pm-succinct+pre | 0 / 85952 | 0 / 501 | 0 / 4 | 0.000 / 1.006 | 0 / 496 | 0 / 302 | 0.000 / 302.000 | 0 / 3 |
| pm-succinct+iter | 0 / 327 | 0 / 6 | 0 / 2 | 0.000 / 1.015 | 0 / 5 | 0 / 303 | 0.000 / 303.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 321 | 0 / 6 | 0 / 2 | 0.000 / 1.016 | 0 / 5 | 0 / 302 | 0.000 / 302.000 | 0 / 2 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=0.gm · 1000 vertices / 9357 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 9357 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.275 | 1307.297 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.285 | 1307.293 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 487 / 513 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.866 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 487 / 513 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.856 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.240 | 1307.230 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.241 | 1307.230 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 487 / 513 | 1501 / 2001 | 3 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 487 / 513 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 487 / 513 | 1500 / 1998 | 3 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 487 / 513 | 1500 / 1998 | 3 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 487 / 513 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 487 / 513 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1498 / 1997 | 3 / 4 | 3 / 4 | 1.001 / 1.002 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1497 / 1994 | 3 / 4 | 2 / 2 | 1.001 / 1.002 | 2 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1497 / 1994 | 3 / 4 | 2 / 2 | 1.001 / 1.002 | 2 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=1.gm · 1000 vertices / 6860 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 6860 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.257 | 1306.387 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.235 | 1306.523 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 461 / 539 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.901 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 461 / 539 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.906 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.215 | 1306.504 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.245 | 1306.383 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 461 / 539 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 461 / 539 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 461 / 539 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 461 / 539 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.424 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 461 / 539 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 461 / 539 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 461 / 539 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 2495 | 4 / 5 | 4 / 4 | 1.002 / 1.002 | 1 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=10.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.136 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.137 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.137 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.123 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=11.gm · 1000 vertices / 6176 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 6176 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.279 | 1306.473 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.288 | 1306.352 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 531 / 469 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.987 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 531 / 469 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.989 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.219 | 1306.496 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.227 | 1306.496 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 531 / 469 | 2999 / 2500 | 6 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.455 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 531 / 469 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 531 / 469 | 2991 / 2495 | 6 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.421 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 531 / 469 | 2991 / 2495 | 6 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 531 / 469 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 531 / 469 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 531 / 469 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 2993 / 2495 | 6 / 5 | 4 / 4 | 1.002 / 1.002 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2985 / 2490 | 6 / 5 | 2 / 2 | 1.002 / 1.002 | 5 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2985 / 2490 | 6 / 5 | 2 / 2 | 1.002 / 1.002 | 5 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=12.gm · 1000 vertices / 6504 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 6504 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.242 | 1306.504 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.251 | 1306.359 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 518 / 482 | 3 / 2 | 1 / 1 | 3 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.917 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 518 / 482 | 3 / 2 | 1 / 1 | 3 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.928 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.222 | 1306.500 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.252 | 1306.500 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 518 / 482 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.436 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 518 / 482 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 518 / 482 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 518 / 482 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 518 / 482 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 518 / 482 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 518 / 482 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |

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
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1997 / 2495 | 4 / 5 | 4 / 4 | 1.002 / 1.002 | 1 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=13.gm · 1000 vertices / 7851 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7851 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.239 | 1306.441 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.259 | 1306.617 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 486 / 514 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.892 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 486 / 514 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.875 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.244 | 1306.309 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.246 | 1306.559 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 486 / 514 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.436 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 486 / 514 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 486 / 514 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.425 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 486 / 514 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 486 / 514 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 486 / 514 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 1997 | 4 / 4 | 4 / 4 | 1.002 / 1.002 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=14.gm · 1000 vertices / 7808 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7808 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.253 | 1306.512 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.241 | 1306.449 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 496 / 504 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.887 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 496 / 504 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.877 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.239 | 1306.445 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.257 | 1306.438 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 496 / 504 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 496 / 504 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 496 / 504 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 496 / 504 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.417 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 496 / 504 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 496 / 504 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 496 / 504 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1997 / 1997 | 4 / 4 | 4 / 4 | 1.002 / 1.002 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=15.gm · 1000 vertices / 7854 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7854 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.285 | 1306.488 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.284 | 1306.309 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 489 / 511 | 5 / 3 | 1 / 1 | 5 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.968 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 489 / 511 | 5 / 3 | 1 / 1 | 5 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.970 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.252 | 1306.531 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.278 | 1306.516 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 489 / 511 | 2500 / 2500 | 5 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 489 / 511 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 489 / 511 | 2495 / 2495 | 5 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 489 / 511 | 2495 / 2495 | 5 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 489 / 511 | 5 / 3 | 1 / 1 | 5 / 3 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 489 / 511 | 5 / 3 | 1 / 1 | 5 / 3 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 489 / 511 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 4 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 3 | 5.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 4 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 3 | 5.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 2495 / 2495 | 5 / 5 | 4 / 4 | 1.002 / 1.002 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2490 / 2490 | 5 / 5 | 2 / 2 | 1.002 / 1.002 | 4 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2490 / 2490 | 5 / 5 | 2 / 2 | 1.002 / 1.002 | 4 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 4 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 3 | 5.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 4 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 3 | 5.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=16.gm · 1000 vertices / 8630 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 8630 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.251 | 1306.473 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.241 | 1306.484 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 528 / 472 | 4 / 1 | 1 / 1 | 4 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.960 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 528 / 472 | 4 / 1 | 1 / 1 | 4 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.968 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.239 | 1306.484 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.238 | 1306.469 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 528 / 472 | 2500 / 2001 | 5 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 528 / 472 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 528 / 472 | 2495 / 2498 | 5 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.432 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 528 / 472 | 2495 / 2498 | 5 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 528 / 472 | 4 / 1 | 1 / 1 | 4 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 528 / 472 | 4 / 1 | 1 / 1 | 4 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 1 | 4.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 1 | 4.000 / 1.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 2495 / 1997 | 5 / 4 | 4 / 4 | 1.002 / 1.002 | 2 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2490 / 2493 | 5 / 5 | 2 / 3 | 1.002 / 1.002 | 4 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2490 / 2493 | 5 / 5 | 2 / 3 | 1.002 / 1.002 | 4 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 3 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 1 | 4.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 3 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 1 | 4.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

