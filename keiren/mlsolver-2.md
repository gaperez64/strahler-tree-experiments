# mlsolver, part 2

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=3.gm · 234577 vertices / 319754 edges · 15 complete · 1 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 234577 | 319754 | 17 | 369435906932739 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.316 | 1123.758 | - | - | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.315 | 1123.617 | - | - | - | - | preprocess: residual=214615 shaved_even=19962 shaved_odd=0 single=0 loops=19962 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.305 | 1123.754 | - | - | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.264 | 1123.746 | - | - | - | - | preprocess: residual=214615 shaved_even=19962 shaved_odd=0 single=0 loops=19962 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 60.797 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 234577 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 19.550 | 60.828 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 234577 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=10, K=2, t=1 / H=9, K=2, t=1 | 19.711 | 60.695 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 234577 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 7.177 | 60.699 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.237 | 1123.621 | - | - | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.249 | 1123.695 | - | - | - | - | preprocess: residual=214615 shaved_even=19962 shaved_odd=0 single=0 loops=19962 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.246 | 1123.816 | - | - | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.289 | 1123.691 | - | - | - | - | preprocess: residual=214615 shaved_even=19962 shaved_odd=0 single=0 loops=19962 wcwc=0 |
| pm-strahler | complete | 234577 / 0 | 248 / 0 | 41 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 1.233 | 60.707 | even | - | - | false | - |
| pm-strahler+pre | complete | 234577 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 1.058 | 60.648 | even | - | - | false | - |
| pm-strahler+iter | complete | 234577 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 0.945 | 60.770 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 234577 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 0.902 | 60.633 | even | - | - | false | - |
| pm-succinct | complete | 234577 / 0 | 259 / 0 | 47 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 1.687 | 60.770 | even | - | - | false | - |
| pm-succinct+pre | complete | 234577 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 1.205 | 60.648 | even | - | - | false | - |
| pm-succinct+iter | complete | 234577 / 0 | 95 / 0 | 17 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 0.966 | 60.578 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 234577 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 0.834 | 60.688 | even | - | - | false | - |
| zielonka | complete | 234577 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 0.795 | 60.824 | even | - | - | false | - |
| zielonka+pre | complete | 234577 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 0.785 | 60.887 | even | - | - | false | - |
| zielonka-sym | complete | 234577 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 1.484 | 60.551 | even | - | - | false | - |
| zielonka-sym+pre | complete | 234577 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 1.279 | 60.699 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 10 / 0 | 2 / 0 | 2 / 0 | 1.100 / 0.000 | 1 / 0 | 6 / 0 | 6.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 10 / 0 | 2 / 0 | 2 / 0 | 1.100 / 0.000 | 1 / 0 | 6 / 0 | 6.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 207 / 0 | 41 / 0 | 7 / 0 | 1.193 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 126 / 0 | 33 / 0 | 7 / 0 | 1.254 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 159 / 0 | 33 / 0 | 7 / 0 | 1.201 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 112 / 0 | 31 / 0 | 7 / 0 | 1.268 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-succinct | 212 / 0 | 47 / 0 | 5 / 0 | 1.217 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 17 / 0 | 3 / 0 | 1.205 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=3_compact.gm · 6650 vertices / 40753 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6650 | 40753 | 13 | 369435906932738 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.481 | 1373.297 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.645 | 1373.023 | - | true | - | - | preprocess: residual=6637 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.491 | 1373.168 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.350 | 1373.027 | - | true | - | - | preprocess: residual=6637 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-adaptive | complete | 6650 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.793 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6650 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.608 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6650 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.620 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6650 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.466 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.473 | 1373.070 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.432 | 1373.020 | - | true | - | - | preprocess: residual=6637 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.395 | 1373.172 | - | true | - | - | Solver failed: failed to build the Even host U^7_{12,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.278 | 1373.016 | - | true | - | - | preprocess: residual=6637 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| pm-strahler | complete | 6650 / 0 | 30 / 0 | 5 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 2.195 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 6650 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 1.408 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 6650 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.423 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6650 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 6650 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.997 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 6650 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.771 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 6650 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6650 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.401 | 58.574 | even | true | true | false | - |
| zielonka | complete | 6650 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 6650 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 6650 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.423 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6650 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 13 / 0 | 3 / 0 | 3 / 0 | 1.154 / 0.000 | 1 / 0 | 5 / 0 | 6.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 25 / 0 | 5 / 0 | 4 / 0 | 1.160 / 0.000 | 2 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 16 / 0 | 3 / 0 | 3 / 0 | 1.125 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |
| zielonka-sym | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=4.gm · 567753 vertices / 766649 edges · 13 complete · 3 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 567753 | 766649 | 17 | 6473924464345091 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.352 | 1475.688 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.559 | 1475.801 | - | - | - | - | preprocess: residual=533367 shaved_even=34386 shaved_odd=0 single=0 loops=34386 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.579 | 1475.543 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.464 | 1475.781 | - | - | - | - | preprocess: residual=533367 shaved_even=34386 shaved_odd=0 single=0 loops=34386 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 145.391 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 145.289 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 145.355 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 567753 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 19.155 | 145.355 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.390 | 1475.691 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.551 | 1475.875 | - | - | - | - | preprocess: residual=533367 shaved_even=34386 shaved_odd=0 single=0 loops=34386 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.409 | 1475.609 | - | - | - | - | Solver failed: failed to build the Even host U^10_{19,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.399 | 1475.812 | - | - | - | - | preprocess: residual=533367 shaved_even=34386 shaved_odd=0 single=0 loops=34386 wcwc=0 |
| pm-strahler | complete | 567753 / 0 | 240 / 0 | 39 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 2.551 | 145.133 | even | - | - | false | - |
| pm-strahler+pre | complete | 567753 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 2.098 | 145.176 | even | - | - | false | - |
| pm-strahler+iter | complete | 567753 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 1.809 | 145.297 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 567753 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 1.693 | 145.281 | even | - | - | false | - |
| pm-succinct | complete | 567753 / 0 | 259 / 0 | 47 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 3.632 | 145.367 | even | - | - | false | - |
| pm-succinct+pre | complete | 567753 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 2.395 | 145.234 | even | - | - | false | - |
| pm-succinct+iter | complete | 567753 / 0 | 95 / 0 | 17 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 1.931 | 145.238 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 567753 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 1.456 | 145.367 | even | - | - | false | - |
| zielonka | complete | 567753 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 1.429 | 145.148 | even | - | - | false | - |
| zielonka+pre | complete | 567753 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 1.329 | 145.355 | even | - | - | false | - |
| zielonka-sym | complete | 567753 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 3.029 | 145.355 | even | - | - | false | - |
| zielonka-sym+pre | complete | 567753 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 2.573 | 145.289 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 201 / 0 | 39 / 0 | 7 / 0 | 1.189 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 126 / 0 | 33 / 0 | 7 / 0 | 1.254 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 159 / 0 | 33 / 0 | 7 / 0 | 1.201 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 112 / 0 | 31 / 0 | 7 / 0 | 1.268 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-succinct | 212 / 0 | 47 / 0 | 5 / 0 | 1.217 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 17 / 0 | 3 / 0 | 1.205 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=4_compact.gm · 15427 vertices / 95008 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15427 | 95008 | 13 | 6473924464345090 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.231 | 1209.172 | - | true | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.241 | 1209.320 | - | true | - | - | preprocess: residual=15414 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.220 | 1209.258 | - | true | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.053 | 1209.270 | - | true | - | - | preprocess: residual=15414 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-adaptive | complete | 15427 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.332 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 15427 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.879 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 15427 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.907 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 15427 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.549 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.181 | 1209.312 | - | true | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.136 | 1209.309 | - | true | - | - | preprocess: residual=15414 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.150 | 1209.195 | - | true | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.106 | 1209.184 | - | true | - | - | preprocess: residual=15414 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| pm-strahler | complete | 15427 / 0 | 30 / 0 | 5 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 9.625 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 15427 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 5.192 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 15427 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.501 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 15427 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 15427 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 3.450 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 15427 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 2.250 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 15427 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 15427 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.399 | 58.574 | even | true | true | false | - |
| zielonka | complete | 15427 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 15427 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 15427 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.453 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 15427 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.440 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 13 / 0 | 3 / 0 | 3 / 0 | 1.154 / 0.000 | 1 / 0 | 5 / 0 | 6.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 25 / 0 | 5 / 0 | 4 / 0 | 1.160 / 0.000 | 2 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 16 / 0 | 3 / 0 | 3 / 0 | 1.125 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |
| zielonka-sym | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=5.gm · 1348959 vertices / 1807450 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1348959 | 1807450 | 17 | 112589990684262399 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.328 | 1170.012 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.389 | 1170.078 | - | - | - | - | preprocess: residual=1286141 shaved_even=62818 shaved_odd=0 single=0 loops=62818 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.327 | 1170.055 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.503 | 1169.965 | - | - | - | - | preprocess: residual=1286141 shaved_even=62818 shaved_odd=0 single=0 loops=62818 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 346.445 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 346.387 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 346.445 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 346.574 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.301 | 1169.984 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 3.408 | 1170.078 | - | - | - | - | preprocess: residual=1286141 shaved_even=62818 shaved_odd=0 single=0 loops=62818 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.277 | 1170.074 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.515 | 1170.070 | - | - | - | - | preprocess: residual=1286141 shaved_even=62818 shaved_odd=0 single=0 loops=62818 wcwc=0 |
| pm-strahler | complete | 1348959 / 0 | 386 / 0 | 61 / 0 | 10 / 0 | k=2, t=2, depth=9 / k=2, t=2, depth=9 | 10.169 | 346.336 | even | - | - | false | - |
| pm-strahler+pre | complete | 1348959 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 4.526 | 346.395 | even | - | - | false | - |
| pm-strahler+iter | complete | 1348959 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 3.873 | 346.395 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1348959 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 3.701 | 346.453 | even | - | - | false | - |
| pm-succinct | complete | 1348959 / 0 | 259 / 0 | 47 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 8.286 | 346.379 | even | - | - | false | - |
| pm-succinct+pre | complete | 1348959 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 5.322 | 346.395 | even | - | - | false | - |
| pm-succinct+iter | complete | 1348959 / 0 | 95 / 0 | 17 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 4.315 | 346.395 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1348959 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 3.038 | 346.457 | even | - | - | false | - |
| zielonka | complete | 1348959 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 2.844 | 346.578 | even | - | - | false | - |
| zielonka+pre | complete | 1348959 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 2.727 | 346.504 | even | - | - | false | - |
| zielonka-sym | complete | 1348959 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 6.837 | 346.281 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1348959 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 5.583 | 346.512 | even | - | - | false | - |

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
| pm-strahler | 325 / 0 | 61 / 0 | 15 / 0 | 1.185 / 0.000 | 7 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 126 / 0 | 33 / 0 | 7 / 0 | 1.254 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 159 / 0 | 33 / 0 | 7 / 0 | 1.201 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 112 / 0 | 31 / 0 | 7 / 0 | 1.268 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-succinct | 212 / 0 | 47 / 0 | 5 / 0 | 1.217 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 17 / 0 | 3 / 0 | 1.205 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=5_compact.gm · 35388 vertices / 218527 edges · 15 complete · 1 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 35388 | 218527 | 13 | 112589990684262398 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.427 | 1299.785 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.478 | 1299.844 | - | - | - | - | preprocess: residual=35375 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.459 | 1299.750 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.311 | 1299.785 | - | - | - | - | preprocess: residual=35375 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-adaptive | complete | 35388 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 2.619 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 35388 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.534 | 58.574 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 35388 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.555 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 35388 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.743 | 58.574 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.419 | 1299.652 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.394 | 1299.848 | - | - | - | - | preprocess: residual=35375 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.391 | 1299.617 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.301 | 1299.707 | - | - | - | - | preprocess: residual=35375 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 35388 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 23.803 | 58.574 | even | - | - | false | - |
| pm-strahler+iter | complete | 35388 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.952 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 35388 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.492 | 58.574 | even | - | - | false | - |
| pm-succinct | complete | 35388 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 16.134 | 58.574 | even | - | - | false | - |
| pm-succinct+pre | complete | 35388 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 9.710 | 58.574 | even | - | - | false | - |
| pm-succinct+iter | complete | 35388 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.451 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 35388 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.451 | 58.574 | even | - | - | false | - |
| zielonka | complete | 35388 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.463 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 35388 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.451 | 58.574 | even | - | - | false | - |
| zielonka-sym | complete | 35388 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.542 | 58.574 | even | - | - | false | - |
| zielonka-sym+pre | complete | 35388 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.532 | 58.574 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 13 / 0 | 3 / 0 | 3 / 0 | 1.154 / 0.000 | 1 / 0 | 5 / 0 | 6.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 16 / 0 | 3 / 0 | 3 / 0 | 1.125 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |
| zielonka-sym | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=6.gm · 3155971 vertices / 4201801 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3155971 | 4201801 | 17 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.285 | 1227.703 | - | - | - | - | Solver failed: failed to build the Even host U^10_{21,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.614 | 1227.664 | - | - | - | - | preprocess: residual=3035137 shaved_even=120834 shaved_odd=0 single=0 loops=120834 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.335 | 1227.797 | - | - | - | - | Solver failed: failed to build the Even host U^10_{21,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.472 | 1227.926 | - | - | - | - | preprocess: residual=3035137 shaved_even=120834 shaved_odd=0 single=0 loops=120834 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 813.984 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 814.176 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.043 | 814.051 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 814.180 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.175 | 1227.707 | - | - | - | - | Solver failed: failed to build the Even host U^10_{21,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.585 | 1227.758 | - | - | - | - | preprocess: residual=3035137 shaved_even=120834 shaved_odd=0 single=0 loops=120834 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.245 | 1228.070 | - | - | - | - | Solver failed: failed to build the Even host U^10_{21,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.579 | 1228.066 | - | - | - | - | preprocess: residual=3035137 shaved_even=120834 shaved_odd=0 single=0 loops=120834 wcwc=0 |
| pm-strahler | complete | 3155971 / 0 | 248 / 0 | 41 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 13.094 | 813.965 | even | - | - | false | - |
| pm-strahler+pre | complete | 3155971 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 10.673 | 814.059 | even | - | - | false | - |
| pm-strahler+iter | complete | 3155971 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 9.018 | 814.098 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 3155971 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 8.364 | 813.852 | even | - | - | false | - |
| pm-succinct | complete | 3155971 / 0 | 259 / 0 | 47 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 19.362 | 813.988 | even | - | - | false | - |
| pm-succinct+pre | complete | 3155971 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 12.448 | 814.043 | even | - | - | false | - |
| pm-succinct+iter | complete | 3155971 / 0 | 95 / 0 | 17 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 10.286 | 813.938 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 3155971 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 6.822 | 814.055 | even | - | - | false | - |
| zielonka | complete | 3155971 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 6.418 | 814.055 | even | - | - | false | - |
| zielonka+pre | complete | 3155971 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 5.996 | 813.906 | even | - | - | false | - |
| zielonka-sym | complete | 3155971 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 15.573 | 814.051 | even | - | - | false | - |
| zielonka-sym+pre | complete | 3155971 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 13.112 | 814.039 | even | - | - | false | - |

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
| pm-strahler | 207 / 0 | 41 / 0 | 7 / 0 | 1.193 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 126 / 0 | 33 / 0 | 7 / 0 | 1.254 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 159 / 0 | 33 / 0 | 7 / 0 | 1.201 / 0.000 | 8 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 112 / 0 | 31 / 0 | 7 / 0 | 1.268 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-succinct | 212 / 0 | 47 / 0 | 5 / 0 | 1.217 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 17 / 0 | 3 / 0 | 1.205 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=6_compact.gm · 80133 vertices / 495630 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 80133 | 495630 | 13 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.862 | 1345.961 | - | - | - | - | Solver failed: failed to build the Even host U^7_{16,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.760 | 1346.199 | - | - | - | - | preprocess: residual=80120 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.738 | 1345.891 | - | - | - | - | Solver failed: failed to build the Even host U^7_{16,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.659 | 1346.148 | - | - | - | - | preprocess: residual=80120 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-adaptive | complete | 80133 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 5.629 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 80133 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 3.052 | 58.574 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 80133 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 3.083 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 80133 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.181 | 58.574 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.680 | 1345.906 | - | - | - | - | Solver failed: failed to build the Even host U^7_{16,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.922 | 1346.184 | - | - | - | - | preprocess: residual=80120 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.778 | 1345.887 | - | - | - | - | Solver failed: failed to build the Even host U^7_{16,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.673 | 1346.133 | - | - | - | - | preprocess: residual=80120 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 80133 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 3.012 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 80133 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.738 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 80133 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.556 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 80133 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.575 | 58.574 | even | - | - | false | - |
| zielonka | complete | 80133 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.563 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 80133 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.564 | 58.574 | even | - | - | false | - |
| zielonka-sym | complete | 80133 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.789 | 58.574 | even | - | - | false | - |
| zielonka-sym+pre | complete | 80133 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.759 | 58.574 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 13 / 0 | 3 / 0 | 3 / 0 | 1.154 / 0.000 | 1 / 0 | 5 / 0 | 6.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 8 / 0 | 2 / 0 | 2 / 0 | 1.125 / 0.000 | 1 / 0 | 5 / 0 | 5.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 4 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 21 / 0 | 4 / 0 | 4 / 0 | 1.143 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 16 / 0 | 3 / 0 | 3 / 0 | 1.125 / 0.000 | 1 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 27 / 0 | 7 / 0 | 3 / 0 | 1.222 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 18 / 0 | 4 / 0 | 2 / 0 | 1.167 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |
| zielonka-sym | 10 / 0 | 3 / 0 | 2 / 0 | 1.400 / 0.000 | 4 / 0 | 3 / 0 | 5.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 5 / 0 | 2 / 0 | 2 / 0 | 1.600 / 0.000 | 3 / 0 | 3 / 0 | 4.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FairSchedulern=1.gm · 354 vertices / 430 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 354 | 430 | 13 | 88080387 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1413.309 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=8 / H=5, K=5, t=8 | 9.965 | 96.113 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 1413.359 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=8 / H=5, K=5, t=8 | 9.765 | 95.980 | even | true | true | false | - |
| lifting-adaptive | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | H=9, K=1, t=0 / H=8, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.373 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | H=9, K=1, t=0 / H=8, K=1, t=0 | 0.370 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.370 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | H=9, K=9, t=8 / H=8, K=8, t=8 | 20.140 | 1892.465 | even | true | true | false | - |
| lifting-sym+pre | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=8 / H=5, K=5, t=8 | 1.491 | 113.078 | even | true | true | false | - |
| lifting-sym+iter | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | H=9, K=9, t=8 / H=8, K=8, t=8 | 20.028 | 1892.480 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=8 / H=5, K=5, t=8 | 1.466 | 113.141 | even | true | true | false | - |
| pm-strahler | complete | 354 / 0 | 131 / 0 | 26 / 0 | 9 / 0 | k=2, t=2, depth=8 / k=2, t=2, depth=8 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 354 / 0 | 87 / 0 | 25 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 354 / 0 | 115 / 0 | 24 / 0 | 9 / 0 | k=2, t=2, depth=8 / k=2, t=2, depth=8 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 354 / 0 | 87 / 0 | 25 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 354 / 0 | 99 / 0 | 21 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 354 / 0 | 53 / 0 | 17 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=5 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 354 / 0 | 83 / 0 | 19 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 0.370 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 354 / 0 | 53 / 0 | 17 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=5 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 354 / 0 | 9 / 0 | 1 / 0 | 9 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 354 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 105 / 0 | 26 / 0 | 9 / 0 | 1.238 / 0.000 | 5 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 62 / 0 | 25 / 0 | 12 / 0 | 1.387 / 0.000 | 4 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 91 / 0 | 24 / 0 | 9 / 0 | 1.253 / 0.000 | 5 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 62 / 0 | 25 / 0 | 12 / 0 | 1.387 / 0.000 | 4 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-succinct | 78 / 0 | 21 / 0 | 6 / 0 | 1.256 / 0.000 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 36 / 0 | 17 / 0 | 6 / 0 | 1.444 / 0.000 | 9 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 64 / 0 | 19 / 0 | 6 / 0 | 1.281 / 0.000 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 36 / 0 | 17 / 0 | 6 / 0 | 1.444 / 0.000 | 9 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 8 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/FairSchedulern=1_compact.gm · 19 vertices / 43 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19 | 43 | 5 | 88080386 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.415 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | H=4, K=4, t=4 / H=4, K=4, t=4 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 19 / 0 | 7 / 0 | 2 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | k=1, t=1, depth=3 / k=1, t=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 19 / 0 | 7 / 0 | 2 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 19 / 0 | 7 / 0 | 2 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 19 / 0 | 4 / 0 | 1 / 0 | 4 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 5 / 0 | 2 / 0 | 2 / 0 | 1.200 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 3 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/FairSchedulern=2.gm · 140309 vertices / 167007 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 140309 | 167007 | 22 | 4947802324995 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.171 | 1117.707 | - | true | - | - | Solver failed: failed to build the Even host U^14_{17,14} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.181 | 1117.707 | - | true | - | - | preprocess: residual=136587 shaved_even=3722 shaved_odd=0 single=0 loops=3722 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.201 | 1117.574 | - | true | - | - | Solver failed: failed to build the Even host U^14_{17,14} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.162 | 1117.570 | - | true | - | - | preprocess: residual=136587 shaved_even=3722 shaved_odd=0 single=0 loops=3722 wcwc=0 |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.153 | 1117.711 | - | true | - | - | Solver failed: failed to build the Even host U^14_{17,14} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.152 | 1117.773 | - | true | - | - | preprocess: residual=136587 shaved_even=3722 shaved_odd=0 single=0 loops=3722 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.160 | 1117.707 | - | true | - | - | Solver failed: failed to build the Even host U^14_{17,14} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.130 | 1117.711 | - | true | - | - | preprocess: residual=136587 shaved_even=3722 shaved_odd=0 single=0 loops=3722 wcwc=0 |
| pm-strahler | complete | 140309 / 0 | 3789 / 0 | 688 / 0 | 14 / 0 | k=3, t=2, depth=13 / k=3, t=2, depth=13 | 6.489 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 140309 / 0 | 2983 / 0 | 606 / 0 | 10 / 0 | k=3, t=3, depth=9 / k=3, t=3, depth=9 | 5.123 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 140309 / 0 | 3763 / 0 | 686 / 0 | 14 / 0 | k=3, t=2, depth=13 / k=3, t=2, depth=13 | 1.645 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 140309 / 0 | 2983 / 0 | 606 / 0 | 10 / 0 | k=3, t=3, depth=9 / k=3, t=3, depth=9 | 3.081 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 140309 / 0 | 1576 / 0 | 320 / 0 | 14 / 0 | bits=3, depth=13 / bits=3, depth=13 | 4.927 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 140309 / 0 | 1503 / 0 | 379 / 0 | 10 / 0 | bits=3, depth=9 / bits=3, depth=9 | 1.678 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 140309 / 0 | 1550 / 0 | 318 / 0 | 14 / 0 | bits=3, depth=13 / bits=3, depth=13 | 1.739 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 140309 / 0 | 1503 / 0 | 379 / 0 | 10 / 0 | bits=3, depth=9 / bits=3, depth=9 | 1.218 | 58.574 | even | true | true | false | - |
| zielonka | complete | 140309 / 0 | 28 / 0 | 8 / 0 | 14 / 0 | — / — | 0.703 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 140309 / 0 | 19 / 0 | 8 / 0 | 7 / 0 | — / — | 0.650 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 140309 / 0 | 28 / 0 | 8 / 0 | 14 / 0 | — / — | 1.847 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 140309 / 0 | 19 / 0 | 8 / 0 | 7 / 0 | — / — | 1.148 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 3101 / 0 | 688 / 0 | 15 / 0 | 1.222 / 0.000 | 130 / 0 | 14 / 0 | 14.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 2377 / 0 | 606 / 0 | 31 / 0 | 1.255 / 0.000 | 89 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 3077 / 0 | 686 / 0 | 15 / 0 | 1.223 / 0.000 | 130 / 0 | 14 / 0 | 14.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 2377 / 0 | 606 / 0 | 31 / 0 | 1.255 / 0.000 | 89 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct | 1256 / 0 | 320 / 0 | 8 / 0 | 1.254 / 0.000 | 147 / 0 | 14 / 0 | 14.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 1124 / 0 | 379 / 0 | 15 / 0 | 1.336 / 0.000 | 169 / 0 | 10 / 0 | 10.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 1232 / 0 | 318 / 0 | 8 / 0 | 1.257 / 0.000 | 147 / 0 | 14 / 0 | 14.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 1124 / 0 | 379 / 0 | 15 / 0 | 1.336 / 0.000 | 169 / 0 | 10 / 0 | 10.000 / 0.000 | 4 / 0 |
| zielonka | 20 / 0 | 6 / 0 | 4 / 0 | 1.350 / 0.000 | 4 / 0 | 7 / 0 | 9.375 / 0.000 | 3 / 0 |
| zielonka+pre | 11 / 0 | 6 / 0 | 4 / 0 | 1.636 / 0.000 | 4 / 0 | 4 / 0 | 5.625 / 0.000 | 3 / 0 |
| zielonka-sym | 20 / 0 | 6 / 0 | 4 / 0 | 1.350 / 0.000 | 4 / 0 | 7 / 0 | 9.375 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 11 / 0 | 6 / 0 | 4 / 0 | 1.636 / 0.000 | 4 / 0 | 4 / 0 | 5.625 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/FairSchedulern=2_compact.gm · 5596 vertices / 130825 edges · 15 complete · 1 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5596 | 130825 | 13 | 4947802324994 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.551 | 1345.918 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.251 | 2002.570 | - | true | - | - | preprocess: residual=5583 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.550 | 1345.855 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.147 | 2002.566 | - | true | - | - | preprocess: residual=5583 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-adaptive | complete | 5596 / 0 | 29 / 0 | 6 / 0 | 8 / 0 | H=8, K=2, t=1 / H=8, K=2, t=1 | 1.958 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5596 / 0 | 17 / 0 | 6 / 0 | 5 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | 1.536 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5596 / 0 | 22 / 0 | 5 / 0 | 7 / 0 | H=8, K=2, t=1 / H=8, K=2, t=1 | 1.987 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5596 / 0 | 17 / 0 | 6 / 0 | 5 / 0 | H=6, K=2, t=1 / H=6, K=2, t=1 | 1.531 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.547 | 1345.777 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.179 | 2002.508 | - | true | - | - | preprocess: residual=5583 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.429 | 1345.785 | - | true | - | - | Solver failed: failed to build the Even host U^8_{12,8} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.914 | 2002.555 | - | true | - | - | preprocess: residual=5583 shaved_even=13 shaved_odd=0 single=0 loops=13 wcwc=0 |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 5596 / 0 | 63 / 0 | 13 / 0 | 6 / 0 | k=2, t=2, depth=5 / k=2, t=2, depth=6 | 7.360 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5596 / 0 | 379 / 0 | 80 / 0 | 8 / 0 | k=3, t=2, depth=7 / k=3, t=2, depth=8 | 14.920 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5596 / 0 | 21 / 0 | 4 / 0 | 6 / 0 | k=2, t=2, depth=5 / k=2, t=2, depth=6 | 0.522 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5596 / 0 | 101 / 0 | 21 / 0 | 8 / 0 | bits=2, depth=7 / bits=2, depth=8 | 8.046 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5596 / 0 | 92 / 0 | 23 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 8.353 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5596 / 0 | 94 / 0 | 20 / 0 | 8 / 0 | bits=2, depth=7 / bits=2, depth=8 | 3.074 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5596 / 0 | 87 / 0 | 22 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=6 | 1.102 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5596 / 0 | 22 / 0 | 8 / 0 | 8 / 0 | — / — | 0.410 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5596 / 0 | 17 / 0 | 8 / 0 | 5 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5596 / 0 | 22 / 0 | 8 / 0 | 8 / 0 | — / — | 0.452 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5596 / 0 | 17 / 0 | 8 / 0 | 5 / 0 | — / — | 0.430 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 23 / 0 | 6 / 0 | 4 / 0 | 1.217 / 0.000 | 3 / 0 | 5 / 0 | 6.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 11 / 0 | 5 / 0 | 5 / 0 | 1.455 / 0.000 | 2 / 0 | 2 / 0 | 3.833 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 17 / 0 | 5 / 0 | 4 / 0 | 1.235 / 0.000 | 2 / 0 | 5 / 0 | 6.200 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 11 / 0 | 5 / 0 | 5 / 0 | 1.455 / 0.000 | 2 / 0 | 2 / 0 | 3.833 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 50 / 0 | 13 / 0 | 10 / 0 | 1.240 / 0.000 | 2 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 299 / 0 | 80 / 0 | 12 / 0 | 1.264 / 0.000 | 17 / 0 | 8 / 0 | 8.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 17 / 0 | 4 / 0 | 4 / 0 | 1.176 / 0.000 | 1 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-succinct | 80 / 0 | 21 / 0 | 5 / 0 | 1.250 / 0.000 | 10 / 0 | 8 / 0 | 8.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 69 / 0 | 23 / 0 | 8 / 0 | 1.319 / 0.000 | 8 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 74 / 0 | 20 / 0 | 5 / 0 | 1.257 / 0.000 | 10 / 0 | 8 / 0 | 8.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 65 / 0 | 22 / 0 | 7 / 0 | 1.323 / 0.000 | 8 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka | 14 / 0 | 6 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka+pre | 9 / 0 | 6 / 0 | 4 / 0 | 1.778 / 0.000 | 4 / 0 | 2 / 0 | 3.625 / 0.000 | 3 / 0 |
| zielonka-sym | 14 / 0 | 6 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 6.000 / 0.000 | 3 / 0 |
| zielonka-sym+pre | 9 / 0 | 6 / 0 | 4 / 0 | 1.778 / 0.000 | 4 / 0 | 2 / 0 | 3.625 / 0.000 | 3 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=1.gm · 693 vertices / 940 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 693 | 940 | 11 | 115 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.037 | 707.547 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 323.145 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.038 | 707.203 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 323.102 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=7, t=9 / H=6, K=6, t=9 | 16.579 | 821.000 | even | true | true | false | - |
| lifting-sym+pre | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=9 / H=5, K=5, t=9 | 5.662 | 323.289 | even | true | true | false | - |
| lifting-sym+iter | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=7, t=9 / H=6, K=6, t=9 | 16.697 | 820.883 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=9 / H=5, K=5, t=9 | 5.728 | 323.137 | even | true | true | false | - |
| pm-strahler | complete | 693 / 0 | 503 / 0 | 181 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.389 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 693 / 0 | 308 / 0 | 134 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.379 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 693 / 0 | 497 / 0 | 180 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.382 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 693 / 0 | 308 / 0 | 134 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=5 | 0.382 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 693 / 0 | 342 / 0 | 130 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 693 / 0 | 238 / 0 | 117 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=5 | 0.381 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 693 / 0 | 336 / 0 | 129 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.383 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 693 / 0 | 238 / 0 | 117 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=5 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 693 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 693 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 322 / 0 | 181 / 0 | 15 / 0 | 1.559 / 0.000 | 36 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 174 / 0 | 134 / 0 | 15 / 0 | 1.764 / 0.000 | 28 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 317 / 0 | 180 / 0 | 15 / 0 | 1.565 / 0.000 | 36 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 174 / 0 | 134 / 0 | 15 / 0 | 1.764 / 0.000 | 28 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 212 / 0 | 130 / 0 | 12 / 0 | 1.608 / 0.000 | 52 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 121 / 0 | 117 / 0 | 12 / 0 | 1.959 / 0.000 | 39 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 207 / 0 | 129 / 0 | 12 / 0 | 1.618 / 0.000 | 52 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 121 / 0 | 117 / 0 | 12 / 0 | 1.959 / 0.000 | 39 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=1_compact.gm · 298 vertices / 556 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 298 | 556 | 9 | 114 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 101.594 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 3.610 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 101.805 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 3.989 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.372 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.053 | 160.371 | even | true | true | false | - |
| lifting-sym+pre | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.526 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.056 | 160.430 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.523 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 298 / 0 | 171 / 0 | 47 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 298 / 0 | 122 / 0 | 54 / 0 | 4 / 0 | k=2, t=3, depth=3 / k=2, t=3, depth=4 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 298 / 0 | 81 / 0 | 22 / 0 | 6 / 0 | k=2, t=2, depth=5 / k=2, t=2, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 298 / 0 | 51 / 0 | 30 / 0 | 4 / 0 | k=2, t=3, depth=3 / k=2, t=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 298 / 0 | 95 / 0 | 31 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 298 / 0 | 60 / 0 | 32 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 298 / 0 | 95 / 0 | 31 / 0 | 6 / 0 | bits=2, depth=5 / bits=2, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 298 / 0 | 27 / 0 | 17 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| zielonka | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 298 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.370 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 298 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 124 / 0 | 47 / 0 | 14 / 0 | 1.371 / 0.000 | 8 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 68 / 0 | 54 / 0 | 24 / 0 | 1.779 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 59 / 0 | 22 / 0 | 14 / 0 | 1.356 / 0.000 | 3 / 0 | 6 / 0 | 6.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 21 / 0 | 30 / 0 | 19 / 0 | 2.381 / 0.000 | 2 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct | 64 / 0 | 31 / 0 | 6 / 0 | 1.469 / 0.000 | 15 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 28 / 0 | 32 / 0 | 8 / 0 | 2.107 / 0.000 | 10 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 64 / 0 | 31 / 0 | 6 / 0 | 1.469 / 0.000 | 15 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 10 / 0 | 17 / 0 | 8 / 0 | 2.600 / 0.000 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=2.gm · 1126 vertices / 1560 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1126 | 1560 | 11 | 139 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.154 | 1774.172 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 667.590 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.155 | 1775.191 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.040 | 667.566 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1126 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.425 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1126 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.142 | 1775.797 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 26.985 | 790.281 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.146 | 1776.430 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 26.830 | 790.289 | even | true | true | false | - |
| pm-strahler | complete | 1126 / 0 | 741 / 0 | 255 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1126 / 0 | 577 / 0 | 273 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1126 / 0 | 692 / 0 | 237 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.389 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1126 / 0 | 577 / 0 | 273 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1126 / 0 | 618 / 0 | 241 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1126 / 0 | 521 / 0 | 255 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.380 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1126 / 0 | 612 / 0 | 240 / 0 | 7 / 0 | bits=3, depth=6 / bits=3, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1126 / 0 | 221 / 0 | 121 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.370 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1126 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1126 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1126 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 486 / 0 | 255 / 0 | 31 / 0 | 1.523 / 0.000 | 38 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 304 / 0 | 273 / 0 | 29 / 0 | 1.895 / 0.000 | 45 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 455 / 0 | 237 / 0 | 31 / 0 | 1.519 / 0.000 | 37 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 304 / 0 | 273 / 0 | 29 / 0 | 1.895 / 0.000 | 45 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 377 / 0 | 241 / 0 | 15 / 0 | 1.637 / 0.000 | 91 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 266 / 0 | 255 / 0 | 16 / 0 | 1.955 / 0.000 | 83 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 372 / 0 | 240 / 0 | 15 / 0 | 1.642 / 0.000 | 91 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 100 / 0 | 121 / 0 | 16 / 0 | 2.200 / 0.000 | 37 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=2_compact.gm · 467 vertices / 858 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 467 | 858 | 9 | 138 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 101.691 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 7.237 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 101.676 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 7.151 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.369 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.092 | 160.488 | even | true | true | false | - |
| lifting-sym+pre | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.533 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=8 / H=6, K=6, t=8 | 2.085 | 160.234 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=8 / H=4, K=4, t=8 | 0.533 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 467 / 0 | 370 / 0 | 113 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 467 / 0 | 157 / 0 | 83 / 0 | 4 / 0 | k=3, t=3, depth=3 / k=3, t=3, depth=4 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 467 / 0 | 200 / 0 | 71 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.370 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 467 / 0 | 81 / 0 | 42 / 0 | 4 / 0 | k=2, t=3, depth=3 / k=2, t=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 467 / 0 | 253 / 0 | 90 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 467 / 0 | 118 / 0 | 69 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 467 / 0 | 108 / 0 | 40 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 0.369 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 467 / 0 | 53 / 0 | 33 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.371 | 58.574 | even | true | true | false | - |
| zielonka | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.362 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 467 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 467 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.369 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 257 / 0 | 113 / 0 | 13 / 0 | 1.436 / 0.000 | 27 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 74 / 0 | 83 / 0 | 21 / 0 | 2.108 / 0.000 | 12 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 129 / 0 | 71 / 0 | 13 / 0 | 1.543 / 0.000 | 19 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 39 / 0 | 42 / 0 | 23 / 0 | 2.051 / 0.000 | 3 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct | 163 / 0 | 90 / 0 | 12 / 0 | 1.546 / 0.000 | 41 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 49 / 0 | 69 / 0 | 12 / 0 | 2.388 / 0.000 | 19 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 68 / 0 | 40 / 0 | 8 / 0 | 1.574 / 0.000 | 19 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 20 / 0 | 33 / 0 | 10 / 0 | 2.600 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=3.gm · 1559 vertices / 2180 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1559 | 2180 | 11 | 163 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.161 | 1772.379 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.047 | 667.719 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.161 | 1772.383 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.041 | 667.645 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1559 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1559 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.435 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.142 | 1774.500 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.273 | 790.328 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.148 | 1772.773 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.175 | 790.219 | even | true | true | false | - |
| pm-strahler | complete | 1559 / 0 | 1206 / 0 | 449 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.483 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1559 / 0 | 892 / 0 | 426 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.400 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1559 / 0 | 1200 / 0 | 448 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.410 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1559 / 0 | 892 / 0 | 426 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=5 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1559 / 0 | 1003 / 0 | 392 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.481 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1559 / 0 | 713 / 0 | 362 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1559 / 0 | 463 / 0 | 196 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1559 / 0 | 342 / 0 | 192 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.390 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1559 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1559 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.384 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1559 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 757 / 0 | 449 / 0 | 31 / 0 | 1.592 / 0.000 | 69 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 466 / 0 | 426 / 0 | 31 / 0 | 1.912 / 0.000 | 60 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 752 / 0 | 448 / 0 | 31 / 0 | 1.594 / 0.000 | 69 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 466 / 0 | 426 / 0 | 31 / 0 | 1.912 / 0.000 | 60 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 611 / 0 | 392 / 0 | 20 / 0 | 1.640 / 0.000 | 152 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 351 / 0 | 362 / 0 | 20 / 0 | 2.028 / 0.000 | 113 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 267 / 0 | 196 / 0 | 20 / 0 | 1.730 / 0.000 | 73 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 150 / 0 | 192 / 0 | 20 / 0 | 2.273 / 0.000 | 55 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=3_compact.gm · 636 vertices / 1156 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 636 | 1156 | 9 | 162 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 323.238 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 27.653 | 58.574 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 323.258 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 27.752 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.382 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.400 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.382 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.543 | 435.824 | even | true | true | false | - |
| lifting-sym+pre | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.015 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.608 | 435.812 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.017 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 636 / 0 | 486 / 0 | 135 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 636 / 0 | 304 / 0 | 158 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.422 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 636 / 0 | 267 / 0 | 90 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.381 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 636 / 0 | 131 / 0 | 72 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 636 / 0 | 341 / 0 | 119 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 636 / 0 | 156 / 0 | 93 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 636 / 0 | 325 / 0 | 113 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 636 / 0 | 145 / 0 | 87 / 0 | 4 / 0 | bits=3, depth=3 / bits=3, depth=4 | 0.383 | 58.574 | even | true | true | false | - |
| zielonka | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 636 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 636 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.372 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 351 / 0 | 135 / 0 | 28 / 0 | 1.382 / 0.000 | 21 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 146 / 0 | 158 / 0 | 39 / 0 | 2.075 / 0.000 | 17 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 177 / 0 | 90 / 0 | 13 / 0 | 1.503 / 0.000 | 22 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 59 / 0 | 72 / 0 | 38 / 0 | 2.203 / 0.000 | 6 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 222 / 0 | 119 / 0 | 16 / 0 | 1.532 / 0.000 | 52 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 63 / 0 | 93 / 0 | 16 / 0 | 2.460 / 0.000 | 25 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 212 / 0 | 113 / 0 | 15 / 0 | 1.528 / 0.000 | 48 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 58 / 0 | 87 / 0 | 15 / 0 | 2.483 / 0.000 | 23 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=4.gm · 1992 vertices / 2800 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1992 | 2800 | 11 | 187 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.162 | 1774.336 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 667.715 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.163 | 1777.273 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.041 | 667.770 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1992 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.455 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.454 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1992 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.444 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.142 | 1775.242 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.510 | 790.387 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.149 | 1776.020 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=6, t=10 / H=5, K=5, t=10 | 27.075 | 790.410 | even | true | true | false | - |
| pm-strahler | complete | 1992 / 0 | 1396 / 0 | 511 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.524 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1992 / 0 | 1275 / 0 | 643 / 0 | 6 / 0 | k=4, t=3, depth=5 / k=4, t=3, depth=5 | 0.420 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1992 / 0 | 1390 / 0 | 510 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1992 / 0 | 876 / 0 | 434 / 0 | 6 / 0 | k=4, t=3, depth=5 / k=4, t=3, depth=5 | 0.410 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1992 / 0 | 1319 / 0 | 513 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.522 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1992 / 0 | 953 / 0 | 483 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1992 / 0 | 1313 / 0 | 512 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1992 / 0 | 953 / 0 | 483 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.390 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1992 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1992 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1992 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| pm-strahler | 885 / 0 | 511 / 0 | 30 / 0 | 1.576 / 0.000 | 81 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 632 / 0 | 643 / 0 | 31 / 0 | 2.016 / 0.000 | 120 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 880 / 0 | 510 / 0 | 30 / 0 | 1.578 / 0.000 | 81 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 442 / 0 | 434 / 0 | 31 / 0 | 1.980 / 0.000 | 89 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct | 806 / 0 | 513 / 0 | 31 / 0 | 1.635 / 0.000 | 192 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 470 / 0 | 483 / 0 | 31 / 0 | 2.026 / 0.000 | 145 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 801 / 0 | 512 / 0 | 31 / 0 | 1.638 / 0.000 | 192 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 470 / 0 | 483 / 0 | 31 / 0 | 2.026 / 0.000 | 145 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=4_compact.gm · 805 vertices / 1454 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 805 | 1454 | 9 | 186 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 323.043 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 323.133 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.702 | 435.801 | even | true | true | false | - |
| lifting-sym+pre | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.056 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.746 | 435.863 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.058 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 805 / 0 | 663 / 0 | 201 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 805 / 0 | 295 / 0 | 153 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 805 / 0 | 512 / 0 | 160 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.382 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 805 / 0 | 167 / 0 | 90 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 805 / 0 | 434 / 0 | 155 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.400 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 805 / 0 | 225 / 0 | 135 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 805 / 0 | 354 / 0 | 128 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 805 / 0 | 116 / 0 | 75 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 805 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 805 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 462 / 0 | 201 / 0 | 21 / 0 | 1.433 / 0.000 | 42 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 142 / 0 | 153 / 0 | 47 / 0 | 2.070 / 0.000 | 20 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 352 / 0 | 160 / 0 | 15 / 0 | 1.452 / 0.000 | 36 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 77 / 0 | 90 / 0 | 47 / 0 | 2.156 / 0.000 | 9 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 279 / 0 | 155 / 0 | 20 / 0 | 1.552 / 0.000 | 66 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 90 / 0 | 135 / 0 | 22 / 0 | 2.489 / 0.000 | 35 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 226 / 0 | 128 / 0 | 15 / 0 | 1.562 / 0.000 | 54 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 41 / 0 | 75 / 0 | 18 / 0 | 2.805 / 0.000 | 18 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=5.gm · 2425 vertices / 3420 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2425 | 3420 | 11 | 211 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.525 | 1388.152 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1467.414 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.555 | 1388.027 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.130 | 1468.715 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 2425 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2425 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.452 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2425 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.463 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2425 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.452 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.358 | 1388.039 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.117 | 1470.145 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.496 | 1388.023 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.153 | 1467.668 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 2425 / 0 | 1749 / 0 | 618 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.586 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2425 / 0 | 1160 / 0 | 541 / 0 | 6 / 0 | k=4, t=3, depth=5 / k=4, t=3, depth=5 | 0.442 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2425 / 0 | 1743 / 0 | 617 / 0 | 7 / 0 | k=3, t=3, depth=6 / k=3, t=3, depth=6 | 0.423 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2425 / 0 | 1160 / 0 | 541 / 0 | 6 / 0 | k=4, t=3, depth=5 / k=4, t=3, depth=5 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2425 / 0 | 1550 / 0 | 614 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.567 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2425 / 0 | 1137 / 0 | 591 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2425 / 0 | 1544 / 0 | 613 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.410 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2425 / 0 | 1137 / 0 | 591 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=5 | 0.390 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2425 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2425 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.379 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2425 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2425 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1131 / 0 | 618 / 0 | 29 / 0 | 1.546 / 0.000 | 99 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 619 / 0 | 541 / 0 | 31 / 0 | 1.872 / 0.000 | 78 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-strahler+iter | 1126 / 0 | 617 / 0 | 29 / 0 | 1.547 / 0.000 | 99 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 619 / 0 | 541 / 0 | 31 / 0 | 1.872 / 0.000 | 78 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct | 936 / 0 | 614 / 0 | 31 / 0 | 1.655 / 0.000 | 231 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 546 / 0 | 591 / 0 | 31 / 0 | 2.081 / 0.000 | 170 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 931 / 0 | 613 / 0 | 31 / 0 | 1.657 / 0.000 | 231 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 546 / 0 | 591 / 0 | 31 / 0 | 2.081 / 0.000 | 170 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=5_compact.gm · 974 vertices / 1752 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 974 | 1752 | 9 | 210 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 323.152 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 323.137 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.390 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.682 | 435.977 | even | true | true | false | - |
| lifting-sym+pre | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.086 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=6, t=9 / H=6, K=6, t=9 | 8.787 | 435.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=9 / H=4, K=4, t=9 | 1.096 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 974 / 0 | 759 / 0 | 227 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 974 / 0 | 349 / 0 | 186 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.442 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 974 / 0 | 577 / 0 | 188 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 974 / 0 | 200 / 0 | 113 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 974 / 0 | 582 / 0 | 216 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 974 / 0 | 290 / 0 | 176 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 974 / 0 | 421 / 0 | 164 / 0 | 6 / 0 | bits=3, depth=5 / bits=3, depth=6 | 0.382 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 974 / 0 | 134 / 0 | 86 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 974 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 974 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 532 / 0 | 227 / 0 | 28 / 0 | 1.425 / 0.000 | 41 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 163 / 0 | 186 / 0 | 46 / 0 | 2.135 / 0.000 | 21 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 389 / 0 | 188 / 0 | 15 / 0 | 1.481 / 0.000 | 40 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 87 / 0 | 113 / 0 | 45 / 0 | 2.287 / 0.000 | 10 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 366 / 0 | 216 / 0 | 26 / 0 | 1.587 / 0.000 | 89 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 114 / 0 | 176 / 0 | 27 / 0 | 2.535 / 0.000 | 44 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 257 / 0 | 164 / 0 | 15 / 0 | 1.634 / 0.000 | 67 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 48 / 0 | 86 / 0 | 20 / 0 | 2.771 / 0.000 | 21 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=6.gm · 2858 vertices / 4040 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2858 | 4040 | 11 | 235 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.575 | 1385.973 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1465.668 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.574 | 1386.062 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.133 | 1466.617 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 2858 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.493 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2858 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.483 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2858 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.495 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2858 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.483 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.370 | 1386.062 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.115 | 1465.863 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.140 | 1385.934 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1468.527 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 2858 / 0 | 1832 / 0 | 656 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 1.212 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2858 / 0 | 1567 / 0 | 730 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.483 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2858 / 0 | 1671 / 0 | 589 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 0.422 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2858 / 0 | 828 / 0 | 392 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2858 / 0 | 1864 / 0 | 741 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.596 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2858 / 0 | 1461 / 0 | 766 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2858 / 0 | 1858 / 0 | 740 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2858 / 0 | 733 / 0 | 413 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.424 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2858 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2858 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2858 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2858 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1176 / 0 | 656 / 0 | 31 / 0 | 1.557 / 0.000 | 102 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre | 837 / 0 | 730 / 0 | 63 / 0 | 1.871 / 0.000 | 92 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 1082 / 0 | 589 / 0 | 27 / 0 | 1.543 / 0.000 | 99 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 436 / 0 | 392 / 0 | 63 / 0 | 1.897 / 0.000 | 50 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 1123 / 0 | 741 / 0 | 31 / 0 | 1.659 / 0.000 | 272 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 695 / 0 | 766 / 0 | 40 / 0 | 2.101 / 0.000 | 228 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 1118 / 0 | 740 / 0 | 31 / 0 | 1.661 / 0.000 | 272 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 320 / 0 | 413 / 0 | 40 / 0 | 2.288 / 0.000 | 114 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=6_compact.gm · 1143 vertices / 2050 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1143 | 2050 | 9 | 234 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 667.520 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 667.695 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1143 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.414 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1143 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.071 | 840.703 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.134 | 103.176 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.075 | 839.375 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.153 | 103.117 | even | true | true | false | - |
| pm-strahler | complete | 1143 / 0 | 988 / 0 | 288 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.433 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1143 / 0 | 501 / 0 | 296 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.461 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1143 / 0 | 629 / 0 | 206 / 0 | 6 / 0 | k=3, t=2, depth=5 / k=3, t=2, depth=6 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1143 / 0 | 243 / 0 | 163 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1143 / 0 | 799 / 0 | 295 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=6 | 0.431 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1143 / 0 | 351 / 0 | 216 / 0 | 4 / 0 | bits=5, depth=3 / bits=5, depth=4 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1143 / 0 | 395 / 0 | 150 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1143 / 0 | 169 / 0 | 111 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1143 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1143 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1143 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 700 / 0 | 288 / 0 | 30 / 0 | 1.410 / 0.000 | 53 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 205 / 0 | 296 / 0 | 33 / 0 | 2.439 / 0.000 | 44 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 423 / 0 | 206 / 0 | 15 / 0 | 1.485 / 0.000 | 42 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 80 / 0 | 163 / 0 | 30 / 0 | 3.025 / 0.000 | 26 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 504 / 0 | 295 / 0 | 32 / 0 | 1.583 / 0.000 | 126 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 135 / 0 | 216 / 0 | 32 / 0 | 2.593 / 0.000 | 53 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 245 / 0 | 150 / 0 | 20 / 0 | 1.608 / 0.000 | 60 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 58 / 0 | 111 / 0 | 22 / 0 | 2.897 / 0.000 | 25 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=7.gm · 3291 vertices / 4660 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3291 | 4660 | 11 | 259 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.615 | 1386.031 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.117 | 1466.535 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.512 | 1385.898 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.128 | 1466.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 3291 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.534 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3291 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.525 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3291 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.526 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3291 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.514 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.340 | 1386.031 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1469.305 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.374 | 1385.902 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1467.785 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 3291 / 0 | 2186 / 0 | 781 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 1.313 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3291 / 0 | 1780 / 0 | 830 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.505 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3291 / 0 | 2000 / 0 | 703 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 0.443 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3291 / 0 | 1780 / 0 | 830 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.462 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3291 / 0 | 2164 / 0 | 862 / 0 | 7 / 0 | bits=5, depth=6 / bits=5, depth=6 | 1.382 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3291 / 0 | 1738 / 0 | 915 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.443 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3291 / 0 | 2082 / 0 | 837 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3291 / 0 | 854 / 0 | 482 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.421 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3291 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3291 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3291 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3291 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1405 / 0 | 781 / 0 | 31 / 0 | 1.555 / 0.000 | 121 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre | 950 / 0 | 830 / 0 | 60 / 0 | 1.873 / 0.000 | 101 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 1297 / 0 | 703 / 0 | 31 / 0 | 1.541 / 0.000 | 116 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 950 / 0 | 830 / 0 | 60 / 0 | 1.873 / 0.000 | 101 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 1302 / 0 | 862 / 0 | 31 / 0 | 1.661 / 0.000 | 318 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 823 / 0 | 915 / 0 | 44 / 0 | 2.111 / 0.000 | 267 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 1245 / 0 | 837 / 0 | 31 / 0 | 1.671 / 0.000 | 307 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 372 / 0 | 482 / 0 | 44 / 0 | 2.293 / 0.000 | 133 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=7_compact.gm · 1312 vertices / 2348 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1312 | 2348 | 9 | 258 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 667.582 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.059 | 667.578 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1312 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1312 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.414 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 840.453 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.210 | 103.289 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 837.078 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.218 | 103.188 | even | true | true | false | - |
| pm-strahler | complete | 1312 / 0 | 1155 / 0 | 336 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=6 | 0.503 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1312 / 0 | 663 / 0 | 377 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.472 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1312 / 0 | 649 / 0 | 210 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.421 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1312 / 0 | 287 / 0 | 185 / 0 | 4 / 0 | k=3, t=4, depth=3 / k=3, t=4, depth=4 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1312 / 0 | 908 / 0 | 334 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=6 | 0.452 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1312 / 0 | 393 / 0 | 242 / 0 | 4 / 0 | bits=5, depth=3 / bits=5, depth=4 | 0.432 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1312 / 0 | 463 / 0 | 177 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.421 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1312 / 0 | 193 / 0 | 128 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.422 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1312 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1312 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1312 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 819 / 0 | 336 / 0 | 35 / 0 | 1.409 / 0.000 | 59 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 286 / 0 | 377 / 0 | 59 / 0 | 2.315 / 0.000 | 49 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 439 / 0 | 210 / 0 | 28 / 0 | 1.476 / 0.000 | 41 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 102 / 0 | 185 / 0 | 29 / 0 | 2.804 / 0.000 | 30 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 574 / 0 | 334 / 0 | 36 / 0 | 1.580 / 0.000 | 140 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 151 / 0 | 242 / 0 | 36 / 0 | 2.596 / 0.000 | 59 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 286 / 0 | 177 / 0 | 22 / 0 | 1.615 / 0.000 | 71 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 65 / 0 | 128 / 0 | 24 / 0 | 2.954 / 0.000 | 28 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=8.gm · 3724 vertices / 5280 edges · 16 complete · 4 timeout · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3724 | 5280 | 11 | 283 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.578 | 1388.137 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1466.332 | - | true | - | - | deadline exceeded |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.577 | 1388.297 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.129 | 1469.402 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 3724 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.567 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3724 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.554 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3724 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | H=7, K=1, t=0 / H=6, K=1, t=0 | 0.577 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3724 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=6, K=1, t=0 / H=5, K=1, t=0 | 0.557 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.337 | 1388.262 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.113 | 1467.918 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.385 | 1388.258 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.124 | 1468.160 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 3724 / 0 | 3681 / 0 | 1413 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 1.484 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3724 / 0 | 1884 / 0 | 879 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.524 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3724 / 0 | 2680 / 0 | 1032 / 0 | 7 / 0 | k=4, t=3, depth=6 / k=4, t=3, depth=6 | 0.442 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3724 / 0 | 1884 / 0 | 879 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=5 | 0.472 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3724 / 0 | 2404 / 0 | 961 / 0 | 7 / 0 | bits=5, depth=6 / bits=5, depth=6 | 1.524 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3724 / 0 | 1992 / 0 | 1052 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.461 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3724 / 0 | 2168 / 0 | 880 / 0 | 7 / 0 | bits=4, depth=6 / bits=4, depth=6 | 0.453 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3724 / 0 | 989 / 0 | 565 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=5 | 0.421 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3724 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3724 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3724 / 0 | 7 / 0 | 1 / 0 | 7 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3724 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 2268 / 0 | 1413 / 0 | 31 / 0 | 1.623 / 0.000 | 259 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre | 1005 / 0 | 879 / 0 | 57 / 0 | 1.874 / 0.000 | 112 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 1648 / 0 | 1032 / 0 | 29 / 0 | 1.626 / 0.000 | 205 / 0 | 7 / 0 | 7.000 / 0.000 | 4 / 0 |
| pm-strahler+pre+iter | 1005 / 0 | 879 / 0 | 57 / 0 | 1.874 / 0.000 | 112 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-succinct | 1443 / 0 | 961 / 0 | 31 / 0 | 1.665 / 0.000 | 352 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre | 940 / 0 | 1052 / 0 | 48 / 0 | 2.118 / 0.000 | 304 / 0 | 6 / 0 | 6.000 / 0.000 | 5 / 0 |
| pm-succinct+iter | 1288 / 0 | 880 / 0 | 31 / 0 | 1.682 / 0.000 | 318 / 0 | 7 / 0 | 7.000 / 0.000 | 5 / 0 |
| pm-succinct+pre+iter | 424 / 0 | 565 / 0 | 48 / 0 | 2.330 / 0.000 | 152 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| zielonka | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym | 6 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/Includen=8_compact.gm · 1481 vertices / 2646 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1481 | 2646 | 9 | 282 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 667.691 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.057 | 667.730 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1481 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.411 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1481 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=6, K=1, t=0 / H=6, K=1, t=0 | 0.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=1, t=0 / H=4, K=1, t=0 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.072 | 841.703 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.205 | 94.832 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.075 | 839.418 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=4, K=4, t=10 / H=4, K=4, t=10 | 3.294 | 94.777 | even | true | true | false | - |
| pm-strahler | complete | 1481 / 0 | 1341 / 0 | 390 / 0 | 6 / 0 | k=3, t=4, depth=5 / k=3, t=4, depth=6 | 0.546 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1481 / 0 | 778 / 0 | 415 / 0 | 4 / 0 | k=3, t=5, depth=3 / k=3, t=5, depth=4 | 0.614 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1481 / 0 | 774 / 0 | 254 / 0 | 6 / 0 | k=3, t=3, depth=5 / k=3, t=3, depth=6 | 0.420 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1481 / 0 | 350 / 0 | 194 / 0 | 4 / 0 | k=3, t=5, depth=3 / k=3, t=5, depth=4 | 0.502 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1481 / 0 | 1035 / 0 | 385 / 0 | 6 / 0 | bits=5, depth=5 / bits=5, depth=6 | 0.464 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1481 / 0 | 450 / 0 | 282 / 0 | 4 / 0 | bits=5, depth=3 / bits=5, depth=4 | 0.453 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1481 / 0 | 542 / 0 | 209 / 0 | 6 / 0 | bits=4, depth=5 / bits=4, depth=6 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1481 / 0 | 229 / 0 | 154 / 0 | 4 / 0 | bits=4, depth=3 / bits=4, depth=4 | 0.415 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1481 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1481 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1481 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 951 / 0 | 390 / 0 | 41 / 0 | 1.409 / 0.000 | 68 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre | 363 / 0 | 415 / 0 | 84 / 0 | 2.140 / 0.000 | 39 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-strahler+iter | 520 / 0 | 254 / 0 | 30 / 0 | 1.487 / 0.000 | 51 / 0 | 6 / 0 | 6.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 156 / 0 | 194 / 0 | 82 / 0 | 2.237 / 0.000 | 16 / 0 | 4 / 0 | 4.000 / 0.000 | 3 / 0 |
| pm-succinct | 650 / 0 | 385 / 0 | 40 / 0 | 1.591 / 0.000 | 161 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre | 168 / 0 | 282 / 0 | 40 / 0 | 2.673 / 0.000 | 66 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| pm-succinct+iter | 333 / 0 | 209 / 0 | 24 / 0 | 1.625 / 0.000 | 82 / 0 | 6 / 0 | 6.000 / 0.000 | 4 / 0 |
| pm-succinct+pre+iter | 75 / 0 | 154 / 0 | 26 / 0 | 3.040 / 0.000 | 32 / 0 | 4 / 0 | 4.000 / 0.000 | 4 / 0 |
| zielonka | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 5 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=1.gm · 14 vertices / 16 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14 | 16 | 3 | 23 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 3 / 11 | 5 / 3 | 2 / 1 | 3 / 3 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 3 / 11 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 3 / 11 | 5 / 3 | 2 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 3 / 11 | 5 / 3 | 2 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 3 / 11 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 3 / 11 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 3 / 2 | 2 / 1 | 2 / 1 | 1.333 / 1.000 | 1 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 3 / 2 | 2 / 1 | 2 / 1 | 1.333 / 1.000 | 1 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 2 | 2 / 1 | 2 / 1 | 1.333 / 1.000 | 1 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=1_compact.gm · 7 vertices / 10 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7 | 10 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.416 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2 / 5 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.395 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2 / 5 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2 / 5 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2 / 5 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=2.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.123 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.123 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 89:1: unexpected keyword |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=2_compact.gm · 15 vertices / 25 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15 | 25 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.408 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.397 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 6 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 6 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 6 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 6 / 9 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 6 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 6 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 6 / 9 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 6 / 9 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 6 / 9 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 6 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=3.gm · 334 vertices / 458 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 334 | 458 | 3 | 95 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.615 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.613 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=8 / H=2, K=2, t=8 | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 227 / 107 | 29 / 3 | 17 / 1 | 3 / 3 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 227 / 107 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 227 / 107 | 25 / 3 | 17 / 1 | 3 / 3 | bits=2, depth=2 / bits=2, depth=2 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 227 / 107 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 227 / 107 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 227 / 107 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 12 / 2 | 17 / 1 | 11 / 1 | 2.333 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 8 / 2 | 17 / 1 | 7 / 1 | 3.000 / 1.000 | 4 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=3_compact.gm · 30 vertices / 53 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30 | 53 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 20 / 10 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 20 / 10 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 20 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 20 / 10 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 20 / 10 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 20 / 10 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 20 / 10 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 20 / 10 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 20 / 10 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 20 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=4.gm · 970 vertices / 1371 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 970 | 1371 | 3 | 133 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 1.882 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 1.882 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.630 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.641 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 783 / 187 | 41 / 3 | 24 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 783 / 187 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 783 / 187 | 33 / 3 | 24 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 783 / 187 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 783 / 187 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 783 / 187 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 17 / 2 | 24 / 1 | 16 / 1 | 2.353 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9 / 2 | 24 / 1 | 8 / 1 | 3.556 / 1.000 | 5 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=4_compact.gm · 65 vertices / 122 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 65 | 122 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 53 / 12 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 53 / 12 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.407 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 53 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 53 / 12 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 53 / 12 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 53 / 12 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 53 / 12 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 53 / 12 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 53 / 12 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 53 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.406 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=5.gm · 2443 vertices / 3482 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2443 | 3482 | 3 | 171 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 18.411 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 18.359 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 3.132 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 3.072 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2153 / 290 | 49 / 3 | 31 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.379 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2153 / 290 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2153 / 290 | 40 / 3 | 31 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.369 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2153 / 290 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.370 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.370 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.371 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2153 / 290 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.369 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2153 / 290 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 18 / 2 | 31 / 1 | 17 / 1 | 2.667 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9 / 2 | 31 / 1 | 14 / 1 | 4.333 / 1.000 | 5 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=5_compact.gm · 148 vertices / 287 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 148 | 287 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.405 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.396 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 134 / 14 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 134 / 14 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 134 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 134 / 14 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 134 / 14 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 134 / 14 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 134 / 14 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 134 / 14 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 134 / 14 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 134 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=6.gm · 5837 vertices / 8343 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5837 | 8343 | 3 | 209 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.436 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.446 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=12 / H=2, K=2, t=12 | 12.726 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=12 / H=2, K=2, t=12 | 12.776 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 5426 / 411 | 63 / 3 | 38 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.381 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5426 / 411 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 5426 / 411 | 51 / 3 | 38 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5426 / 411 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 5426 / 411 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5426 / 411 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 25 / 2 | 38 / 1 | 24 / 1 | 2.480 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 2 | 38 / 1 | 15 / 1 | 3.846 / 1.000 | 6 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=6_compact.gm · 332 vertices / 654 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 332 | 654 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.436 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.435 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 316 / 16 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 316 / 16 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 316 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 316 / 16 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 316 / 16 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 316 / 16 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 316 / 16 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 316 / 16 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 316 / 16 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 316 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=7.gm · 13687 vertices / 19598 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13687 | 19598 | 3 | 247 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 65.406 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 65.188 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 13135 / 552 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 13135 / 552 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.463 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 65.387 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 65.180 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 13135 / 552 | 77 / 3 | 45 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.462 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 13135 / 552 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 13135 / 552 | 59 / 3 | 45 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.468 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.424 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 13135 / 552 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.425 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.436 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 13135 / 552 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 13135 / 552 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 13135 / 552 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 32 / 2 | 45 / 1 | 31 / 1 | 2.375 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 14 / 2 | 45 / 1 | 15 / 1 | 4.143 / 1.000 | 7 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=7_compact.gm · 778 vertices / 1545 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 778 | 1545 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.539 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.382 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.539 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.414 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.411 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 760 / 18 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 760 / 18 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 760 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 760 / 18 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 760 / 18 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 760 / 18 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 760 / 18 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 760 / 18 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 760 / 18 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 760 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/LTMucalcBinaryCountern=8.gm · 32233 vertices / 46339 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 32233 | 46339 | 3 | 285 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 93.328 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 93.398 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 31518 / 715 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.504 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 31518 / 715 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.536 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 94.133 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 102.957 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 31518 / 715 | 69 / 3 | 52 / 1 | 3 / 3 | k=3, t=4, depth=2 / k=3, t=4, depth=2 | 0.818 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.509 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 31518 / 715 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.499 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.443 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 31518 / 715 | 69 / 3 | 52 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.638 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.453 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 31518 / 715 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.465 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.454 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 31518 / 715 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.466 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.469 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 31518 / 715 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.506 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 31518 / 715 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 2 | 52 / 1 | 16 / 1 | 4.000 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 17 / 2 | 52 / 1 | 16 / 1 | 4.000 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/LTMucalcBinaryCountern=8_compact.gm · 1794 vertices / 3576 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1794 | 3576 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 1.021 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.372 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 1.021 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.443 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=10 / H=1, K=1, t=10 | 0.443 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 1774 / 20 | 3 / 3 | 2 / 2 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1774 / 20 | 0 / 3 | 0 / 2 | 0 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1774 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.394 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1774 / 20 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 1774 / 20 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1774 / 20 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.390 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1774 / 20 | 3 / 3 | 2 / 2 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1774 / 20 | 0 / 3 | 0 / 2 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 1774 / 20 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1774 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.380 | 58.574 | odd | false | true | false | - |

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
<summary>mlsolver/games/MuCalcLimitClosurephi=p_n=0.gm · 16 vertices / 20 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16 | 20 | 4 | 49 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.408 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.396 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 16 / 0 | 18 / 0 | 11 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 16 / 0 | 17 / 0 | 11 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler | 7 / 0 | 11 / 0 | 6 / 0 | 2.429 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 6 / 0 | 10 / 0 | 6 / 0 | 2.500 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 6 / 0 | 10 / 0 | 6 / 0 | 2.500 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 6 / 0 | 10 / 0 | 6 / 0 | 2.500 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct | 6 / 0 | 11 / 0 | 7 / 0 | 2.667 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 5 / 0 | 10 / 0 | 7 / 0 | 2.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 5 / 0 | 10 / 0 | 7 / 0 | 2.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 5 / 0 | 10 / 0 | 7 / 0 | 2.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| zielonka | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym | 2 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |

</details>

