# pgsolver, part 3

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=8.gm · 10000 vertices / 105449 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105449 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.134 | 1212.793 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.134 | 1212.695 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5032 / 4968 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.538 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5032 / 4968 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.549 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.099 | 1212.734 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.109 | 1212.719 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5032 / 4968 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.550 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5032 / 4968 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5032 / 4968 | 41 / 50 | 10 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5032 / 4968 | 32 / 33 | 8 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5032 / 4968 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.442 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5032 / 4968 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 31 / 41 | 10 / 9 | 4 / 5 | 1.290 / 1.195 | 5 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 27 | 8 / 6 | 3 / 3 | 1.292 / 1.185 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(10000,_10,_1,_20)id=9.gm · 10000 vertices / 105071 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105071 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.151 | 1212.773 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.139 | 1212.895 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting+pre+iter | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5072 / 4928 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.538 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5072 / 4928 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.538 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.109 | 1212.773 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.096 | 1212.895 | - | false | - | - | Solver failed: failed to build the Even host U^6_{13,6} |
| lifting-sym+pre+iter | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5072 / 4928 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.537 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5072 / 4928 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.452 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5072 / 4928 | 32 / 48 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.567 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.431 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5072 / 4928 | 27 / 37 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5072 / 4928 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5072 / 4928 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.443 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5072 / 4928 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 25 / 39 | 7 / 9 | 4 / 4 | 1.240 / 1.205 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 30 | 6 / 7 | 3 / 3 | 1.238 / 1.200 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=0.gm · 20000 vertices / 208373 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 208373 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.976 | 1089.199 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.934 | 1089.391 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9975 / 10025 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.723 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9975 / 10025 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.731 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.043 | 1089.523 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.899 | 1089.398 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9975 / 10025 | 33 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.746 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9975 / 10025 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.526 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9975 / 10025 | 39 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.792 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.486 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9975 / 10025 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9975 / 10025 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9975 / 10025 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.506 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9975 / 10025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 26 / 34 | 7 / 7 | 4 / 5 | 1.231 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 30 / 41 | 9 / 10 | 4 / 4 | 1.267 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=1.gm · 20000 vertices / 209336 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209336 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.951 | 1089.434 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.490 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.949 | 1089.492 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 9976 / 10024 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 9976 / 10024 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.734 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.916 | 1089.559 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.974 | 1089.398 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 9976 / 10024 | 39 / 42 | 8 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.756 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.495 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9976 / 10024 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.528 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 9976 / 10024 | 35 / 59 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9976 / 10024 | 30 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.577 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 9976 / 10024 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 9976 / 10024 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 9976 / 10024 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 31 / 35 | 8 / 7 | 6 / 6 | 1.226 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
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
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=10.gm · 20000 vertices / 210993 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210993 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.969 | 1089.406 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.978 | 1089.594 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9978 / 10022 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.735 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9978 / 10022 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.744 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.930 | 1089.680 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.898 | 1089.520 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9978 / 10022 | 30 / 42 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.727 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9978 / 10022 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.535 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9978 / 10022 | 34 / 63 | 8 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9978 / 10022 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.579 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9978 / 10022 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9978 / 10022 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9978 / 10022 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 35 | 6 / 7 | 5 / 6 | 1.208 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 51 | 8 / 12 | 4 / 6 | 1.269 / 1.216 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=11.gm · 20000 vertices / 211061 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 211061 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.957 | 1089.656 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.905 | 1089.375 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9965 / 10035 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.735 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9965 / 10035 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.722 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.913 | 1089.656 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.903 | 1089.648 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9965 / 10035 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.735 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9965 / 10035 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.526 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9965 / 10035 | 50 / 62 | 13 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.805 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9965 / 10035 | 33 / 40 | 9 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.587 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9965 / 10035 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9965 / 10035 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.506 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9965 / 10035 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 37 / 50 | 13 / 12 | 5 / 5 | 1.324 / 1.220 | 7 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 9 / 8 | 3 / 3 | 1.333 / 1.219 | 5 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=12.gm · 20000 vertices / 210481 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210481 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.019 | 1089.406 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.905 | 1089.457 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10130 / 9870 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.725 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10130 / 9870 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.722 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.986 | 1089.504 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.995 | 1089.621 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10130 / 9870 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.723 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10130 / 9870 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.516 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10130 / 9870 | 38 / 54 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.804 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.472 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10130 / 9870 | 29 / 43 | 7 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10130 / 9870 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.484 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10130 / 9870 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10130 / 9870 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 29 / 43 | 9 / 11 | 4 / 4 | 1.276 / 1.233 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 34 | 7 / 9 | 3 / 3 | 1.273 / 1.235 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=13.gm · 20000 vertices / 209796 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209796 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.970 | 1089.605 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.968 | 1089.488 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9843 / 10157 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9843 / 10157 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.732 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.942 | 1089.633 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.959 | 1089.332 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9843 / 10157 | 21 / 46 | 4 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.734 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9843 / 10157 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.516 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9843 / 10157 | 32 / 57 | 7 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.796 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9843 / 10157 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.579 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9843 / 10157 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9843 / 10157 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.506 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9843 / 10157 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 38 | 4 / 8 | 4 / 5 | 1.176 / 1.184 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 46 | 7 / 11 | 4 / 5 | 1.240 / 1.217 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=14.gm · 20000 vertices / 211569 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 211569 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.969 | 1089.504 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.957 | 1089.582 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9883 / 10117 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.714 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9883 / 10117 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.712 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.901 | 1089.707 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.966 | 1089.719 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9883 / 10117 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.715 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.497 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9883 / 10117 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.526 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9883 / 10117 | 32 / 55 | 7 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9883 / 10117 | 27 / 38 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9883 / 10117 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.484 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9883 / 10117 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.526 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9883 / 10117 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 34 | 6 / 7 | 5 / 5 | 1.208 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 44 | 7 / 11 | 4 / 5 | 1.240 / 1.227 | 3 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 30 | 6 / 8 | 3 / 3 | 1.238 / 1.233 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=15.gm · 20000 vertices / 210626 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210626 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.934 | 1089.582 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.944 | 1089.648 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10111 / 9889 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.793 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10111 / 9889 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.751 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.924 | 1089.645 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.913 | 1089.535 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10111 / 9889 | 30 / 42 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.727 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10111 / 9889 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.524 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.483 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10111 / 9889 | 39 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.802 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10111 / 9889 | 30 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.576 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10111 / 9889 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10111 / 9889 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10111 / 9889 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 35 | 6 / 7 | 5 / 6 | 1.208 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 30 / 41 | 9 / 10 | 4 / 4 | 1.267 / 1.220 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 32 | 7 / 8 | 3 / 3 | 1.261 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=16.gm · 20000 vertices / 209878 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209878 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.939 | 1089.414 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.928 | 1089.434 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10023 / 9977 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.746 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10023 / 9977 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.755 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.919 | 1089.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.480 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.916 | 1089.555 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10023 / 9977 | 25 / 42 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.714 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.494 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10023 / 9977 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.515 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10023 / 9977 | 34 / 57 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.807 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10023 / 9977 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.581 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10023 / 9977 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.483 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10023 / 9977 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.514 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10023 / 9977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 35 | 5 / 7 | 4 / 6 | 1.200 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 46 | 8 / 11 | 4 / 5 | 1.269 / 1.217 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=17.gm · 20000 vertices / 210250 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210250 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.946 | 1089.363 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.944 | 1089.629 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10089 / 9911 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.723 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10089 / 9911 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.731 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.927 | 1089.523 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.948 | 1089.516 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10089 / 9911 | 30 / 52 | 6 / 9 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.712 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.483 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10089 / 9911 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.516 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10089 / 9911 | 36 / 58 | 8 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.802 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10089 / 9911 | 27 / 38 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.577 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10089 / 9911 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10089 / 9911 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.516 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10089 / 9911 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 28 / 46 | 8 / 12 | 4 / 4 | 1.250 / 1.239 | 4 / 7 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 30 | 6 / 8 | 3 / 3 | 1.238 / 1.233 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=18.gm · 20000 vertices / 209474 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209474 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.043 | 1089.312 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.909 | 1089.523 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.479 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9991 / 10009 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.735 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9991 / 10009 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.731 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.923 | 1089.609 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.913 | 1089.469 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9991 / 10009 | 30 / 42 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.724 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9991 / 10009 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.525 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9991 / 10009 | 36 / 51 | 8 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.797 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9991 / 10009 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.486 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9991 / 10009 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9991 / 10009 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.506 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9991 / 10009 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 24 / 35 | 6 / 7 | 5 / 6 | 1.208 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 41 | 8 / 10 | 4 / 4 | 1.250 / 1.220 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=19.gm · 20000 vertices / 208566 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 208566 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.948 | 1089.449 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.958 | 1089.297 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 9958 / 10042 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.736 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 9958 / 10042 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.920 | 1089.574 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.907 | 1089.555 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 9958 / 10042 | 29 / 47 | 6 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.716 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9958 / 10042 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.525 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 9958 / 10042 | 38 / 59 | 9 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.804 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.477 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9958 / 10042 | 29 / 42 | 7 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.473 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 9958 / 10042 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 9958 / 10042 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.504 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 9958 / 10042 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 23 / 39 | 6 / 8 | 4 / 6 | 1.217 / 1.179 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 29 / 47 | 9 / 12 | 4 / 5 | 1.276 / 1.234 | 5 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 33 | 7 / 9 | 3 / 3 | 1.273 / 1.242 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=2.gm · 20000 vertices / 209484 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209484 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.947 | 1089.492 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.956 | 1089.438 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10024 / 9976 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.736 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10024 / 9976 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.732 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.913 | 1089.566 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.956 | 1089.434 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10024 / 9976 | 34 / 41 | 7 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.715 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10024 / 9976 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.517 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10024 / 9976 | 32 / 53 | 7 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.805 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10024 / 9976 | 27 / 42 | 6 / 9 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.580 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.477 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10024 / 9976 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.491 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10024 / 9976 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.505 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10024 / 9976 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 25 / 42 | 7 / 11 | 4 / 4 | 1.240 / 1.238 | 3 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 33 | 6 / 9 | 3 / 3 | 1.238 / 1.242 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=20.gm · 20000 vertices / 210190 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210190 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.006 | 1089.582 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.923 | 1089.457 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10055 / 9945 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.725 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10055 / 9945 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.723 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.900 | 1089.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.900 | 1089.637 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10055 / 9945 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.724 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10055 / 9945 | 6 / 0 | 1 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.535 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10055 / 9945 | 34 / 61 | 8 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.806 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.487 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10055 / 9945 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.579 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10055 / 9945 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10055 / 9945 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.507 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10055 / 9945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | even | true | true | false | - |

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
| pm-strahler+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 26 / 49 | 8 / 12 | 4 / 5 | 1.269 / 1.224 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=21.gm · 20000 vertices / 209585 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209585 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.964 | 1089.461 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.955 | 1089.520 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 9961 / 10039 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.724 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 9961 / 10039 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.722 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.915 | 1089.535 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.922 | 1089.465 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 9961 / 10039 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.713 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9961 / 10039 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.516 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.493 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 9961 / 10039 | 38 / 57 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.479 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9961 / 10039 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.575 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 9961 / 10039 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 9961 / 10039 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.504 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 9961 / 10039 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 29 / 46 | 9 / 11 | 4 / 5 | 1.276 / 1.217 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=22.gm · 20000 vertices / 210186 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210186 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.960 | 1089.480 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.499 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.970 | 1089.512 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9953 / 10047 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.735 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9953 / 10047 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.734 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.954 | 1089.578 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.892 | 1089.582 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9953 / 10047 | 25 / 35 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.725 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9953 / 10047 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.527 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9953 / 10047 | 41 / 51 | 10 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.806 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9953 / 10047 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.576 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.487 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9953 / 10047 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9953 / 10047 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.507 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9953 / 10047 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 29 | 5 / 6 | 4 / 4 | 1.200 / 1.172 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 31 / 41 | 10 / 10 | 4 / 4 | 1.290 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=23.gm · 20000 vertices / 210544 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210544 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.936 | 1089.508 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.926 | 1089.641 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10048 / 9952 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.724 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10048 / 9952 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.732 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.917 | 1089.516 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.969 | 1089.496 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.491 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10048 / 9952 | 30 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.724 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10048 / 9952 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.517 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10048 / 9952 | 40 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.807 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10048 / 9952 | 30 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10048 / 9952 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.483 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10048 / 9952 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.505 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 31 / 41 | 9 / 10 | 5 / 4 | 1.258 / 1.220 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 32 | 7 / 8 | 3 / 3 | 1.261 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=24.gm · 20000 vertices / 209780 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209780 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.979 | 1089.570 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.927 | 1089.594 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10106 / 9894 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.747 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10106 / 9894 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.742 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.911 | 1089.586 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.904 | 1089.414 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10106 / 9894 | 30 / 46 | 6 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.725 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.488 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10106 / 9894 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.526 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10106 / 9894 | 36 / 57 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.805 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.488 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10106 / 9894 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.573 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10106 / 9894 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.484 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10106 / 9894 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.514 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10106 / 9894 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 28 / 46 | 8 / 11 | 4 / 5 | 1.250 / 1.217 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=3.gm · 20000 vertices / 210196 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210196 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.957 | 1089.641 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=2, t=1 / H=3, K=2, t=1 | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.956 | 1089.516 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=2, t=1 / H=3, K=2, t=1 | 0.485 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 9943 / 10057 | 1 / 4 | 1 / 1 | 1 / 4 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.756 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=1, t=0 / H=3, K=1, t=0 | 0.486 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 9943 / 10057 | 1 / 4 | 1 / 1 | 1 / 4 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.737 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=1, t=0 / H=3, K=1, t=0 | 0.478 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.905 | 1089.520 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=2, t=1 / H=3, K=2, t=1 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.945 | 1089.648 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | H=4, K=2, t=1 / H=3, K=2, t=1 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 9943 / 10057 | 30 / 38 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.713 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9943 / 10057 | 0 / 10 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.487 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9943 / 10057 | 0 / 10 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.527 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9943 / 10057 | 0 / 10 | 0 / 2 | 0 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 9943 / 10057 | 38 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9943 / 10057 | 0 / 10 | 0 / 2 | 0 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9943 / 10057 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.579 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9943 / 10057 | 0 / 10 | 0 / 2 | 0 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 9943 / 10057 | 1 / 4 | 1 / 1 | 1 / 4 | — / — | 0.487 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.472 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 9943 / 10057 | 1 / 4 | 1 / 1 | 1 / 4 | — / — | 0.570 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 9943 / 10057 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.448 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 0 / 3 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 4 | 1.000 / 4.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 0 / 3 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 4 | 1.000 / 4.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 24 / 31 | 6 / 7 | 5 / 4 | 1.208 / 1.194 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 8 | 0 / 2 | 0 / 2 | 0.000 / 1.125 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-strahler+iter | 0 / 8 | 0 / 2 | 0 / 2 | 0.000 / 1.125 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 8 | 0 / 2 | 0 / 2 | 0.000 / 1.125 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-succinct | 29 / 41 | 9 / 10 | 4 / 4 | 1.276 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 8 | 0 / 2 | 0 / 2 | 0.000 / 1.125 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 8 | 0 / 2 | 0 / 2 | 0.000 / 1.125 | 0 / 1 | 0 / 7 | 0.000 / 7.000 | 0 / 2 |
| zielonka | 0 / 3 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 4 | 1.000 / 4.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 0 / 3 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 4 | 1.000 / 4.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=4.gm · 20000 vertices / 210006 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210006 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.966 | 1089.613 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.945 | 1089.477 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.483 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10048 / 9952 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10048 / 9952 | 1 / 6 | 1 / 1 | 1 / 6 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.732 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.912 | 1089.551 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.923 | 1089.543 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10048 / 9952 | 30 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.736 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10048 / 9952 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.535 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10048 / 9952 | 36 / 61 | 8 / 12 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.795 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10048 / 9952 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10048 / 9952 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10048 / 9952 | 1 / 6 | 1 / 1 | 1 / 6 | — / — | 0.516 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10048 / 9952 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 28 / 49 | 8 / 12 | 4 / 5 | 1.250 / 1.224 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 5 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 6 | 1.000 / 6.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=5.gm · 20000 vertices / 207502 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 207502 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.927 | 1089.145 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.997 | 1089.344 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 9838 / 10162 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 9838 / 10162 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.720 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.911 | 1089.473 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.894 | 1089.160 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 9838 / 10162 | 30 / 42 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.718 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9838 / 10162 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.526 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 9838 / 10162 | 38 / 51 | 9 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.791 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9838 / 10162 | 29 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 9838 / 10162 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 9838 / 10162 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.506 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 9838 / 10162 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 35 | 6 / 7 | 5 / 6 | 1.208 / 1.171 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 29 / 41 | 9 / 10 | 4 / 4 | 1.276 / 1.220 | 5 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 32 | 7 / 8 | 3 / 3 | 1.273 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=6.gm · 20000 vertices / 210077 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210077 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.021 | 1089.355 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.957 | 1089.633 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10138 / 9862 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.736 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10138 / 9862 | 3 / 2 | 1 / 1 | 3 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.742 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.920 | 1089.438 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.472 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.914 | 1089.504 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10138 / 9862 | 25 / 35 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.714 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.489 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10138 / 9862 | 6 / 0 | 1 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.581 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10138 / 9862 | 36 / 55 | 8 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.805 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.486 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10138 / 9862 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10138 / 9862 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.486 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10138 / 9862 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.525 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10138 / 9862 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 20 / 29 | 5 / 6 | 4 / 4 | 1.200 / 1.172 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 44 | 8 / 11 | 4 / 4 | 1.250 / 1.227 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=7.gm · 20000 vertices / 209265 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209265 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.967 | 1089.500 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.966 | 1089.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10025 / 9975 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.734 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10025 / 9975 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.735 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.922 | 1089.508 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.901 | 1089.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10025 / 9975 | 26 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.725 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10025 / 9975 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.525 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10025 / 9975 | 37 / 51 | 8 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.794 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.477 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10025 / 9975 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10025 / 9975 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.485 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10025 / 9975 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.505 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10025 / 9975 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 21 / 30 | 5 / 6 | 5 / 5 | 1.190 / 1.167 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 29 / 41 | 8 / 10 | 5 / 4 | 1.241 / 1.220 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 32 | 6 / 8 | 3 / 3 | 1.238 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=8.gm · 20000 vertices / 208604 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 208604 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.929 | 1089.469 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.938 | 1089.367 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 9982 / 10018 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.725 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9982 / 10018 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.721 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.921 | 1089.477 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.932 | 1089.559 | - | true | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 9982 / 10018 | 25 / 46 | 5 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.734 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 9982 / 10018 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.535 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 9982 / 10018 | 39 / 65 | 9 / 13 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.803 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.475 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 9982 / 10018 | 30 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.577 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| zielonka | complete | 9982 / 10018 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 9982 / 10018 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.505 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9982 / 10018 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 30 / 52 | 9 / 13 | 4 / 5 | 1.267 / 1.231 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 32 | 7 / 8 | 3 / 3 | 1.261 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(20000,_10,_1,_20)id=9.gm · 20000 vertices / 209557 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 209557 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.956 | 1089.445 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.935 | 1089.438 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting+pre+iter | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 10066 / 9934 | 2 / 2 | 1 / 1 | 2 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 10066 / 9934 | 2 / 2 | 1 / 1 | 2 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.781 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.918 | 1089.574 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.906 | 1089.555 | - | false | - | - | Solver failed: failed to build the Even host U^6_{14,6} |
| lifting-sym+pre+iter | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 10066 / 9934 | 29 / 41 | 6 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.723 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.495 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10066 / 9934 | 6 / 0 | 1 / 0 | 6 / 0 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.525 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.485 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 10066 / 9934 | 37 / 57 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.801 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10066 / 9934 | 32 / 40 | 8 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.578 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.484 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 10066 / 9934 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.496 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 10066 / 9934 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.515 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 10066 / 9934 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 23 / 34 | 6 / 7 | 4 / 5 | 1.217 / 1.176 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 46 | 9 / 11 | 4 / 5 | 1.286 / 1.217 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 32 | 8 / 8 | 3 / 3 | 1.292 / 1.219 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=0.gm · 5000 vertices / 51817 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 51817 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.872 | 2002.160 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.005 | 2002.430 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2538 / 2462 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2538 / 2462 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.421 | 2002.648 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 8.010 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 13.679 | 2002.598 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.811 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2538 / 2462 | 26 / 31 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.502 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.460 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2538 / 2462 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.415 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2538 / 2462 | 32 / 39 | 7 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.495 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.471 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2538 / 2462 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.442 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.422 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2538 / 2462 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2538 / 2462 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 21 / 26 | 5 / 5 | 5 / 5 | 1.190 / 1.154 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=1.gm · 5000 vertices / 52230 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52230 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.615 | 2002.762 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.582 | 2002.773 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2509 / 2491 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2509 / 2491 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.466 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.423 | 2002.480 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.038 | 2002.785 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2509 / 2491 | 26 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.496 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.449 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2509 / 2491 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.467 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2509 / 2491 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.469 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2509 / 2491 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2509 / 2491 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2509 / 2491 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2509 / 2491 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |

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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=10.gm · 5000 vertices / 52199 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52199 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.613 | 2002.629 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.582 | 2002.812 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2516 / 2484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.497 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2516 / 2484 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.474 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.222 | 2002.559 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.871 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.417 | 2002.402 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2516 / 2484 | 25 / 46 | 5 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.545 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.464 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2516 / 2484 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2516 / 2484 | 35 / 46 | 8 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.495 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2516 / 2484 | 30 / 40 | 7 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.425 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2516 / 2484 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2516 / 2484 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2516 / 2484 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 27 / 37 | 8 / 9 | 4 / 4 | 1.259 / 1.216 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 23 / 32 | 7 / 8 | 3 / 3 | 1.261 / 1.219 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=11.gm · 5000 vertices / 52094 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52094 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.554 | 2002.520 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.563 | 2002.777 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2514 / 2486 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.484 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2514 / 2486 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.474 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.272 | 2002.645 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.526 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.138 | 2002.754 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2514 / 2486 | 29 / 36 | 6 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.490 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.459 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2514 / 2486 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2514 / 2486 | 36 / 47 | 8 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.465 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2514 / 2486 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2514 / 2486 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2514 / 2486 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2514 / 2486 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 28 / 38 | 8 / 9 | 4 / 4 | 1.250 / 1.211 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 29 | 6 / 7 | 3 / 3 | 1.238 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=12.gm · 5000 vertices / 52910 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52910 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.662 | 2002.750 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.427 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.661 | 2002.520 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2511 / 2489 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.479 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2511 / 2489 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.469 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.448 | 2002.508 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.525 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.052 | 2002.684 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2511 / 2489 | 21 / 30 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.491 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.449 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2511 / 2489 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.447 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2511 / 2489 | 27 / 43 | 6 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2511 / 2489 | 27 / 37 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.436 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.410 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2511 / 2489 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2511 / 2489 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2511 / 2489 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 21 / 35 | 6 / 8 | 3 / 4 | 1.238 / 1.200 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 30 | 6 / 7 | 3 / 3 | 1.238 / 1.200 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=13.gm · 5000 vertices / 52120 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52120 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.577 | 2002.672 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.545 | 2002.734 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2488 / 2512 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.484 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2488 / 2512 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.204 | 2002.809 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.079 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.661 | 2002.668 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.437 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2488 / 2512 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.510 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.426 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2488 / 2512 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2488 / 2512 | 32 / 46 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.473 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2488 / 2512 | 27 / 40 | 6 / 8 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2488 / 2512 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2488 / 2512 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2488 / 2512 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=14.gm · 5000 vertices / 52546 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52546 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.530 | 2002.758 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.430 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.561 | 2002.723 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.438 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2548 / 2452 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.508 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.427 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2548 / 2452 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.024 | 2002.621 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.030 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.469 | 2002.727 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.855 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2548 / 2452 | 25 / 36 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.484 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.422 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2548 / 2452 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2548 / 2452 | 36 / 42 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.486 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2548 / 2452 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.445 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2548 / 2452 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2548 / 2452 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.424 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2548 / 2452 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=15.gm · 5000 vertices / 52512 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52512 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.575 | 2002.676 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.545 | 2002.633 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2533 / 2467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2533 / 2467 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.220 | 2002.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.023 | 2002.508 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2533 / 2467 | 21 / 41 | 4 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.498 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2533 / 2467 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.456 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2533 / 2467 | 32 / 44 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.466 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2533 / 2467 | 27 / 33 | 6 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2533 / 2467 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2533 / 2467 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.465 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2533 / 2467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 25 / 36 | 7 / 8 | 4 / 4 | 1.240 / 1.194 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 27 | 6 / 6 | 3 / 3 | 1.238 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=16.gm · 5000 vertices / 52856 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52856 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.626 | 2002.711 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.636 | 2002.727 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2498 / 2502 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2498 / 2502 | 6 / 2 | 1 / 1 | 6 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.497 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.448 | 2002.586 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.900 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.398 | 2002.672 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.458 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2498 / 2502 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.495 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.424 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2498 / 2502 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.424 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2498 / 2502 | 32 / 48 | 7 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.486 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2498 / 2502 | 23 / 37 | 5 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2498 / 2502 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2498 / 2502 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2498 / 2502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 25 | 5 / 5 | 4 / 4 | 1.200 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 25 / 39 | 7 / 9 | 4 / 4 | 1.240 / 1.205 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 3 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 30 | 5 / 7 | 3 / 3 | 1.222 / 1.200 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=17.gm · 5000 vertices / 52630 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52630 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.571 | 2002.371 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.580 | 2002.602 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2538 / 2462 | 1 / 3 | 1 / 1 | 1 / 3 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2538 / 2462 | 1 / 3 | 1 / 1 | 1 / 3 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.274 | 2002.539 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.009 | 2002.527 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2538 / 2462 | 25 / 35 | 5 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.477 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.446 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2538 / 2462 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.468 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2538 / 2462 | 29 / 51 | 7 / 10 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.463 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2538 / 2462 | 29 / 36 | 7 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.431 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2538 / 2462 | 1 / 3 | 1 / 1 | 1 / 3 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2538 / 2462 | 1 / 3 | 1 / 1 | 1 / 3 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 20 / 29 | 5 / 6 | 4 / 4 | 1.200 / 1.172 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 41 | 7 / 10 | 3 / 4 | 1.273 / 1.220 | 4 / 6 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 22 / 29 | 7 / 7 | 3 / 3 | 1.273 / 1.207 | 4 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=18.gm · 5000 vertices / 52787 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52787 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.598 | 2002.551 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.607 | 2002.289 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2460 / 2540 | 1 / 3 | 1 / 1 | 1 / 3 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2460 / 2540 | 1 / 3 | 1 / 1 | 1 / 3 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.309 | 2002.625 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.066 | 2002.691 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2460 / 2540 | 21 / 36 | 4 / 6 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.474 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.463 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2460 / 2540 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.469 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2460 / 2540 | 28 / 47 | 6 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.478 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.415 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2460 / 2540 | 23 / 36 | 5 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.432 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2460 / 2540 | 1 / 3 | 1 / 1 | 1 / 3 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2460 / 2540 | 1 / 3 | 1 / 1 | 1 / 3 | — / — | 0.426 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2460 / 2540 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 17 / 30 | 4 / 6 | 4 / 5 | 1.176 / 1.167 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 38 | 6 / 9 | 4 / 4 | 1.227 / 1.211 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 29 | 5 / 7 | 3 / 3 | 1.222 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 2 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 3 | 1.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=19.gm · 5000 vertices / 52742 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52742 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.631 | 2002.570 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.630 | 2002.578 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2535 / 2465 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2535 / 2465 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.488 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.202 | 2002.723 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.012 | 2002.594 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2535 / 2465 | 25 / 44 | 5 / 8 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.499 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.448 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2535 / 2465 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.449 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2535 / 2465 | 37 / 58 | 9 / 11 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.473 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2535 / 2465 | 32 / 33 | 8 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2535 / 2465 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2535 / 2465 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2535 / 2465 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 20 / 36 | 5 / 8 | 4 / 4 | 1.200 / 1.194 | 2 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 28 / 47 | 9 / 11 | 4 / 4 | 1.286 / 1.213 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24 / 27 | 8 / 6 | 3 / 3 | 1.292 / 1.185 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=2.gm · 5000 vertices / 52450 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52450 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.534 | 2002.594 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.649 | 2002.734 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2493 / 2507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.477 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2493 / 2507 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.277 | 2002.480 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.546 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.068 | 2002.574 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2493 / 2507 | 30 / 30 | 6 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.487 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.461 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2493 / 2507 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.446 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2493 / 2507 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.472 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.410 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2493 / 2507 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2493 / 2507 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2493 / 2507 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2493 / 2507 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 24 / 25 | 6 / 5 | 5 / 4 | 1.208 / 1.160 | 2 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=20.gm · 5000 vertices / 52605 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52605 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.592 | 2002.648 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.550 | 2002.652 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2559 / 2441 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2559 / 2441 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.224 | 2002.535 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.012 | 2002.605 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2559 / 2441 | 25 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.499 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.449 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2559 / 2441 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.448 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2559 / 2441 | 32 / 42 | 7 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.475 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2559 / 2441 | 27 / 36 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2559 / 2441 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.411 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2559 / 2441 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

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
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=21.gm · 5000 vertices / 52507 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52507 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.739 | 2002.691 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.672 | 2002.500 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2438 / 2562 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2438 / 2562 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.499 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.174 | 2002.641 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.373 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.781 | 2002.574 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.187 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2438 / 2562 | 26 / 30 | 5 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.495 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2438 / 2562 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2438 / 2562 | 28 / 47 | 6 / 9 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2438 / 2562 | 23 / 36 | 5 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.454 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.432 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2438 / 2562 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2438 / 2562 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2438 / 2562 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 21 / 25 | 5 / 5 | 5 / 4 | 1.190 / 1.160 | 1 / 2 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 38 | 6 / 9 | 4 / 4 | 1.227 / 1.211 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 3 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 29 | 5 / 7 | 3 / 3 | 1.222 / 1.207 | 3 / 4 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=22.gm · 5000 vertices / 52289 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52289 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.447 | 2002.758 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.410 | 2002.387 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2501 / 2499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.476 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2501 / 2499 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.221 | 2002.469 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.015 | 2002.723 | - | false | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2501 / 2499 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.476 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.447 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2501 / 2499 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.457 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2501 / 2499 | 32 / 39 | 7 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.473 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2501 / 2499 | 23 / 33 | 5 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2501 / 2499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2501 / 2499 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2501 / 2499 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 25 / 32 | 7 / 7 | 4 / 4 | 1.240 / 1.188 | 4 / 3 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 27 | 5 / 6 | 3 / 3 | 1.222 / 1.185 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(5000,_10,_1,_20)id=23.gm · 5000 vertices / 52399 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52399 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.644 | 2002.766 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.439 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.685 | 2002.586 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting+pre+iter | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2595 / 2405 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.486 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2595 / 2405 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.490 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.278 | 2002.539 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.008 | 2002.652 | - | true | - | - | Solver failed: failed to build the Even host U^6_{12,6} |
| lifting-sym+pre+iter | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2595 / 2405 | 25 / 41 | 5 / 7 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.490 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.448 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2595 / 2405 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.458 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2595 / 2405 | 36 / 39 | 8 / 8 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.472 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2595 / 2405 | 27 / 33 | 6 / 7 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.431 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.415 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2595 / 2405 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.410 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2595 / 2405 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2595 / 2405 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

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
| pm-succinct | 28 / 31 | 8 / 8 | 4 / 4 | 1.250 / 1.226 | 4 / 5 | 6 / 7 | 6.000 / 7.000 | 3 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 26 | 6 / 7 | 3 / 3 | 1.238 / 1.231 | 3 / 5 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

