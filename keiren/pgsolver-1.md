# pgsolver, part 1

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/cliquegame(100).gm · 100 vertices / 9900 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 100 | 9900 | 100 | 99 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.377 | 1222.074 | - | true | - | - | Solver failed: failed to build the Even host U^7_{6,51} |
| lifting+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.366 | 1222.121 | - | true | - | - | Solver failed: failed to build the Even host U^7_{6,51} |
| lifting+pre+iter | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 50 / 50 | 2 / 1 | 1 / 1 | 2 / 1 | H=51, K=1, t=0 / H=50, K=1, t=0 | 0.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 50 / 50 | 2 / 1 | 1 / 1 | 2 / 1 | H=51, K=1, t=0 / H=50, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.381 | 1221.953 | - | true | - | - | Solver failed: failed to build the Even host U^7_{6,51} |
| lifting-sym+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.338 | 1222.082 | - | true | - | - | Solver failed: failed to build the Even host U^7_{6,51} |
| lifting-sym+pre+iter | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 50 / 50 | 51 / 51 | 1 / 1 | 51 / 51 | k=1, t=1, depth=50 / k=1, t=1, depth=50 | 0.424 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=50 / k=1, t=1, depth=50 | 0.415 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 50 / 50 | 51 / 51 | 1 / 1 | 51 / 51 | k=1, t=1, depth=50 / k=1, t=1, depth=50 | 0.424 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=50 / k=1, t=1, depth=50 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 50 / 50 | 51 / 51 | 1 / 1 | 51 / 51 | bits=1, depth=50 / bits=1, depth=50 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=50 / bits=0, depth=50 | 0.396 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 50 / 50 | 51 / 51 | 1 / 1 | 51 / 51 | bits=1, depth=50 / bits=1, depth=50 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=50 / bits=0, depth=50 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 50 / 50 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 50 / 50 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 50 / 50 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 50 / 50 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 51 / 51 | 51.000 / 51.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 50 / 50 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 51 / 51 | 51.000 / 51.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 50 / 50 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 51 / 51 | 51.000 / 51.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 50 / 50 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 51 / 51 | 51.000 / 51.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(1000).gm · 1000 vertices / 999000 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 999000 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.389 | 1327.066 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.550 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.418 | 1326.992 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 11.601 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.526 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 11.531 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.523 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.269 | 1327.023 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.526 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.268 | 1327.102 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.524 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 500 / 500 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 9.012 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.533 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 500 / 500 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 4.764 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.513 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 500 / 500 | 501 / 501 | 1 / 1 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 9.416 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.534 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 500 / 500 | 501 / 501 | 1 / 1 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 4.973 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.525 | 58.574 | even | true | true | false | - |
| zielonka | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.535 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.503 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.617 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.515 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(200).gm · 200 vertices / 39800 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 200 | 39800 | 200 | 199 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.813 | 1482.645 | - | true | - | - | Solver failed: failed to build the Even host U^8_{7,101} |
| lifting+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.833 | 1482.699 | - | true | - | - | Solver failed: failed to build the Even host U^8_{7,101} |
| lifting+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=101, K=1, t=0 / H=100, K=1, t=0 | 0.505 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=101, K=1, t=0 / H=100, K=1, t=0 | 0.506 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.795 | 1482.578 | - | true | - | - | Solver failed: failed to build the Even host U^8_{7,101} |
| lifting-sym+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.784 | 1482.586 | - | true | - | - | Solver failed: failed to build the Even host U^8_{7,101} |
| lifting-sym+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 100 / 100 | 101 / 101 | 1 / 1 | 101 / 101 | k=1, t=1, depth=100 / k=1, t=1, depth=100 | 0.475 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=100 / k=1, t=1, depth=100 | 0.416 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 100 / 100 | 101 / 101 | 1 / 1 | 101 / 101 | k=1, t=1, depth=100 / k=1, t=1, depth=100 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=100 / k=1, t=1, depth=100 | 0.415 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 100 / 100 | 101 / 101 | 1 / 1 | 101 / 101 | bits=1, depth=100 / bits=1, depth=100 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=100 / bits=0, depth=100 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 100 / 100 | 101 / 101 | 1 / 1 | 101 / 101 | bits=1, depth=100 / bits=1, depth=100 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=100 / bits=0, depth=100 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 100 / 100 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 101 / 101 | 101.000 / 101.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 100 / 100 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 101 / 101 | 101.000 / 101.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 100 / 100 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 101 / 101 | 101.000 / 101.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 100 / 100 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 101 / 101 | 101.000 / 101.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(500).gm · 500 vertices / 249500 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 500 | 249500 | 500 | 499 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.523 | 1393.480 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,251} |
| lifting+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.522 | 1393.551 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,251} |
| lifting+pre+iter | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 250 / 250 | 2 / 1 | 1 / 1 | 2 / 1 | H=251, K=1, t=0 / H=250, K=1, t=0 | 1.852 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.469 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 250 / 250 | 2 / 1 | 1 / 1 | 2 / 1 | H=251, K=1, t=0 / H=250, K=1, t=0 | 1.851 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.447 | 1393.496 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,251} |
| lifting-sym+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.449 | 1393.621 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,251} |
| lifting-sym+pre+iter | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 250 / 250 | 251 / 251 | 1 / 1 | 251 / 251 | k=1, t=1, depth=250 / k=1, t=1, depth=250 | 1.485 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=250 / k=1, t=1, depth=250 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 250 / 250 | 251 / 251 | 1 / 1 | 251 / 251 | k=1, t=1, depth=250 / k=1, t=1, depth=250 | 0.958 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=250 / k=1, t=1, depth=250 | 0.421 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 250 / 250 | 251 / 251 | 1 / 1 | 251 / 251 | bits=1, depth=250 / bits=1, depth=250 | 1.556 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=250 / bits=0, depth=250 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 250 / 250 | 251 / 251 | 1 / 1 | 251 / 251 | bits=1, depth=250 / bits=1, depth=250 | 0.989 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=250 / bits=0, depth=250 | 0.401 | 58.574 | even | true | true | false | - |
| zielonka | complete | 250 / 250 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 250 / 250 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.433 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 250 / 250 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 250 / 250 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 251 / 251 | 251.000 / 251.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 250 / 250 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 251 / 251 | 251.000 / 251.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 250 / 250 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 251 / 251 | 251.000 / 251.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 250 / 250 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 251 / 251 | 251.000 / 251.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(-u,_3).gm · 588 vertices / 1096 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 588 | 1096 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.970 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.557 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.960 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.567 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.384 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.463 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.463 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 76 / 512 | 2 / 33 | 1 / 23 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 76 / 512 | 0 / 31 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 76 / 512 | 0 / 31 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 76 / 512 | 0 / 31 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 76 / 512 | 2 / 25 | 1 / 17 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 76 / 512 | 0 / 23 | 0 / 16 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 76 / 512 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 76 / 512 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 76 / 512 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 76 / 512 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 1 / 10 | 1 / 23 | 1 / 15 | 1.000 / 3.200 | 0 / 2 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 22 | 0 / 15 | 0.000 / 3.333 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 9 | 0 / 22 | 0 / 15 | 0.000 / 3.333 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 22 | 0 / 15 | 0.000 / 3.333 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 1 / 8 | 1 / 17 | 1 / 7 | 1.000 / 3.000 | 0 / 4 | 2 / 3 | 2.000 / 3.000 | 1 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 16 | 0 / 7 | 0.000 / 3.143 | 0 / 4 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(-u,_4).gm · 2832 vertices / 5924 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2832 | 5924 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 12.372 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 7.983 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 12.359 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 8.076 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.585 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.451 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.614 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.460 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 272 / 2560 | 2 / 25 | 1 / 15 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 272 / 2560 | 0 / 31 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.426 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 272 / 2560 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.396 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 272 / 2560 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 272 / 2560 | 2 / 25 | 1 / 17 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 272 / 2560 | 0 / 23 | 0 / 16 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 272 / 2560 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 272 / 2560 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 272 / 2560 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 272 / 2560 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.372 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 1 / 10 | 1 / 15 | 1 / 9 | 1.000 / 2.400 | 0 / 2 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 22 | 0 / 15 | 0.000 / 3.333 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 1 / 8 | 1 / 17 | 1 / 7 | 1.000 / 3.000 | 0 / 4 | 2 / 3 | 2.000 / 3.000 | 1 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 16 | 0 / 7 | 0.000 / 3.143 | 0 / 4 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(-u,_5).gm · 16356 vertices / 38194 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16356 | 38194 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.453 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.465 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 29.409 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.804 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 29.334 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.775 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 1210 / 15146 | 2 / 33 | 1 / 23 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.616 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1210 / 15146 | 0 / 31 | 0 / 22 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.606 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1210 / 15146 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.506 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1210 / 15146 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.508 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 1210 / 15146 | 2 / 25 | 1 / 17 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.529 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1210 / 15146 | 0 / 23 | 0 / 16 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.528 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1210 / 15146 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.495 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1210 / 15146 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.476 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.423 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 1210 / 15146 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.422 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1210 / 15146 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.423 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 1 / 10 | 1 / 23 | 1 / 15 | 1.000 / 3.200 | 0 / 2 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 22 | 0 / 15 | 0.000 / 3.333 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 1 / 8 | 1 / 17 | 1 / 7 | 1.000 / 3.000 | 0 / 4 | 2 / 3 | 2.000 / 3.000 | 1 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 16 | 0 / 7 | 0.000 / 3.143 | 0 / 4 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(-u,_6).gm · 111456 vertices / 287964 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 111456 | 287964 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 6578 / 104878 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.942 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 6578 / 104878 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.911 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 6578 / 104878 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.008 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 6578 / 104878 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.987 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 6578 / 104878 | 2 / 25 | 1 / 15 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 1.987 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 6578 / 104878 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.141 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 6578 / 104878 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.109 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 6578 / 104878 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.076 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 6578 / 104878 | 2 / 25 | 1 / 17 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 2.202 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 6578 / 104878 | 0 / 23 | 0 / 16 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 2.213 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 6578 / 104878 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.856 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 6578 / 104878 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.554 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 6578 / 104878 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.708 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 6578 / 104878 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.707 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 6578 / 104878 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.823 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 6578 / 104878 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.822 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 10 | 1 / 15 | 1 / 9 | 1.000 / 2.400 | 0 / 2 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 1 / 8 | 1 / 17 | 1 / 7 | 1.000 / 3.000 | 0 / 4 | 2 / 3 | 2.000 / 3.000 | 1 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 16 | 0 / 7 | 0.000 / 3.143 | 0 / 4 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(-u,_7).gm · 876780 vertices / 2484252 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 876780 | 2484252 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 361.820 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 362.988 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 361.672 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.044 | 363.137 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 42556 / 834224 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.778 | 361.879 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 42556 / 834224 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.598 | 361.879 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 42556 / 834224 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 6.266 | 361.816 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 42556 / 834224 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.998 | 361.883 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 361.812 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.041 | 362.930 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 361.922 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 362.938 | - | false | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 373.551 | - | false | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 373.648 | - | false | - | - | deadline exceeded |
| pm-strahler+iter | complete | 42556 / 834224 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 15.085 | 366.863 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 42556 / 834224 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 14.989 | 365.398 | odd | false | true | false | - |
| pm-succinct | complete | 42556 / 834224 | 2 / 25 | 1 / 17 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 16.867 | 366.648 | odd | false | true | false | - |
| pm-succinct+pre | complete | 42556 / 834224 | 0 / 23 | 0 / 16 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 16.921 | 366.289 | odd | false | true | false | - |
| pm-succinct+iter | complete | 42556 / 834224 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 13.791 | 367.094 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 42556 / 834224 | 0 / 17 | 0 / 12 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 9.977 | 361.797 | odd | false | true | false | - |
| zielonka | complete | 42556 / 834224 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 2.516 | 361.883 | odd | false | true | false | - |
| zielonka+pre | complete | 42556 / 834224 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.621 | 361.945 | odd | false | true | false | - |
| zielonka-sym | complete | 42556 / 834224 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 3.367 | 361.941 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 42556 / 834224 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.223 | 361.945 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 1 / 8 | 1 / 17 | 1 / 7 | 1.000 / 3.000 | 0 / 4 | 2 / 3 | 2.000 / 3.000 | 1 / 3 |
| pm-succinct+pre | 0 / 7 | 0 / 16 | 0 / 7 | 0.000 / 3.143 | 0 / 4 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre+iter | 0 / 5 | 0 / 12 | 0 / 7 | 0.000 / 3.200 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(3).gm · 564 vertices / 950 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 564 | 950 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.172 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.667 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.150 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.683 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.536 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.431 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.536 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.435 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 507 / 57 | 8 / 3 | 7 / 1 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 507 / 57 | 8 / 3 | 7 / 1 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 507 / 57 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.412 | 58.574 | even | true | true | false | - |
| zielonka | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 507 / 57 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 507 / 57 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 2 | 7 / 1 | 7 / 1 | 7.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 2 | 7 / 1 | 7 / 1 | 7.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(4).gm · 2688 vertices / 4544 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2688 | 4544 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 27.942 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 22.088 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 28.126 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 22.159 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.922 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.767 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.931 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.797 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2369 / 319 | 13 / 3 | 12 / 1 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2369 / 319 | 13 / 3 | 12 / 1 | 2 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2369 / 319 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2369 / 319 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.383 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2369 / 319 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.372 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 2 | 12 / 1 | 12 / 1 | 12.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 2 | 12 / 1 | 12 / 1 | 12.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(5).gm · 15684 vertices / 26354 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15684 | 26354 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 13639 / 2045 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.753 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 13639 / 2045 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.465 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 13639 / 2045 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.686 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 13639 / 2045 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.477 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 13639 / 2045 | 18 / 3 | 17 / 1 | 2 / 3 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.678 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 0.627 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.506 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 0.515 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 13639 / 2045 | 18 / 3 | 17 / 1 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 0.544 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.527 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.495 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 13639 / 2045 | 18 / 0 | 17 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 0.484 | 58.574 | even | true | true | false | - |
| zielonka | complete | 13639 / 2045 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 13639 / 2045 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 13639 / 2045 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 13639 / 2045 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 2 | 17 / 1 | 17 / 1 | 17.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 2 | 17 / 1 | 17 / 1 | 17.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 17 / 0 | 17 / 0 | 17.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(6).gm · 108336 vertices / 180898 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 108336 | 180898 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 93381 / 14955 | 3 / 2 | 2 / 1 | 2 / 2 | H=2, K=2, t=1 / H=2, K=2, t=1 | 4.783 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 93381 / 14955 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.318 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 93381 / 14955 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 4.175 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 93381 / 14955 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.458 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 93381 / 14955 | 25 / 3 | 24 / 1 | 2 / 3 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 3.177 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 3.064 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 1.939 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 1.950 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 93381 / 14955 | 25 / 3 | 24 / 1 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 2.171 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 2.054 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 1.756 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 93381 / 14955 | 25 / 0 | 24 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 1.616 | 58.574 | even | true | true | false | - |
| zielonka | complete | 93381 / 14955 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.678 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 93381 / 14955 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.646 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 93381 / 14955 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 0.781 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 93381 / 14955 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.736 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 2 | 24 / 1 | 24 / 1 | 24.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 2 | 24 / 1 | 24 / 1 | 24.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 24 / 0 | 24 / 0 | 24.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/elevatorverification(7).gm · 861780 vertices / 1431610 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 861780 | 1431610 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 282.340 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 297.859 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 282.332 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 298.363 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 282.316 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 738323 / 123457 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 14.167 | 282.215 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 282.277 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 738323 / 123457 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 14.208 | 282.203 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 282.273 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 297.883 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 282.207 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.030 | 298.559 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 738323 / 123457 | 32 / 3 | 31 / 1 | 2 / 3 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 23.316 | 307.207 | even | - | - | false | - |
| pm-strahler+pre | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=3, t=4, depth=2 | 21.649 | 307.320 | even | - | - | false | - |
| pm-strahler+iter | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 11.667 | 306.008 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | k=2, t=4, depth=1 / k=2, t=4, depth=2 | 11.903 | 307.012 | even | - | - | false | - |
| pm-succinct | complete | 738323 / 123457 | 32 / 3 | 31 / 1 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 13.463 | 296.770 | even | - | - | false | - |
| pm-succinct+pre | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 12.570 | 296.887 | even | - | - | false | - |
| pm-succinct+iter | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 10.506 | 297.023 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 738323 / 123457 | 32 / 0 | 31 / 0 | 2 / 0 | bits=4, depth=1 / bits=4, depth=2 | 9.501 | 297.074 | even | - | - | false | - |
| zielonka | complete | 738323 / 123457 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 2.180 | 282.172 | even | - | - | false | - |
| zielonka+pre | complete | 738323 / 123457 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.953 | 282.062 | even | - | - | false | - |
| zielonka-sym | complete | 738323 / 123457 | 3 / 2 | 2 / 1 | 2 / 2 | — / — | 2.948 | 282.270 | even | - | - | false | - |
| zielonka-sym+pre | complete | 738323 / 123457 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 2.763 | 282.340 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 2 | 31 / 1 | 31 / 1 | 31.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 2 | 31 / 1 | 31 / 1 | 31.000 / 1.000 | 1 / 0 | 2 / 3 | 2.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 31 / 0 | 31 / 0 | 31.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 1 / 1 | 2 / 1 | 2 / 1 | 2.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(100,_100).gm · 30200 vertices / 80199 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30200 | 80199 | 202 | 201 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.026 | 1079.820 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,102} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.015 | 1079.938 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.035 | 1079.762 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,102} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.897 | 1079.934 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.853 | 1079.945 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,102} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.865 | 1079.871 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.853 | 1079.820 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,102} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.885 | 1079.945 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 30000 / 200 | 3132 / 0 | 31 / 0 | 102 / 0 | k=3, t=3, depth=101 / k=3, t=3, depth=101 | 1.185 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 30000 / 200 | 3132 / 0 | 31 / 0 | 102 / 0 | k=3, t=3, depth=101 / k=3, t=3, depth=101 | 1.174 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 30000 / 200 | 203 / 0 | 2 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 0.965 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 30000 / 200 | 304 / 0 | 3 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 0.963 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 85.340 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 85.223 | - | - | - | - | deadline exceeded |
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
| pm-strahler+iter | 3101 / 0 | 31 / 0 | 31 / 0 | 1.010 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 3101 / 0 | 31 / 0 | 31 / 0 | 1.010 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 201 / 0 | 2 / 0 | 2 / 0 | 1.005 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 301 / 0 | 3 / 0 | 3 / 0 | 1.007 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(100,_200).gm · 60400 vertices / 160599 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 60400 | 160599 | 202 | 201 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.443 | 1304.496 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,102} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.648 | 1304.711 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.442 | 1304.641 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,102} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.334 | 1304.676 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.265 | 1304.695 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,102} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.392 | 1304.668 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.328 | 1304.633 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,102} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.272 | 1304.648 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 60000 / 400 | 708 / 0 | 7 / 0 | 102 / 0 | k=5, t=3, depth=101 / k=5, t=3, depth=101 | 2.483 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 60000 / 400 | 607 / 0 | 6 / 0 | 102 / 0 | k=5, t=3, depth=101 / k=5, t=3, depth=101 | 2.488 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 60000 / 400 | 304 / 0 | 3 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 2.571 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 60000 / 400 | 203 / 0 | 2 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 2.562 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 170.375 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 169.605 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 701 / 0 | 7 / 0 | 7 / 0 | 1.009 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 601 / 0 | 6 / 0 | 6 / 0 | 1.008 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 301 / 0 | 3 / 0 | 3 / 0 | 1.007 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 201 / 0 | 2 / 0 | 2 / 0 | 1.005 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(100,_50).gm · 15100 vertices / 39999 edges · 6 complete · 10 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15100 | 39999 | 202 | 201 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.212 | 1208.977 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,102} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.191 | 1209.031 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.202 | 1208.980 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,102} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.007 | 1209.043 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.005 | 1208.844 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,102} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.069 | 1208.906 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.059 | 1208.984 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,102} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.970 | 1208.977 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 15000 / 100 | 1314 / 0 | 13 / 0 | 102 / 0 | k=2, t=3, depth=101 / k=2, t=3, depth=101 | 0.707 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 15000 / 100 | 1213 / 0 | 12 / 0 | 102 / 0 | k=2, t=3, depth=101 / k=2, t=3, depth=101 | 0.708 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 15000 / 100 | 304 / 0 | 3 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 0.574 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 15000 / 100 | 203 / 0 | 2 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 0.563 | 58.574 | even | - | - | false | - |
| zielonka | complete | 15000 / 100 | 5001 / 101 | 4901 / 1 | 101 / 101 | — / — | 18.113 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 15000 / 100 | 4901 / 101 | 4801 / 1 | 101 / 101 | — / — | 17.677 | 58.574 | even | - | - | false | - |
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
| pm-strahler+iter | 1301 / 0 | 13 / 0 | 13 / 0 | 1.009 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1201 / 0 | 12 / 0 | 12 / 0 | 1.009 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 301 / 0 | 3 / 0 | 3 / 0 | 1.007 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 201 / 0 | 2 / 0 | 2 / 0 | 1.005 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| zielonka | 100 / 100 | 50 / 1 | 50 / 1 | 50.000 / 1.000 | 100 / 0 | 2 / 101 | 51.510 / 101.000 | 2 / 1 |
| zielonka+pre | 100 / 100 | 49 / 1 | 49 / 1 | 49.000 / 1.000 | 100 / 0 | 2 / 101 | 51.510 / 101.000 | 2 / 1 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(100,_500).gm · 151000 vertices / 401799 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 151000 | 401799 | 202 | 201 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.269 | 1121.242 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,102} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.248 | 1121.465 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.247 | 1121.316 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,102} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.169 | 1121.457 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.138 | 1121.461 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,102} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.196 | 1121.445 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.136 | 1121.402 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,102} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.078 | 1121.527 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 150000 / 1000 | 2324 / 0 | 23 / 0 | 102 / 0 | k=4, t=5, depth=101 / k=4, t=5, depth=101 | 10.017 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 150000 / 1000 | 2223 / 0 | 22 / 0 | 102 / 0 | k=4, t=5, depth=101 / k=4, t=5, depth=101 | 10.039 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 150000 / 1000 | 304 / 0 | 3 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 13.242 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 150000 / 1000 | 203 / 0 | 2 / 0 | 102 / 0 | bits=1, depth=101 / bits=1, depth=101 | 13.474 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 398.199 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 398.695 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 2301 / 0 | 23 / 0 | 23 / 0 | 1.010 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 2201 / 0 | 22 / 0 | 22 / 0 | 1.010 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 301 / 0 | 3 / 0 | 3 / 0 | 1.007 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 201 / 0 | 2 / 0 | 2 / 0 | 1.005 / 0.000 | 1 / 0 | 102 / 0 | 102.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(200,_100).gm · 60200 vertices / 159999 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 60200 | 159999 | 402 | 401 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.470 | 1301.129 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,202} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.470 | 1301.109 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.480 | 1300.996 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,202} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.357 | 1300.988 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.250 | 1301.004 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,202} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.366 | 1301.129 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.393 | 1301.105 | - | - | - | - | Solver failed: failed to build the Even host U^16_{15,202} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.265 | 1301.184 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 60000 / 200 | 6232 / 0 | 31 / 0 | 202 / 0 | k=3, t=3, depth=201 / k=3, t=3, depth=201 | 3.056 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 60000 / 200 | 6232 / 0 | 31 / 0 | 202 / 0 | k=3, t=3, depth=201 / k=3, t=3, depth=201 | 3.053 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 60000 / 200 | 403 / 0 | 2 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 1.903 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 60000 / 200 | 604 / 0 | 3 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 1.907 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 141.062 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 141.207 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 6201 / 0 | 31 / 0 | 31 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 6201 / 0 | 31 / 0 | 31 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 401 / 0 | 2 / 0 | 2 / 0 | 1.002 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 601 / 0 | 3 / 0 | 3 / 0 | 1.003 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(200,_200).gm · 120400 vertices / 320399 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 120400 | 320399 | 402 | 401 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.741 | 1344.285 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,202} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.905 | 1344.270 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.904 | 1344.266 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,202} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.714 | 1344.277 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 69.242 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 69.191 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 69.223 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 69.297 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.602 | 1344.102 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,202} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.685 | 1344.289 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.756 | 1344.098 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,202} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.580 | 1344.285 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 120000 / 400 | 1408 / 0 | 7 / 0 | 202 / 0 | k=5, t=3, depth=201 / k=5, t=3, depth=201 | 6.939 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 120000 / 400 | 1207 / 0 | 6 / 0 | 202 / 0 | k=5, t=3, depth=201 / k=5, t=3, depth=201 | 6.895 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 120000 / 400 | 604 / 0 | 3 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 5.335 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 120000 / 400 | 403 / 0 | 2 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 5.292 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 276.230 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 276.242 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 1401 / 0 | 7 / 0 | 7 / 0 | 1.004 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1201 / 0 | 6 / 0 | 6 / 0 | 1.004 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 601 / 0 | 3 / 0 | 3 / 0 | 1.003 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 401 / 0 | 2 / 0 | 2 / 0 | 1.002 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(200,_50).gm · 30100 vertices / 79799 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30100 | 79799 | 402 | 401 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 1.935 | 1080.637 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,202} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.966 | 1080.637 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.987 | 1080.770 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,202} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.854 | 1080.766 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.799 | 1080.707 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,202} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.846 | 1080.629 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.905 | 1080.699 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,202} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.795 | 1080.633 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 30000 / 100 | 2614 / 0 | 13 / 0 | 202 / 0 | k=2, t=3, depth=201 / k=2, t=3, depth=201 | 1.582 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 30000 / 100 | 2413 / 0 | 12 / 0 | 202 / 0 | k=2, t=3, depth=201 / k=2, t=3, depth=201 | 1.553 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 30000 / 100 | 604 / 0 | 3 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 0.934 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 30000 / 100 | 403 / 0 | 2 / 0 | 202 / 0 | bits=1, depth=201 / bits=1, depth=201 | 0.926 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 70.750 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 70.301 | - | - | - | - | deadline exceeded |
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
| pm-strahler+iter | 2601 / 0 | 13 / 0 | 13 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 2401 / 0 | 12 / 0 | 12 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 601 / 0 | 3 / 0 | 3 / 0 | 1.003 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 401 / 0 | 2 / 0 | 2 / 0 | 1.002 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(200,_500).gm · 301000 vertices / 801599 edges · 2 complete · 14 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 301000 | 801599 | 402 | 401 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.701 | 1370.051 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,202} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.733 | 1370.117 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.717 | 1369.918 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,202} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.675 | 1369.805 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 103.863 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 103.859 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 103.719 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 103.738 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.582 | 1369.918 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,202} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.662 | 1370.047 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.613 | 1369.922 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,202} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.554 | 1370.035 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 103.684 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 103.809 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 300000 / 1000 | 4624 / 0 | 23 / 0 | 202 / 0 | k=4, t=5, depth=201 / k=4, t=5, depth=201 | 25.446 | 103.723 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 300000 / 1000 | 4423 / 0 | 22 / 0 | 202 / 0 | k=4, t=5, depth=201 / k=4, t=5, depth=201 | 25.287 | 103.680 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.684 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.605 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 103.742 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 103.738 | - | - | - | - | deadline exceeded |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.054 | 614.969 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.052 | 618.578 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.863 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 103.836 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 4601 / 0 | 23 / 0 | 23 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 4401 / 0 | 22 / 0 | 22 / 0 | 1.005 / 0.000 | 1 / 0 | 202 / 0 | 202.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(50,_100).gm · 15200 vertices / 40299 edges · 6 complete · 10 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15200 | 40299 | 102 | 101 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.232 | 1208.340 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,52} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.233 | 1208.629 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.180 | 1208.359 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,52} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.007 | 1208.426 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.033 | 1208.562 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,52} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.064 | 1208.691 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.039 | 1208.457 | - | - | - | - | Solver failed: failed to build the Even host U^14_{13,52} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.980 | 1208.484 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 15000 / 200 | 1582 / 0 | 31 / 0 | 52 / 0 | k=3, t=3, depth=51 / k=3, t=3, depth=51 | 0.666 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 15000 / 200 | 1582 / 0 | 31 / 0 | 52 / 0 | k=3, t=3, depth=51 / k=3, t=3, depth=51 | 0.656 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 15000 / 200 | 103 / 0 | 2 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 0.625 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 15000 / 200 | 154 / 0 | 3 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 0.625 | 58.574 | even | - | - | false | - |
| zielonka | complete | 15000 / 200 | 5001 / 51 | 4951 / 1 | 51 / 51 | — / — | 10.731 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 15000 / 200 | 4951 / 51 | 4901 / 1 | 51 / 51 | — / — | 10.581 | 58.574 | even | - | - | false | - |
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
| pm-strahler+iter | 1551 / 0 | 31 / 0 | 31 / 0 | 1.019 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1551 / 0 | 31 / 0 | 31 / 0 | 1.019 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 101 / 0 | 2 / 0 | 2 / 0 | 1.010 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 151 / 0 | 3 / 0 | 3 / 0 | 1.013 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| zielonka | 50 / 50 | 100 / 1 | 100 / 1 | 100.000 / 1.000 | 50 / 0 | 2 / 51 | 26.505 / 51.000 | 2 / 1 |
| zielonka+pre | 50 / 50 | 99 / 1 | 99 / 1 | 99.000 / 1.000 | 50 / 0 | 2 / 51 | 26.505 / 51.000 | 2 / 1 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(50,_200).gm · 30400 vertices / 80699 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30400 | 80699 | 102 | 101 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.023 | 1081.121 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,52} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.023 | 1081.250 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.022 | 1081.223 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,52} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.856 | 1081.305 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 1.798 | 1081.246 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,52} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.867 | 1081.137 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.880 | 1081.086 | - | - | - | - | Solver failed: failed to build the Even host U^15_{14,52} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.847 | 1081.227 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 30000 / 400 | 358 / 0 | 7 / 0 | 52 / 0 | k=5, t=3, depth=51 / k=5, t=3, depth=51 | 1.216 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 30000 / 400 | 307 / 0 | 6 / 0 | 52 / 0 | k=5, t=3, depth=51 / k=5, t=3, depth=51 | 1.207 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 30000 / 400 | 154 / 0 | 3 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 1.379 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 30000 / 400 | 103 / 0 | 2 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 1.342 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 104.492 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 104.383 | - | - | - | - | deadline exceeded |
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
| pm-strahler+iter | 351 / 0 | 7 / 0 | 7 / 0 | 1.017 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 301 / 0 | 6 / 0 | 6 / 0 | 1.017 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 151 / 0 | 3 / 0 | 3 / 0 | 1.013 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 101 / 0 | 2 / 0 | 2 / 0 | 1.010 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(50,_50).gm · 7600 vertices / 20099 edges · 8 complete · 8 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7600 | 20099 | 102 | 101 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.433 | 1373.289 | - | - | - | - | Solver failed: failed to build the Even host U^13_{12,52} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.465 | 1373.398 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.484 | 1373.418 | - | - | - | - | Solver failed: failed to build the Even host U^13_{12,52} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.267 | 1373.414 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.239 | 1373.281 | - | - | - | - | Solver failed: failed to build the Even host U^13_{12,52} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.347 | 1373.547 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.303 | 1373.281 | - | - | - | - | Solver failed: failed to build the Even host U^13_{12,52} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.223 | 1373.281 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 7500 / 100 | 664 / 0 | 13 / 0 | 52 / 0 | k=2, t=3, depth=51 / k=2, t=3, depth=51 | 0.471 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 7500 / 100 | 613 / 0 | 12 / 0 | 52 / 0 | k=2, t=3, depth=51 / k=2, t=3, depth=51 | 0.471 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 7500 / 100 | 154 / 0 | 3 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 0.441 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 7500 / 100 | 103 / 0 | 2 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 0.441 | 58.574 | even | - | - | false | - |
| zielonka | complete | 7500 / 100 | 2501 / 51 | 2451 / 1 | 51 / 51 | — / — | 3.204 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 7500 / 100 | 2451 / 51 | 2401 / 1 | 51 / 51 | — / — | 3.146 | 58.574 | even | - | - | false | - |
| zielonka-sym | complete | 7500 / 100 | 2501 / 51 | 2451 / 1 | 51 / 51 | — / — | 9.362 | 58.574 | even | - | - | false | - |
| zielonka-sym+pre | complete | 7500 / 100 | 2451 / 51 | 2401 / 1 | 51 / 51 | — / — | 9.172 | 58.574 | even | - | - | false | - |

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
| pm-strahler+iter | 651 / 0 | 13 / 0 | 13 / 0 | 1.018 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 601 / 0 | 12 / 0 | 12 / 0 | 1.018 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 151 / 0 | 3 / 0 | 3 / 0 | 1.013 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 101 / 0 | 2 / 0 | 2 / 0 | 1.010 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| zielonka | 50 / 50 | 50 / 1 | 50 / 1 | 50.000 / 1.000 | 50 / 0 | 2 / 51 | 26.510 / 51.000 | 2 / 1 |
| zielonka+pre | 50 / 50 | 49 / 1 | 49 / 1 | 49.000 / 1.000 | 50 / 0 | 2 / 51 | 26.510 / 51.000 | 2 / 1 |
| zielonka-sym | 50 / 50 | 50 / 1 | 50 / 1 | 50.000 / 1.000 | 50 / 0 | 2 / 51 | 26.510 / 51.000 | 2 / 1 |
| zielonka-sym+pre | 50 / 50 | 49 / 1 | 49 / 1 | 49.000 / 1.000 | 50 / 0 | 2 / 51 | 26.510 / 51.000 | 2 / 1 |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(50,_500).gm · 76000 vertices / 201899 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 76000 | 201899 | 102 | 101 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.826 | 1338.926 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,52} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.826 | 1339.184 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.816 | 1339.199 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,52} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.663 | 1339.203 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.549 | 1339.195 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,52} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.609 | 1339.199 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.609 | 1339.199 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,52} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.494 | 1339.141 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 75000 / 1000 | 1174 / 0 | 23 / 0 | 52 / 0 | k=4, t=5, depth=51 / k=4, t=5, depth=51 | 4.591 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 75000 / 1000 | 1123 / 0 | 22 / 0 | 52 / 0 | k=4, t=5, depth=51 / k=4, t=5, depth=51 | 4.620 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 75000 / 1000 | 154 / 0 | 3 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 5.991 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 75000 / 1000 | 103 / 0 | 2 / 0 | 52 / 0 | bits=1, depth=51 / bits=1, depth=51 | 5.981 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 251.570 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 251.559 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 1151 / 0 | 23 / 0 | 23 / 0 | 1.019 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1101 / 0 | 22 / 0 | 22 / 0 | 1.019 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 151 / 0 | 3 / 0 | 3 / 0 | 1.013 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 101 / 0 | 2 / 0 | 2 / 0 | 1.010 / 0.000 | 1 / 0 | 52 / 0 | 52.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(500,_100).gm · 150200 vertices / 399399 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 150200 | 399399 | 1002 | 1001 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.283 | 1125.402 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,502} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.282 | 1125.535 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.282 | 1125.340 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,502} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.178 | 1125.453 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 79.098 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 79.047 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 79.188 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 79.254 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.129 | 1125.277 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,502} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.202 | 1125.457 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.135 | 1125.172 | - | - | - | - | Solver failed: failed to build the Even host U^18_{17,502} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.083 | 1125.402 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 150000 / 200 | 15532 / 0 | 31 / 0 | 502 / 0 | k=3, t=3, depth=501 / k=3, t=3, depth=501 | 19.610 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 150000 / 200 | 15532 / 0 | 31 / 0 | 502 / 0 | k=3, t=3, depth=501 / k=3, t=3, depth=501 | 19.320 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 150000 / 200 | 1003 / 0 | 2 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 8.257 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 150000 / 200 | 1504 / 0 | 3 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 8.299 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 317.117 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 317.234 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 74.750 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 74.766 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 15501 / 0 | 31 / 0 | 31 / 0 | 1.002 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 15501 / 0 | 31 / 0 | 31 / 0 | 1.002 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 1001 / 0 | 2 / 0 | 2 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1501 / 0 | 3 / 0 | 3 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(500,_200).gm · 300400 vertices / 799799 edges · 2 complete · 14 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 300400 | 799799 | 1002 | 1001 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.710 | 1371.031 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,502} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.721 | 1371.008 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.711 | 1372.836 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,502} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.672 | 1373.000 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 103.176 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 102.922 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.070 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.191 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.619 | 1370.887 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,502} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.676 | 1370.965 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.678 | 1372.941 | - | - | - | - | Solver failed: failed to build the Even host U^19_{18,502} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.615 | 1373.082 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 103.008 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 103.062 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.074 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.074 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.074 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 103.062 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 300000 / 400 | 1504 / 0 | 3 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 21.738 | 103.062 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 300000 / 400 | 1003 / 0 | 2 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 21.886 | 103.074 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.050 | 590.250 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.050 | 592.824 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 146.594 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 146.820 | - | - | - | - | deadline exceeded |

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
| pm-succinct+iter | 1501 / 0 | 3 / 0 | 3 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1001 / 0 | 2 / 0 | 2 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(500,_50).gm · 75100 vertices / 199199 edges · 4 complete · 12 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 75100 | 199199 | 1002 | 1001 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.716 | 1341.840 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,502} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.715 | 1341.844 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.828 | 1341.715 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,502} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.642 | 1341.988 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 572.352 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 572.355 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 572.305 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 572.492 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.519 | 1341.680 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,502} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.693 | 1341.930 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.662 | 1341.848 | - | - | - | - | Solver failed: failed to build the Even host U^17_{16,502} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.626 | 1341.918 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 75000 / 100 | 6514 / 0 | 13 / 0 | 502 / 0 | k=2, t=3, depth=501 / k=2, t=3, depth=501 | 8.282 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 75000 / 100 | 6013 / 0 | 12 / 0 | 502 / 0 | k=2, t=3, depth=501 / k=2, t=3, depth=501 | 8.250 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 75000 / 100 | 1504 / 0 | 3 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 3.352 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 75000 / 100 | 1003 / 0 | 2 / 0 | 502 / 0 | bits=1, depth=501 / bits=1, depth=501 | 3.370 | 58.574 | even | - | - | false | - |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 163.859 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 163.371 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |

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
| pm-strahler+iter | 6501 / 0 | 13 / 0 | 13 / 0 | 1.002 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 6001 / 0 | 12 / 0 | 12 / 0 | 1.002 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 1501 / 0 | 3 / 0 | 3 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1001 / 0 | 2 / 0 | 2 / 0 | 1.001 / 0.000 | 1 / 0 | 502 / 0 | 502.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/jurdzinskigame(500,_500).gm · 751000 vertices / 2000999 edges · 16 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 751000 | 2000999 | 1002 | 1001 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.974 | 1532.312 | - | - | - | - | Solver failed: failed to build the Even host U^20_{19,502} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.061 | 1532.367 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.911 | 1532.344 | - | - | - | - | Solver failed: failed to build the Even host U^20_{19,502} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.789 | 1532.504 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 256.066 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 256.051 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 255.996 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 256.000 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.640 | 1532.312 | - | - | - | - | Solver failed: failed to build the Even host U^20_{19,502} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.773 | 1532.301 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.659 | 1532.441 | - | - | - | - | Solver failed: failed to build the Even host U^20_{19,502} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.780 | 1532.434 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 256.023 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 255.887 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 256.016 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 256.016 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 256.012 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 256.020 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 256.016 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 255.883 | - | - | - | - | deadline exceeded |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.101 | 1188.676 | - | - | - | - | deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.099 | 1176.367 | - | - | - | - | deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 256.000 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 256.066 | - | - | - | - | deadline exceeded |

</details>

<details>
<summary>pgsolver/games/laddergame(100).gm · 200 vertices / 400 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 200 | 400 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.419 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.420 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.418 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 100 / 100 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 100 / 100 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 100 / 100 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 100 / 100 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 100 / 100 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 100 / 100 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(1000).gm · 2000 vertices / 4000 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2000 | 4000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.787 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.787 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.567 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.577 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 1000 / 1000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1000 / 1000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1000 / 1000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1000 / 1000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1000 / 1000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.373 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(10000).gm · 20000 vertices / 40000 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 40000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.464 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.507 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=14 / H=1, K=1, t=14 | 27.565 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=14 / H=1, K=1, t=14 | 27.565 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 10000 / 10000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 10000 / 10000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 10000 / 10000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.443 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 10000 / 10000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.455 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.455 | 58.574 | even | true | true | false | - |
| zielonka | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.446 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 10000 / 10000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10000 / 10000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.400 | 58.574 | even | true | true | false | - |

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
| lifting-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(200).gm · 400 vertices / 800 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 400 | 800 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.452 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.399 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 200 / 200 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 200 / 200 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 200 / 200 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 200 / 200 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 200 / 200 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 200 / 200 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(2000).gm · 4000 vertices / 8000 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4000 | 8000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.966 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.954 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.047 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.051 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2000 / 2000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2000 / 2000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2000 / 2000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2000 / 2000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2000 / 2000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2000 / 2000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(20000).gm · 40000 vertices / 80000 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 40000 | 80000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 20000 / 20000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.517 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.527 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 20000 / 20000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.569 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.549 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.448 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 20000 / 20000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.485 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.486 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 20000 / 20000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.507 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.509 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 20000 / 20000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.505 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.496 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 20000 / 20000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.510 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.498 | 58.574 | even | true | true | false | - |
| zielonka | complete | 20000 / 20000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.486 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 20000 / 20000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.506 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 20000 / 20000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(500).gm · 1000 vertices / 2000 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 2000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.497 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.497 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.444 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.454 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 500 / 500 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 500 / 500 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 500 / 500 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 500 / 500 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 500 / 500 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(5000).gm · 10000 vertices / 20000 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 20000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 16.903 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 16.883 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.400 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 7.117 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 7.117 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 5000 / 5000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5000 / 5000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5000 / 5000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5000 / 5000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.413 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5000 / 5000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5000 / 5000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/laddergame(50000).gm · 100000 vertices / 200000 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 100000 | 200000 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.515 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 50000 / 50000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.629 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.600 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 50000 / 50000 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.705 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.622 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.560 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 50000 / 50000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.631 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.626 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 50000 / 50000 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.641 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.633 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 50000 / 50000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.611 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.583 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 50000 / 50000 | 2 / 2 | 1 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.603 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.604 | 58.574 | even | true | true | false | - |
| zielonka | complete | 50000 / 50000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.558 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.558 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 50000 / 50000 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.602 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 50000 / 50000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.569 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(100).gm · 301 vertices / 401 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 301 | 401 | 201 | 200 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.610 | 1386.840 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,101} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.578 | 1386.840 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.537 | 1386.859 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,101} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.377 | 1386.844 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=101, K=1, t=0 / H=101, K=1, t=0 | 0.753 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=101, K=1, t=0 / H=101, K=1, t=0 | 0.752 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=101, K=1, t=0 / H=101, K=1, t=0 | 0.763 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=101, K=1, t=0 / H=101, K=1, t=0 | 0.764 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.555 | 1386.602 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,101} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.534 | 1386.855 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.520 | 1386.730 | - | true | - | - | Solver failed: failed to build the Even host U^9_{8,101} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.471 | 1386.855 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 301 / 0 | 8901 / 0 | 101 / 0 | 101 / 0 | k=2, t=1, depth=100 / k=2, t=1, depth=101 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 301 / 0 | 8901 / 0 | 101 / 0 | 101 / 0 | k=2, t=1, depth=100 / k=2, t=1, depth=101 | 0.454 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 301 / 0 | 8901 / 0 | 101 / 0 | 101 / 0 | k=2, t=1, depth=100 / k=2, t=1, depth=101 | 0.443 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 301 / 0 | 8901 / 0 | 101 / 0 | 101 / 0 | k=2, t=1, depth=100 / k=2, t=1, depth=101 | 0.443 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 301 / 0 | 7651 / 0 | 101 / 0 | 101 / 0 | bits=1, depth=100 / bits=1, depth=101 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 301 / 0 | 7651 / 0 | 101 / 0 | 101 / 0 | bits=1, depth=100 / bits=1, depth=101 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 301 / 0 | 7651 / 0 | 101 / 0 | 101 / 0 | bits=1, depth=100 / bits=1, depth=101 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 301 / 0 | 7651 / 0 | 101 / 0 | 101 / 0 | bits=1, depth=100 / bits=1, depth=101 | 0.445 | 58.574 | even | true | true | false | - |
| zielonka | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 301 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 8800 / 0 | 101 / 0 | 5 / 0 | 1.011 / 0.000 | 25 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 8800 / 0 | 101 / 0 | 5 / 0 | 1.011 / 0.000 | 25 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 8800 / 0 | 101 / 0 | 5 / 0 | 1.011 / 0.000 | 25 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 8800 / 0 | 101 / 0 | 5 / 0 | 1.011 / 0.000 | 25 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-succinct | 7550 / 0 | 101 / 0 | 3 / 0 | 1.013 / 0.000 | 50 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 7550 / 0 | 101 / 0 | 3 / 0 | 1.013 / 0.000 | 50 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 7550 / 0 | 101 / 0 | 3 / 0 | 1.013 / 0.000 | 50 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 7550 / 0 | 101 / 0 | 3 / 0 | 1.013 / 0.000 | 50 / 0 | 101 / 0 | 101.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(200).gm · 601 vertices / 801 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 601 | 801 | 401 | 400 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.313 | 1306.344 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,201} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.367 | 1306.406 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.344 | 1306.301 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,201} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.129 | 1306.387 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=201, K=1, t=0 / H=201, K=1, t=0 | 3.563 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=201, K=1, t=0 / H=201, K=1, t=0 | 3.518 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=201, K=1, t=0 / H=201, K=1, t=0 | 3.530 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=201, K=1, t=0 / H=201, K=1, t=0 | 3.556 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.105 | 1306.352 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,201} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.247 | 1306.289 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.207 | 1306.426 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,201} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.228 | 1306.422 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 601 / 0 | 35301 / 0 | 201 / 0 | 201 / 0 | k=2, t=1, depth=200 / k=2, t=1, depth=201 | 0.599 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 601 / 0 | 35301 / 0 | 201 / 0 | 201 / 0 | k=2, t=1, depth=200 / k=2, t=1, depth=201 | 0.609 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 601 / 0 | 35301 / 0 | 201 / 0 | 201 / 0 | k=2, t=1, depth=200 / k=2, t=1, depth=201 | 0.611 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 601 / 0 | 35301 / 0 | 201 / 0 | 201 / 0 | k=2, t=1, depth=200 / k=2, t=1, depth=201 | 0.600 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 601 / 0 | 30301 / 0 | 201 / 0 | 201 / 0 | bits=1, depth=200 / bits=1, depth=201 | 0.568 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 601 / 0 | 30301 / 0 | 201 / 0 | 201 / 0 | bits=1, depth=200 / bits=1, depth=201 | 0.568 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 601 / 0 | 30301 / 0 | 201 / 0 | 201 / 0 | bits=1, depth=200 / bits=1, depth=201 | 0.567 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 601 / 0 | 30301 / 0 | 201 / 0 | 201 / 0 | bits=1, depth=200 / bits=1, depth=201 | 0.569 | 58.574 | even | true | true | false | - |
| zielonka | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 601 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 35100 / 0 | 201 / 0 | 5 / 0 | 1.006 / 0.000 | 50 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 35100 / 0 | 201 / 0 | 5 / 0 | 1.006 / 0.000 | 50 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 35100 / 0 | 201 / 0 | 5 / 0 | 1.006 / 0.000 | 50 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 35100 / 0 | 201 / 0 | 5 / 0 | 1.006 / 0.000 | 50 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-succinct | 30100 / 0 | 201 / 0 | 3 / 0 | 1.007 / 0.000 | 100 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 30100 / 0 | 201 / 0 | 3 / 0 | 1.007 / 0.000 | 100 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 30100 / 0 | 201 / 0 | 3 / 0 | 1.007 / 0.000 | 100 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 30100 / 0 | 201 / 0 | 3 / 0 | 1.007 / 0.000 | 100 / 0 | 201 / 0 | 201.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(500).gm · 1501 vertices / 2001 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1501 | 2001 | 1001 | 1000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.571 | 1370.426 | - | true | - | - | Solver failed: failed to build the Even host U^11_{10,501} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.520 | 1370.355 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.571 | 1370.484 | - | true | - | - | Solver failed: failed to build the Even host U^11_{10,501} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.305 | 1370.434 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.290 | 1370.352 | - | true | - | - | Solver failed: failed to build the Even host U^11_{10,501} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.371 | 1370.461 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.385 | 1370.465 | - | true | - | - | Solver failed: failed to build the Even host U^11_{10,501} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.353 | 1370.496 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 1501 / 0 | 219501 / 0 | 501 / 0 | 501 / 0 | k=2, t=1, depth=500 / k=2, t=1, depth=501 | 1.748 | 162.910 | even | true | true | false | - |
| pm-strahler+pre | complete | 1501 / 0 | 219501 / 0 | 501 / 0 | 501 / 0 | k=2, t=1, depth=500 / k=2, t=1, depth=501 | 1.721 | 162.953 | even | true | true | false | - |
| pm-strahler+iter | complete | 1501 / 0 | 219501 / 0 | 501 / 0 | 501 / 0 | k=2, t=1, depth=500 / k=2, t=1, depth=501 | 1.722 | 162.961 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1501 / 0 | 219501 / 0 | 501 / 0 | 501 / 0 | k=2, t=1, depth=500 / k=2, t=1, depth=501 | 1.723 | 163.047 | even | true | true | false | - |
| pm-succinct | complete | 1501 / 0 | 188251 / 0 | 501 / 0 | 501 / 0 | bits=1, depth=500 / bits=1, depth=501 | 1.526 | 148.164 | even | true | true | false | - |
| pm-succinct+pre | complete | 1501 / 0 | 188251 / 0 | 501 / 0 | 501 / 0 | bits=1, depth=500 / bits=1, depth=501 | 1.551 | 148.219 | even | true | true | false | - |
| pm-succinct+iter | complete | 1501 / 0 | 188251 / 0 | 501 / 0 | 501 / 0 | bits=1, depth=500 / bits=1, depth=501 | 1.535 | 148.285 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1501 / 0 | 188251 / 0 | 501 / 0 | 501 / 0 | bits=1, depth=500 / bits=1, depth=501 | 1.554 | 148.133 | even | true | true | false | - |
| zielonka | complete | 1501 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1501 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1501 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1501 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 219000 / 0 | 501 / 0 | 5 / 0 | 1.002 / 0.000 | 125 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 219000 / 0 | 501 / 0 | 5 / 0 | 1.002 / 0.000 | 125 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 219000 / 0 | 501 / 0 | 5 / 0 | 1.002 / 0.000 | 125 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 219000 / 0 | 501 / 0 | 5 / 0 | 1.002 / 0.000 | 125 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-succinct | 187750 / 0 | 501 / 0 | 3 / 0 | 1.003 / 0.000 | 250 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 187750 / 0 | 501 / 0 | 3 / 0 | 1.003 / 0.000 | 250 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 187750 / 0 | 501 / 0 | 3 / 0 | 1.003 / 0.000 | 250 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 187750 / 0 | 501 / 0 | 3 / 0 | 1.003 / 0.000 | 250 / 0 | 501 / 0 | 501.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=0.gm · 1000 vertices / 10390 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10390 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 323.297 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.352 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.572 | 436.027 | odd | false | true | false | - |
| lifting-sym+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.639 | 436.133 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 504 / 496 | 21 / 25 | 4 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 504 / 496 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.381 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 504 / 496 | 20 / 39 | 4 / 7 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.384 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 504 / 496 | 20 / 33 | 4 / 6 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.381 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 504 / 496 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 504 / 496 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=1.gm · 1000 vertices / 10685 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10685 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.250 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 323.309 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.390 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.496 | 435.957 | odd | false | true | false | - |
| lifting-sym+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.723 | 484.215 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 473 / 527 | 25 / 25 | 5 / 4 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.371 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 473 / 527 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 473 / 527 | 32 / 34 | 7 / 6 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.380 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 473 / 527 | 27 / 28 | 6 / 5 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 473 / 527 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 473 / 527 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

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
| pm-succinct | 25 / 28 | 7 / 6 | 4 / 4 | 1.240 / 1.179 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 21 / 23 | 6 / 5 | 3 / 3 | 1.238 / 1.174 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/randomgame(1000,_10,_1,_20)id=10.gm · 1000 vertices / 10460 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 10460 | 11 | 10 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 323.434 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 323.434 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.389 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.717 | 435.668 | even | true | true | false | - |
| lifting-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.540 | 436.047 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 490 / 510 | 21 / 31 | 4 / 5 | 6 / 7 | k=2, t=1, depth=5 / k=2, t=1, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 490 / 510 | 6 / 7 | 1 / 1 | 6 / 7 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5 / k=1, t=1, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 490 / 510 | 28 / 34 | 6 / 6 | 6 / 7 | bits=2, depth=5 / bits=2, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 490 / 510 | 23 / 28 | 5 / 5 | 6 / 7 | bits=1, depth=5 / bits=1, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5 / bits=0, depth=6 | 0.379 | 58.574 | even | true | true | false | - |
| zielonka | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 490 / 510 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 17 / 26 | 4 / 5 | 4 / 5 | 1.176 / 1.154 | 1 / 1 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 6 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 7 | 6.000 / 7.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 22 / 28 | 6 / 6 | 4 / 4 | 1.227 / 1.179 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 18 / 23 | 5 / 5 | 3 / 3 | 1.222 / 1.174 | 3 / 3 | 6 / 7 | 6.000 / 7.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

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

