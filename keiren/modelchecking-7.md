# modelchecking, part 7

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_no_generation_of_messages.gm · 3344 vertices / 11922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3344 | 11922 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.421 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.417 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.413 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.414 | 88.344 | even | true | true | false | - |
| zielonka | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 3344 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3344 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 88.344 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_nodeadlock.gm · 1345 vertices / 4865 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1345 | 4865 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.407 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.407 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.415 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.415 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.415 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=10 / H=1, K=1, t=10 | 0.406 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.415 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.436 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.395 | 88.344 | even | true | true | false | - |
| zielonka | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 1345 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1345 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_read_then_eventually_send.gm · 7897 vertices / 26073 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7897 | 26073 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.767 | 88.344 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 6.772 | 88.344 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 88.344 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 88.344 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.686 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.688 | 88.344 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.390 | 88.344 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 7897 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.411 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 88.344 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 7897 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 88.344 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.390 | 88.344 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 7897 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 88.344 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 7897 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.412 | 88.344 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.403 | 88.344 | odd | false | true | false | - |
| zielonka | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.403 | 88.344 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 7897 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 88.344 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 7897 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 88.344 | odd | false | true | false | - |

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
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=1_read_then_eventually_send_if_fair.gm · 2690 vertices / 7322 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2690 | 7322 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.131 | 88.344 | even | true | true | false | - |
| lifting+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 88.344 | even | true | true | false | - |
| lifting+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 3.130 | 88.344 | even | true | true | false | - |
| lifting+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 88.344 | even | true | true | false | - |
| lifting-adaptive | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 88.344 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-sym | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.732 | 88.344 | even | true | true | false | - |
| lifting-sym+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 88.344 | even | true | true | false | - |
| lifting-sym+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 1.754 | 88.344 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 88.344 | even | true | true | false | - |
| pm-strahler | complete | 2690 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.400 | 88.344 | even | true | true | false | - |
| pm-strahler+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.380 | 88.344 | even | true | true | false | - |
| pm-strahler+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.382 | 88.344 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.383 | 88.344 | even | true | true | false | - |
| pm-succinct | complete | 2690 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 88.344 | even | true | true | false | - |
| pm-succinct+iter | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 88.344 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.397 | 88.344 | even | true | true | false | - |
| zielonka | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.397 | 88.344 | even | true | true | false | - |
| zielonka+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 88.344 | even | true | true | false | - |
| zielonka-sym | complete | 2690 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 88.344 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2690 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 88.344 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 2245634 vertices / 6978309 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2245634 | 6978309 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.067 | 782.574 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 782.531 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.068 | 782.719 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 782.715 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 8.488 | 782.578 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 8.489 | 782.715 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 9.099 | 782.656 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 9.150 | 782.578 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.069 | 782.578 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.062 | 782.695 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.063 | 782.590 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 782.445 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 782.652 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 782.508 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 0 / 2245634 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 15.750 | 782.590 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 2245634 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 15.819 | 782.535 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 2245634 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 14.729 | 782.387 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 2245634 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 14.699 | 782.594 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 2245634 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.700 | 782.590 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 2245634 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 7.554 | 782.422 | odd | - | - | false | - |
| zielonka | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.690 | 782.715 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.859 | 782.699 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 4.793 | 782.695 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 2245634 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 4.804 | 782.578 | odd | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_lost.gm · 512018 vertices / 2504114 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 512018 | 2504114 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.145 | 1457.387 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.404 | 222.211 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.143 | 1457.383 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.295 | 221.863 | even | - | - | false | - |
| lifting-adaptive | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 2.735 | 222.078 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.317 | 222.211 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 3.088 | 222.082 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.528 | 222.145 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1459.184 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.207 | 222.098 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.125 | 1462.375 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.420 | 222.211 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 222.086 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 1.476 | 221.961 | even | - | - | false | - |
| pm-strahler+iter | complete | 362945 / 149073 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 4.106 | 222.027 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 1.531 | 222.094 | even | - | - | false | - |
| pm-succinct | complete | 362945 / 149073 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 25.146 | 222.027 | even | - | - | false | - |
| pm-succinct+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.350 | 222.020 | even | - | - | false | - |
| pm-succinct+iter | complete | 362945 / 149073 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 3.507 | 221.953 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 1.385 | 222.074 | even | - | - | false | - |
| zielonka | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 1.405 | 221.914 | even | - | - | false | - |
| zielonka+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.260 | 222.207 | even | - | - | false | - |
| zielonka-sym | complete | 362945 / 149073 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 1.793 | 222.191 | even | - | - | false | - |
| zielonka-sym+pre | complete | 362945 / 149073 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.279 | 222.141 | even | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 5 / 0 | 4 / 0 | 1.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 3 | 3 / 2 | 2 / 2 | 1.667 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_read_write.gm · 353089 vertices / 800769 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 353089 | 800769 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 113.055 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 113.059 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 112.852 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 113.059 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 10.849 | 108.797 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 10.787 | 109.055 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 11.242 | 108.941 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 11.294 | 108.711 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 112.789 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 112.914 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 113.062 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 112.922 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.456 | 109.016 | even | - | - | false | - |
| pm-strahler+pre | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.438 | 109.016 | even | - | - | false | - |
| pm-strahler+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.445 | 108.781 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.493 | 108.891 | even | - | - | false | - |
| pm-succinct | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.326 | 108.742 | even | - | - | false | - |
| pm-succinct+pre | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.380 | 109.016 | even | - | - | false | - |
| pm-succinct+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.602 | 108.945 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 353089 / 0 | 7 / 0 | 6 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 1.651 | 109.016 | even | - | - | false | - |
| zielonka | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.947 | 108.949 | even | - | - | false | - |
| zielonka+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 0.940 | 108.938 | even | - | - | false | - |
| zielonka-sym | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 1.313 | 109.055 | even | - | - | false | - |
| zielonka-sym+pre | complete | 353089 / 0 | 6 / 0 | 5 / 0 | 2 / 0 | — / — | 1.294 | 108.883 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 6 / 0 | 6 / 0 | 6.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 5 / 0 | 5 / 0 | 5.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_receive_d1.gm · 163394 vertices / 611074 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 163394 | 611074 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 89.137 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.643 | 89.137 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 89.137 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.639 | 89.137 | even | true | true | false | - |
| lifting-adaptive | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.994 | 89.137 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.748 | 89.137 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.107 | 89.137 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.757 | 89.137 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 89.137 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.688 | 89.137 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 89.137 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.684 | 89.137 | even | true | true | false | - |
| pm-strahler | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 4.107 | 89.137 | even | true | true | false | - |
| pm-strahler+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.735 | 89.137 | even | true | true | false | - |
| pm-strahler+iter | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.991 | 89.137 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.727 | 89.137 | even | true | true | false | - |
| pm-succinct | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.429 | 89.137 | even | true | true | false | - |
| pm-succinct+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.727 | 89.137 | even | true | true | false | - |
| pm-succinct+iter | complete | 163394 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 2.429 | 89.137 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.726 | 89.137 | even | true | true | false | - |
| zielonka | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.695 | 89.137 | even | true | true | false | - |
| zielonka+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.693 | 89.137 | even | true | true | false | - |
| zielonka-sym | complete | 163394 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.767 | 89.137 | even | true | true | false | - |
| zielonka-sym+pre | complete | 163394 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.695 | 89.137 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_infinitely_often_receive_for_all_d.gm · 653574 vertices / 2444297 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 653574 | 2444297 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 255.418 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.484 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.426 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 255.492 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.673 | 255.422 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.674 | 255.422 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.833 | 255.414 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.833 | 255.422 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 255.430 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 255.422 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 255.414 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 255.422 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 16.203 | 255.406 | even | - | - | false | - |
| pm-strahler+pre | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 15.814 | 255.402 | even | - | - | false | - |
| pm-strahler+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 10.214 | 255.371 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 9.857 | 255.496 | even | - | - | false | - |
| pm-succinct | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.093 | 255.223 | even | - | - | false | - |
| pm-succinct+pre | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 8.138 | 255.355 | even | - | - | false | - |
| pm-succinct+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.737 | 255.355 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 653574 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.801 | 255.500 | even | - | - | false | - |
| zielonka | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.385 | 255.344 | even | - | - | false | - |
| zielonka+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.441 | 255.531 | even | - | - | false | - |
| zielonka-sym | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.652 | 255.430 | even | - | - | false | - |
| zielonka-sym+pre | complete | 653574 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.623 | 255.551 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_invariantly_infinitely_many_reachable_taus.gm · 421057 vertices / 1456769 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 421057 | 1456769 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 154.871 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 154.969 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 155.105 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 154.840 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.468 | 155.055 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.478 | 155.105 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.502 | 154.969 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.563 | 154.828 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 155.105 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 154.961 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 155.160 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 155.031 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.062 | 154.926 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 2.259 | 154.922 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 421057 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.422 | 154.980 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 421057 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.427 | 154.918 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 2.905 | 154.984 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 421057 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 2.959 | 154.922 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 421057 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.792 | 154.965 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 421057 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.803 | 155.047 | odd | false | true | false | - |
| zielonka | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.128 | 154.965 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.213 | 155.035 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.333 | 154.980 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 421057 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.336 | 154.961 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_no_duplication_of_messages.gm · 858114 vertices / 3433490 edges · 19 complete · 5 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 858114 | 3433490 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 340.547 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.694 | 340.656 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 340.547 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.695 | 340.648 | odd | - | - | false | - |
| lifting-adaptive | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.602 | 340.551 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.859 | 340.539 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.835 | 340.547 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.848 | 340.488 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 340.680 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.775 | 340.547 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 340.555 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.754 | 340.547 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 340.559 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.906 | 340.543 | odd | - | - | false | - |
| pm-strahler+iter | complete | 494528 / 363586 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.315 | 340.480 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.892 | 340.555 | odd | - | - | false | - |
| pm-succinct | complete | 494528 / 363586 | 2 / 43 | 1 / 21 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 26.934 | 340.496 | odd | - | - | false | - |
| pm-succinct+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.755 | 340.539 | odd | - | - | false | - |
| pm-succinct+iter | complete | 494528 / 363586 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.365 | 340.543 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.784 | 340.539 | odd | - | - | false | - |
| zielonka | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.706 | 340.555 | odd | - | - | false | - |
| zielonka+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.612 | 340.680 | odd | - | - | false | - |
| zielonka-sym | complete | 494528 / 363586 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.203 | 340.676 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 494528 / 363586 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.601 | 340.680 | odd | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 22 | 1 / 21 | 1 / 21 | 1.000 / 1.909 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_no_generation_of_messages.gm · 211955 vertices / 876954 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 211955 | 876954 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.811 | 89.574 | even | true | true | false | - |
| lifting+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.696 | 89.574 | even | true | true | false | - |
| lifting+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.828 | 89.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| lifting-adaptive | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.793 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.672 | 89.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.795 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.671 | 89.574 | even | true | true | false | - |
| lifting-sym | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.774 | 89.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.793 | 89.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.670 | 89.574 | even | true | true | false | - |
| pm-strahler | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.837 | 89.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.714 | 89.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.797 | 89.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.724 | 89.574 | even | true | true | false | - |
| pm-succinct | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.971 | 89.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.711 | 89.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.797 | 89.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.717 | 89.574 | even | true | true | false | - |
| zielonka | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.686 | 89.574 | even | true | true | false | - |
| zielonka+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.673 | 89.574 | even | true | true | false | - |
| zielonka-sym | complete | 211955 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.746 | 89.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 211955 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.683 | 89.574 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_nodeadlock.gm · 140353 vertices / 588033 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 140353 | 588033 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.663 | 89.574 | even | true | true | false | - |
| lifting+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.589 | 89.574 | even | true | true | false | - |
| lifting+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.672 | 89.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 89.574 | even | true | true | false | - |
| lifting-adaptive | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.661 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.577 | 89.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.662 | 89.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.579 | 89.574 | even | true | true | false | - |
| lifting-sym | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.649 | 89.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.580 | 89.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.665 | 89.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.621 | 89.574 | even | true | true | false | - |
| pm-strahler | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.683 | 89.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.609 | 89.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.651 | 89.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.609 | 89.574 | even | true | true | false | - |
| pm-succinct | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.774 | 89.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.600 | 89.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.651 | 89.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.600 | 89.574 | even | true | true | false | - |
| zielonka | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.589 | 89.574 | even | true | true | false | - |
| zielonka+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.578 | 89.574 | even | true | true | false | - |
| zielonka-sym | complete | 140353 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.607 | 89.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 140353 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.566 | 89.574 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_read_then_eventually_send.gm · 869569 vertices / 3200129 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 869569 | 3200129 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 333.828 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.746 | 333.699 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 333.832 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.725 | 333.762 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.980 | 333.812 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.891 | 333.766 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.156 | 333.832 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.865 | 333.836 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 333.707 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.819 | 333.773 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 333.766 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.786 | 333.559 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 869569 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 5.704 | 333.777 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.120 | 333.777 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 869569 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.516 | 333.578 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.043 | 333.711 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 869569 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 5.463 | 333.648 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.054 | 333.777 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 869569 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.686 | 333.777 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.000 | 333.645 | odd | - | - | false | - |
| zielonka | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.886 | 333.582 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.779 | 333.766 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 869569 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.219 | 333.793 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 869569 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.747 | 333.836 | odd | - | - | false | - |

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
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=2_read_then_eventually_send_if_fair.gm · 388418 vertices / 1125698 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 388418 | 1125698 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 129.062 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.882 | 129.062 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 128.922 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.866 | 128.879 | even | - | - | false | - |
| lifting-adaptive | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.746 | 129.062 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.998 | 129.062 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.841 | 129.047 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.987 | 128.941 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 129.043 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.934 | 128.938 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 128.926 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.919 | 129.062 | even | - | - | false | - |
| pm-strahler | complete | 388418 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 12.227 | 129.012 | even | - | - | false | - |
| pm-strahler+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.023 | 128.734 | even | - | - | false | - |
| pm-strahler+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.275 | 128.871 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.012 | 129.008 | even | - | - | false | - |
| pm-succinct | complete | 388418 / 0 | 10 / 0 | 9 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 4.581 | 129.008 | even | - | - | false | - |
| pm-succinct+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.016 | 128.738 | even | - | - | false | - |
| pm-succinct+iter | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 1.437 | 128.945 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.033 | 128.879 | even | - | - | false | - |
| zielonka | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.952 | 128.992 | even | - | - | false | - |
| zielonka+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.910 | 128.992 | even | - | - | false | - |
| zielonka-sym | complete | 388418 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.195 | 128.938 | even | - | - | false | - |
| zielonka-sym+pre | complete | 388418 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.947 | 128.996 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 9 / 0 | 9 / 0 | 9.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_enabled_then_infinitely_often_taken.gm · 147458 vertices / 406665 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 147458 | 406665 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.837 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.847 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.857 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.868 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | false | - | - | deadline exceeded |
| pm-strahler | complete | 0 / 147458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.470 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 147458 | 0 / 23 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.732 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 147458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.353 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 147458 | 0 / 11 | 0 / 6 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 1.352 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 147458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.333 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 147458 | 0 / 19 | 0 / 13 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 1.334 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 147458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.885 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 147458 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.897 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.675 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.676 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.749 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 147458 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.740 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 9 | 0 / 14 | 0 / 8 | 0.000 / 2.444 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 5 | 0 / 6 | 0 / 4 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+pre | 0 / 6 | 0 / 13 | 0 / 7 | 0.000 / 3.000 | 0 / 3 | 0 / 3 | 0.000 / 3.000 | 0 / 3 |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_lost.gm · 12818 vertices / 49890 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 12818 | 49890 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.444 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.464 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 9393 / 3425 | 26 / 5 | 13 / 2 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 1.229 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.412 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 9393 / 3425 | 10 / 0 | 5 / 0 | 3 / 0 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.463 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.423 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 9393 / 3425 | 26 / 5 | 13 / 2 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.711 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.435 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 9393 / 3425 | 6 / 5 | 3 / 2 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.474 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.444 | 90.051 | even | true | true | false | - |
| zielonka | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.454 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 9393 / 3425 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.455 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9393 / 3425 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | even | true | true | false | - |

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
| pm-strahler | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 5 / 0 | 5 / 0 | 4 / 0 | 1.800 / 0.000 | 2 / 0 | 3 / 0 | 3.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 3 | 13 / 2 | 12 / 2 | 1.923 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 3 / 3 | 3 / 2 | 2 / 2 | 1.667 / 1.333 | 2 / 1 | 3 / 3 | 3.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_read_write.gm · 10369 vertices / 22849 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10369 | 22849 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.454 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.464 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.452 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.473 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.475 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.473 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.422 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.421 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.433 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 10369 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| zielonka | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.390 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.391 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.411 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 10369 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 4 / 0 | 4 / 0 | 4.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_receive_d1.gm · 4898 vertices / 17378 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4898 | 17378 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.667 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=12 / H=2, K=2, t=12 | 0.666 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.430 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.369 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.420 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 4898 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.370 | 90.051 | even | true | true | false | - |
| zielonka | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 4898 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4898 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_infinitely_often_receive_for_all_d.gm · 39178 vertices / 139025 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 39178 | 139025 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.506 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.506 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.514 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.504 | 90.051 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=15 / H=2, K=2, t=15 | 29.933 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.104 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.221 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.006 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 1.018 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.936 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.906 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.854 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 39178 / 0 | 12 / 0 | 11 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.874 | 90.051 | even | true | true | false | - |
| zielonka | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.531 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.530 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.550 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 39178 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.550 | 90.051 | even | true | true | false | - |

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
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 11 / 0 | 11 / 0 | 11.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_invariantly_infinitely_many_reachable_taus.gm · 13825 vertices / 43393 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13825 | 43393 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.040 | 90.051 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.083 | 90.051 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 21.009 | 90.051 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.956 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 90.051 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.597 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.578 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.567 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.433 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.433 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 13825 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.412 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 13825 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.414 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.445 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 13825 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.443 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 13825 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.427 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 13825 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.425 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.414 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 13825 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.413 | 90.051 | odd | false | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_no_duplication_of_messages.gm · 41762 vertices / 154498 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 41762 | 154498 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.579 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.643 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.541 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.487 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.498 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 36624 / 5138 | 2 / 39 | 1 / 19 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 2.184 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.495 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 36624 / 5138 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.508 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.487 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 36624 / 5138 | 2 / 39 | 1 / 19 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 1.642 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.478 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 36624 / 5138 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.497 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.509 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.496 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 36624 / 5138 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.517 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 36624 / 5138 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.485 | 90.051 | odd | false | true | false | - |

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
| pm-strahler | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 20 | 1 / 19 | 1 / 19 | 1.000 / 1.900 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_no_generation_of_messages.gm · 28964 vertices / 106938 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 28964 | 106938 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.447 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.446 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.448 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.443 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.444 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.423 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=14 / H=1, K=1, t=14 | 0.443 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.424 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.444 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.433 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.443 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.434 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.454 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.434 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.444 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.433 | 90.051 | even | true | true | false | - |
| zielonka | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.423 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.434 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 28964 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.432 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 28964 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_nodeadlock.gm · 4609 vertices / 17089 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4609 | 17089 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.409 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.418 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.413 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.414 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=12 / H=1, K=1, t=12 | 0.416 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 90.051 | even | true | true | false | - |
| zielonka | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.417 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.417 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 4609 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 4609 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 90.051 | even | true | true | false | - |

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
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_read_then_eventually_send.gm · 45937 vertices / 160561 edges · 21 complete · 3 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 45937 | 160561 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.445 | 90.051 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.443 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.527 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.518 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.601 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.550 | 90.051 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 90.051 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.509 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=15 / H=2, K=2, t=15 | 21.321 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 45937 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.641 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.548 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 45937 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.571 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.528 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 45937 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.621 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.506 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 45937 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.526 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.508 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.506 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 45937 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.516 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 45937 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.506 | 90.051 | odd | false | true | false | - |

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
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 13 | 0 / 12 | 0 / 12 | 0.000 / 1.846 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=8_windowsize=1_read_then_eventually_send_if_fair.gm · 9986 vertices / 26994 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9986 | 26994 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 90.051 | even | true | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 90.051 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.411 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.520 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=13 / H=2, K=2, t=13 | 20.481 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 9986 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.485 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.411 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.400 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 9986 / 0 | 8 / 0 | 7 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 0.431 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.402 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 90.051 | even | true | true | false | - |
| zielonka | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 9986 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 9986 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | even | true | true | false | - |

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
| lifting-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Snakewidth=4_height=4_black_has_winning_strategy.gm · 4860 vertices / 6922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4860 | 6922 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.147 | 90.051 | odd | false | true | false | - |
| lifting+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 90.051 | odd | false | true | false | - |
| lifting+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.156 | 90.051 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-adaptive | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.380 | 90.051 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | odd | false | true | false | - |
| lifting-sym | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 2.356 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.379 | 90.051 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 2.407 | 90.051 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | odd | false | true | false | - |
| pm-strahler | complete | 1886 / 2974 | 12 / 2 | 11 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.403 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.379 | 90.051 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1886 / 2974 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.380 | 90.051 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct | complete | 1886 / 2974 | 12 / 2 | 11 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.391 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1886 / 2974 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.381 | 90.051 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.382 | 90.051 | odd | false | true | false | - |
| zielonka | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 90.051 | odd | false | true | false | - |
| zielonka+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | odd | false | true | false | - |
| zielonka-sym | complete | 1886 / 2974 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.401 | 90.051 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1886 / 2974 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 90.051 | odd | false | true | false | - |

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
<summary>modelchecking/games/Snakewidth=4_height=4_white_has_winning_strategy.gm · 4860 vertices / 6922 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 4860 | 6922 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.463 | 90.051 | even | true | true | false | - |
| lifting+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 90.051 | even | true | true | false | - |
| lifting+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 5.453 | 90.051 | even | true | true | false | - |
| lifting+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 90.051 | even | true | true | false | - |
| lifting-adaptive | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.379 | 90.051 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.369 | 90.051 | even | true | true | false | - |
| lifting-sym | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 1.674 | 90.051 | even | true | true | false | - |
| lifting-sym+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 90.051 | even | true | true | false | - |
| lifting-sym+iter | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 1.712 | 90.051 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 90.051 | even | true | true | false | - |
| pm-strahler | complete | 2975 / 1885 | 14 / 2 | 13 / 1 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-strahler+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-strahler+iter | complete | 2975 / 1885 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.401 | 90.051 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-succinct | complete | 2975 / 1885 | 14 / 2 | 13 / 1 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.413 | 90.051 | even | true | true | false | - |
| pm-succinct+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.403 | 90.051 | even | true | true | false | - |
| pm-succinct+iter | complete | 2975 / 1885 | 4 / 2 | 3 / 1 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.401 | 90.051 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 0.402 | 90.051 | even | true | true | false | - |
| zielonka | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 90.051 | even | true | true | false | - |
| zielonka-sym | complete | 2975 / 1885 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 90.051 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2975 / 1885 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 90.051 | even | true | true | false | - |

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
| pm-strahler | 1 / 1 | 13 / 1 | 13 / 1 | 13.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 1 | 13 / 1 | 13 / 1 | 13.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 1 | 3 / 1 | 3 / 1 | 3.000 / 1.000 | 1 / 0 | 2 / 2 | 2.000 / 2.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hesselinkdatasize=3_nodeadlock.gm · 13834801 vertices / 29028241 edges · 9 complete · 7 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 13834801 | 29028241 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 13834801 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=23 / H=1, K=1, t=23 | 17.729 | 1657.484 | even | - | - | false | - |
| lifting+pre | complete | 13834801 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 13.922 | 1607.340 | even | - | - | false | - |
| lifting+iter | complete | 13834801 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=23 / H=1, K=1, t=23 | 18.264 | 1597.227 | even | - | - | false | - |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.083 | 816.234 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.252 | 914.461 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.303 | 933.859 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 13834801 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 24.729 | 1700.965 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 13834801 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 8.377 | 1700.965 | even | - | - | false | - |
| lifting-sym | complete | 13834801 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=23 / H=1, K=1, t=23 | 27.578 | 1936.305 | even | - | - | false | - |
| lifting-sym+pre | complete | 13834801 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 12.355 | 1700.980 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.146 | 1938.012 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 13834801 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 23.109 | 1700.715 | even | - | - | false | - |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 14.346 | 1700.680 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 27.501 | 1700.789 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 26.066 | 1696.672 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 19.196 | 1684.422 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 21.303 | 1700.738 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 21.257 | 1700.848 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 21.256 | 1700.789 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 23.512 | 1700.672 | - | - | - | - | Failed to allocate memory |
| zielonka | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 1700.781 | - | - | - | - | metrics: deadline exceeded |
| zielonka+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 1700.777 | - | - | - | - | metrics: deadline exceeded |
| zielonka-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.151 | 1825.617 | - | - | - | - | deadline exceeded |
| zielonka-sym+pre | complete | 13834801 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 21.632 | 1700.789 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Hesselinkdatasize=3_property2.gm · 27876961 vertices / 58309201 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 27876961 | 58309201 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.439 | 1294.543 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.448 | 1294.348 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.438 | 1294.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.119 | 1294.422 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 14.088 | 1294.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.078 | 1294.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.451 | 1294.297 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.543 | 1294.293 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.492 | 1294.297 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.344 | 1294.594 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.198 | 1294.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.177 | 1294.480 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.576 | 1294.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.586 | 1294.281 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.498 | 1294.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.540 | 1294.484 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 5.625 | 1294.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.525 | 1294.473 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.572 | 1294.430 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.580 | 1294.430 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.482 | 1294.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.411 | 1294.590 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.431 | 1294.609 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.463 | 1294.477 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 20712450 vertices / 70290691 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 20712450 | 70290691 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 6.889 | 1380.453 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.940 | 1380.508 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.940 | 1380.770 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.166 | 1380.637 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 8.446 | 1380.387 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.114 | 1380.641 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.667 | 1380.379 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.421 | 1380.652 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.325 | 1380.512 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.173 | 1380.633 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.927 | 1380.641 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.916 | 1380.512 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 6.800 | 1380.688 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.790 | 1380.324 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.780 | 1380.445 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.350 | 1380.551 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 7.352 | 1380.652 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.339 | 1380.281 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.903 | 1380.367 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.882 | 1380.430 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 6.879 | 1380.523 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.935 | 1380.523 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.914 | 1380.551 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.918 | 1380.508 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_lost.gm · 8964338 vertices / 51952370 edges · 10 complete · 2 timeout · 12 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8964338 | 51952370 | 3 | 3 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 9.233 | 1576.223 | - | - | - | - | Failed to allocate memory |
| lifting+pre | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 11.237 | 1529.051 | even | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.264 | 1577.504 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 17.327 | 1528.875 | even | - | - | false | - |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.115 | 1710.102 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 15.322 | 1528.809 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.122 | 1711.027 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 23.209 | 1528.969 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.812 | 1576.398 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 16.017 | 1528.703 | even | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.920 | 1577.512 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 10.515 | 1528.750 | even | - | - | false | - |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 10.767 | 1355.473 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.872 | 1529.121 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.688 | 1355.695 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.656 | 1529.000 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 8.321 | 1355.488 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.430 | 1528.984 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.814 | 1355.629 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 12.109 | 1528.875 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 6449793 / 2514545 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 13.868 | 1355.695 | even | - | - | false | - |
| zielonka+pre | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 10.382 | 1529.000 | even | - | - | false | - |
| zielonka-sym | complete | 6449793 / 2514545 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 21.419 | 1779.891 | even | - | - | false | - |
| zielonka-sym+pre | complete | 6449793 / 2514545 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 10.260 | 1529.039 | even | - | - | false | - |

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
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_infinitely_often_receive_for_all_d.gm · 6974724 vertices / 24927749 edges · 6 complete · 18 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6974724 | 24927749 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 36.238 | 1674.516 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 35.976 | 1674.914 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 36.237 | 1675.824 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.159 | 1675.734 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.085 | 1079.379 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.086 | 1079.469 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 22.318 | 1080.211 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 22.495 | 1080.305 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.145 | 1677.684 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.430 | 1674.988 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.214 | 1675.762 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.204 | 1678.496 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.141 | 1612.969 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.138 | 1612.891 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.112 | 1616.422 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.147 | 1616.523 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.116 | 1546.414 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.117 | 1546.301 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.133 | 1548.648 | - | - | - | - | deadline exceeded |
| pm-succinct+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.134 | 1548.516 | - | - | - | - | deadline exceeded |
| zielonka | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 6.618 | 936.961 | even | - | - | false | - |
| zielonka+pre | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.102 | 936.945 | even | - | - | false | - |
| zielonka-sym | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 9.715 | 1133.289 | even | - | - | false | - |
| zielonka-sym+pre | complete | 6974724 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 9.475 | 1133.426 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
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
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_invariantly_infinitely_many_reachable_taus.gm · 7767169 vertices / 28309249 edges · 10 complete · 6 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7767169 | 28309249 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 13.767 | 1704.090 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 14.606 | 1709.875 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.606 | 1711.168 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 28.355 | 1759.320 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.101 | 1150.863 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.101 | 1150.922 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 18.839 | 1192.293 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 19.213 | 1192.418 | odd | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.617 | 1758.508 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.672 | 1758.523 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.188 | 1759.566 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.568 | 1759.566 | - | - | - | - | Failed to allocate memory |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.146 | 1784.094 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.188 | 1784.125 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 0 / 7767169 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 17.450 | 1724.168 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 7767169 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 14.342 | 1724.180 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.150 | 1722.582 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.155 | 1721.781 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 0 / 7767169 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 29.775 | 1724.078 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 7767169 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 28.754 | 1724.426 | odd | - | - | false | - |
| zielonka | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 10.073 | 1047.609 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 7.781 | 1047.609 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 11.183 | 1315.027 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 7767169 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 11.382 | 1314.992 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_no_duplication_of_messages.gm · 11488274 vertices / 45840722 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11488274 | 45840722 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.404 | 1052.789 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.404 | 1052.730 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.444 | 1052.793 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.474 | 1052.777 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 4.370 | 1052.789 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.445 | 1052.789 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.358 | 1052.793 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.387 | 1052.781 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.398 | 1052.898 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.372 | 1052.906 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.443 | 1052.859 | - | - | - | - | 1:1: failed to allocate the graph edges |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.380 | 1052.855 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.602 | 1052.668 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.438 | 1052.801 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.408 | 1052.797 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.430 | 1052.656 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.430 | 1052.738 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.442 | 1052.668 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.428 | 1052.863 | - | - | - | - | 1:1: failed to allocate the graph edges |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.365 | 1052.781 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.447 | 1052.918 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.450 | 1052.922 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.418 | 1052.902 | - | - | - | - | 1:1: failed to allocate the graph edges |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.387 | 1052.902 | - | - | - | - | 1:1: failed to allocate the graph edges |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_read_then_eventually_send.gm · 10782593 vertices / 39508737 edges · 3 complete · 1 timeout · 20 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 10782593 | 39508737 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.690 | 1470.109 | - | - | - | - | Failed to allocate memory |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.853 | 1449.520 | - | - | - | - | Failed to allocate memory |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.659 | 1471.375 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 11.568 | 1454.898 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive | complete | 0 / 10782593 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 29.964 | 1687.266 | odd | - | - | false | - |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 10.690 | 1454.848 | - | - | - | - | Failed to allocate memory |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.102 | 1688.719 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 10.977 | 1454.887 | - | - | - | - | Failed to allocate memory |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.555 | 1470.074 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.234 | 1454.914 | - | - | - | - | Failed to allocate memory |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.913 | 1471.227 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.851 | 1455.020 | - | - | - | - | Failed to allocate memory |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 7.188 | 1455.086 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.864 | 1454.953 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.928 | 1454.887 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.927 | 1455.086 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.977 | 1455.086 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.896 | 1454.961 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.160 | 1454.961 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.905 | 1454.984 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 0 / 10782593 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 10.253 | 1455.012 | odd | - | - | false | - |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.209 | 1455.121 | - | - | - | - | Failed to allocate memory |
| zielonka-sym | complete | 0 / 10782593 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 19.680 | 1686.359 | odd | - | - | false | - |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.658 | 1455.121 | - | - | - | - | Failed to allocate memory |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
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
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=2_windowsize=4_read_then_eventually_send_if_fair.gm · 7310722 vertices / 22667778 edges · 17 complete · 7 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7310722 | 22667778 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.166 | 1658.617 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.861 | 955.719 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.167 | 1659.266 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.988 | 955.594 | even | - | - | false | - |
| lifting-adaptive | complete | 7310722 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 29.453 | 1097.328 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 7.423 | 955.426 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.070 | 1098.086 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.464 | 955.602 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.176 | 1658.605 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.617 | 955.734 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.169 | 1659.473 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.064 | 955.715 | even | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.160 | 1612.047 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 8.616 | 1472.047 | even | - | - | false | - |
| pm-strahler+iter | complete | 7310722 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 16.170 | 1529.637 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 8.089 | 1474.320 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.168 | 1613.566 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 8.003 | 1472.090 | even | - | - | false | - |
| pm-succinct+iter | complete | 7310722 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 17.611 | 1531.242 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 8.356 | 1474.438 | even | - | - | false | - |
| zielonka | complete | 7310722 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 6.254 | 955.461 | even | - | - | false | - |
| zielonka+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.457 | 955.461 | even | - | - | false | - |
| zielonka-sym | complete | 7310722 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 10.806 | 1161.641 | even | - | - | false | - |
| zielonka-sym+pre | complete | 7310722 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.476 | 955.664 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_infinitely_often_read_write.gm · 19550209 vertices / 45106177 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 19550209 | 45106177 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 4.443 | 1279.340 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.338 | 1279.336 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.401 | 1279.195 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.333 | 1279.336 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 4.372 | 1279.277 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.393 | 1279.215 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.290 | 1279.211 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.394 | 1279.062 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.331 | 1279.062 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.308 | 1279.320 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.360 | 1279.207 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.360 | 1279.266 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 4.380 | 1279.082 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.349 | 1279.148 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.349 | 1279.199 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.315 | 1279.215 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 4.295 | 1279.074 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.397 | 1279.020 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.302 | 1279.215 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.281 | 1279.219 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 4.292 | 1279.195 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.303 | 1279.336 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 4.269 | 1279.270 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.259 | 1279.340 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_infinitely_often_receive_d1.gm · 8835074 vertices / 34391042 edges · 11 complete · 1 timeout · 12 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8835074 | 34391042 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 7.795 | 1501.676 | - | - | - | - | Failed to allocate memory |
| lifting+pre | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.494 | 1305.137 | even | - | - | false | - |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.862 | 1502.559 | - | - | - | - | Failed to allocate memory |
| lifting+pre+iter | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.604 | 1305.254 | even | - | - | false | - |
| lifting-adaptive | complete | 8835074 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 29.940 | 1409.723 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.187 | 1305.234 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.091 | 1410.836 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.419 | 1305.094 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 7.464 | 1501.492 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.498 | 1305.059 | even | - | - | false | - |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.424 | 1502.734 | - | - | - | - | Failed to allocate memory |
| lifting-sym+pre+iter | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.119 | 1305.188 | even | - | - | false | - |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 13.694 | 1710.871 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.752 | 1673.125 | - | - | - | - | Failed to allocate memory |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.195 | 1710.680 | - | - | - | - | Failed to allocate memory |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 14.226 | 1673.059 | - | - | - | - | Failed to allocate memory |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 23.920 | 1709.766 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 13.934 | 1671.805 | - | - | - | - | Failed to allocate memory |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 24.603 | 1710.629 | - | - | - | - | Failed to allocate memory |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 15.864 | 1673.043 | - | - | - | - | Failed to allocate memory |
| zielonka | complete | 8835074 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 8.694 | 1208.027 | even | - | - | false | - |
| zielonka+pre | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.024 | 1305.133 | even | - | - | false | - |
| zielonka-sym | complete | 8835074 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 13.013 | 1477.934 | even | - | - | false | - |
| zielonka-sym+pre | complete | 8835074 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 9.012 | 1305.258 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_invariantly_infinitely_many_reachable_taus.gm · 22288897 vertices / 80830465 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 22288897 | 80830465 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 8.046 | 1457.770 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.056 | 1457.703 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.054 | 1458.027 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.910 | 1457.863 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 8.913 | 1457.910 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.892 | 1457.801 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.138 | 1457.773 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.243 | 1457.973 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 9.157 | 1457.898 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.662 | 1457.773 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.590 | 1458.023 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.518 | 1457.770 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 8.733 | 1457.773 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.795 | 1457.781 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.723 | 1457.777 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.584 | 1457.570 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 6.572 | 1457.652 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.531 | 1457.742 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.105 | 1457.902 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.727 | 1457.766 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 6.724 | 1457.836 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.804 | 1458.141 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 5.846 | 1457.992 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.688 | 1458.047 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

<details>
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_no_generation_of_messages.gm · 6690605 vertices / 29413398 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6690605 | 29413398 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 10.215 | 967.930 | even | - | - | false | - |
| lifting+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.301 | 940.699 | even | - | - | false | - |
| lifting+iter | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 10.549 | 968.715 | even | - | - | false | - |
| lifting+pre+iter | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.058 | 940.699 | even | - | - | false | - |
| lifting-adaptive | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 10.381 | 967.934 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.370 | 940.844 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 10.564 | 968.758 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.063 | 940.781 | even | - | - | false | - |
| lifting-sym | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 9.608 | 1221.336 | even | - | - | false | - |
| lifting-sym+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.243 | 940.844 | even | - | - | false | - |
| lifting-sym+iter | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 9.937 | 1222.086 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.932 | 940.973 | even | - | - | false | - |
| pm-strahler | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 12.390 | 1578.086 | even | - | - | false | - |
| pm-strahler+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 7.640 | 1545.703 | even | - | - | false | - |
| pm-strahler+iter | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 10.426 | 1547.559 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 7.355 | 1547.891 | even | - | - | false | - |
| pm-succinct | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 17.382 | 1578.184 | even | - | - | false | - |
| pm-succinct+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 7.354 | 1545.828 | even | - | - | false | - |
| pm-succinct+iter | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 11.037 | 1547.695 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 7.223 | 1547.961 | even | - | - | false | - |
| zielonka | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 5.560 | 940.973 | even | - | - | false | - |
| zielonka+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.997 | 940.969 | even | - | - | false | - |
| zielonka-sym | complete | 6690605 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 7.610 | 1169.883 | even | - | - | false | - |
| zielonka-sym+pre | complete | 6690605 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 4.916 | 940.785 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_nodeadlock.gm · 7429633 vertices / 32985601 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 7429633 | 32985601 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 11.228 | 1079.508 | even | - | - | false | - |
| lifting+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.884 | 1047.102 | even | - | - | false | - |
| lifting+iter | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 11.679 | 1080.516 | even | - | - | false | - |
| lifting+pre+iter | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.520 | 1046.891 | even | - | - | false | - |
| lifting-adaptive | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 11.190 | 1079.602 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.851 | 1047.148 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 11.515 | 1080.512 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.512 | 1047.031 | even | - | - | false | - |
| lifting-sym | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 10.592 | 1360.820 | even | - | - | false | - |
| lifting-sym+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.767 | 1047.145 | even | - | - | false | - |
| lifting-sym+iter | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=22 / H=1, K=1, t=22 | 10.916 | 1361.703 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.464 | 1047.145 | even | - | - | false | - |
| pm-strahler | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 13.103 | 1759.688 | even | - | - | false | - |
| pm-strahler+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 9.381 | 1723.809 | even | - | - | false | - |
| pm-strahler+iter | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 11.505 | 1726.078 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 8.282 | 1725.969 | even | - | - | false | - |
| pm-succinct | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 25.105 | 1759.488 | even | - | - | false | - |
| pm-succinct+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 8.309 | 1723.750 | even | - | - | false | - |
| pm-succinct+iter | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 19.059 | 1697.684 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 16.295 | 1726.008 | even | - | - | false | - |
| zielonka | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 6.654 | 1047.035 | even | - | - | false | - |
| zielonka+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 6.167 | 1047.035 | even | - | - | false | - |
| zielonka-sym | complete | 7429633 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 9.123 | 1303.723 | even | - | - | false | - |
| zielonka-sym+pre | complete | 7429633 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 5.341 | 1047.098 | even | - | - | false | - |

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
<summary>modelchecking/games/SWPdatasize=4_windowsize=3_read_then_eventually_send_if_fair.gm · 24565250 vertices / 73675010 edges · 24 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 24565250 | 73675010 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 5.680 | 1438.098 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 5.680 | 1438.047 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 5.680 | 1438.160 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 9.177 | 1437.977 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive | out of memory | - / - | - / - | - / - | - / - | - / - | 9.156 | 1437.984 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 9.166 | 1438.094 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.912 | 1438.109 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-adaptive+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.922 | 1438.090 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 8.943 | 1437.859 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.273 | 1437.984 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.242 | 1437.973 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 6.211 | 1438.090 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler | out of memory | - / - | - / - | - / - | - / - | - / - | 7.547 | 1437.855 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 7.588 | 1437.914 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 7.557 | 1437.988 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-strahler+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.726 | 1437.973 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct | out of memory | - / - | - / - | - / - | - / - | - / - | 8.734 | 1438.105 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 8.714 | 1437.922 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.724 | 1437.992 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| pm-succinct+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 8.727 | 1438.055 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka | out of memory | - / - | - / - | - / - | - / - | - / - | 8.616 | 1437.848 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.949 | 1438.234 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 6.879 | 1437.844 | - | - | - | - | 16777216:1: failed to allocate the declaration list |
| zielonka-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 6.848 | 1438.164 | - | - | - | - | 16777216:1: failed to allocate the declaration list |

</details>

