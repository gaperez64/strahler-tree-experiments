# pgsolver, part 5

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=17.gm · 1000 vertices / 9011 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 9011 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.275 | 1307.219 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.419 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.278 | 1307.352 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 520 / 480 | 6 / 2 | 1 / 1 | 6 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.887 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 520 / 480 | 6 / 2 | 1 / 1 | 6 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.877 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.217 | 1307.352 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.237 | 1307.281 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 520 / 480 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 520 / 480 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 520 / 480 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 520 / 480 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.411 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 520 / 480 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 520 / 480 | 6 / 2 | 1 / 1 | 6 / 2 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 520 / 480 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 1997 | 4 / 4 | 4 / 4 | 1.002 / 1.002 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 5 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 6 / 2 | 6.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=18.gm · 1000 vertices / 6762 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 6762 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.270 | 1306.516 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.270 | 1306.527 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 487 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.968 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 487 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.971 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.221 | 1306.398 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.268 | 1306.512 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 487 / 513 | 2500 / 3996 | 5 / 8 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.454 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 487 / 513 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 487 / 513 | 2495 / 3980 | 5 / 8 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 487 / 513 | 2495 / 3980 | 5 / 8 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.386 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 487 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 487 / 513 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 487 / 513 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 2495 / 3988 | 5 / 8 | 4 / 4 | 1.002 / 1.002 | 2 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2490 / 3972 | 5 / 8 | 2 / 2 | 1.002 / 1.002 | 4 / 7 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2490 / 3972 | 5 / 8 | 2 / 2 | 1.002 / 1.002 | 4 / 7 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=19.gm · 1000 vertices / 7750 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7750 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.263 | 1306.559 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.273 | 1306.570 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 490 / 510 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.919 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 490 / 510 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.917 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.263 | 1306.582 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.223 | 1306.309 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 490 / 510 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 490 / 510 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 490 / 510 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 490 / 510 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 490 / 510 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 490 / 510 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 1997 | 4 / 4 | 4 / 4 | 1.002 / 1.002 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 1994 | 4 / 4 | 2 / 2 | 1.002 / 1.002 | 3 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=2.gm · 1000 vertices / 7589 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7589 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.290 | 1306.562 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.258 | 1306.430 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 528 / 472 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.919 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 528 / 472 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.923 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.229 | 1306.562 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.271 | 1306.285 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 528 / 472 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 528 / 472 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 528 / 472 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.425 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 528 / 472 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 528 / 472 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 528 / 472 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 528 / 472 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=20.gm · 1000 vertices / 8658 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 8658 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.277 | 1306.434 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.273 | 1306.457 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 484 / 516 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.927 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 484 / 516 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.916 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.217 | 1306.609 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.259 | 1306.336 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 484 / 516 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.434 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 484 / 516 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 484 / 516 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.421 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 484 / 516 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.394 | 58.574 | even | true | true | false | - |
| zielonka | complete | 484 / 516 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 484 / 516 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 484 / 516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=21.gm · 1000 vertices / 11189 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 11189 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.252 | 1306.719 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.241 | 1306.582 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 498 / 502 | 3 / 2 | 1 / 1 | 3 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.896 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 498 / 502 | 3 / 2 | 1 / 1 | 3 / 2 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.884 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.219 | 1306.727 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.231 | 1306.727 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 498 / 502 | 1501 / 1501 | 3 / 3 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.435 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 498 / 502 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 498 / 502 | 1500 / 1500 | 3 / 3 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 498 / 502 | 1500 / 1500 | 3 / 3 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 498 / 502 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 498 / 502 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 498 / 502 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 1498 / 1498 | 3 / 3 | 3 / 3 | 1.001 / 1.001 | 1 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1497 / 1497 | 3 / 3 | 2 / 2 | 1.001 / 1.001 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1497 / 1497 | 3 / 3 | 2 / 2 | 1.001 / 1.001 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=22.gm · 1000 vertices / 8750 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 8750 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.273 | 1306.387 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.264 | 1306.410 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 533 / 467 | 2 / 6 | 1 / 1 | 2 / 6 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.898 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 533 / 467 | 2 / 6 | 1 / 1 | 2 / 6 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.884 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.265 | 1306.621 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.232 | 1306.559 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 533 / 467 | 2001 / 2001 | 4 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 533 / 467 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 533 / 467 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.424 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 533 / 467 | 1998 / 1998 | 4 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 533 / 467 | 2 / 6 | 1 / 1 | 2 / 6 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 533 / 467 | 2 / 6 | 1 / 1 | 2 / 6 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 533 / 467 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 5 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 6 | 2.000 / 6.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 5 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 6 | 2.000 / 6.000 | 1 / 1 |
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
| zielonka | 1 / 5 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 6 | 2.000 / 6.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 5 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 6 | 2.000 / 6.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=23.gm · 1000 vertices / 7400 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7400 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.243 | 1306.316 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.283 | 1306.484 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 490 / 510 | 5 / 4 | 1 / 1 | 5 / 4 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.940 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 490 / 510 | 5 / 4 | 1 / 1 | 5 / 4 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.926 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.218 | 1306.496 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.271 | 1306.371 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 490 / 510 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.444 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.414 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 490 / 510 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 490 / 510 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.425 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 490 / 510 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 490 / 510 | 5 / 4 | 1 / 1 | 5 / 4 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 490 / 510 | 5 / 4 | 1 / 1 | 5 / 4 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 490 / 510 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 4 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 4 | 5.000 / 4.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 4 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 4 | 5.000 / 4.000 | 1 / 1 |
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
| zielonka | 4 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 4 | 5.000 / 4.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 4 / 3 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5 / 4 | 5.000 / 4.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=24.gm · 1000 vertices / 7452 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7452 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.255 | 1306.461 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.255 | 1306.430 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 485 / 515 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.909 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 485 / 515 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.897 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.239 | 1306.336 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.257 | 1306.367 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 485 / 515 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 485 / 515 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.417 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 485 / 515 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.439 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.419 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 485 / 515 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.424 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.397 | 58.574 | even | true | true | false | - |
| zielonka | complete | 485 / 515 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 485 / 515 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 485 / 515 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 2495 | 4 / 5 | 4 / 4 | 1.002 / 1.002 | 1 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=3.gm · 1000 vertices / 6034 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 6034 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.273 | 1306.512 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.262 | 1306.488 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 544 / 456 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.930 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 544 / 456 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.926 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.238 | 1306.320 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.230 | 1306.379 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 544 / 456 | 2500 / 2999 | 5 / 6 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.444 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 544 / 456 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 544 / 456 | 2495 / 3490 | 5 / 7 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.433 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 544 / 456 | 2495 / 3490 | 5 / 7 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.390 | 58.574 | even | true | true | false | - |
| zielonka | complete | 544 / 456 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 544 / 456 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 544 / 456 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 2495 / 2993 | 5 / 6 | 4 / 4 | 1.002 / 1.002 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2490 / 3483 | 5 / 7 | 2 / 3 | 1.002 / 1.002 | 4 / 5 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2490 / 3483 | 5 / 7 | 2 / 3 | 1.002 / 1.002 | 4 / 5 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=4.gm · 1000 vertices / 7185 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7185 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.288 | 1306.238 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.245 | 1306.246 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 463 / 537 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.941 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 463 / 537 | 2 / 1 | 1 / 1 | 2 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.939 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.251 | 1306.352 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.236 | 1306.539 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 463 / 537 | 2999 / 2999 | 6 / 6 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.446 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 463 / 537 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.411 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 463 / 537 | 2991 / 2991 | 6 / 6 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.431 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 463 / 537 | 2991 / 2991 | 6 / 6 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.422 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 463 / 537 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 463 / 537 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 463 / 537 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 2993 / 2993 | 6 / 6 | 4 / 4 | 1.002 / 1.002 | 2 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2985 / 2985 | 6 / 6 | 2 / 2 | 1.002 / 1.002 | 5 / 5 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2985 / 2985 | 6 / 6 | 2 / 2 | 1.002 / 1.002 | 5 / 5 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=5.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.136 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.136 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | true | - | - | exit 3: 1002:1: unexpected keyword |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=6.gm · - vertices / - edges · 24 invalid input</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| - | - | - | - |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | invalid input | - / - | - / - | - / - | - / - | - / - | 0.127 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-adaptive+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| lifting-sym+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.126 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.135 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-strahler+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| pm-succinct+pre+iter | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym | invalid input | - / - | - / - | - / - | - / - | - / - | 0.125 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |
| zielonka-sym+pre | invalid input | - / - | - / - | - / - | - / - | - / - | 0.124 | 58.574 | - | false | - | - | exit 3: 1002:1: unexpected keyword |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=7.gm · 1000 vertices / 7449 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7449 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.253 | 1306.348 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.262 | 1306.570 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 483 / 517 | 3 / 3 | 1 / 1 | 3 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.938 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 483 / 517 | 3 / 3 | 1 / 1 | 3 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.928 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.222 | 1306.293 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.250 | 1306.551 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 483 / 517 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.433 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.415 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 483 / 517 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 483 / 517 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 483 / 517 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.393 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 483 / 517 | 3 / 3 | 1 / 1 | 3 / 3 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 483 / 517 | 3 / 3 | 1 / 1 | 3 / 3 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 483 / 517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
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
| zielonka | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=8.gm · 1000 vertices / 7835 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7835 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.251 | 1306.426 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 58.574 | odd | false | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.251 | 1306.406 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 486 / 514 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.948 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 486 / 514 | 3 / 1 | 1 / 1 | 3 / 1 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.948 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.275 | 1306.410 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.244 | 1306.422 | - | false | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 486 / 514 | 2500 / 2001 | 5 / 4 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.434 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 486 / 514 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.406 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 486 / 514 | 2495 / 1998 | 5 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.423 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 486 / 514 | 2495 / 1998 | 5 / 4 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.413 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.403 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 486 / 514 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.401 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 486 / 514 | 3 / 1 | 1 / 1 | 3 / 1 | — / — | 0.404 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 486 / 514 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 2495 / 1997 | 5 / 4 | 4 / 4 | 1.002 / 1.002 | 2 / 1 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 2490 / 1994 | 5 / 4 | 2 / 2 | 1.002 / 1.002 | 4 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 2490 / 1994 | 5 / 4 | 2 / 2 | 1.002 / 1.002 | 4 / 3 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 3 / 1 | 3.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(1000,_1,_20,_1,_20)id=9.gm · 1000 vertices / 7554 edges · 20 complete · 4 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1000 | 7554 | 1000 | 999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.279 | 1306.527 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.269 | 1306.551 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 500 / 500 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.918 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 500 / 500 | 2 / 3 | 1 / 1 | 2 / 3 | H=501, K=1, t=0 / H=500, K=1, t=0 | 0.914 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.221 | 1306.520 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.238 | 1306.277 | - | true | - | - | Solver failed: failed to build the Even host U^10_{9,501} |
| lifting-sym+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 500 / 500 | 2001 / 2500 | 4 / 5 | 501 / 501 | k=2, t=1, depth=500 / k=2, t=1, depth=500 | 0.445 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 500 / 500 | 501 / 501 | 1 / 1 | 501 / 501 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=500 / k=1, t=1, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 500 / 500 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.401 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 500 / 500 | 1998 / 2495 | 4 / 5 | 501 / 501 | bits=1, depth=500 / bits=1, depth=500 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=500 / bits=0, depth=500 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 500 / 500 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 500 / 500 | 2 / 3 | 1 / 1 | 2 / 3 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 500 / 500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 58.574 | even | true | true | false | - |

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
| pm-strahler | 1997 / 2495 | 4 / 5 | 4 / 4 | 1.002 / 1.002 | 1 / 2 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 500 / 500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 501 / 501 | 501.000 / 501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1994 / 2490 | 4 / 5 | 2 / 2 | 1.002 / 1.002 | 3 / 4 | 501 / 501 | 501.000 / 501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/towersofhanoi(10).gm · 236196 vertices / 413340 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 236196 | 413340 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 85.930 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.750 | 85.824 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 85.949 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.918 | 85.887 | even | true | true | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 85.812 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.765 | 85.828 | even | true | true | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 85.887 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.737 | 85.676 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 85.762 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.726 | 85.891 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 85.812 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.843 | 85.934 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 94.996 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.830 | 85.809 | even | true | true | false | - |
| pm-strahler+iter | complete | 177148 / 59048 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.839 | 85.812 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.785 | 85.770 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 91.680 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.754 | 85.762 | even | true | true | false | - |
| pm-succinct+iter | complete | 177148 / 59048 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.865 | 85.895 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.719 | 85.773 | even | true | true | false | - |
| zielonka | complete | 177148 / 59048 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.688 | 85.949 | even | true | true | false | - |
| zielonka+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.646 | 85.812 | even | true | true | false | - |
| zielonka-sym | complete | 177148 / 59048 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.794 | 85.953 | even | true | true | false | - |
| zielonka-sym+pre | complete | 177148 / 59048 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.657 | 85.949 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>pgsolver/games/towersofhanoi(11).gm · 708588 vertices / 1240026 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 708588 | 1240026 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 267.273 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.431 | 267.203 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 267.207 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.374 | 267.250 | even | true | true | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 267.145 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.485 | 267.270 | even | true | true | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 267.254 | - | true | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.412 | 267.133 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 267.188 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.400 | 267.270 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 267.188 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.542 | 267.141 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 274.645 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.678 | 267.133 | even | true | true | false | - |
| pm-strahler+iter | complete | 531442 / 177146 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.757 | 267.133 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.565 | 266.941 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 267.227 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.595 | 267.070 | even | true | true | false | - |
| pm-succinct+iter | complete | 531442 / 177146 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 1.873 | 267.148 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.490 | 267.094 | even | true | true | false | - |
| zielonka | complete | 531442 / 177146 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.389 | 267.207 | even | true | true | false | - |
| zielonka+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.252 | 267.133 | even | true | true | false | - |
| zielonka-sym | complete | 531442 / 177146 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.717 | 267.254 | even | true | true | false | - |
| zielonka-sym+pre | complete | 531442 / 177146 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.264 | 267.207 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
<summary>pgsolver/games/towersofhanoi(5).gm · 972 vertices / 1698 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 972 | 1698 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.519 | 62.645 | even | true | true | false | - |
| lifting+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 62.645 | even | true | true | false | - |
| lifting+iter | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.516 | 62.645 | even | true | true | false | - |
| lifting+pre+iter | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 62.645 | even | true | true | false | - |
| lifting-adaptive | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 62.645 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 62.645 | even | true | true | false | - |
| lifting-sym | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.424 | 62.645 | even | true | true | false | - |
| lifting-sym+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 62.645 | even | true | true | false | - |
| lifting-sym+iter | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.425 | 62.645 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 62.645 | even | true | true | false | - |
| pm-strahler | complete | 730 / 242 | 34 / 2 | 33 / 1 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 0.414 | 62.645 | even | true | true | false | - |
| pm-strahler+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 62.645 | even | true | true | false | - |
| pm-strahler+iter | complete | 730 / 242 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 62.645 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.395 | 62.645 | even | true | true | false | - |
| pm-succinct | complete | 730 / 242 | 34 / 2 | 33 / 1 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 0.414 | 62.645 | even | true | true | false | - |
| pm-succinct+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.392 | 62.645 | even | true | true | false | - |
| pm-succinct+iter | complete | 730 / 242 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.401 | 62.645 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.393 | 62.645 | even | true | true | false | - |
| zielonka | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 62.645 | even | true | true | false | - |
| zielonka+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 62.645 | even | true | true | false | - |
| zielonka-sym | complete | 730 / 242 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.382 | 62.645 | even | true | true | false | - |
| zielonka-sym+pre | complete | 730 / 242 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 62.645 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 33 / 1 | 33 / 1 | 33.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 33 / 1 | 33 / 1 | 33.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/towersofhanoi(6).gm · 2916 vertices / 5100 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2916 | 5100 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.789 | 62.645 | even | true | true | false | - |
| lifting+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 62.645 | even | true | true | false | - |
| lifting+iter | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.798 | 62.645 | even | true | true | false | - |
| lifting+pre+iter | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 62.645 | even | true | true | false | - |
| lifting-adaptive | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.400 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 62.645 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.422 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 62.645 | even | true | true | false | - |
| lifting-sym | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.649 | 62.645 | even | true | true | false | - |
| lifting-sym+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 62.645 | even | true | true | false | - |
| lifting-sym+iter | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.658 | 62.645 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 62.645 | even | true | true | false | - |
| pm-strahler | complete | 2188 / 728 | 66 / 2 | 65 / 1 | 2 / 2 | k=2, t=6, depth=1 / k=2, t=6, depth=1 | 0.484 | 62.645 | even | true | true | false | - |
| pm-strahler+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 62.645 | even | true | true | false | - |
| pm-strahler+iter | complete | 2188 / 728 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.508 | 62.645 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.549 | 62.645 | even | true | true | false | - |
| pm-succinct | complete | 2188 / 728 | 66 / 2 | 65 / 1 | 2 / 2 | bits=6, depth=1 / bits=6, depth=1 | 0.640 | 62.645 | even | true | true | false | - |
| pm-succinct+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.433 | 62.645 | even | true | true | false | - |
| pm-succinct+iter | complete | 2188 / 728 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.401 | 62.645 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 62.645 | even | true | true | false | - |
| zielonka | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 62.645 | even | true | true | false | - |
| zielonka+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 62.645 | even | true | true | false | - |
| zielonka-sym | complete | 2188 / 728 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 62.645 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2188 / 728 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 62.645 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 65 / 1 | 65 / 1 | 65.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 65 / 1 | 65 / 1 | 65.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/towersofhanoi(7).gm · 8748 vertices / 15306 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8748 | 15306 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 18.272 | 62.645 | even | true | true | false | - |
| lifting+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 62.645 | even | true | true | false | - |
| lifting+iter | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 18.230 | 62.645 | even | true | true | false | - |
| lifting+pre+iter | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 62.645 | even | true | true | false | - |
| lifting-adaptive | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.554 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.396 | 62.645 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.555 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 62.645 | even | true | true | false | - |
| lifting-sym | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 3.548 | 62.645 | even | true | true | false | - |
| lifting-sym+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 62.645 | even | true | true | false | - |
| lifting-sym+iter | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=13 / H=1, K=1, t=13 | 3.560 | 62.645 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 62.645 | even | true | true | false | - |
| pm-strahler | complete | 6562 / 2186 | 130 / 2 | 129 / 1 | 2 / 2 | k=2, t=7, depth=1 / k=2, t=7, depth=1 | 0.920 | 62.645 | even | true | true | false | - |
| pm-strahler+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 62.645 | even | true | true | false | - |
| pm-strahler+iter | complete | 6562 / 2186 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 62.645 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 62.645 | even | true | true | false | - |
| pm-succinct | complete | 6562 / 2186 | 130 / 2 | 129 / 1 | 2 / 2 | bits=7, depth=1 / bits=7, depth=1 | 0.922 | 62.645 | even | true | true | false | - |
| pm-succinct+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.391 | 62.645 | even | true | true | false | - |
| pm-succinct+iter | complete | 6562 / 2186 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 62.645 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.391 | 62.645 | even | true | true | false | - |
| zielonka | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 62.645 | even | true | true | false | - |
| zielonka+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 62.645 | even | true | true | false | - |
| zielonka-sym | complete | 6562 / 2186 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 62.645 | even | true | true | false | - |
| zielonka-sym+pre | complete | 6562 / 2186 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 62.645 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 129 / 1 | 129 / 1 | 129.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 129 / 1 | 129 / 1 | 129.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/towersofhanoi(8).gm · 26244 vertices / 45924 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 26244 | 45924 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 62.645 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 62.645 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 62.645 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 62.645 | even | true | true | false | - |
| lifting-adaptive | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.689 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.519 | 62.645 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.604 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 62.645 | even | true | true | false | - |
| lifting-sym | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=14 / H=1, K=1, t=14 | 19.425 | 62.645 | even | true | true | false | - |
| lifting-sym+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 62.645 | even | true | true | false | - |
| lifting-sym+iter | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=14 / H=1, K=1, t=14 | 18.852 | 62.645 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 62.645 | even | true | true | false | - |
| pm-strahler | complete | 19684 / 6560 | 258 / 2 | 257 / 1 | 2 / 2 | k=2, t=8, depth=1 / k=2, t=8, depth=1 | 3.758 | 62.645 | even | true | true | false | - |
| pm-strahler+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.422 | 62.645 | even | true | true | false | - |
| pm-strahler+iter | complete | 19684 / 6560 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.434 | 62.645 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.426 | 62.645 | even | true | true | false | - |
| pm-succinct | complete | 19684 / 6560 | 258 / 2 | 257 / 1 | 2 / 2 | bits=8, depth=1 / bits=8, depth=1 | 3.761 | 62.645 | even | true | true | false | - |
| pm-succinct+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.433 | 62.645 | even | true | true | false | - |
| pm-succinct+iter | complete | 19684 / 6560 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.442 | 62.645 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.432 | 62.645 | even | true | true | false | - |
| zielonka | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.443 | 62.645 | even | true | true | false | - |
| zielonka+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 62.645 | even | true | true | false | - |
| zielonka-sym | complete | 19684 / 6560 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.456 | 62.645 | even | true | true | false | - |
| zielonka-sym+pre | complete | 19684 / 6560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 62.645 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 257 / 1 | 257 / 1 | 257.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 257 / 1 | 257 / 1 | 257.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/towersofhanoi(9).gm · 78732 vertices / 137778 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 78732 | 137778 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 62.645 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 62.645 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 62.645 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 62.645 | even | true | true | false | - |
| lifting-adaptive | complete | 59050 / 19682 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 9.039 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.583 | 62.645 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 59050 / 19682 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 9.209 | 62.645 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.582 | 62.645 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 62.645 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.550 | 62.645 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 62.645 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.559 | 62.645 | even | true | true | false | - |
| pm-strahler | complete | 59050 / 19682 | 514 / 2 | 513 / 1 | 2 / 2 | k=2, t=9, depth=1 / k=2, t=9, depth=1 | 23.075 | 62.645 | even | true | true | false | - |
| pm-strahler+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.548 | 62.645 | even | true | true | false | - |
| pm-strahler+iter | complete | 59050 / 19682 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.571 | 62.645 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.538 | 62.645 | even | true | true | false | - |
| pm-succinct | complete | 59050 / 19682 | 514 / 2 | 513 / 1 | 2 / 2 | bits=9, depth=1 / bits=9, depth=1 | 20.576 | 62.645 | even | true | true | false | - |
| pm-succinct+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.537 | 62.645 | even | true | true | false | - |
| pm-succinct+iter | complete | 59050 / 19682 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.579 | 62.645 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.539 | 62.645 | even | true | true | false | - |
| zielonka | complete | 59050 / 19682 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.528 | 62.645 | even | true | true | false | - |
| zielonka+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 62.645 | even | true | true | false | - |
| zielonka-sym | complete | 59050 / 19682 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.559 | 62.645 | even | true | true | false | - |
| zielonka-sym+pre | complete | 59050 / 19682 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.519 | 62.645 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 513 / 1 | 513 / 1 | 513.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 513 / 1 | 513 / 1 | 513.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(2000).gm · 2000 vertices / 3998000 edges · 12 complete · 4 timeout · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2000 | 3998000 | 2000 | 1999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.735 | 173.734 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.066 | 173.730 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.749 | 173.598 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.025 | 173.723 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.712 | 173.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.022 | 173.793 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.720 | 173.586 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.023 | 173.727 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.713 | 173.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.034 | 173.859 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.713 | 173.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.022 | 173.859 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 173.680 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1000 / k=1, t=1, depth=1000 | 1.105 | 173.531 | even | true | true | false | - |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 173.664 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1000 / k=1, t=1, depth=1000 | 1.099 | 173.742 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 173.680 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1000 / bits=0, depth=1000 | 1.089 | 173.734 | even | true | true | false | - |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 173.742 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1000 / bits=0, depth=1000 | 1.086 | 173.531 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.709 | 173.859 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.009 | 173.859 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.710 | 173.719 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 1000 / 1000 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.995 | 173.730 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/cliquegame(5000).gm · 5000 vertices / 24995000 edges · 12 complete · 4 timeout · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 24995000 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 4.360 | 1083.598 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 8.471 | 1083.918 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 4.361 | 1083.648 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 11.505 | 1083.777 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 9.863 | 1083.566 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.350 | 1083.723 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 5.595 | 1083.914 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.790 | 1083.914 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 4.274 | 1083.789 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.854 | 1083.844 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 4.277 | 1083.914 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.787 | 1083.965 | even | true | true | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.047 | 1083.723 | - | true | - | - | deadline exceeded |
| pm-strahler+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 5.987 | 1083.863 | even | true | true | false | - |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 1083.930 | - | true | - | - | deadline exceeded |
| pm-strahler+pre+iter | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 5.977 | 1083.930 | even | true | true | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.052 | 1083.531 | - | true | - | - | deadline exceeded |
| pm-succinct+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 5.940 | 1083.930 | even | true | true | false | - |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.052 | 1083.738 | - | true | - | - | deadline exceeded |
| pm-succinct+pre+iter | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 5.858 | 1083.859 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 4.284 | 1083.852 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.831 | 1083.734 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 4.423 | 1083.859 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2500 / 2500 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.793 | 1083.984 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
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
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(1000).gm · 3001 vertices / 4001 edges · 8 complete · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3001 | 4001 | 2001 | 2000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.672 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.124 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.125 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | complete | 3001 / 0 | 876501 / 0 | 1001 / 0 | 1001 / 0 | k=2, t=1, depth=1000 / k=2, t=1, depth=1001 | 6.975 | 560.148 | even | true | true | false | - |
| pm-strahler+pre | complete | 3001 / 0 | 876501 / 0 | 1001 / 0 | 1001 / 0 | k=2, t=1, depth=1000 / k=2, t=1, depth=1001 | 7.227 | 560.246 | even | true | true | false | - |
| pm-strahler+iter | complete | 3001 / 0 | 876501 / 0 | 1001 / 0 | 1001 / 0 | k=2, t=1, depth=1000 / k=2, t=1, depth=1001 | 7.238 | 560.094 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3001 / 0 | 876501 / 0 | 1001 / 0 | 1001 / 0 | k=2, t=1, depth=1000 / k=2, t=1, depth=1001 | 7.109 | 560.074 | even | true | true | false | - |
| pm-succinct | complete | 3001 / 0 | 751501 / 0 | 1001 / 0 | 1001 / 0 | bits=1, depth=1000 / bits=1, depth=1001 | 6.214 | 500.691 | even | true | true | false | - |
| pm-succinct+pre | complete | 3001 / 0 | 751501 / 0 | 1001 / 0 | 1001 / 0 | bits=1, depth=1000 / bits=1, depth=1001 | 6.099 | 500.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 3001 / 0 | 751501 / 0 | 1001 / 0 | 1001 / 0 | bits=1, depth=1000 / bits=1, depth=1001 | 5.707 | 500.770 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3001 / 0 | 751501 / 0 | 1001 / 0 | 1001 / 0 | bits=1, depth=1000 / bits=1, depth=1001 | 5.849 | 500.727 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

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
| pm-strahler | 875500 / 0 | 1001 / 0 | 5 / 0 | 1.001 / 0.000 | 250 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 875500 / 0 | 1001 / 0 | 5 / 0 | 1.001 / 0.000 | 250 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 875500 / 0 | 1001 / 0 | 5 / 0 | 1.001 / 0.000 | 250 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 875500 / 0 | 1001 / 0 | 5 / 0 | 1.001 / 0.000 | 250 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-succinct | 750500 / 0 | 1001 / 0 | 3 / 0 | 1.001 / 0.000 | 500 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 750500 / 0 | 1001 / 0 | 3 / 0 | 1.001 / 0.000 | 500 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 750500 / 0 | 1001 / 0 | 3 / 0 | 1.001 / 0.000 | 500 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 750500 / 0 | 1001 / 0 | 3 / 0 | 1.001 / 0.000 | 500 / 0 | 1001 / 0 | 1001.000 / 0.000 | 2 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(10000).gm · 30001 vertices / 40001 edges · 8 out of memory · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 30001 | 40001 | 20001 | 20000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 3.487 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.160 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 3.511 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 3.510 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 3.596 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 3.595 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 3.577 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 5.100 | 1856.441 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.097 | 1856.469 | - | true | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.154 | 1854.695 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.759 | 1854.695 | - | true | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.571 | 1856.637 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.636 | 1856.586 | - | true | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.864 | 1854.535 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.575 | 1854.605 | - | true | - | - | Failed to allocate memory |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 2.974 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.177 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 2.965 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(2000).gm · 6001 vertices / 8001 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6001 | 8001 | 4001 | 4000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.249 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.238 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.238 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.238 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.238 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.246 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 31.719 | 1664.457 | - | true | - | - | metrics: deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 31.911 | 1682.609 | - | true | - | - | metrics: deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 31.777 | 1675.125 | - | true | - | - | metrics: deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 37.416 | 1743.547 | - | true | - | - | metrics: deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 37.173 | 1786.707 | - | true | - | - | metrics: deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 37.447 | 1795.203 | - | true | - | - | metrics: deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.094 | 1119.590 | - | true | - | - | metrics: deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.092 | 1119.754 | - | true | - | - | metrics: deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 20.584 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.247 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.242 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(20000).gm · 60001 vertices / 80001 edges · 1 timeout · 7 out of memory · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 60001 | 80001 | 40001 | 40000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.200 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 24.252 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 24.416 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.231 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 24.184 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.176 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 23.951 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.220 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 24.218 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.264 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 24.046 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 9.240 | 1909.918 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 21.898 | 1909.930 | - | true | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.435 | 1909.973 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 21.723 | 1909.879 | - | true | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 9.257 | 1909.816 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 22.822 | 1909.719 | - | true | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.286 | 1909.816 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.127 | 1909.781 | - | true | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.231 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 21.531 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.263 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 17.316 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/modelcheckerladder(5000).gm · 15001 vertices / 20001 edges · 8 out of memory · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 15001 | 20001 | 10001 | 10000 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.171 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.902 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.151 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.877 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.158 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.857 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.149 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.848 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.863 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.857 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 11.562 | 1905.016 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 11.390 | 1915.465 | - | true | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.232 | 1871.332 | - | true | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 29.039 | 1931.129 | - | true | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 27.090 | 1945.402 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 28.935 | 1935.164 | - | true | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 27.234 | 1944.883 | - | true | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.036 | 1944.895 | - | true | - | - | Failed to allocate memory |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 21.321 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.831 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.822 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(1000).gm · 5000 vertices / 10997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 10997 | 3002 | 3002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.161 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.159 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.149 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.136 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.133 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.123 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.124 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.123 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(10000).gm · 50000 vertices / 109997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 109997 | 30002 | 30002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.189 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.189 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.187 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.185 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.185 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.176 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.187 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(2000).gm · 10000 vertices / 21997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 21997 | 6002 | 6002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.139 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.137 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.133 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(20000).gm · 100000 vertices / 219997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 100000 | 219997 | 60002 | 60002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.261 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.270 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.260 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.270 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.248 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.260 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.248 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.268 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.249 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.259 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.246 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.259 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.238 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.246 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.226 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.246 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(500).gm · 2500 vertices / 5497 edges · 2 complete · 6 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2500 | 5497 | 1502 | 1502 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.137 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.137 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.135 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.134 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.000 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 0 / 2500 | 0 / 783 | 0 / 6 | 0 / 753 | bits=1, depth=751 / bits=1, depth=752 | 19.400 | 124.797 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 2500 | 0 / 777 | 0 / 6 | 0 / 752 | bits=1, depth=750 / bits=1, depth=751 | 19.409 | 124.797 | odd | - | - | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.140 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.124 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.124 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.124 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

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
| pm-succinct+iter | 0 / 777 | 0 / 6 | 0 / 2 | 0.000 / 1.006 | 0 / 5 | 0 / 753 | 0.000 / 753.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 771 | 0 / 6 | 0 / 2 | 0.000 / 1.006 | 0 / 5 | 0 / 752 | 0.000 / 752.000 | 0 / 2 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>pgsolver/games/recursiveladder(5000).gm · 25000 vertices / 54997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 25000 | 54997 | 15002 | 15002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.171 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.171 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.170 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.169 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.178 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/recursiveladder(50000).gm · 250000 vertices / 549997 edges · 8 timeout · 16 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 250000 | 549997 | 150002 | 150002 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.458 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | error | - / - | - / - | - / - | - / - | - / - | 0.489 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.446 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.468 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.436 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | error | - / - | - / - | - / - | - / - | - / - | 0.467 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.435 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.476 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.437 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.477 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.447 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | error | - / - | - / - | - / - | - / - | - / - | 0.485 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.797 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 124.797 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 124.797 | - | - | - | - | deadline exceeded |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.433 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | error | - / - | - / - | - / - | - / - | - / - | 0.441 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.400 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | error | - / - | - / - | - / - | - / - | - / - | 0.441 | 124.797 | - | - | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=0.gm · 10000 vertices / 101768 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 101768 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5027 / 4973 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.763 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5027 / 4973 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.505 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5027 / 4973 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.724 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5027 / 4973 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.712 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5027 / 4973 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=1.gm · 10000 vertices / 108037 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 108037 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.158 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 5006 / 4994 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.775 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5006 / 4994 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.446 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 5006 / 4994 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.734 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5006 / 4994 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.712 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.427 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5006 / 4994 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=10.gm · 10000 vertices / 101999 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 101999 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.158 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4919 / 5081 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.805 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4919 / 5081 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4919 / 5081 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.751 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4919 / 5081 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.743 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4919 / 5081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 24995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=11.gm · 10000 vertices / 91370 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 91370 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 4945 / 5055 | 25000 / 20001 | 5 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.787 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.436 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4945 / 5055 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.497 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 4945 / 5055 | 24995 / 19998 | 5 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.754 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4945 / 5055 | 24995 / 19998 | 5 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.746 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.458 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4945 / 5055 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 24995 / 19997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 24990 / 19994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24990 / 19994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=12.gm · 10000 vertices / 104537 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 104537 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5003 / 4997 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.817 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5003 / 4997 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5003 / 4997 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.756 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5003 / 4997 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 24995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=13.gm · 10000 vertices / 126174 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 126174 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.164 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 4979 / 5021 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.806 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4979 / 5021 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.516 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.442 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 4979 / 5021 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.753 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4979 / 5021 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.724 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.443 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4979 / 5021 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=14.gm · 10000 vertices / 132175 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 132175 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5050 / 4950 | 15001 / 20001 | 3 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.774 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5050 / 4950 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.516 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5050 / 4950 | 15000 / 19998 | 3 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.726 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5050 / 4950 | 15000 / 19998 | 3 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.700 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.444 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5050 / 4950 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 14998 / 19997 | 3 / 4 | 3 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 14997 / 19994 | 3 / 4 | 2 / 2 | 1.000 / 1.000 | 2 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 14997 / 19994 | 3 / 4 | 2 / 2 | 1.000 / 1.000 | 2 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=15.gm · 10000 vertices / 109528 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 109528 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5023 / 4977 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.804 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5023 / 4977 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.517 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5023 / 4977 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.764 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5023 / 4977 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.744 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.435 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5023 / 4977 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 24995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 24990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=16.gm · 10000 vertices / 111173 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 111173 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4962 / 5038 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.785 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4962 / 5038 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4962 / 5038 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.435 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4962 / 5038 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4962 / 5038 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=17.gm · 10000 vertices / 90141 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 90141 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5003 / 4997 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.870 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5003 / 4997 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.498 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5003 / 4997 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.732 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5003 / 4997 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.700 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5003 / 4997 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=18.gm · 10000 vertices / 89214 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 89214 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.466 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.182 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4840 / 5160 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.763 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4840 / 5160 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4840 / 5160 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.712 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4840 / 5160 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.690 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4840 / 5160 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 19997 / 19997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 19994 / 19994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

