# modelchecking, part 5

[Definitions and summary](../KEIREN.md).

## Winner checks

No disagreements in winner counts or start winners, and no recorded reference mismatches.

## Inventory

<details>
<summary>modelchecking/games/Onebitdatasize=2_messages_read_are_inevitably_sent.gm · 153985 vertices / 870977 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 153985 | 870977 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 81.496 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.662 | 81.496 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 81.496 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.660 | 81.496 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 153985 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.006 | 81.496 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.766 | 81.496 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 153985 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.088 | 81.496 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.767 | 81.496 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 81.496 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.706 | 81.496 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 81.496 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.714 | 81.496 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 153985 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 2.478 | 81.496 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.800 | 81.496 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 153985 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.880 | 81.496 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.763 | 81.496 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 153985 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 2.307 | 81.496 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.759 | 81.496 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 153985 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.996 | 81.496 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.772 | 81.496 | odd | false | true | false | - |
| zielonka | complete | 0 / 153985 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.765 | 81.496 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.735 | 81.496 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 153985 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.841 | 81.496 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 153985 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.714 | 81.496 | odd | false | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=2_no_duplication_of_messages.gm · 258050 vertices / 1456802 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 258050 | 1456802 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 124.184 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.880 | 124.055 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 124.109 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.876 | 124.188 | odd | false | true | false | - |
| lifting-adaptive | complete | 153472 / 104578 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.870 | 124.125 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.975 | 124.125 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 153472 / 104578 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.965 | 124.254 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.987 | 124.121 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 124.113 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.922 | 124.250 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 124.254 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.930 | 124.250 | odd | false | true | false | - |
| pm-strahler | complete | 153472 / 104578 | 2 / 43 | 1 / 21 | 2 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 23.756 | 124.113 | odd | false | true | false | - |
| pm-strahler+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.973 | 124.195 | odd | false | true | false | - |
| pm-strahler+iter | complete | 153472 / 104578 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.119 | 124.199 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.962 | 124.125 | odd | false | true | false | - |
| pm-succinct | complete | 153472 / 104578 | 2 / 43 | 1 / 21 | 2 / 3 | bits=4, depth=1 / bits=4, depth=2 | 17.637 | 124.113 | odd | false | true | false | - |
| pm-succinct+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.953 | 124.133 | odd | false | true | false | - |
| pm-succinct+iter | complete | 153472 / 104578 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.258 | 124.082 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.975 | 124.113 | odd | false | true | false | - |
| zielonka | complete | 153472 / 104578 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 0.963 | 124.254 | odd | false | true | false | - |
| zielonka+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.910 | 124.109 | odd | false | true | false | - |
| zielonka-sym | complete | 153472 / 104578 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 1.087 | 124.250 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 153472 / 104578 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.835 | 124.125 | odd | false | true | false | - |

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
| pm-strahler | 1 / 22 | 1 / 21 | 1 / 21 | 1.000 / 1.909 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
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
<summary>modelchecking/games/Onebitdatasize=2_no_generation_of_messages.gm · 65506 vertices / 365971 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 65506 | 365971 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.540 | 81.496 | even | true | true | false | - |
| lifting+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.508 | 81.496 | even | true | true | false | - |
| lifting+iter | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.549 | 81.496 | even | true | true | false | - |
| lifting+pre+iter | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 81.496 | even | true | true | false | - |
| lifting-adaptive | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.536 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 81.496 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.537 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.494 | 81.496 | even | true | true | false | - |
| lifting-sym | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.527 | 81.496 | even | true | true | false | - |
| lifting-sym+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.496 | 81.496 | even | true | true | false | - |
| lifting-sym+iter | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=15 / H=1, K=1, t=15 | 0.540 | 81.496 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.499 | 81.496 | even | true | true | false | - |
| pm-strahler | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.551 | 81.496 | even | true | true | false | - |
| pm-strahler+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.507 | 81.496 | even | true | true | false | - |
| pm-strahler+iter | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.538 | 81.496 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.516 | 81.496 | even | true | true | false | - |
| pm-succinct | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.633 | 81.496 | even | true | true | false | - |
| pm-succinct+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.507 | 81.496 | even | true | true | false | - |
| pm-succinct+iter | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.538 | 81.496 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.507 | 81.496 | even | true | true | false | - |
| zielonka | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.504 | 81.496 | even | true | true | false | - |
| zielonka+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.497 | 81.496 | even | true | true | false | - |
| zielonka-sym | complete | 65506 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.517 | 81.496 | even | true | true | false | - |
| zielonka-sym+pre | complete | 65506 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 81.496 | even | true | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=2_no_spontaneous_messages.gm · 185089 vertices / 1094241 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 185089 | 1094241 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.840 | 91.852 | even | true | true | false | - |
| lifting+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.727 | 91.852 | even | true | true | false | - |
| lifting+iter | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.862 | 91.848 | even | true | true | false | - |
| lifting+pre+iter | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.702 | 91.977 | even | true | true | false | - |
| lifting-adaptive | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.816 | 91.957 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.702 | 91.957 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.827 | 91.957 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.703 | 91.844 | even | true | true | false | - |
| lifting-sym | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.805 | 91.957 | even | true | true | false | - |
| lifting-sym+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.700 | 91.793 | even | true | true | false | - |
| lifting-sym+iter | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=17 / H=1, K=1, t=17 | 0.823 | 91.852 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.702 | 91.977 | even | true | true | false | - |
| pm-strahler | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.899 | 91.723 | even | true | true | false | - |
| pm-strahler+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.767 | 91.922 | even | true | true | false | - |
| pm-strahler+iter | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.826 | 91.801 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.755 | 91.797 | even | true | true | false | - |
| pm-succinct | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.135 | 91.859 | even | true | true | false | - |
| pm-succinct+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.746 | 91.840 | even | true | true | false | - |
| pm-succinct+iter | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.824 | 91.793 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.750 | 91.797 | even | true | true | false | - |
| zielonka | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.721 | 91.914 | even | true | true | false | - |
| zielonka+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.701 | 91.910 | even | true | true | false | - |
| zielonka-sym | complete | 185089 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.773 | 91.844 | even | true | true | false | - |
| zielonka-sym+pre | complete | 185089 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.690 | 91.961 | even | true | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=2_nodeadlock.gm · 81921 vertices / 468161 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 81921 | 468161 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.582 | 81.496 | even | true | true | false | - |
| lifting+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.539 | 81.496 | even | true | true | false | - |
| lifting+iter | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.591 | 81.496 | even | true | true | false | - |
| lifting+pre+iter | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.526 | 81.496 | even | true | true | false | - |
| lifting-adaptive | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.576 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.525 | 81.496 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.578 | 81.496 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.527 | 81.496 | even | true | true | false | - |
| lifting-sym | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.570 | 81.496 | even | true | true | false | - |
| lifting-sym+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.527 | 81.496 | even | true | true | false | - |
| lifting-sym+iter | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=16 / H=1, K=1, t=16 | 0.578 | 81.496 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.525 | 81.496 | even | true | true | false | - |
| pm-strahler | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.609 | 81.496 | even | true | true | false | - |
| pm-strahler+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.558 | 81.496 | even | true | true | false | - |
| pm-strahler+iter | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.579 | 81.496 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.547 | 81.496 | even | true | true | false | - |
| pm-succinct | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.701 | 81.496 | even | true | true | false | - |
| pm-succinct+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.549 | 81.496 | even | true | true | false | - |
| pm-succinct+iter | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.578 | 81.496 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.546 | 81.496 | even | true | true | false | - |
| zielonka | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.527 | 81.496 | even | true | true | false | - |
| zielonka+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.527 | 81.496 | even | true | true | false | - |
| zielonka-sym | complete | 81921 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.558 | 81.496 | even | true | true | false | - |
| zielonka-sym+pre | complete | 81921 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.517 | 81.496 | even | true | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=2_read_then_eventually_send.gm · 297089 vertices / 1483457 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 297089 | 1483457 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 133.387 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.902 | 133.434 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 133.430 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.896 | 133.500 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 297089 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.498 | 133.453 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.007 | 133.496 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 297089 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.559 | 133.457 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.030 | 133.516 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 133.223 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.947 | 133.305 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 133.457 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.933 | 133.387 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 297089 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 3.457 | 133.266 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.084 | 133.398 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 297089 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.252 | 133.336 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.034 | 133.336 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 297089 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 3.143 | 133.191 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.045 | 133.398 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 297089 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 1.382 | 133.320 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.038 | 133.383 | odd | - | - | false | - |
| zielonka | complete | 0 / 297089 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.023 | 133.500 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.939 | 133.328 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 297089 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.149 | 133.328 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 297089 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.940 | 133.496 | odd | - | - | false | - |

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
| pm-strahler | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_infinitely_often_enabled_then_infinitely_often_taken.gm · 3471554 vertices / 13612756 edges · 10 complete · 14 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3471554 | 13612756 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.089 | 1369.461 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.089 | 1369.227 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.088 | 1369.332 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.078 | 1369.305 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.610 | 1369.324 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.607 | 1369.355 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.547 | 1369.238 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 16.546 | 1369.250 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.089 | 1369.324 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.085 | 1369.441 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.087 | 1369.441 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.071 | 1369.270 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1369.469 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.079 | 1369.129 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.070 | 1369.133 | - | - | - | - | deadline exceeded |
| pm-strahler+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.076 | 1369.273 | - | - | - | - | deadline exceeded |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.061 | 1369.281 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.075 | 1369.277 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 0 / 3471554 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 15.019 | 1369.328 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 3471554 | 0 / 7 | 0 / 4 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 15.008 | 1369.277 | odd | - | - | false | - |
| zielonka | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 6.481 | 1369.188 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 6.624 | 1369.465 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 8.278 | 1369.465 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 3471554 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 8.402 | 1369.191 | odd | - | - | false | - |

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
| pm-strahler+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 4 | 0 / 3 | 0.000 / 2.000 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_infinitely_often_read_write.gm · 607753 vertices / 2008153 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 607753 | 2008153 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 217.297 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 217.297 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 217.148 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 217.168 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 7.187 | 217.180 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 7.207 | 217.301 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 7.731 | 217.195 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 7.795 | 217.316 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 217.180 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.020 | 217.301 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 217.188 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 217.246 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 19.602 | 217.262 | even | - | - | false | - |
| pm-strahler+pre | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 18.089 | 217.266 | even | - | - | false | - |
| pm-strahler+iter | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.314 | 217.262 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 6.121 | 217.141 | even | - | - | false | - |
| pm-succinct | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 9.501 | 217.258 | even | - | - | false | - |
| pm-succinct+pre | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 9.624 | 217.262 | even | - | - | false | - |
| pm-succinct+iter | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.100 | 217.191 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 607753 / 0 | 5 / 0 | 4 / 0 | 2 / 0 | bits=2, depth=1 / bits=2, depth=2 | 3.132 | 217.195 | even | - | - | false | - |
| zielonka | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 1.334 | 217.301 | even | - | - | false | - |
| zielonka+pre | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 1.375 | 217.184 | even | - | - | false | - |
| zielonka-sym | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 1.922 | 217.043 | even | - | - | false | - |
| zielonka-sym+pre | complete | 607753 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | — / — | 1.940 | 217.195 | even | - | - | false | - |

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
<summary>modelchecking/games/Onebitdatasize=3_infinitely_often_receive_d1.gm · 308738 vertices / 1709138 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 308738 | 1709138 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 147.398 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.027 | 147.605 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 147.672 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.013 | 147.535 | even | - | - | false | - |
| lifting-adaptive | complete | 308738 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.829 | 147.668 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.153 | 147.539 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 308738 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 1.943 | 147.672 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.136 | 147.574 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.013 | 147.547 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.089 | 147.480 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 147.602 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.096 | 147.668 | even | - | - | false | - |
| pm-strahler | complete | 308738 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 12.976 | 147.613 | even | - | - | false | - |
| pm-strahler+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.147 | 147.480 | even | - | - | false | - |
| pm-strahler+iter | complete | 308738 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 8.931 | 147.531 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.107 | 147.531 | even | - | - | false | - |
| pm-succinct | complete | 308738 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.299 | 147.551 | even | - | - | false | - |
| pm-succinct+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.120 | 147.488 | even | - | - | false | - |
| pm-succinct+iter | complete | 308738 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 7.122 | 147.488 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.119 | 147.555 | even | - | - | false | - |
| zielonka | complete | 308738 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.048 | 147.477 | even | - | - | false | - |
| zielonka+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.066 | 147.668 | even | - | - | false | - |
| zielonka-sym | complete | 308738 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.255 | 147.535 | even | - | - | false | - |
| zielonka-sym+pre | complete | 308738 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.068 | 147.652 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_infinitely_often_receive_for_all_d.gm · 926213 vertices / 5127415 edges · 14 complete · 10 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 926213 | 5127415 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 440.559 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 440.758 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 440.824 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 440.680 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.431 | 440.559 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.452 | 440.535 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.819 | 440.828 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 4.850 | 440.773 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 440.691 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 440.703 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 440.695 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 440.559 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 440.707 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.029 | 440.742 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 24.247 | 440.777 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 24.188 | 440.508 | even | - | - | false | - |
| pm-succinct | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 19.641 | 440.777 | even | - | - | false | - |
| pm-succinct+pre | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 19.723 | 440.781 | even | - | - | false | - |
| pm-succinct+iter | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 19.041 | 440.641 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 926213 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 18.617 | 440.559 | even | - | - | false | - |
| zielonka | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.341 | 440.812 | even | - | - | false | - |
| zielonka+pre | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.309 | 440.617 | even | - | - | false | - |
| zielonka-sym | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.771 | 440.695 | even | - | - | false | - |
| zielonka-sym+pre | complete | 926213 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.758 | 440.816 | even | - | - | false | - |

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
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_invariantly_infinitely_many_reachable_taus.gm · 867889 vertices / 4933009 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 867889 | 4933009 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 425.277 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 425.293 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 425.305 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.034 | 425.219 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.036 | 425.234 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.078 | 425.430 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.116 | 425.309 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 3.137 | 425.352 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.044 | 425.348 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 425.184 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 425.371 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 425.129 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 7.998 | 425.348 | even | - | - | false | - |
| pm-strahler+pre | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 8.245 | 425.320 | even | - | - | false | - |
| pm-strahler+iter | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 5.036 | 425.316 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 4.901 | 425.320 | even | - | - | false | - |
| pm-succinct | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 4.032 | 425.285 | even | - | - | false | - |
| pm-succinct+pre | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 4.014 | 425.246 | even | - | - | false | - |
| pm-succinct+iter | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 3.314 | 425.234 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 867889 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 3.273 | 425.371 | even | - | - | false | - |
| zielonka | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.104 | 425.230 | even | - | - | false | - |
| zielonka+pre | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.169 | 425.242 | even | - | - | false | - |
| zielonka-sym | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.387 | 425.246 | even | - | - | false | - |
| zielonka-sym+pre | complete | 867889 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.356 | 425.234 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_message_can_be_lost_infinitely_often.gm · 579745 vertices / 3354841 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 579745 | 3354841 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.027 | 280.938 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.513 | 281.117 | even | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 280.992 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.509 | 281.051 | even | - | - | false | - |
| lifting-adaptive | complete | 579745 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 2.731 | 281.008 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.643 | 281.008 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 579745 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=1, K=1, t=0 | 2.888 | 281.133 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.665 | 281.070 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 281.004 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.692 | 281.066 | even | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 281.008 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.577 | 280.930 | even | - | - | false | - |
| pm-strahler | complete | 579745 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 10.608 | 280.949 | even | - | - | false | - |
| pm-strahler+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.755 | 280.742 | even | - | - | false | - |
| pm-strahler+iter | complete | 579745 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.968 | 281.008 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.772 | 281.016 | even | - | - | false | - |
| pm-succinct | complete | 579745 / 0 | 13 / 0 | 12 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=1 | 8.034 | 280.953 | even | - | - | false | - |
| pm-succinct+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.745 | 280.945 | even | - | - | false | - |
| pm-succinct+iter | complete | 579745 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 2.354 | 280.949 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.688 | 280.934 | even | - | - | false | - |
| zielonka | complete | 579745 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 1.664 | 281.051 | even | - | - | false | - |
| zielonka+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.544 | 281.055 | even | - | - | false | - |
| zielonka-sym | complete | 579745 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 2.020 | 281.133 | even | - | - | false | - |
| zielonka-sym+pre | complete | 579745 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.535 | 280.934 | even | - | - | false | - |

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
| pm-strahler | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 12 / 0 | 12 / 0 | 12.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_messages_can_be_overtaken.gm · 638065 vertices / 3680785 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 638065 | 3680785 | 1 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 307.906 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.567 | 307.891 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 308.031 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.529 | 308.035 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 638065 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 2.234 | 307.965 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.684 | 307.809 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 638065 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 2.292 | 307.895 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.732 | 307.895 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.033 | 308.012 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.620 | 308.035 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 308.035 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.585 | 307.898 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 638065 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 2.372 | 307.914 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.867 | 307.855 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 638065 | 0 / 2 | 0 / 1 | 0 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 2.460 | 307.848 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.810 | 307.895 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 638065 | 0 / 2 | 0 / 1 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 3.220 | 307.914 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.744 | 307.789 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 638065 | 0 / 2 | 0 / 1 | 0 / 2 | bits=1, depth=1 / bits=1, depth=1 | 3.247 | 307.852 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=1 | 1.771 | 307.781 | odd | - | - | false | - |
| zielonka | complete | 0 / 638065 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 1.645 | 308.016 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.581 | 308.016 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 638065 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 1.891 | 308.016 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 638065 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.595 | 307.961 | odd | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-adaptive+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_messages_read_are_inevitably_sent.gm · 579745 vertices / 3354841 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 579745 | 3354841 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.031 | 281.070 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.515 | 280.801 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.030 | 280.883 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.500 | 280.801 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 579745 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.806 | 281.070 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.655 | 280.934 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 579745 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 2.963 | 281.074 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.646 | 280.801 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 280.977 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.579 | 280.949 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 281.074 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.565 | 281.070 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 579745 | 0 / 25 | 0 / 12 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 8.932 | 280.891 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.764 | 280.949 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 579745 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.225 | 280.934 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 1.746 | 280.945 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 579745 | 0 / 25 | 0 / 12 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 8.039 | 280.879 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.751 | 280.953 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 579745 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 2.657 | 280.922 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 1.678 | 280.816 | odd | false | true | false | - |
| zielonka | complete | 0 / 579745 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 1.692 | 281.074 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.537 | 280.746 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 579745 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.036 | 281.070 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 579745 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.569 | 280.945 | odd | false | true | false | - |

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
<summary>modelchecking/games/Onebitdatasize=3_no_duplication_of_messages.gm · 1191962 vertices / 6907934 edges · 18 complete · 6 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1191962 | 6907934 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 580.969 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.799 | 580.965 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.048 | 580.910 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.791 | 581.035 | odd | - | - | false | - |
| lifting-adaptive | complete | 838728 / 353234 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 7.547 | 580.965 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.070 | 580.906 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 838728 / 353234 | 1 / 2 | 1 / 1 | 1 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 7.841 | 580.969 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.937 | 581.023 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.053 | 580.953 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.716 | 580.957 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 581.094 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.856 | 580.969 | odd | - | - | false | - |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 581.039 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.038 | 580.902 | odd | - | - | false | - |
| pm-strahler+iter | complete | 838728 / 353234 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.533 | 580.973 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 2.976 | 580.848 | odd | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 580.977 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 2.906 | 580.977 | odd | - | - | false | - |
| pm-succinct+iter | complete | 838728 / 353234 | 2 / 7 | 1 / 3 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 4.138 | 580.957 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.005 | 580.883 | odd | - | - | false | - |
| zielonka | complete | 838728 / 353234 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 2.715 | 580.969 | odd | - | - | false | - |
| zielonka+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.561 | 580.973 | odd | - | - | false | - |
| zielonka-sym | complete | 838728 / 353234 | 1 / 2 | 1 / 1 | 1 / 2 | — / — | 3.405 | 581.117 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 838728 / 353234 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.643 | 580.949 | odd | - | - | false | - |

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
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 4 | 1 / 3 | 1 / 3 | 1.000 / 1.500 | 0 / 1 | 2 / 3 | 2.000 / 3.000 | 1 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 1 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 1 / 2 | 1.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Onebitdatasize=3_no_generation_of_messages.gm · 474914 vertices / 2739604 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 474914 | 2739604 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.543 | 232.320 | even | - | - | false | - |
| lifting+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.265 | 232.047 | even | - | - | false | - |
| lifting+iter | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.585 | 232.184 | even | - | - | false | - |
| lifting+pre+iter | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.210 | 232.195 | even | - | - | false | - |
| lifting-adaptive | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.510 | 232.191 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.200 | 232.191 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.549 | 232.305 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.223 | 232.180 | even | - | - | false | - |
| lifting-sym | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.478 | 232.301 | even | - | - | false | - |
| lifting-sym+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.202 | 232.262 | even | - | - | false | - |
| lifting-sym+iter | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.514 | 232.195 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.194 | 232.324 | even | - | - | false | - |
| pm-strahler | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.720 | 231.992 | even | - | - | false | - |
| pm-strahler+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.360 | 232.199 | even | - | - | false | - |
| pm-strahler+iter | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.546 | 232.207 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.347 | 232.125 | even | - | - | false | - |
| pm-succinct | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 2.318 | 232.188 | even | - | - | false | - |
| pm-succinct+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.337 | 231.992 | even | - | - | false | - |
| pm-succinct+iter | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.551 | 232.199 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 1.334 | 232.141 | even | - | - | false | - |
| zielonka | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.240 | 232.238 | even | - | - | false | - |
| zielonka+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.185 | 232.133 | even | - | - | false | - |
| zielonka-sym | complete | 474914 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 1.371 | 232.324 | even | - | - | false | - |
| zielonka-sym+pre | complete | 474914 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 1.173 | 232.320 | even | - | - | false | - |

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
<summary>modelchecking/games/Onebitdatasize=3_no_spontaneous_messages.gm · 1278433 vertices / 7843609 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1278433 | 7843609 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 3.806 | 647.438 | even | - | - | false | - |
| lifting+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.801 | 647.305 | even | - | - | false | - |
| lifting+iter | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 3.867 | 647.250 | even | - | - | false | - |
| lifting+pre+iter | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.702 | 647.270 | even | - | - | false | - |
| lifting-adaptive | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 3.592 | 647.371 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.724 | 647.457 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 3.667 | 647.312 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.733 | 647.438 | even | - | - | false | - |
| lifting-sym | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 3.488 | 647.301 | even | - | - | false | - |
| lifting-sym+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.732 | 647.293 | even | - | - | false | - |
| lifting-sym+iter | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=20 / H=1, K=1, t=20 | 3.548 | 647.250 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.701 | 647.238 | even | - | - | false | - |
| pm-strahler | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 4.183 | 647.301 | even | - | - | false | - |
| pm-strahler+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 3.192 | 647.383 | even | - | - | false | - |
| pm-strahler+iter | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 3.714 | 647.379 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 3.236 | 647.355 | even | - | - | false | - |
| pm-succinct | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 6.139 | 647.242 | even | - | - | false | - |
| pm-succinct+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 3.204 | 647.207 | even | - | - | false | - |
| pm-succinct+iter | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 3.702 | 647.258 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 3.140 | 647.301 | even | - | - | false | - |
| zielonka | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 2.851 | 647.418 | even | - | - | false | - |
| zielonka+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.767 | 647.301 | even | - | - | false | - |
| zielonka-sym | complete | 1278433 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 3.178 | 647.488 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1278433 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.681 | 647.301 | even | - | - | false | - |

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
<summary>modelchecking/games/Onebitdatasize=3_nodeadlock.gm · 289297 vertices / 1689697 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 289297 | 1689697 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.109 | 143.020 | even | - | - | false | - |
| lifting+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.923 | 142.805 | even | - | - | false | - |
| lifting+iter | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.120 | 142.891 | even | - | - | false | - |
| lifting+pre+iter | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.887 | 142.746 | even | - | - | false | - |
| lifting-adaptive | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.063 | 143.004 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.887 | 142.891 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 1.085 | 143.020 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.898 | 142.887 | even | - | - | false | - |
| lifting-sym | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.042 | 142.949 | even | - | - | false | - |
| lifting-sym+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.896 | 142.957 | even | - | - | false | - |
| lifting-sym+iter | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=18 / H=1, K=1, t=18 | 1.062 | 142.879 | even | - | - | false | - |
| lifting-sym+pre+iter | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.886 | 142.891 | even | - | - | false | - |
| pm-strahler | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.172 | 142.832 | even | - | - | false | - |
| pm-strahler+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.976 | 142.969 | even | - | - | false | - |
| pm-strahler+iter | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 1.090 | 142.906 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.973 | 142.945 | even | - | - | false | - |
| pm-succinct | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.550 | 142.969 | even | - | - | false | - |
| pm-succinct+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.963 | 142.926 | even | - | - | false | - |
| pm-succinct+iter | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 1.078 | 142.906 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.996 | 142.691 | even | - | - | false | - |
| zielonka | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.903 | 143.023 | even | - | - | false | - |
| zielonka+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.889 | 143.020 | even | - | - | false | - |
| zielonka-sym | complete | 289297 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.990 | 142.883 | even | - | - | false | - |
| zielonka-sym+pre | complete | 289297 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.866 | 142.891 | even | - | - | false | - |

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
<summary>modelchecking/games/Onebitdatasize=3_read_then_eventually_send.gm · 1350433 vertices / 7068673 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1350433 | 7068673 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 619.992 | - | - | - | - | deadline exceeded |
| lifting+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.919 | 620.066 | odd | - | - | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.049 | 619.988 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.910 | 620.105 | odd | - | - | false | - |
| lifting-adaptive | complete | 0 / 1350433 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.535 | 620.129 | odd | - | - | false | - |
| lifting-adaptive+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.057 | 619.855 | odd | - | - | false | - |
| lifting-adaptive+iter | complete | 0 / 1350433 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 5.736 | 620.066 | odd | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 3.068 | 620.062 | odd | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.058 | 620.105 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.956 | 620.129 | odd | - | - | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 619.996 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.955 | 620.105 | odd | - | - | false | - |
| pm-strahler | complete | 0 / 1350433 | 0 / 27 | 0 / 13 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 13.667 | 619.938 | odd | - | - | false | - |
| pm-strahler+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.501 | 619.797 | odd | - | - | false | - |
| pm-strahler+iter | complete | 0 / 1350433 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 4.456 | 620.070 | odd | - | - | false | - |
| pm-strahler+pre+iter | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 3.394 | 619.988 | odd | - | - | false | - |
| pm-succinct | complete | 0 / 1350433 | 0 / 27 | 0 / 13 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 11.740 | 619.938 | odd | - | - | false | - |
| pm-succinct+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.269 | 619.957 | odd | - | - | false | - |
| pm-succinct+iter | complete | 0 / 1350433 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 4.689 | 620.004 | odd | - | - | false | - |
| pm-succinct+pre+iter | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 3.154 | 619.988 | odd | - | - | false | - |
| zielonka | complete | 0 / 1350433 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 2.971 | 620.000 | odd | - | - | false | - |
| zielonka+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.679 | 620.188 | odd | - | - | false | - |
| zielonka-sym | complete | 0 / 1350433 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 3.535 | 619.992 | odd | - | - | false | - |
| zielonka-sym+pre | complete | 0 / 1350433 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 2.681 | 620.109 | odd | - | - | false | - |

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
| pm-strahler | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 14 | 0 / 13 | 0 / 13 | 0.000 / 1.857 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=2_infinitely_often_enabled_then_infinitely_often_taken.gm · 730 vertices / 1027 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 730 | 1027 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.937 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.936 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.936 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.938 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.383 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 730 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 730 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 730 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.401 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 730 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 730 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 730 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 730 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 730 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 730 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.370 | 82.871 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=2_infinitely_often_read_write.gm · 108 vertices / 135 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 108 | 135 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.417 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.396 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.396 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 108 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 82.871 | even | true | true | false | - |
| zielonka | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.397 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 108 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=2_infinitely_often_receive_d1.gm · 96 vertices / 123 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 96 | 123 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.415 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.414 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.395 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 96 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 96 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 96 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 96 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| zielonka | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=2_infinitely_often_receive_for_all_d.gm · 192 vertices / 247 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 192 | 247 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.447 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.446 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.446 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.435 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.406 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 192 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| zielonka | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.396 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 192 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.395 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=2_invariantly_infinitely_many_reachable_taus.gm · 274 vertices / 419 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 274 | 419 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.405 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.417 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.416 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 274 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 274 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 274 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 274 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 274 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 274 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.406 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 274 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 274 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.407 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 274 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.406 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/Pardatasize=2_no_duplication_of_messages.gm · 272 vertices / 353 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 272 | 353 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.397 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.395 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.395 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.397 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| zielonka | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 272 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 272 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=2_no_generation_of_messages.gm · 96 vertices / 121 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 96 | 121 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.408 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.407 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.418 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.417 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| zielonka | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 96 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 96 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=2_nodeadlock.gm · 92 vertices / 119 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 92 | 119 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.409 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=6 / H=1, K=1, t=6 | 0.408 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.407 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.407 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| zielonka | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 92 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 92 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=2_read_then_eventually_send.gm · 282 vertices / 367 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 282 | 367 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.415 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.414 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 282 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 282 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 282 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 282 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 282 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 282 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.395 | 82.871 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=4_infinitely_often_enabled_then_infinitely_often_taken.gm · 2866 vertices / 4077 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2866 | 4077 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 9.140 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 9.203 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 9.211 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 9.172 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.463 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.466 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 2866 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.400 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 2866 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 2866 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 2866 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 2866 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 2866 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.390 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 2866 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 2866 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.401 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.382 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 2866 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.381 | 82.871 | odd | false | true | false | - |

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
| pm-strahler | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=4_infinitely_often_read_write.gm · 210 vertices / 267 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 210 | 267 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.427 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.427 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.415 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.414 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 210 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.407 | 82.871 | even | true | true | false | - |
| zielonka | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.417 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.417 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 210 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.417 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=4_infinitely_often_receive_d1.gm · 184 vertices / 241 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 184 | 241 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.437 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.445 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 184 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 184 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 184 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 184 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| zielonka | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 184 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 184 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=4_infinitely_often_receive_for_all_d.gm · 734 vertices / 965 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 734 | 965 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.019 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.017 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.017 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 1.018 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.381 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 734 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| zielonka | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.383 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 734 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.371 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=4_invariantly_infinitely_many_reachable_taus.gm · 538 vertices / 831 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 538 | 831 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.436 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.437 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.448 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.435 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 538 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 538 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 538 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 538 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 538 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 538 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 538 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 538 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 538 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/Pardatasize=4_no_duplication_of_messages.gm · 892 vertices / 1169 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 892 | 1169 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.408 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.407 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.394 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| zielonka | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 892 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 892 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=4_no_generation_of_messages.gm · 542 vertices / 713 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 542 | 713 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.408 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.398 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=9 / H=1, K=1, t=9 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.395 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.400 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.391 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.413 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.391 | 82.871 | even | true | true | false | - |
| zielonka | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 542 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 542 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=4_nodeadlock.gm · 180 vertices / 237 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 180 | 237 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.407 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.405 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=7 / H=1, K=1, t=7 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.408 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.407 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| zielonka | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 180 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 180 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=4_read_then_eventually_send.gm · 912 vertices / 1197 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 912 | 1197 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.498 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.384 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.497 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.403 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=9 / H=2, K=2, t=9 | 0.412 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.401 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 912 | 0 / 29 | 0 / 14 | 0 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 912 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 912 | 0 / 29 | 0 / 14 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 912 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 912 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 912 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | odd | false | true | false | - |

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
| pm-strahler | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 0 / 15 | 0 / 14 | 0 / 14 | 0.000 / 1.867 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 0 / 4 | 0 / 3 | 0 / 3 | 0.000 / 1.500 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=8_infinitely_often_enabled_then_infinitely_often_taken.gm · 11362 vertices / 16249 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 11362 | 16249 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 82.871 | - | false | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 82.871 | - | false | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 82.871 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.001 | 82.871 | - | false | - | - | deadline exceeded |
| lifting-adaptive | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.424 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.421 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.422 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.571 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.567 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.579 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=13 / H=2, K=2, t=13 | 1.588 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 11362 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.463 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 11362 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.452 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 11362 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.454 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 11362 | 0 / 24 | 0 / 18 | 0 / 3 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.455 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 11362 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.432 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 11362 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.432 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 11362 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.435 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 11362 | 0 / 23 | 0 / 17 | 0 / 3 | bits=3, depth=1 / bits=3, depth=2 | 0.433 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.405 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.404 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 11362 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.402 | 82.871 | odd | false | true | false | - |

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
| lifting-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| lifting-sym+pre+iter | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| pm-strahler | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+pre+iter | 0 / 6 | 0 / 18 | 0 / 14 | 0.000 / 3.833 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+pre+iter | 0 / 6 | 0 / 17 | 0 / 13 | 0.000 / 3.667 | 0 / 2 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |
| zielonka-sym+pre | 0 / 1 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 2 | 0.000 / 2.000 | 0 / 1 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=8_infinitely_often_read_write.gm · 414 vertices / 531 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 414 | 531 | 3 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.498 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.487 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=1 / H=2, K=2, t=1 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.443 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.443 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.442 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.433 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 414 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| zielonka | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 414 / 0 | 3 / 0 | 2 / 0 | 2 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| lifting-sym+pre+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=8_infinitely_often_receive_d1.gm · 360 vertices / 477 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 360 | 477 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.548 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.540 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 360 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 360 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 360 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 360 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=1 / bits=0, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| zielonka | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 360 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 360 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 82.871 | even | true | true | false | - |

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
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=8_infinitely_often_receive_for_all_d.gm · 2874 vertices / 3817 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2874 | 3817 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.488 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.427 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.465 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 10.446 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.390 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.461 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.462 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.465 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=11 / H=2, K=2, t=11 | 0.483 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | k=2, t=3, depth=1 / k=2, t=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2874 / 0 | 14 / 0 | 13 / 0 | 2 / 0 | bits=3, depth=1 / bits=3, depth=2 | 0.393 | 82.871 | even | true | true | false | - |
| zielonka | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.381 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2874 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.380 | 82.871 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| lifting-sym+pre+iter | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| pm-strahler | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 0 | 13 / 0 | 13 / 0 | 13.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| zielonka | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |
| zielonka-sym+pre | 0 / 0 | 1 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 1 / 0 | 1.000 / 0.000 | 1 / 0 |

</details>

<details>
<summary>modelchecking/games/Pardatasize=8_invariantly_infinitely_many_reachable_taus.gm · 1066 vertices / 1655 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1066 | 1655 | 2 | 2 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.581 | 82.871 | odd | false | true | false | - |
| lifting+pre | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.580 | 82.871 | odd | false | true | false | - |
| lifting+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.579 | 82.871 | odd | false | true | false | - |
| lifting+pre+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.568 | 82.871 | odd | false | true | false | - |
| lifting-adaptive | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.394 | 82.871 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 82.871 | odd | false | true | false | - |
| lifting-sym | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.423 | 82.871 | odd | false | true | false | - |
| lifting-sym+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.412 | 82.871 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.417 | 82.871 | odd | false | true | false | - |
| pm-strahler | complete | 0 / 1066 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.440 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre | complete | 0 / 1066 | 0 / 9 | 0 / 4 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.399 | 82.871 | odd | false | true | false | - |
| pm-strahler+iter | complete | 0 / 1066 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 0 / 1066 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct | complete | 0 / 1066 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.390 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre | complete | 0 / 1066 | 0 / 9 | 0 / 4 | 0 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.392 | 82.871 | odd | false | true | false | - |
| pm-succinct+iter | complete | 0 / 1066 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 82.871 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 0 / 1066 | 0 / 7 | 0 / 3 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.394 | 82.871 | odd | false | true | false | - |
| zielonka | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.392 | 82.871 | odd | false | true | false | - |
| zielonka+pre | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.398 | 82.871 | odd | false | true | false | - |
| zielonka-sym | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.398 | 82.871 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 0 / 1066 | 0 / 2 | 0 / 1 | 0 / 2 | — / — | 0.383 | 82.871 | odd | false | true | false | - |

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
<summary>modelchecking/games/Pardatasize=8_no_duplication_of_messages.gm · 3188 vertices / 4193 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3188 | 4193 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.414 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.403 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.394 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.414 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.404 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.416 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.416 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.417 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.417 | 82.871 | even | true | true | false | - |
| zielonka | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.416 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 3188 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3188 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=8_no_generation_of_messages.gm · 2490 vertices / 3313 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2490 | 3313 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.405 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.414 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.403 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.402 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=11 / H=1, K=1, t=11 | 0.392 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.413 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.414 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.412 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.403 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.407 | 82.871 | even | true | true | false | - |
| zielonka | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 2490 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2490 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |

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
<summary>modelchecking/games/Pardatasize=8_nodeadlock.gm · 356 vertices / 473 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 356 | 473 | 1 | 0 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.405 | 82.871 | even | true | true | false | - |
| lifting+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 82.871 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.406 | 82.871 | even | true | true | false | - |
| lifting-sym+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.397 | 82.871 | even | true | true | false | - |
| lifting-sym+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=1, K=1, t=8 / H=1, K=1, t=8 | 0.398 | 82.871 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.406 | 82.871 | even | true | true | false | - |
| pm-strahler | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.391 | 82.871 | even | true | true | false | - |
| pm-strahler+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-strahler+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=0 / k=1, t=1, depth=1 | 0.392 | 82.871 | even | true | true | false | - |
| pm-succinct | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| pm-succinct+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.402 | 82.871 | even | true | true | false | - |
| pm-succinct+iter | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | bits=1, depth=0 / bits=1, depth=1 | 0.394 | 82.871 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=0 / bits=0, depth=1 | 0.405 | 82.871 | even | true | true | false | - |
| zielonka | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.403 | 82.871 | even | true | true | false | - |
| zielonka+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym | complete | 356 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.392 | 82.871 | even | true | true | false | - |
| zielonka-sym+pre | complete | 356 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 82.871 | even | true | true | false | - |

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

