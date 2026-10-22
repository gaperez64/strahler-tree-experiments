# pgsolver, part 6

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=2.gm · 10000 vertices / 97147 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 97147 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4966 / 5034 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.868 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.435 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4966 / 5034 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4966 / 5034 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.773 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4966 / 5034 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.752 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4966 / 5034 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=20.gm · 10000 vertices / 97015 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 97015 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 5020 / 4980 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 1.850 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.423 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5020 / 4980 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.494 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 5020 / 4980 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.704 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.435 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5020 / 4980 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.701 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.164 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5020 / 4980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 124.797 | odd | false | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=21.gm · 10000 vertices / 101640 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 101640 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4897 / 5103 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.785 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4897 / 5103 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4897 / 5103 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4897 / 5103 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.703 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4897 / 5103 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=22.gm · 10000 vertices / 107295 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 107295 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 5116 / 4884 | 25000 / 20001 | 5 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.806 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.436 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5116 / 4884 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.505 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 5116 / 4884 | 29994 / 19998 | 6 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.784 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5116 / 4884 | 29994 / 19998 | 6 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.762 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5116 / 4884 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 124.797 | odd | false | true | false | - |

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
| pm-succinct | 29988 / 19994 | 6 / 4 | 3 / 2 | 1.000 / 1.000 | 4 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 29988 / 19994 | 6 / 4 | 3 / 2 | 1.000 / 1.000 | 4 / 3 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=23.gm · 10000 vertices / 98217 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 98217 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 4974 / 5026 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.764 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 4974 / 5026 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.505 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 4974 / 5026 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.725 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 4974 / 5026 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.703 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4974 / 5026 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 124.797 | odd | false | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=24.gm · 10000 vertices / 99239 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 99239 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5032 / 4968 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.785 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5032 / 4968 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.496 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5032 / 4968 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.752 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5032 / 4968 | 19998 / 24995 | 4 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.733 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.175 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.176 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5032 / 4968 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=3.gm · 10000 vertices / 95995 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 95995 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4963 / 5037 | 20001 / 25000 | 4 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.785 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4963 / 5037 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.504 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4963 / 5037 | 24998 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.774 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4963 / 5037 | 24998 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.761 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4963 / 5037 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |

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
| pm-succinct | 24993 / 24990 | 5 / 5 | 3 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24993 / 24990 | 5 / 5 | 3 / 2 | 1.000 / 1.000 | 3 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=4.gm · 10000 vertices / 93391 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 93391 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.158 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 5055 / 4945 | 25000 / 25000 | 5 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.817 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5055 / 4945 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 5055 / 4945 | 24995 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.773 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.431 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5055 / 4945 | 24995 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.763 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.154 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5055 / 4945 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.422 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 24995 / 24995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 24990 / 24990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24990 / 24990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=5.gm · 10000 vertices / 105372 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 105372 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.155 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4954 / 5046 | 25000 / 25000 | 5 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.836 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4954 / 5046 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.432 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4954 / 5046 | 24995 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.792 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.435 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4954 / 5046 | 24995 / 24995 | 5 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.764 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4954 / 5046 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 24995 / 24995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 24990 / 24990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 24990 / 24990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=6.gm · 10000 vertices / 111298 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 111298 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 4881 / 5119 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.786 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 4881 / 5119 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.507 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.434 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 4881 / 5119 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.743 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.433 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 4881 / 5119 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.710 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.443 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.156 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 4881 / 5119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=7.gm · 10000 vertices / 122675 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 122675 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5058 / 4942 | 15001 / 25000 | 3 / 5 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.786 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5058 / 4942 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.515 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5058 / 4942 | 15000 / 24995 | 3 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.737 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.446 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5058 / 4942 | 15000 / 24995 | 3 / 5 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.723 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.444 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5058 / 4942 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 14998 / 24995 | 3 / 5 | 3 / 4 | 1.000 / 1.000 | 1 / 2 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5000 / 5000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 5001 / 5001 | 5001.000 / 5001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 14997 / 24990 | 3 / 5 | 2 / 2 | 1.000 / 1.000 | 2 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 14997 / 24990 | 3 / 5 | 2 / 2 | 1.000 / 1.000 | 2 / 4 | 5001 / 5001 | 5001.000 / 5001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=8.gm · 10000 vertices / 114637 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 114637 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.167 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 5114 / 4886 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.784 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.435 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5114 / 4886 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.514 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.442 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 5114 / 4886 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.747 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.441 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5114 / 4886 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.717 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.432 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5114 / 4886 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 124.797 | odd | false | true | false | - |

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
<summary>pgsolver/games/steadygame(10000,_1,_20,_1,_20)id=9.gm · 10000 vertices / 123116 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10000 | 123116 | 10000 | 9999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.437 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.168 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.165 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 5013 / 4987 | 20001 / 20001 | 4 / 4 | 5001 / 5001 | k=2, t=1, depth=5000 / k=2, t=1, depth=5000 | 0.785 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 5013 / 4987 | 5001 / 5001 | 1 / 1 | 5001 / 5001 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.515 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=5000 / k=1, t=1, depth=5000 | 0.443 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 5013 / 4987 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.742 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.445 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 5013 / 4987 | 19998 / 19998 | 4 / 4 | 5001 / 5001 | bits=1, depth=5000 / bits=1, depth=5000 | 0.723 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=5000 / bits=0, depth=5000 | 0.443 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.166 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.157 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 5013 / 4987 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.433 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=0.gm · 20000 vertices / 230193 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 230193 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.211 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.505 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.211 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.511 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.523 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.514 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.210 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.515 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.209 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10001 / 9999 | 50000 / 40001 | 5 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.352 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.509 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10001 / 9999 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.640 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10001 / 9999 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.253 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10001 / 9999 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.141 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.497 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10001 / 9999 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.472 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 49995 / 39997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=1.gm · 20000 vertices / 275660 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 275660 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.219 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.218 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 9985 / 10015 | 40001 / 30001 | 4 / 3 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.258 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.506 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9985 / 10015 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.660 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.504 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 9985 / 10015 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.125 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.507 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9985 / 10015 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.041 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.503 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9985 / 10015 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 29998 | 4 / 3 | 4 / 3 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=10.gm · 20000 vertices / 221533 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 221533 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 9913 / 10087 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.247 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9913 / 10087 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.638 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.494 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 9913 / 10087 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.135 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.496 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9913 / 10087 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.073 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.494 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=11.gm · 20000 vertices / 193426 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 193426 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 9938 / 10062 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.207 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.485 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9938 / 10062 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.628 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.484 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 9938 / 10062 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.094 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.476 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9938 / 10062 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.055 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.486 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9938 / 10062 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=12.gm · 20000 vertices / 196836 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 196836 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10073 / 9927 | 40001 / 50000 | 4 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.290 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.493 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10073 / 9927 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.629 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.489 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10073 / 9927 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.179 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.484 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10073 / 9927 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.135 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.474 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.464 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10073 / 9927 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 49995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=13.gm · 20000 vertices / 235034 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 235034 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.209 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.489 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10049 / 9951 | 50000 / 40001 | 5 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.310 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.497 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10049 / 9951 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.640 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.498 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10049 / 9951 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.216 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.506 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10049 / 9951 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.166 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.505 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10049 / 9951 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.462 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 49995 / 39997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=14.gm · 20000 vertices / 236466 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 236466 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.209 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10070 / 9930 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.258 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10070 / 9930 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.639 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.493 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10070 / 9930 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.155 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10070 / 9930 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.092 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10070 / 9930 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=15.gm · 20000 vertices / 181963 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 181963 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.189 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.187 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.185 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.533 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9881 / 10119 | 40001 / 50000 | 4 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.247 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.490 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9881 / 10119 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.608 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.476 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9881 / 10119 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.167 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9881 / 10119 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.114 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.474 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.185 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.189 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9881 / 10119 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 49995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=16.gm · 20000 vertices / 264246 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 264246 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.219 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.218 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10002 / 9998 | 40001 / 30001 | 4 / 3 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.229 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.505 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10002 / 9998 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.659 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.515 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10002 / 9998 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.104 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10002 / 9998 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.033 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.218 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10002 / 9998 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 29998 | 4 / 3 | 4 / 3 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=17.gm · 20000 vertices / 201195 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 201195 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10137 / 9863 | 40001 / 50000 | 4 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.270 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.493 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10137 / 9863 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.621 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.487 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10137 / 9863 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.179 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10137 / 9863 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.137 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.476 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10137 / 9863 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 49995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=18.gm · 20000 vertices / 212209 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 212209 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9913 / 10087 | 50000 / 50000 | 5 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.341 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.483 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9913 / 10087 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.628 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9913 / 10087 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.261 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.483 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9913 / 10087 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.207 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.496 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9913 / 10087 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.455 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 49995 / 49995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=19.gm · 20000 vertices / 272503 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 272503 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.219 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.218 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9879 / 10121 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.312 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9879 / 10121 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.671 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.517 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9879 / 10121 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.207 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.516 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9879 / 10121 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.124 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.504 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9879 / 10121 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=2.gm · 20000 vertices / 224917 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 224917 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.482 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10057 / 9943 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.395 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.483 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10057 / 9943 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.630 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.487 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10057 / 9943 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.146 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10057 / 9943 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.093 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=20.gm · 20000 vertices / 211497 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 211497 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 9919 / 10081 | 40001 / 50000 | 4 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.279 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.486 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9919 / 10081 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.639 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.482 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 9919 / 10081 | 39998 / 59997 | 4 / 6 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.238 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.496 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9919 / 10081 | 39998 / 59997 | 4 / 6 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.198 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9919 / 10081 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 49995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 59991 | 4 / 6 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 59991 | 4 / 6 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=21.gm · 20000 vertices / 208638 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 208638 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10022 / 9978 | 50000 / 50000 | 5 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.330 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.484 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10022 / 9978 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.629 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10022 / 9978 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.249 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10022 / 9978 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.201 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.467 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.200 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10022 / 9978 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 49995 / 49995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=22.gm · 20000 vertices / 210762 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 210762 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10040 / 9960 | 40001 / 50000 | 4 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.290 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.504 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10040 / 9960 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.629 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.483 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10040 / 9960 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.213 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.510 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10040 / 9960 | 39998 / 49995 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.193 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.498 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10040 / 9960 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 49995 | 4 / 5 | 4 / 4 | 1.000 / 1.000 | 1 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 49990 | 4 / 5 | 2 / 2 | 1.000 / 1.000 | 3 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=23.gm · 20000 vertices / 201159 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 201159 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10020 / 9980 | 50000 / 40001 | 5 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.301 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10020 / 9980 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.630 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.494 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10020 / 9980 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.176 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.486 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10020 / 9980 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.127 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10020 / 9980 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.452 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 49995 / 39997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=24.gm · 20000 vertices / 191616 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 191616 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.200 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.188 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10096 / 9904 | 50000 / 50000 | 5 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.328 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.486 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10096 / 9904 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.620 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.485 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10096 / 9904 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.238 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.475 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10096 / 9904 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.194 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.486 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.186 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10096 / 9904 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.442 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 49995 / 49995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=3.gm · 20000 vertices / 225152 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 225152 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.199 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9867 / 10133 | 50000 / 40001 | 5 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.311 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.493 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9867 / 10133 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.639 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.494 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9867 / 10133 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.212 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.498 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9867 / 10133 | 49995 / 39998 | 5 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.148 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.496 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9867 / 10133 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.453 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 49995 / 39997 | 5 / 4 | 4 / 4 | 1.000 / 1.000 | 2 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 39994 | 5 / 4 | 2 / 2 | 1.000 / 1.000 | 4 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=4.gm · 20000 vertices / 234858 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 234858 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.209 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 10059 / 9941 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.279 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.496 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 10059 / 9941 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.650 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.495 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 10059 / 9941 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.165 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.497 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 10059 / 9941 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.091 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.505 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=5.gm · 20000 vertices / 278603 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 278603 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.220 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.500 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.219 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.216 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.499 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.500 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.219 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.505 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 9941 / 10059 | 40001 / 30001 | 4 / 3 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.257 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.504 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 9941 / 10059 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.669 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.514 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 9941 / 10059 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.139 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.508 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 9941 / 10059 | 39998 / 30000 | 4 / 3 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.045 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.506 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.208 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9941 / 10059 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 29998 | 4 / 3 | 4 / 3 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 29997 | 4 / 3 | 2 / 2 | 1.000 / 1.000 | 3 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=6.gm · 20000 vertices / 229972 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 229972 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.203 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.491 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.202 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.488 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10065 / 9935 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.257 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.494 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10065 / 9935 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.650 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10065 / 9935 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.144 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.496 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10065 / 9935 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.104 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.503 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10065 / 9935 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=7.gm · 20000 vertices / 212965 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 212965 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.477 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.195 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10057 / 9943 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.246 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.484 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10057 / 9943 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.628 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.485 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10057 / 9943 | 39998 / 49998 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.199 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10057 / 9943 | 39998 / 49998 | 4 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.154 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.495 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.472 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10057 / 9943 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 49993 | 4 / 5 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 49993 | 4 / 5 | 2 / 3 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=8.gm · 20000 vertices / 216324 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 216324 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.198 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.474 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.476 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.197 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.473 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 10059 / 9941 | 50000 / 50000 | 5 / 5 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.341 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.504 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 10059 / 9941 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.639 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.484 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 10059 / 9941 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.258 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.485 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 10059 / 9941 | 49995 / 49995 | 5 / 5 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.217 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.483 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.465 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.196 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 10059 / 9941 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.456 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 49995 / 49995 | 5 / 5 | 4 / 4 | 1.000 / 1.000 | 2 / 2 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 49990 / 49990 | 5 / 5 | 2 / 2 | 1.000 / 1.000 | 4 / 4 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(20000,_1,_20,_1,_20)id=9.gm · 20000 vertices / 265528 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20000 | 265528 | 20000 | 19999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.209 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.218 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.217 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.495 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 9918 / 10082 | 40001 / 40001 | 4 / 4 | 10001 / 10001 | k=2, t=1, depth=10000 / k=2, t=1, depth=10000 | 1.317 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.516 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 9918 / 10082 | 10001 / 10001 | 1 / 1 | 10001 / 10001 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.661 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=10000 / k=1, t=1, depth=10000 | 0.506 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 9918 / 10082 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.193 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.518 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 9918 / 10082 | 39998 / 39998 | 4 / 4 | 10001 / 10001 | bits=1, depth=10000 / bits=1, depth=10000 | 1.124 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=10000 / bits=0, depth=10000 | 0.516 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.206 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.493 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.207 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 9918 / 10082 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 124.797 | even | true | true | false | - |

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
| pm-strahler | 39997 / 39997 | 4 / 4 | 4 / 4 | 1.000 / 1.000 | 1 / 1 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 10000 / 10000 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 10001 / 10001 | 10001.000 / 10001.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 39994 / 39994 | 4 / 4 | 2 / 2 | 1.000 / 1.000 | 3 / 3 | 10001 / 10001 | 10001.000 / 10001.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=0.gm · 5000 vertices / 41501 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 41501 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2508 / 2492 | 10001 / 12500 | 4 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.599 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2508 / 2492 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.444 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2508 / 2492 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.568 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2508 / 2492 | 9998 / 12495 | 4 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.558 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2508 / 2492 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | even | true | true | false | - |

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
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=1.gm · 5000 vertices / 57805 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 57805 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | odd | false | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.147 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | odd | false | true | false | - |
| pm-strahler | complete | 2468 / 2532 | 7501 / 12500 | 3 / 5 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.576 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.412 | 124.797 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2468 / 2532 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.441 | 124.797 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.411 | 124.797 | odd | false | true | false | - |
| pm-succinct | complete | 2468 / 2532 | 7500 / 12495 | 3 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.557 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2468 / 2532 | 7500 / 12495 | 3 / 5 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.547 | 124.797 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | odd | false | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | odd | false | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | false | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2468 / 2532 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 124.797 | odd | false | true | false | - |

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
| pm-strahler | 7498 / 12495 | 3 / 5 | 3 / 4 | 1.000 / 1.000 | 1 / 2 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2500 / 2500 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2501 / 2501 | 2501.000 / 2501.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 7497 / 12490 | 3 / 5 | 2 / 2 | 1.000 / 1.000 | 2 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 7497 / 12490 | 3 / 5 | 2 / 2 | 1.000 / 1.000 | 2 / 4 | 2501 / 2501 | 2501.000 / 2501.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>pgsolver/games/steadygame(5000,_1,_20,_1,_20)id=10.gm · 5000 vertices / 52754 edges · 16 complete · 8 error</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5000 | 52754 | 5000 | 4999 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | error | - / - | - / - | - / - | - / - | - / - | 0.148 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting+iter | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting+pre+iter | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 124.797 | even | true | true | false | - |
| lifting-adaptive+iter | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-adaptive+pre+iter | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| lifting-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.414 | 124.797 | even | true | true | false | - |
| lifting-sym+iter | error | - / - | - / - | - / - | - / - | - / - | 0.144 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| lifting-sym+pre+iter | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 124.797 | even | true | true | false | - |
| pm-strahler | complete | 2442 / 2558 | 10001 / 10001 | 4 / 4 | 2501 / 2501 | k=2, t=1, depth=2500 / k=2, t=1, depth=2500 | 0.569 | 124.797 | even | true | true | false | - |
| pm-strahler+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.423 | 124.797 | even | true | true | false | - |
| pm-strahler+iter | complete | 2442 / 2558 | 2501 / 2501 | 1 / 1 | 2501 / 2501 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.443 | 124.797 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2500 / k=1, t=1, depth=2500 | 0.414 | 124.797 | even | true | true | false | - |
| pm-succinct | complete | 2442 / 2558 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.548 | 124.797 | even | true | true | false | - |
| pm-succinct+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| pm-succinct+iter | complete | 2442 / 2558 | 9998 / 9998 | 4 / 4 | 2501 / 2501 | bits=1, depth=2500 / bits=1, depth=2500 | 0.548 | 124.797 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2500 / bits=0, depth=2500 | 0.413 | 124.797 | even | true | true | false | - |
| zielonka | error | - / - | - / - | - / - | - / - | - / - | 0.146 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 124.797 | even | true | true | false | - |
| zielonka-sym | error | - / - | - / - | - / - | - / - | - / - | 0.145 | 124.797 | - | true | - | - | exit 4: Solver failed: priority depth exceeds the safe recursion depth |
| zielonka-sym+pre | complete | 2442 / 2558 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 124.797 | even | true | true | false | - |

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

