# pgsolver, part 7

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=11.gm · 5000 vertices / 56081 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 56081 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2484 / 2516 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.578 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2484 / 2516 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.445 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2484 / 2516 | 12498 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.578 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2484 / 2516 | 12498 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.557 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2484 / 2516 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 12493 / 9994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 12493 / 9994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=12.gm · 5000 vertices / 49837 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 49837 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.420 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2538 / 2462 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.567 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.462 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2538 / 2462 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.451 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2538 / 2462 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2538 / 2462 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.536 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2538 / 2462 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=13.gm · 5000 vertices / 44687 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 44687 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2526 / 2474 | 10001 / 12500 | 4 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.579 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2526 / 2474 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2526 / 2474 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.557 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.424 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2526 / 2474 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 12495 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=14.gm · 5000 vertices / 46583 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 46583 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2491 / 2509 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.570 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.424 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2491 / 2509 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.445 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2491 / 2509 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.548 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2491 / 2509 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.536 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=15.gm · 5000 vertices / 57789 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 57789 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2506 / 2494 | 10001 / 12500 | 4 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.589 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2506 / 2494 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2506 / 2494 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.580 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2506 / 2494 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.557 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2506 / 2494 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 12495 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=16.gm · 5000 vertices / 50813 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 50813 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.138 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2515 / 2485 | 10001 / 12500 | 4 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.588 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2515 / 2485 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2515 / 2485 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.556 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2515 / 2485 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.558 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2515 / 2485 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 12495 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=17.gm · 5000 vertices / 45563 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 45563 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2440 / 2560 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.556 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2440 / 2560 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.416 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2440 / 2560 | 12498 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.559 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.425 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2440 / 2560 | 12498 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.412 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2440 / 2560 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 12493 / 9994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 12493 / 9994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=18.gm · 5000 vertices / 45532 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 45532 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2449 / 2551 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.556 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2449 / 2551 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2449 / 2551 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.548 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.423 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2449 / 2551 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.537 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.415 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2449 / 2551 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=19.gm · 5000 vertices / 51959 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 51959 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2526 / 2474 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.568 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2526 / 2474 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2526 / 2474 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2526 / 2474 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2526 / 2474 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=2.gm · 5000 vertices / 50443 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 50443 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2491 / 2509 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.577 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2491 / 2509 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2491 / 2509 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.546 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2491 / 2509 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.535 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2491 / 2509 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=20.gm · 5000 vertices / 68826 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 68826 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2556 / 2444 | 7501 / 7501 | 3 / 3 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.568 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.432 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2556 / 2444 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.453 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2556 / 2444 | 7500 / 7500 | 3 / 3 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.546 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.422 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2556 / 2444 | 7500 / 7500 | 3 / 3 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.517 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2556 / 2444 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 7498 / 7498 | 3 / 3 | 3 / 3 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 7497 / 7497 | 3 / 3 | 2 / 2 | 1.000 / 1.000 | 2 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 7497 / 7497 | 3 / 3 | 2 / 2 | 1.000 / 1.000 | 2 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=21.gm · 5000 vertices / 52016 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52016 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2478 / 2522 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.588 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2478 / 2522 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2478 / 2522 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.551 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.415 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2478 / 2522 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.549 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.411 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=22.gm · 5000 vertices / 41380 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 41380 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2494 / 2506 | 12500 / 10001 | 5 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.588 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2494 / 2506 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.447 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2494 / 2506 | 12495 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.561 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2494 / 2506 | 12495 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.415 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 12495 / 9997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 12490 / 9994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 12490 / 9994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=23.gm · 5000 vertices / 54754 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 54754 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2559 / 2441 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.578 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2559 / 2441 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2559 / 2441 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.556 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2559 / 2441 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.545 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2559 / 2441 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=24.gm · 5000 vertices / 49564 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 49564 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2483 / 2517 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.577 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2483 / 2517 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2483 / 2517 | 9998 / 12497 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.568 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2483 / 2517 | 9998 / 12497 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.556 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2483 / 2517 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 12492 | 4 / 5 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 12492 | 4 / 5 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=3.gm · 5000 vertices / 43425 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 43425 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2462 / 2538 | 12500 / 12500 | 5 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.633 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.427 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2462 / 2538 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.454 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.426 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2462 / 2538 | 12495 / 12495 | 5 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.584 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2462 / 2538 | 12495 / 12495 | 5 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.580 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.435 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2462 / 2538 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 12495 / 12495 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 12490 / 12490 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 12490 / 12490 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=4.gm · 5000 vertices / 45931 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 45931 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2406 / 2594 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.582 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.438 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2406 / 2594 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.447 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2406 / 2594 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2406 / 2594 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.537 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.424 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2406 / 2594 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=5.gm · 5000 vertices / 48918 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 48918 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.149 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.149 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.429 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2519 / 2481 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.596 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.449 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2519 / 2481 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.474 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2519 / 2481 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.568 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.500 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2519 / 2481 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.564 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.440 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2519 / 2481 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=6.gm · 5000 vertices / 44623 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 44623 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.149 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2471 / 2529 | 12500 / 10001 | 5 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.578 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2471 / 2529 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.453 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2471 / 2529 | 12495 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.568 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2471 / 2529 | 12495 / 9998 | 5 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.548 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.425 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2471 / 2529 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 12495 / 9997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 12490 / 9994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 12490 / 9994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=7.gm · 5000 vertices / 47513 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 47513 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.428 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2494 / 2506 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.591 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.427 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2494 / 2506 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.457 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.431 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2494 / 2506 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.572 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.430 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2494 / 2506 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.574 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.455 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.158 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.173 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2494 / 2506 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.426 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=8.gm · 5000 vertices / 44612 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 44612 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.439 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.472 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.170 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2507 / 2493 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.630 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.415 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2507 / 2493 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2507 / 2493 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2507 / 2493 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.539 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.415 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2507 / 2493 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 9997 / 9997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 9994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=9.gm · 5000 vertices / 45116 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 45116 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.140 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.411 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2478 / 2522 | 10001 / 12500 | 4 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.590 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.435 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2478 / 2522 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2478 / 2522 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.566 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2478 / 2522 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.568 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2478 / 2522 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 9997 / 12495 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 9994 / 12490 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=0.gm · 50000 vertices / 616050 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 616050 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.355 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.699 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.364 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.700 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.366 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.353 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.667 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.348 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.690 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.349 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24928 / 25072 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.086 | 147.684 | even | true | true | false | - |
| pm-strahler+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.692 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24928 / 25072 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.115 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.683 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24928 / 25072 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.662 | 147.730 | even | true | true | false | - |
| pm-succinct+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.709 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24928 / 25072 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.416 | 147.668 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.743 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.352 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.659 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.339 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24928 / 25072 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=1.gm · 50000 vertices / 544367 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 544367 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.664 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.334 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.650 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.340 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.641 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.645 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.320 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.662 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25095 / 24905 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.878 | 147.633 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.683 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25095 / 24905 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.073 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.660 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25095 / 24905 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.531 | 147.668 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.673 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25095 / 24905 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.319 | 147.652 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.660 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.629 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.319 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25095 / 24905 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.587 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=10.gm · 50000 vertices / 600297 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 600297 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.356 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.688 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.355 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.663 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.361 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.334 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.662 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.340 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.333 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.683 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25022 / 24978 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.971 | 147.691 | even | true | true | false | - |
| pm-strahler+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.693 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25022 / 24978 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.115 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.691 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25022 / 24978 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.642 | 147.637 | even | true | true | false | - |
| pm-succinct+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.693 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25022 / 24978 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.352 | 147.543 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.752 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25022 / 24978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.606 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=11.gm · 50000 vertices / 574223 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 574223 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.345 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.665 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.343 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.663 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.340 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.704 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 24836 / 25164 | 100001 / 125000 | 4 / 5 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.115 | 159.781 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.708 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24836 / 25164 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.110 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.671 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 24836 / 25164 | 99998 / 124995 | 4 / 5 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.729 | 159.781 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.671 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24836 / 25164 | 99998 / 124995 | 4 / 5 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.477 | 159.641 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.669 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.319 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24836 / 25164 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.597 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 124995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 124990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 124990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=12.gm · 50000 vertices / 623393 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 623393 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.366 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.696 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.366 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.694 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24884 / 25116 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.034 | 147.836 | even | true | true | false | - |
| pm-strahler+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.712 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24884 / 25116 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.113 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.694 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24884 / 25116 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.597 | 147.711 | even | true | true | false | - |
| pm-succinct+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.695 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24884 / 25116 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.346 | 147.723 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.702 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.644 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.339 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24884 / 25116 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=13.gm · 50000 vertices / 591893 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 591893 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.355 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.675 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.354 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.340 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24868 / 25132 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.050 | 147.676 | even | true | true | false | - |
| pm-strahler+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.691 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24868 / 25132 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.092 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.691 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24868 / 25132 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.534 | 147.762 | even | true | true | false | - |
| pm-succinct+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.672 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24868 / 25132 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.339 | 147.664 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.679 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24868 / 25132 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.641 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=14.gm · 50000 vertices / 661142 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 661142 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.699 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.363 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.691 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.681 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.352 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.706 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25016 / 24984 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.134 | 147.656 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.721 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25016 / 24984 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.148 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.713 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25016 / 24984 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.619 | 147.727 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.704 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25016 / 24984 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.378 | 147.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.701 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25016 / 24984 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.627 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=15.gm · 50000 vertices / 715668 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 715668 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.386 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.717 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.396 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.692 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.372 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.713 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.372 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.371 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.364 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.714 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 24877 / 25123 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.199 | 147.672 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.737 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24877 / 25123 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.197 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.731 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 24877 / 25123 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.705 | 147.750 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.731 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24877 / 25123 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.429 | 147.793 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.722 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.372 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.360 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24877 / 25123 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.648 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=16.gm · 50000 vertices / 571970 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 571970 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.664 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.652 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.332 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25238 / 24762 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.913 | 147.676 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.683 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25238 / 24762 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.093 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.671 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25238 / 24762 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.544 | 147.629 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.685 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25238 / 24762 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.283 | 147.672 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.671 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.318 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25238 / 24762 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.596 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=17.gm · 50000 vertices / 649382 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 649382 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.707 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.375 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.685 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.352 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.705 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.354 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.682 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.694 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 24933 / 25067 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.053 | 147.672 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.715 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24933 / 25067 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.135 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.700 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 24933 / 25067 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.603 | 147.758 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.711 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24933 / 25067 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.344 | 147.812 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.704 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.339 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24933 / 25067 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.627 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=18.gm · 50000 vertices / 727957 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 727957 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.398 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.725 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.398 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.701 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.381 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.723 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.370 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.712 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.371 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.713 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.373 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.723 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25068 / 24932 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.355 | 147.723 | even | true | true | false | - |
| pm-strahler+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25068 / 24932 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.195 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.741 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25068 / 24932 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.772 | 147.672 | even | true | true | false | - |
| pm-succinct+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.723 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25068 / 24932 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.471 | 147.691 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.703 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.371 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.684 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.363 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25068 / 24932 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.647 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=19.gm · 50000 vertices / 661654 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 661654 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.696 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.376 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.361 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.683 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.730 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.352 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.710 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 24857 / 25143 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.213 | 147.609 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.717 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24857 / 25143 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.158 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.712 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 24857 / 25143 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.643 | 147.645 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.703 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24857 / 25143 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.364 | 147.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.698 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.351 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.339 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24857 / 25143 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.627 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=2.gm · 50000 vertices / 632296 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 632296 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.365 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.685 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.365 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.350 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.733 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.353 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.677 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25020 / 24980 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.086 | 147.672 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.710 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25020 / 24980 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.146 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.704 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25020 / 24980 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.664 | 147.676 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.702 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25020 / 24980 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.387 | 147.777 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.691 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.648 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.349 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25020 / 24980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.617 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=20.gm · 50000 vertices / 593284 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 593284 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.356 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.686 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.356 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.663 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.663 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.342 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.664 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.341 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25046 / 24954 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.946 | 147.609 | even | true | true | false | - |
| pm-strahler+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.694 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25046 / 24954 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.097 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.692 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25046 / 24954 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.521 | 147.672 | even | true | true | false | - |
| pm-succinct+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.690 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25046 / 24954 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.284 | 147.742 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.689 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.328 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25046 / 24954 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.606 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=21.gm · 50000 vertices / 542708 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 542708 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.345 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.655 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.320 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.661 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25149 / 24851 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.870 | 147.668 | even | true | true | false | - |
| pm-strahler+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.663 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25149 / 24851 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.082 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.673 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25149 / 24851 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.518 | 147.676 | even | true | true | false | - |
| pm-succinct+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.660 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25149 / 24851 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.306 | 147.688 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.703 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.629 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.318 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25149 / 24851 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.586 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=22.gm · 50000 vertices / 537773 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 537773 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.345 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.654 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.641 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.320 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.320 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.650 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25128 / 24872 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.853 | 147.816 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.671 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25128 / 24872 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.076 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.660 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25128 / 24872 | 124998 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.649 | 159.664 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.659 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25128 / 24872 | 124998 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.443 | 159.609 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.658 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.310 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.632 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.312 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25128 / 24872 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.608 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 124993 / 99994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 124993 / 99994 | 5 / 4 | 3 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=23.gm · 50000 vertices / 849930 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 849930 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.438 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.760 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.437 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.744 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.414 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.763 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.404 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.744 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.412 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.745 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.403 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.754 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 25044 / 24956 | 75001 / 75001 | 3 / 3 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.049 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.795 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 25044 / 24956 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.282 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.776 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 25044 / 24956 | 75000 / 75000 | 3 / 3 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.532 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.764 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 25044 / 24956 | 75000 / 75000 | 3 / 3 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.242 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.774 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.402 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.733 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.401 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25044 / 24956 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.689 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 74998 / 74998 | 3 / 3 | 3 / 3 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 74997 / 74997 | 3 / 3 | 2 / 2 | 1.000 / 1.000 | 2 / 2 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 74997 / 74997 | 3 / 3 | 2 / 2 | 1.000 / 1.000 | 2 / 2 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=24.gm · 50000 vertices / 574556 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 574556 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.345 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.665 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.344 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.330 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.651 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.331 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.662 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.332 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 25242 / 24758 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 2.877 | 147.555 | even | true | true | false | - |
| pm-strahler+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.693 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 25242 / 24758 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.106 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.672 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 25242 / 24758 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.510 | 147.730 | even | true | true | false | - |
| pm-succinct+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.650 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 25242 / 24758 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.301 | 147.652 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.674 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.321 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.640 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.319 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 25242 / 24758 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.596 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=3.gm · 50000 vertices / 719280 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 719280 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.397 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.717 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.397 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.383 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.704 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.371 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.716 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.374 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.740 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.379 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.738 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 24975 / 25025 | 100001 / 100001 | 4 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.271 | 147.676 | even | true | true | false | - |
| pm-strahler+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.755 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 24975 / 25025 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.201 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.735 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 24975 / 25025 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.712 | 147.691 | even | true | true | false | - |
| pm-succinct+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.726 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 24975 / 25025 | 99998 / 99998 | 4 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.448 | 147.715 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.719 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.374 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.690 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.360 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24975 / 25025 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.648 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 99997 / 99997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 99994 / 99994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(50000,_1,_20,_1,_20)id=4.gm · 50000 vertices / 570049 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 50000 | 570049 | 50000 | 49999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.368 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.722 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.367 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.700 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.355 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.713 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.356 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.737 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.373 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.709 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.354 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.714 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 24994 / 25006 | 125000 / 100001 | 5 / 4 | 25001 / 25001 | k=2, t=1, depth=25000 / k=2, t=1, depth=25000 | 3.500 | 159.730 | odd | false | true | false | - |
| pm-strahler+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.754 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 24994 / 25006 | 25001 / 25001 | 1 / 1 | 25001 / 25001 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 1.176 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=25000 / k=1, t=1, depth=25000 | 0.753 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 24994 / 25006 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.915 | 159.703 | odd | false | true | false | - |
| pm-succinct+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.740 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 24994 / 25006 | 124995 / 99998 | 5 / 4 | 25001 / 25001 | bits=1, depth=25000 / bits=1, depth=25000 | 2.699 | 159.734 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=25000 / bits=0, depth=25000 | 0.736 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.345 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.702 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.334 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 24994 / 25006 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.633 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 124995 / 99997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 25000 / 25000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 25001 / 25001 | 25001.000 / 25001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 124990 / 99994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 25001 / 25001 | 25001.000 / 25001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

