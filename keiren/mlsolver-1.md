# mlsolver, part 1

[Definitions and summary](../KEIREN.md).

## Winner checks

| Archive | Game | Problem | Details |
| --- | --- | --- | --- |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-strahler+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-strahler+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-strahler+pre+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-succinct: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-succinct+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-succinct+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | pm-succinct+pre+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | zielonka: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | zielonka+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | zielonka-sym: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1.gm | reference mismatch | zielonka-sym+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | lifting-adaptive: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | lifting-adaptive+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | lifting-adaptive+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | lifting-adaptive+pre+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-strahler: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-strahler+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-strahler+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-strahler+pre+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-succinct: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-succinct+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-succinct+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | pm-succinct+pre+iter: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | zielonka: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | zielonka+pre: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | zielonka-sym: reference=false, start=even |
| mlsolver | mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm | reference mismatch | zielonka-sym+pre: reference=false, start=even |

## Inventory

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=1.gm · 34 vertices / 42 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 34 | 42 | 4 | 983043 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.409 | 52.090 | odd | false | true | false | - |
| lifting+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.409 | 52.090 | odd | false | true | false | - |
| lifting+iter | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.408 | 52.090 | odd | false | true | false | - |
| lifting+pre+iter | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 52.090 | odd | false | true | false | - |
| lifting-adaptive | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 52.090 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.405 | 52.090 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.423 | 52.090 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.432 | 52.090 | odd | false | true | false | - |
| lifting-sym | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.425 | 52.090 | odd | false | true | false | - |
| lifting-sym+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.403 | 52.090 | odd | false | true | false | - |
| lifting-sym+iter | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=5 / H=2, K=2, t=5 | 0.402 | 52.090 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 52.090 | odd | false | true | false | - |
| pm-strahler | complete | 19 / 15 | 10 / 3 | 5 / 1 | 3 / 3 | k=2, t=1, depth=2 / k=2, t=1, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| pm-strahler+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.405 | 52.090 | odd | false | true | false | - |
| pm-strahler+iter | complete | 19 / 15 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.403 | 52.090 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| pm-succinct | complete | 19 / 15 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| pm-succinct+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| pm-succinct+iter | complete | 19 / 15 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.406 | 52.090 | odd | false | true | false | - |
| zielonka | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.406 | 52.090 | odd | false | true | false | - |
| zielonka+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.418 | 52.090 | odd | false | true | false | - |
| zielonka-sym | complete | 19 / 15 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.418 | 52.090 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 19 / 15 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.416 | 52.090 | odd | false | true | false | - |

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
| pm-strahler | 5 / 2 | 5 / 1 | 4 / 1 | 1.800 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=1_compact.gm · 8 vertices / 12 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8 | 12 | 3 | 983042 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting+pre | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting+iter | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 52.324 | odd | false | true | false | - |
| lifting+pre+iter | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting-adaptive | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 52.324 | odd | false | true | false | - |
| lifting-sym | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 52.324 | odd | false | true | false | - |
| lifting-sym+pre | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.405 | 52.324 | odd | false | true | false | - |
| lifting-sym+iter | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.404 | 52.324 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=2 / H=1, K=1, t=2 | 0.404 | 52.324 | odd | false | true | false | - |
| pm-strahler | complete | 3 / 5 | 3 / 5 | 2 / 2 | 2 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.407 | 52.324 | odd | false | true | false | - |
| pm-strahler+pre | complete | 3 / 5 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.408 | 52.324 | odd | false | true | false | - |
| pm-strahler+iter | complete | 3 / 5 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 52.324 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 3 / 5 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.402 | 52.324 | odd | false | true | false | - |
| pm-succinct | complete | 3 / 5 | 3 / 5 | 2 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 52.324 | odd | false | true | false | - |
| pm-succinct+pre | complete | 3 / 5 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 52.324 | odd | false | true | false | - |
| pm-succinct+iter | complete | 3 / 5 | 3 / 5 | 2 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 52.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 3 / 5 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.403 | 52.449 | odd | false | true | false | - |
| zielonka | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.401 | 52.449 | odd | false | true | false | - |
| zielonka+pre | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.408 | 52.449 | odd | false | true | false | - |
| zielonka-sym | complete | 3 / 5 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.408 | 52.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 3 / 5 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.408 | 52.449 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 2 / 2 | 2 / 2 | 2.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 2 / 2 | 2 / 2 | 2.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 2 / 2 | 2 / 2 | 2.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=2.gm · 250 vertices / 316 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 250 | 316 | 4 | 274877906947 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.467 | 52.449 | odd | false | true | false | - |
| lifting+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.385 | 52.449 | odd | false | true | false | - |
| lifting+iter | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.468 | 52.449 | odd | false | true | false | - |
| lifting+pre+iter | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 52.449 | odd | false | true | false | - |
| lifting-adaptive | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.393 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 52.449 | odd | false | true | false | - |
| lifting-sym | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.414 | 52.449 | odd | false | true | false | - |
| lifting-sym+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 52.449 | odd | false | true | false | - |
| lifting-sym+iter | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=7 / H=2, K=2, t=7 | 0.424 | 52.449 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 52.449 | odd | false | true | false | - |
| pm-strahler | complete | 184 / 66 | 23 / 3 | 14 / 1 | 3 / 3 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.402 | 52.449 | odd | false | true | false | - |
| pm-strahler+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.407 | 52.449 | odd | false | true | false | - |
| pm-strahler+iter | complete | 184 / 66 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.405 | 52.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.408 | 52.449 | odd | false | true | false | - |
| pm-succinct | complete | 184 / 66 | 21 / 3 | 14 / 1 | 3 / 3 | bits=2, depth=2 / bits=2, depth=2 | 0.399 | 52.449 | odd | false | true | false | - |
| pm-succinct+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.409 | 52.449 | odd | false | true | false | - |
| pm-succinct+iter | complete | 184 / 66 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.403 | 52.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.402 | 52.449 | odd | false | true | false | - |
| zielonka | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.391 | 52.449 | odd | false | true | false | - |
| zielonka+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 52.449 | odd | false | true | false | - |
| zielonka-sym | complete | 184 / 66 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.403 | 52.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 184 / 66 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.394 | 52.449 | odd | false | true | false | - |

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
| pm-strahler | 9 / 2 | 14 / 1 | 8 / 1 | 2.444 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 7 / 2 | 14 / 1 | 7 / 1 | 2.857 / 1.000 | 3 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=2_compact.gm · 17 vertices / 28 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 17 | 28 | 3 | 274877906946 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.410 | 52.449 | odd | false | true | false | - |
| lifting+pre | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.411 | 52.449 | odd | false | true | false | - |
| lifting+iter | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.411 | 52.449 | odd | false | true | false | - |
| lifting+pre+iter | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 52.449 | odd | false | true | false | - |
| lifting-adaptive | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.408 | 52.449 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 52.449 | odd | false | true | false | - |
| lifting-sym | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.407 | 52.449 | odd | false | true | false | - |
| lifting-sym+pre | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 52.449 | odd | false | true | false | - |
| lifting-sym+iter | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=4 / H=2, K=2, t=4 | 0.408 | 52.449 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 52.449 | odd | false | true | false | - |
| pm-strahler | complete | 8 / 9 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.393 | 52.449 | odd | false | true | false | - |
| pm-strahler+pre | complete | 8 / 9 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 52.449 | odd | false | true | false | - |
| pm-strahler+iter | complete | 8 / 9 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.397 | 52.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 8 / 9 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.394 | 52.449 | odd | false | true | false | - |
| pm-succinct | complete | 8 / 9 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.394 | 52.449 | odd | false | true | false | - |
| pm-succinct+pre | complete | 8 / 9 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.395 | 52.449 | odd | false | true | false | - |
| pm-succinct+iter | complete | 8 / 9 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.396 | 52.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 8 / 9 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 52.449 | odd | false | true | false | - |
| zielonka | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.402 | 52.449 | odd | false | true | false | - |
| zielonka+pre | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 52.449 | odd | false | true | false | - |
| zielonka-sym | complete | 8 / 9 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 52.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 8 / 9 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 52.449 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=3.gm · 795 vertices / 1016 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 795 | 1016 | 4 | 229683580995895295 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 1.558 | 52.574 | odd | false | true | false | - |
| lifting+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.373 | 52.574 | odd | false | true | false | - |
| lifting+iter | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 1.568 | 52.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 52.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.379 | 52.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.392 | 52.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.391 | 52.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 52.574 | odd | false | true | false | - |
| lifting-sym | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.588 | 52.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 52.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=9 / H=2, K=2, t=9 | 0.598 | 52.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 52.574 | odd | false | true | false | - |
| pm-strahler | complete | 660 / 135 | 40 / 3 | 23 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.415 | 52.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.391 | 52.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 660 / 135 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.390 | 52.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.392 | 52.574 | odd | false | true | false | - |
| pm-succinct | complete | 660 / 135 | 32 / 3 | 23 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.413 | 52.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.402 | 52.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 660 / 135 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.396 | 52.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.405 | 52.574 | odd | false | true | false | - |
| zielonka | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.405 | 52.574 | odd | false | true | false | - |
| zielonka+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 52.699 | odd | false | true | false | - |
| zielonka-sym | complete | 660 / 135 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.392 | 52.699 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 660 / 135 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.381 | 52.699 | odd | false | true | false | - |

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
| pm-strahler | 17 / 2 | 23 / 1 | 16 / 1 | 2.294 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9 / 2 | 23 / 1 | 8 / 1 | 3.444 / 1.000 | 5 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=3_compact.gm · 38 vertices / 62 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 38 | 62 | 3 | 229683580995895294 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting+pre | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting+iter | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.405 | 52.824 | odd | false | true | false | - |
| lifting+pre+iter | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting-adaptive | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 52.824 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.406 | 52.824 | odd | false | true | false | - |
| lifting-sym | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.407 | 52.824 | odd | false | true | false | - |
| lifting-sym+pre | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.408 | 52.824 | odd | false | true | false | - |
| lifting-sym+iter | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=5 / H=2, K=2, t=5 | 0.407 | 52.824 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.406 | 52.824 | odd | false | true | false | - |
| pm-strahler | complete | 28 / 10 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.407 | 52.824 | odd | false | true | false | - |
| pm-strahler+pre | complete | 28 / 10 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.405 | 52.824 | odd | false | true | false | - |
| pm-strahler+iter | complete | 28 / 10 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 52.824 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 28 / 10 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.413 | 52.824 | odd | false | true | false | - |
| pm-succinct | complete | 28 / 10 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 52.824 | odd | false | true | false | - |
| pm-succinct+pre | complete | 28 / 10 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.402 | 52.824 | odd | false | true | false | - |
| pm-succinct+iter | complete | 28 / 10 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 52.824 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 28 / 10 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 52.824 | odd | false | true | false | - |
| zielonka | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.393 | 52.824 | odd | false | true | false | - |
| zielonka+pre | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 52.824 | odd | false | true | false | - |
| zielonka-sym | complete | 28 / 10 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.395 | 52.824 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 28 / 10 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.395 | 52.824 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=4.gm · 2265 vertices / 2921 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2265 | 2921 | 4 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 16.763 | 53.074 | odd | false | true | false | - |
| lifting+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.383 | 53.074 | odd | false | true | false | - |
| lifting+iter | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 16.752 | 53.074 | odd | false | true | false | - |
| lifting+pre+iter | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 53.074 | odd | false | true | false | - |
| lifting-adaptive | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.380 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.369 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 53.074 | odd | false | true | false | - |
| lifting-sym | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 2.882 | 53.074 | odd | false | true | false | - |
| lifting-sym+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.370 | 53.074 | odd | false | true | false | - |
| lifting-sym+iter | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=11 / H=2, K=2, t=11 | 2.884 | 53.074 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.372 | 53.074 | odd | false | true | false | - |
| pm-strahler | complete | 2041 / 224 | 51 / 3 | 32 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.371 | 53.074 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.370 | 53.074 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2041 / 224 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.369 | 53.074 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.370 | 53.074 | odd | false | true | false | - |
| pm-succinct | complete | 2041 / 224 | 41 / 3 | 32 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.369 | 53.074 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.369 | 53.074 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2041 / 224 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.370 | 53.074 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.371 | 53.074 | odd | false | true | false | - |
| zielonka | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.369 | 53.074 | odd | false | true | false | - |
| zielonka+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.371 | 53.074 | odd | false | true | false | - |
| zielonka-sym | complete | 2041 / 224 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.370 | 53.074 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2041 / 224 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.374 | 53.074 | odd | false | true | false | - |

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
| pm-strahler | 19 / 2 | 32 / 1 | 18 / 1 | 2.632 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 9 / 2 | 32 / 1 | 15 / 1 | 4.444 / 1.000 | 5 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=4_compact.gm · 89 vertices / 147 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 89 | 147 | 3 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.415 | 53.074 | odd | false | true | false | - |
| lifting+pre | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.405 | 53.074 | odd | false | true | false | - |
| lifting+iter | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.415 | 53.074 | odd | false | true | false | - |
| lifting+pre+iter | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.394 | 53.074 | odd | false | true | false | - |
| lifting-adaptive | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.403 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 53.074 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.404 | 53.074 | odd | false | true | false | - |
| lifting-sym | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.403 | 53.074 | odd | false | true | false | - |
| lifting-sym+pre | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.394 | 53.074 | odd | false | true | false | - |
| lifting-sym+iter | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=6 / H=2, K=2, t=6 | 0.398 | 53.074 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.395 | 53.074 | odd | false | true | false | - |
| pm-strahler | complete | 77 / 12 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.415 | 53.074 | odd | false | true | false | - |
| pm-strahler+pre | complete | 77 / 12 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.413 | 53.074 | odd | false | true | false | - |
| pm-strahler+iter | complete | 77 / 12 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.405 | 53.074 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 77 / 12 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 53.074 | odd | false | true | false | - |
| pm-succinct | complete | 77 / 12 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.395 | 53.074 | odd | false | true | false | - |
| pm-succinct+pre | complete | 77 / 12 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.397 | 53.074 | odd | false | true | false | - |
| pm-succinct+iter | complete | 77 / 12 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 53.074 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 77 / 12 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 53.074 | odd | false | true | false | - |
| zielonka | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 53.074 | odd | false | true | false | - |
| zielonka+pre | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 53.074 | odd | false | true | false | - |
| zielonka-sym | complete | 77 / 12 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 53.074 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 77 / 12 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.392 | 53.074 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=5.gm · 5914 vertices / 7665 edges · 22 complete · 2 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 5914 | 7665 | 4 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 53.449 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.393 | 53.449 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 53.449 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 53.449 | odd | false | true | false | - |
| lifting-adaptive | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.433 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.412 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.443 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.446 | 53.449 | odd | false | true | false | - |
| lifting-sym | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=12 / H=2, K=2, t=12 | 12.838 | 53.449 | odd | false | true | false | - |
| lifting-sym+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.382 | 53.449 | odd | false | true | false | - |
| lifting-sym+iter | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=3, t=12 / H=2, K=2, t=12 | 12.747 | 53.449 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.380 | 53.449 | odd | false | true | false | - |
| pm-strahler | complete | 5578 / 336 | 69 / 3 | 41 / 1 | 3 / 3 | k=2, t=3, depth=2 / k=2, t=3, depth=2 | 0.402 | 53.449 | odd | false | true | false | - |
| pm-strahler+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.404 | 53.449 | odd | false | true | false | - |
| pm-strahler+iter | complete | 5578 / 336 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.402 | 53.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.471 | 53.449 | odd | false | true | false | - |
| pm-succinct | complete | 5578 / 336 | 54 / 3 | 41 / 1 | 3 / 3 | bits=3, depth=2 / bits=3, depth=2 | 0.470 | 53.449 | odd | false | true | false | - |
| pm-succinct+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.428 | 53.449 | odd | false | true | false | - |
| pm-succinct+iter | complete | 5578 / 336 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.405 | 53.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.413 | 53.449 | odd | false | true | false | - |
| zielonka | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.402 | 53.449 | odd | false | true | false | - |
| zielonka+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 53.449 | odd | false | true | false | - |
| zielonka-sym | complete | 5578 / 336 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.406 | 53.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 5578 / 336 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.404 | 53.449 | odd | false | true | false | - |

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
| pm-strahler | 28 / 2 | 41 / 1 | 27 / 1 | 2.429 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 13 / 2 | 41 / 1 | 15 / 1 | 4.077 / 1.000 | 7 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=5_compact.gm · 209 vertices / 349 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 209 | 349 | 3 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.417 | 53.449 | odd | false | true | false | - |
| lifting+pre | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.396 | 53.449 | odd | false | true | false | - |
| lifting+iter | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.427 | 53.449 | odd | false | true | false | - |
| lifting+pre+iter | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.407 | 53.449 | odd | false | true | false | - |
| lifting-adaptive | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.410 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.419 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.439 | 53.449 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.428 | 53.449 | odd | false | true | false | - |
| lifting-sym | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.426 | 53.449 | odd | false | true | false | - |
| lifting-sym+pre | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.403 | 53.449 | odd | false | true | false | - |
| lifting-sym+iter | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=7 / H=2, K=2, t=7 | 0.412 | 53.449 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=3 / H=1, K=1, t=3 | 0.402 | 53.449 | odd | false | true | false | - |
| pm-strahler | complete | 195 / 14 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.403 | 53.449 | odd | false | true | false | - |
| pm-strahler+pre | complete | 195 / 14 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.402 | 53.449 | odd | false | true | false | - |
| pm-strahler+iter | complete | 195 / 14 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 53.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 195 / 14 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 53.449 | odd | false | true | false | - |
| pm-succinct | complete | 195 / 14 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.405 | 53.449 | odd | false | true | false | - |
| pm-succinct+pre | complete | 195 / 14 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.405 | 53.449 | odd | false | true | false | - |
| pm-succinct+iter | complete | 195 / 14 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 53.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 195 / 14 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.401 | 53.449 | odd | false | true | false | - |
| zielonka | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 53.449 | odd | false | true | false | - |
| zielonka+pre | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.402 | 53.449 | odd | false | true | false | - |
| zielonka-sym | complete | 195 / 14 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.392 | 53.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 195 / 14 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.393 | 53.449 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=6.gm · 14399 vertices / 18701 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 14399 | 18701 | 4 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 65.141 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.388 | 54.449 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 65.238 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.440 | 54.449 | odd | false | true | false | - |
| lifting-adaptive | complete | 13931 / 468 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.454 | 54.449 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.402 | 54.449 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 13931 / 468 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.463 | 54.449 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.436 | 54.449 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 65.293 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 54.449 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 65.199 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.391 | 54.449 | odd | false | true | false | - |
| pm-strahler | complete | 13931 / 468 | 67 / 3 | 50 / 1 | 3 / 3 | k=3, t=4, depth=2 / k=3, t=4, depth=2 | 0.483 | 54.449 | odd | false | true | false | - |
| pm-strahler+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.402 | 54.449 | odd | false | true | false | - |
| pm-strahler+iter | complete | 13931 / 468 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.432 | 54.449 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.412 | 54.449 | odd | false | true | false | - |
| pm-succinct | complete | 13931 / 468 | 67 / 3 | 50 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.475 | 54.449 | odd | false | true | false | - |
| pm-succinct+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.424 | 54.449 | odd | false | true | false | - |
| pm-succinct+iter | complete | 13931 / 468 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.435 | 54.449 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.425 | 54.449 | odd | false | true | false | - |
| zielonka | complete | 13931 / 468 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.445 | 54.449 | odd | false | true | false | - |
| zielonka+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.435 | 54.449 | odd | false | true | false | - |
| zielonka-sym | complete | 13931 / 468 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.456 | 54.449 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 13931 / 468 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.447 | 54.449 | odd | false | true | false | - |

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
| pm-strahler | 17 / 2 | 50 / 1 | 16 / 1 | 3.882 / 1.000 | 8 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 17 / 2 | 50 / 1 | 16 / 1 | 3.882 / 1.000 | 8 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=6_compact.gm · 478 vertices / 801 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 478 | 801 | 3 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.476 | 54.574 | odd | false | true | false | - |
| lifting+pre | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.383 | 54.574 | odd | false | true | false | - |
| lifting+iter | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.486 | 54.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.403 | 54.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 54.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 54.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.395 | 54.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 54.574 | odd | false | true | false | - |
| lifting-sym | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.444 | 54.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 54.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=8 / H=2, K=2, t=8 | 0.455 | 54.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.393 | 54.574 | odd | false | true | false | - |
| pm-strahler | complete | 462 / 16 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.401 | 54.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 462 / 16 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.395 | 54.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 462 / 16 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 54.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 462 / 16 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.403 | 54.574 | odd | false | true | false | - |
| pm-succinct | complete | 462 / 16 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.402 | 54.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 462 / 16 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.391 | 54.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 462 / 16 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.404 | 54.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 462 / 16 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.393 | 54.574 | odd | false | true | false | - |
| zielonka | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.393 | 54.574 | odd | false | true | false | - |
| zielonka+pre | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.402 | 54.574 | odd | false | true | false | - |
| zielonka-sym | complete | 462 / 16 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.381 | 54.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 462 / 16 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.382 | 54.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=7.gm · 35037 vertices / 45534 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 35037 | 45534 | 4 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 168.820 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.429 | 56.949 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 168.945 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.407 | 56.949 | odd | false | true | false | - |
| lifting-adaptive | complete | 34415 / 622 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.505 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.425 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 34415 / 622 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.546 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 56.949 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 169.258 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.532 | 56.949 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 178.508 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.486 | 56.949 | odd | false | true | false | - |
| pm-strahler | complete | 34415 / 622 | 76 / 3 | 59 / 1 | 3 / 3 | k=3, t=4, depth=2 / k=3, t=4, depth=2 | 0.768 | 56.949 | odd | false | true | false | - |
| pm-strahler+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.508 | 56.949 | odd | false | true | false | - |
| pm-strahler+iter | complete | 34415 / 622 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.508 | 56.949 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.443 | 56.949 | odd | false | true | false | - |
| pm-succinct | complete | 34415 / 622 | 76 / 3 | 59 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.578 | 56.949 | odd | false | true | false | - |
| pm-succinct+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.444 | 56.949 | odd | false | true | false | - |
| pm-succinct+iter | complete | 34415 / 622 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.465 | 56.949 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.454 | 56.949 | odd | false | true | false | - |
| zielonka | complete | 34415 / 622 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.465 | 56.949 | odd | false | true | false | - |
| zielonka+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.454 | 56.949 | odd | false | true | false | - |
| zielonka-sym | complete | 34415 / 622 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.506 | 56.949 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 34415 / 622 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.444 | 56.949 | odd | false | true | false | - |

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
| pm-strahler | 17 / 2 | 59 / 1 | 16 / 1 | 4.412 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 17 / 2 | 59 / 1 | 16 / 1 | 4.412 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=7_compact.gm · 1123 vertices / 1891 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1123 | 1891 | 3 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.225 | 56.949 | odd | false | true | false | - |
| lifting+pre | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.372 | 56.949 | odd | false | true | false | - |
| lifting+iter | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 1.226 | 56.949 | odd | false | true | false | - |
| lifting+pre+iter | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.369 | 56.949 | odd | false | true | false | - |
| lifting-adaptive | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.383 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.392 | 56.949 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 56.949 | odd | false | true | false | - |
| lifting-sym | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.832 | 56.949 | odd | false | true | false | - |
| lifting-sym+pre | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.370 | 56.949 | odd | false | true | false | - |
| lifting-sym+iter | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=10 / H=2, K=2, t=10 | 0.831 | 56.949 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.394 | 56.949 | odd | false | true | false | - |
| pm-strahler | complete | 1105 / 18 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.404 | 56.949 | odd | false | true | false | - |
| pm-strahler+pre | complete | 1105 / 18 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.392 | 56.949 | odd | false | true | false | - |
| pm-strahler+iter | complete | 1105 / 18 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.392 | 56.949 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 1105 / 18 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.393 | 56.949 | odd | false | true | false | - |
| pm-succinct | complete | 1105 / 18 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.403 | 56.949 | odd | false | true | false | - |
| pm-succinct+pre | complete | 1105 / 18 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 56.949 | odd | false | true | false | - |
| pm-succinct+iter | complete | 1105 / 18 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.384 | 56.949 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 1105 / 18 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.392 | 56.949 | odd | false | true | false | - |
| zielonka | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.393 | 56.949 | odd | false | true | false | - |
| zielonka+pre | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.391 | 56.949 | odd | false | true | false | - |
| zielonka-sym | complete | 1105 / 18 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.391 | 56.949 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 1105 / 18 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.381 | 56.949 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=8.gm · 82968 vertices / 107716 edges · 20 complete · 4 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 82968 | 107716 | 4 | 1152921504606846973 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 331.887 | - | false | - | - | deadline exceeded |
| lifting+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.478 | 58.574 | odd | false | true | false | - |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.036 | 332.035 | - | false | - | - | deadline exceeded |
| lifting+pre+iter | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.457 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 82172 / 796 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.726 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.463 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 82172 / 796 | 3 / 2 | 1 / 1 | 3 / 2 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.732 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.484 | 58.574 | odd | false | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.032 | 332.773 | - | false | - | - | deadline exceeded |
| lifting-sym+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.996 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.030 | 341.031 | - | false | - | - | deadline exceeded |
| lifting-sym+pre+iter | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.520 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 82172 / 796 | 85 / 3 | 68 / 1 | 3 / 3 | k=3, t=4, depth=2 / k=3, t=4, depth=2 | 1.223 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.560 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 82172 / 796 | 3 / 3 | 1 / 1 | 3 / 3 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.498 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | k=1, t=1, depth=2 / k=1, t=1, depth=2 | 0.483 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 82172 / 796 | 85 / 3 | 68 / 1 | 3 / 3 | bits=4, depth=2 / bits=4, depth=2 | 0.880 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.506 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 82172 / 796 | 9 / 3 | 5 / 1 | 3 / 3 | bits=1, depth=2 / bits=1, depth=2 | 0.516 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | bits=0, depth=2 / bits=0, depth=2 | 0.506 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 82172 / 796 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.537 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.507 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 82172 / 796 | 3 / 2 | 1 / 1 | 3 / 2 | — / — | 0.601 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 82172 / 796 | 0 / 0 | 0 / 0 | 0 / 0 | — / — | 0.475 | 58.574 | odd | false | true | false | - |

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
| pm-strahler | 17 / 2 | 68 / 1 | 19 / 1 | 4.941 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-strahler+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-strahler+iter | 2 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 3 | 3.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct | 17 / 2 | 68 / 1 | 19 / 1 | 4.941 / 1.000 | 9 / 0 | 3 / 3 | 3.000 / 3.000 | 3 / 1 |
| pm-succinct+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| pm-succinct+iter | 4 / 2 | 5 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 3 | 3.000 / 3.000 | 2 / 1 |
| pm-succinct+pre+iter | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |
| zielonka-sym | 2 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 3 / 2 | 3.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 0 | 0.000 / 0.000 | 0 / 0 |

</details>

<details>
<summary>mlsolver/games/CTLStarBinaryCountern=8_compact.gm · 2611 vertices / 4394 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2611 | 4394 | 3 | 1152921504606846972 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 4.366 | 58.574 | odd | false | true | false | - |
| lifting+pre | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.381 | 58.574 | odd | false | true | false | - |
| lifting+iter | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 4.377 | 58.574 | odd | false | true | false | - |
| lifting+pre+iter | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.398 | 58.574 | odd | false | true | false | - |
| lifting-adaptive | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.420 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.372 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+iter | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.372 | 58.574 | odd | false | true | false | - |
| lifting-adaptive+pre+iter | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.370 | 58.574 | odd | false | true | false | - |
| lifting-sym | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.343 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.382 | 58.574 | odd | false | true | false | - |
| lifting-sym+iter | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | H=2, K=2, t=11 / H=2, K=2, t=11 | 2.419 | 58.574 | odd | false | true | false | - |
| lifting-sym+pre+iter | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | H=2, K=2, t=4 / H=1, K=1, t=4 | 0.392 | 58.574 | odd | false | true | false | - |
| pm-strahler | complete | 2591 / 20 | 5 / 5 | 4 / 2 | 2 / 3 | k=2, t=2, depth=1 / k=2, t=2, depth=2 | 0.402 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre | complete | 2591 / 20 | 0 / 5 | 0 / 2 | 0 / 3 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.382 | 58.574 | odd | false | true | false | - |
| pm-strahler+iter | complete | 2591 / 20 | 2 / 3 | 1 / 1 | 2 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.383 | 58.574 | odd | false | true | false | - |
| pm-strahler+pre+iter | complete | 2591 / 20 | 0 / 3 | 0 / 1 | 0 / 3 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.397 | 58.574 | odd | false | true | false | - |
| pm-succinct | complete | 2591 / 20 | 5 / 5 | 4 / 2 | 2 / 3 | bits=2, depth=1 / bits=2, depth=2 | 0.428 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre | complete | 2591 / 20 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.398 | 58.574 | odd | false | true | false | - |
| pm-succinct+iter | complete | 2591 / 20 | 4 / 5 | 3 / 2 | 2 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.383 | 58.574 | odd | false | true | false | - |
| pm-succinct+pre+iter | complete | 2591 / 20 | 0 / 5 | 0 / 2 | 0 / 3 | bits=1, depth=1 / bits=1, depth=2 | 0.387 | 58.574 | odd | false | true | false | - |
| zielonka | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.397 | 58.574 | odd | false | true | false | - |
| zielonka+pre | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.402 | 58.574 | odd | false | true | false | - |
| zielonka-sym | complete | 2591 / 20 | 2 / 2 | 1 / 1 | 2 / 2 | — / — | 0.391 | 58.574 | odd | false | true | false | - |
| zielonka-sym+pre | complete | 2591 / 20 | 0 / 1 | 0 / 1 | 0 / 1 | — / — | 0.382 | 58.574 | odd | false | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-adaptive+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-adaptive+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| lifting-sym+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| lifting-sym+pre+iter | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| pm-strahler | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-strahler+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-strahler+iter | 1 / 2 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 3 | 2.000 / 3.000 | 1 / 1 |
| pm-strahler+pre+iter | 0 / 2 | 0 / 1 | 0 / 1 | 0.000 / 1.000 | 0 / 0 | 0 / 3 | 0.000 / 3.000 | 0 / 1 |
| pm-succinct | 1 / 3 | 4 / 2 | 4 / 2 | 4.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| pm-succinct+iter | 1 / 3 | 3 / 2 | 3 / 2 | 3.000 / 1.333 | 1 / 1 | 2 / 3 | 2.000 / 3.000 | 2 / 2 |
| pm-succinct+pre+iter | 0 / 3 | 0 / 2 | 0 / 2 | 0.000 / 1.333 | 0 / 1 | 0 / 3 | 0.000 / 3.000 | 0 / 2 |
| zielonka | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |
| zielonka-sym | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| zielonka-sym+pre | 0 / 0 | 0 / 1 | 0 / 0 | 0.000 / 0.000 | 0 / 0 | 0 / 1 | 0.000 / 1.000 | 0 / 1 |

</details>

<details>
<summary>mlsolver/games/DemriKillerFormulan=1.gm · 16 vertices / 20 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 16 | 20 | 4 | 49 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.416 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.417 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=1, t=0 / H=2, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | H=3, K=3, t=4 / H=2, K=2, t=4 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=3, K=3, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 16 / 0 | 18 / 0 | 11 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 16 / 0 | 16 / 0 | 10 / 0 | 3 / 0 | k=2, t=2, depth=2 / k=2, t=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 16 / 0 | 17 / 0 | 11 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 16 / 0 | 15 / 0 | 10 / 0 | 3 / 0 | bits=2, depth=2 / bits=2, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 16 / 0 | 3 / 0 | 1 / 0 | 3 / 0 | — / — | 0.432 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 16 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.401 | 58.574 | even | true | true | false | - |

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

<details>
<summary>mlsolver/games/DemriKillerFormulan=1_compact.gm · 8 vertices / 11 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 8 | 11 | 3 | 48 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=1, t=0 / H=2, K=1, t=0 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=3 / H=2, K=2, t=3 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | H=2, K=2, t=2 / H=2, K=2, t=2 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | k=2, t=1, depth=1 / k=2, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=1, depth=1 / k=1, t=1, depth=2 | 0.407 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 8 / 0 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=2 | 0.406 | 58.574 | even | true | true | false | - |
| zielonka | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.405 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 8 / 0 | 2 / 0 | 1 / 0 | 2 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 8 / 0 | 1 / 0 | 1 / 0 | 1 / 0 | — / — | 0.406 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/DemriKillerFormulan=2.gm · 33977 vertices / 48764 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 33977 | 48764 | 13 | 961 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.641 | 1300.332 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.236 | 1081.414 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.702 | 1298.746 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.814 | 1081.199 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 28942 / 5035 | 13 / 7 | 3 / 1 | 8 / 7 | H=8, K=2, t=1 / H=7, K=2, t=1 | 10.769 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 28942 / 5035 | 9 / 6 | 3 / 1 | 4 / 6 | H=7, K=2, t=1 / H=6, K=2, t=1 | 6.902 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 28942 / 5035 | 6 / 0 | 2 / 0 | 4 / 0 | H=8, K=2, t=1 / H=7, K=2, t=1 | 1.312 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 28942 / 5035 | 6 / 0 | 2 / 0 | 4 / 0 | H=7, K=2, t=1 / H=6, K=2, t=1 | 1.000 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.281 | 1300.168 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.902 | 1081.434 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.329 | 1300.496 | - | true | - | - | Solver failed: failed to build the Even host U^8_{15,8} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.893 | 1081.281 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 28942 / 5035 | 728 / 83 | 184 / 13 | 8 / 8 | k=3, t=2, depth=7 / k=3, t=2, depth=7 | 1.054 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 28942 / 5035 | 647 / 70 | 203 / 13 | 7 / 7 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.569 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 28942 / 5035 | 187 / 0 | 42 / 0 | 8 / 0 | k=3, t=2, depth=7 / k=3, t=2, depth=7 | 0.496 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 28942 / 5035 | 218 / 0 | 59 / 0 | 7 / 0 | k=3, t=2, depth=6 / k=3, t=2, depth=6 | 0.516 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 28942 / 5035 | 480 / 79 | 136 / 13 | 8 / 8 | bits=3, depth=7 / bits=3, depth=7 | 0.897 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 28942 / 5035 | 363 / 66 | 127 / 13 | 7 / 7 | bits=3, depth=6 / bits=3, depth=6 | 0.538 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 28942 / 5035 | 180 / 0 | 48 / 0 | 8 / 0 | bits=2, depth=7 / bits=2, depth=7 | 0.496 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 28942 / 5035 | 48 / 0 | 14 / 0 | 7 / 0 | bits=2, depth=6 / bits=2, depth=6 | 0.508 | 58.574 | even | true | true | false | - |
| zielonka | complete | 28942 / 5035 | 11 / 7 | 4 / 1 | 8 / 7 | — / — | 0.519 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 28942 / 5035 | 7 / 6 | 4 / 1 | 4 / 6 | — / — | 0.468 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 28942 / 5035 | 11 / 7 | 4 / 1 | 8 / 7 | — / — | 0.691 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 28942 / 5035 | 7 / 6 | 4 / 1 | 4 / 6 | — / — | 0.473 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 10 / 6 | 3 / 1 | 3 / 1 | 1.200 / 1.000 | 1 / 0 | 3 / 7 | 5.000 / 7.000 | 2 / 1 |
| lifting-adaptive+pre | 6 / 5 | 3 / 1 | 3 / 1 | 1.333 / 1.000 | 1 / 0 | 3 / 6 | 3.667 / 6.000 | 2 / 1 |
| lifting-adaptive+iter | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 4 / 0 | 2 / 0 | 2 / 0 | 1.250 / 0.000 | 1 / 0 | 3 / 0 | 3.500 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 544 / 70 | 184 / 13 | 15 / 6 | 1.336 / 1.171 | 28 / 3 | 8 / 8 | 8.000 / 8.000 | 3 / 2 |
| pm-strahler+pre | 444 / 57 | 203 / 13 | 15 / 6 | 1.455 / 1.211 | 34 / 3 | 7 / 7 | 7.000 / 7.000 | 3 / 2 |
| pm-strahler+iter | 145 / 0 | 42 / 0 | 8 / 0 | 1.283 / 0.000 | 10 / 0 | 8 / 0 | 8.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 159 / 0 | 59 / 0 | 12 / 0 | 1.365 / 0.000 | 10 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| pm-succinct | 344 / 66 | 136 / 13 | 8 / 6 | 1.392 / 1.182 | 65 / 5 | 8 / 8 | 8.000 / 8.000 | 4 / 3 |
| pm-succinct+pre | 236 / 53 | 127 / 13 | 9 / 6 | 1.534 / 1.226 | 54 / 5 | 7 / 7 | 7.000 / 7.000 | 4 / 3 |
| pm-succinct+iter | 132 / 0 | 48 / 0 | 7 / 0 | 1.356 / 0.000 | 24 / 0 | 8 / 0 | 8.000 / 0.000 | 3 / 0 |
| pm-succinct+pre+iter | 34 / 0 | 14 / 0 | 4 / 0 | 1.382 / 0.000 | 7 / 0 | 7 / 0 | 7.000 / 0.000 | 3 / 0 |
| zielonka | 7 / 6 | 3 / 1 | 3 / 1 | 1.429 / 1.000 | 2 / 0 | 3 / 7 | 4.500 / 7.000 | 2 / 1 |
| zielonka+pre | 3 / 5 | 3 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 6 | 3.500 / 6.000 | 2 / 1 |
| zielonka-sym | 7 / 6 | 3 / 1 | 3 / 1 | 1.429 / 1.000 | 2 / 0 | 3 / 7 | 4.500 / 7.000 | 2 / 1 |
| zielonka-sym+pre | 3 / 5 | 3 / 1 | 3 / 1 | 2.000 / 1.000 | 2 / 0 | 3 / 6 | 3.500 / 6.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/DemriKillerFormulan=2_compact.gm · 6831 vertices / 19792 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6831 | 19792 | 8 | 960 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.077 | 904.992 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 246.348 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.078 | 904.934 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.015 | 246.148 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 5560 / 1271 | 8 / 5 | 3 / 1 | 5 / 5 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.724 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 5560 / 1271 | 6 / 4 | 3 / 1 | 3 / 4 | H=4, K=2, t=1 / H=4, K=2, t=1 | 0.558 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 5560 / 1271 | 4 / 0 | 2 / 0 | 3 / 0 | H=5, K=2, t=1 / H=5, K=2, t=1 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 5560 / 1271 | 4 / 0 | 2 / 0 | 3 / 0 | H=4, K=2, t=1 / H=4, K=2, t=1 | 0.433 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.071 | 903.379 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.021 | 259.543 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.073 | 908.383 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.022 | 268.488 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 5560 / 1271 | 33 / 31 | 8 / 6 | 5 / 6 | k=2, t=2, depth=4 / k=2, t=2, depth=5 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 5560 / 1271 | 25 / 25 | 8 / 6 | 4 / 5 | k=2, t=2, depth=3 / k=2, t=2, depth=4 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 5560 / 1271 | 25 / 0 | 6 / 0 | 5 / 0 | k=2, t=1, depth=4 / k=2, t=1, depth=5 | 0.380 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 5560 / 1271 | 19 / 0 | 6 / 0 | 4 / 0 | k=2, t=1, depth=3 / k=2, t=1, depth=4 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 5560 / 1271 | 41 / 53 | 11 / 12 | 5 / 6 | bits=3, depth=4 / bits=3, depth=5 | 0.443 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 5560 / 1271 | 30 / 41 | 11 / 12 | 4 / 5 | bits=3, depth=3 / bits=3, depth=4 | 0.442 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 5560 / 1271 | 13 / 0 | 3 / 0 | 5 / 0 | bits=1, depth=4 / bits=1, depth=5 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 5560 / 1271 | 10 / 0 | 3 / 0 | 4 / 0 | bits=1, depth=3 / bits=1, depth=4 | 0.390 | 58.574 | even | true | true | false | - |
| zielonka | complete | 5560 / 1271 | 8 / 5 | 4 / 1 | 5 / 5 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 5560 / 1271 | 6 / 4 | 4 / 1 | 3 / 4 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 5560 / 1271 | 8 / 5 | 4 / 1 | 5 / 5 | — / — | 0.401 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 5560 / 1271 | 6 / 4 | 4 / 1 | 3 / 4 | — / — | 0.402 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 5 / 4 | 3 / 1 | 3 / 1 | 1.400 / 1.000 | 1 / 0 | 2 / 5 | 3.333 / 5.000 | 2 / 1 |
| lifting-adaptive+pre | 3 / 3 | 3 / 1 | 3 / 1 | 1.667 / 1.000 | 1 / 0 | 2 / 4 | 2.667 / 4.000 | 2 / 1 |
| lifting-adaptive+iter | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 2 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 1 / 0 | 2 / 0 | 2.500 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 25 / 25 | 8 / 6 | 8 / 6 | 1.280 / 1.200 | 1 / 1 | 5 / 6 | 5.000 / 6.000 | 2 / 2 |
| pm-strahler+pre | 17 / 19 | 8 / 6 | 8 / 6 | 1.412 / 1.263 | 1 / 1 | 4 / 5 | 4.000 / 5.000 | 2 / 2 |
| pm-strahler+iter | 19 / 0 | 6 / 0 | 6 / 0 | 1.263 / 0.000 | 1 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 13 / 0 | 6 / 0 | 6 / 0 | 1.385 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| pm-succinct | 30 / 41 | 11 / 12 | 8 / 6 | 1.333 / 1.268 | 3 / 4 | 5 / 6 | 5.000 / 6.000 | 2 / 3 |
| pm-succinct+pre | 19 / 29 | 11 / 12 | 8 / 6 | 1.526 / 1.379 | 3 / 4 | 4 / 5 | 4.000 / 5.000 | 2 / 3 |
| pm-succinct+iter | 10 / 0 | 3 / 0 | 3 / 0 | 1.200 / 0.000 | 1 / 0 | 5 / 0 | 5.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 7 / 0 | 3 / 0 | 3 / 0 | 1.286 / 0.000 | 1 / 0 | 4 / 0 | 4.000 / 0.000 | 2 / 0 |
| zielonka | 4 / 4 | 3 / 1 | 3 / 1 | 1.750 / 1.000 | 2 / 0 | 2 / 5 | 3.000 / 5.000 | 2 / 1 |
| zielonka+pre | 2 / 3 | 3 / 1 | 3 / 1 | 2.500 / 1.000 | 2 / 0 | 2 / 4 | 2.500 / 4.000 | 2 / 1 |
| zielonka-sym | 4 / 4 | 3 / 1 | 3 / 1 | 1.750 / 1.000 | 2 / 0 | 2 / 5 | 3.000 / 5.000 | 2 / 1 |
| zielonka-sym+pre | 2 / 3 | 3 / 1 | 3 / 1 | 2.500 / 1.000 | 2 / 0 | 2 / 4 | 2.500 / 4.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=1.gm · 543 vertices / 717 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 543 | 717 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.517 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.414 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.517 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.432 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.404 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 277 / 266 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.423 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.422 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.402 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 277 / 266 | 24 / 16 | 23 / 15 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 277 / 266 | 6 / 16 | 5 / 15 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 277 / 266 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 277 / 266 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 277 / 266 | 24 / 16 | 23 / 15 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 277 / 266 | 6 / 16 | 5 / 15 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 277 / 266 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 277 / 266 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.390 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 277 / 266 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 277 / 266 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 23 / 15 | 23 / 15 | 23.000 / 15.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 15 | 5 / 15 | 5.000 / 15.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 23 / 15 | 23 / 15 | 23.000 / 15.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 15 | 5 / 15 | 5.000 / 15.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=1_compact.gm · 69 vertices / 149 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 69 | 149 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.407 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.406 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 29 / 40 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.407 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.408 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.397 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=6 / H=1, K=1, t=6 | 0.398 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=5 / H=1, K=1, t=5 | 0.407 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 29 / 40 | 6 / 4 | 5 / 3 | 2 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 29 / 40 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 29 / 40 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 29 / 40 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 29 / 40 | 6 / 4 | 5 / 3 | 2 / 2 | bits=2, depth=1 / bits=2, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 29 / 40 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 29 / 40 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 29 / 40 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| zielonka | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 29 / 40 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 29 / 40 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 5 / 3 | 5 / 3 | 5.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 5 / 3 | 5 / 3 | 5.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=2.gm · 3772 vertices / 5112 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3772 | 5112 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 4.107 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 2.320 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 4.139 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 2.351 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.431 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2505 / 1267 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.412 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.965 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.962 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.975 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.987 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2505 / 1267 | 41 / 23 | 40 / 22 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 0.401 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2505 / 1267 | 6 / 23 | 5 / 22 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2505 / 1267 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2505 / 1267 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2505 / 1267 | 41 / 23 | 40 / 22 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2505 / 1267 | 6 / 23 | 5 / 22 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2505 / 1267 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2505 / 1267 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.393 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2505 / 1267 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2505 / 1267 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.381 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 40 / 22 | 40 / 22 | 40.000 / 22.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 22 | 5 / 22 | 5.000 / 22.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 40 / 22 | 40 / 22 | 40.000 / 22.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 22 | 5 / 22 | 5.000 / 22.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=2_compact.gm · 348 vertices / 933 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 348 | 933 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.436 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.404 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.425 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 239 / 109 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.394 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=8 / H=1, K=1, t=8 | 0.415 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=7 / H=1, K=1, t=7 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 239 / 109 | 8 / 4 | 7 / 3 | 2 / 2 | k=2, t=2, depth=1 / k=2, t=2, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 239 / 109 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 239 / 109 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 239 / 109 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 239 / 109 | 8 / 4 | 7 / 3 | 2 / 2 | bits=2, depth=1 / bits=2, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 239 / 109 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 239 / 109 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 239 / 109 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.405 | 58.574 | even | true | true | false | - |
| zielonka | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 239 / 109 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 239 / 109 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 7 / 3 | 7 / 3 | 7.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 7 / 3 | 7 / 3 | 7.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=3.gm · 6431 vertices / 8516 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6431 | 8516 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 12.932 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 3.465 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 12.984 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 3.525 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.472 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.381 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3263 / 3168 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.410 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.095 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.696 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.130 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.723 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 3263 / 3168 | 57 / 21 | 56 / 20 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 0.420 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3263 / 3168 | 6 / 21 | 5 / 20 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.400 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3263 / 3168 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.390 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3263 / 3168 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3263 / 3168 | 57 / 21 | 56 / 20 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 0.412 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3263 / 3168 | 6 / 21 | 5 / 20 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.402 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3263 / 3168 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3263 / 3168 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.404 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3263 / 3168 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3263 / 3168 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 56 / 20 | 56 / 20 | 56.000 / 20.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 20 | 5 / 20 | 5.000 / 20.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 56 / 20 | 56 / 20 | 56.000 / 20.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 20 | 5 / 20 | 5.000 / 20.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=3_compact.gm · 730 vertices / 1709 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 730 | 1709 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.529 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.465 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.528 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.475 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 330 / 400 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.393 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.435 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.442 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.443 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=9 / H=1, K=1, t=9 | 0.432 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 330 / 400 | 10 / 4 | 9 / 3 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.406 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 330 / 400 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 330 / 400 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.395 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 330 / 400 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 330 / 400 | 10 / 4 | 9 / 3 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 330 / 400 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 330 / 400 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 330 / 400 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| zielonka | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 330 / 400 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 330 / 400 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.394 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 9 / 3 | 9 / 3 | 9.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 9 / 3 | 9 / 3 | 9.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=4.gm · 38075 vertices / 51593 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 38075 | 51593 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 24345 / 13730 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 1.281 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24345 / 13730 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.473 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24345 / 13730 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.849 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24345 / 13730 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.505 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 24345 / 13730 | 91 / 28 | 90 / 27 | 2 / 2 | k=2, t=6, depth=1 / k=2, t=6, depth=1 | 1.065 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24345 / 13730 | 6 / 28 | 5 / 27 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.643 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24345 / 13730 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.553 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24345 / 13730 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.540 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24345 / 13730 | 91 / 28 | 90 / 27 | 2 / 2 | bits=6, depth=1 / bits=6, depth=1 | 0.988 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24345 / 13730 | 6 / 28 | 5 / 27 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.591 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24345 / 13730 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.528 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24345 / 13730 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.529 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24345 / 13730 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.509 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24345 / 13730 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.509 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24345 / 13730 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.531 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24345 / 13730 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.511 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 90 / 27 | 90 / 27 | 90.000 / 27.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 27 | 5 / 27 | 5.000 / 27.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 90 / 27 | 90 / 27 | 90.000 / 27.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 27 | 5 / 27 | 5.000 / 27.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=4_compact.gm · 3195 vertices / 9044 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 3195 | 9044 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 3.100 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.863 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 3.049 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 1.884 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.391 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2201 / 994 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.402 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.895 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.891 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.895 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=11 / H=1, K=1, t=11 | 0.909 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 2201 / 994 | 12 / 4 | 11 / 3 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.423 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2201 / 994 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2201 / 994 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2201 / 994 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.393 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2201 / 994 | 12 / 4 | 11 / 3 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.434 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2201 / 994 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2201 / 994 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.403 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2201 / 994 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.404 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.415 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.403 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2201 / 994 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2201 / 994 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.382 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 11 / 3 | 11 / 3 | 11.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 11 / 3 | 11 / 3 | 11.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=5.gm · 60011 vertices / 79752 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 60011 | 79752 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 31339 / 28672 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 2.151 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 31339 / 28672 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.541 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 31339 / 28672 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 1.295 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 31339 / 28672 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.566 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 31339 / 28672 | 114 / 26 | 113 / 25 | 2 / 2 | k=2, t=6, depth=1 / k=2, t=6, depth=1 | 1.430 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 31339 / 28672 | 6 / 26 | 5 / 25 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 0.747 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 31339 / 28672 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.594 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 31339 / 28672 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.591 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 31339 / 28672 | 114 / 26 | 113 / 25 | 2 / 2 | bits=6, depth=1 / bits=6, depth=1 | 1.428 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 31339 / 28672 | 6 / 26 | 5 / 25 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 0.698 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 31339 / 28672 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.582 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 31339 / 28672 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.573 | 58.574 | even | true | true | false | - |
| zielonka | complete | 31339 / 28672 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.541 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 31339 / 28672 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.540 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 31339 / 28672 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.602 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 31339 / 28672 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.562 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 113 / 25 | 113 / 25 | 113.000 / 25.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 25 | 5 / 25 | 5.000 / 25.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 113 / 25 | 113 / 25 | 113.000 / 25.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 25 | 5 / 25 | 5.000 / 25.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=5_compact.gm · 6346 vertices / 15349 edges · 24 complete</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 6346 | 15349 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 10.312 | 58.574 | even | true | true | false | - |
| lifting+pre | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 6.137 | 58.574 | even | true | true | false | - |
| lifting+iter | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 10.333 | 58.574 | even | true | true | false | - |
| lifting+pre+iter | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 6.150 | 58.574 | even | true | true | false | - |
| lifting-adaptive | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.423 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.401 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 3018 / 3328 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.403 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.392 | 58.574 | even | true | true | false | - |
| lifting-sym | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.174 | 58.574 | even | true | true | false | - |
| lifting-sym+pre | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.179 | 58.574 | even | true | true | false | - |
| lifting-sym+iter | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.194 | 58.574 | even | true | true | false | - |
| lifting-sym+pre+iter | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=2, t=12 / H=1, K=1, t=12 | 3.200 | 58.574 | even | true | true | false | - |
| pm-strahler | complete | 3018 / 3328 | 14 / 4 | 13 / 3 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 0.421 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 3018 / 3328 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.427 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 3018 / 3328 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.394 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 3018 / 3328 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 3018 / 3328 | 14 / 4 | 13 / 3 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.422 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 3018 / 3328 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.390 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 3018 / 3328 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.392 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 3018 / 3328 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.391 | 58.574 | even | true | true | false | - |
| zielonka | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 3018 / 3328 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.392 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 3018 / 3328 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.391 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym+iter | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-sym+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| pm-strahler | 1 / 1 | 13 / 3 | 13 / 3 | 13.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 13 / 3 | 13 / 3 | 13.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=6.gm · 325637 vertices / 441635 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 325637 | 441635 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 97.984 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 79.273 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.010 | 98.242 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 79.230 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 205737 / 119900 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 16.967 | 79.301 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 205737 / 119900 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.384 | 79.031 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 205737 / 119900 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 8.851 | 79.301 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 205737 / 119900 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.560 | 79.230 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 97.918 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 79.176 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 98.242 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 79.305 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 205737 / 119900 | 161 / 33 | 160 / 32 | 2 / 2 | k=2, t=7, depth=1 / k=2, t=7, depth=1 | 14.410 | 85.953 | even | true | true | false | - |
| pm-strahler+pre | complete | 205737 / 119900 | 6 / 33 | 5 / 32 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 2.397 | 79.164 | even | true | true | false | - |
| pm-strahler+iter | complete | 205737 / 119900 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 1.081 | 79.176 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 205737 / 119900 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.967 | 79.246 | even | true | true | false | - |
| pm-succinct | complete | 205737 / 119900 | 161 / 33 | 160 / 32 | 2 / 2 | bits=7, depth=1 / bits=7, depth=1 | 10.700 | 81.117 | even | true | true | false | - |
| pm-succinct+pre | complete | 205737 / 119900 | 6 / 33 | 5 / 32 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 2.033 | 79.109 | even | true | true | false | - |
| pm-succinct+iter | complete | 205737 / 119900 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 1.092 | 79.184 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 205737 / 119900 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.990 | 79.250 | even | true | true | false | - |
| zielonka | complete | 205737 / 119900 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.862 | 79.301 | even | true | true | false | - |
| zielonka+pre | complete | 205737 / 119900 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.833 | 79.238 | even | true | true | false | - |
| zielonka-sym | complete | 205737 / 119900 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 1.146 | 79.176 | even | true | true | false | - |
| zielonka-sym+pre | complete | 205737 / 119900 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.981 | 79.281 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 160 / 32 | 160 / 32 | 160.000 / 32.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 32 | 5 / 32 | 5.000 / 32.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 160 / 32 | 160 / 32 | 160.000 / 32.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 32 | 5 / 32 | 5.000 / 32.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=6_compact.gm · 25971 vertices / 75480 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 25971 | 75480 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 18071 / 7900 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.569 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 18071 / 7900 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 18071 / 7900 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.496 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 18071 / 7900 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.444 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.002 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 18071 / 7900 | 16 / 4 | 15 / 3 | 2 / 2 | k=2, t=3, depth=1 / k=2, t=3, depth=1 | 1.000 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 18071 / 7900 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.590 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 18071 / 7900 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.518 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 18071 / 7900 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.496 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 18071 / 7900 | 16 / 4 | 15 / 3 | 2 / 2 | bits=3, depth=1 / bits=3, depth=1 | 0.844 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 18071 / 7900 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.485 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 18071 / 7900 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.495 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 18071 / 7900 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.455 | 58.574 | even | true | true | false | - |
| zielonka | complete | 18071 / 7900 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 18071 / 7900 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.443 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 18071 / 7900 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.454 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 18071 / 7900 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.445 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 15 / 3 | 15 / 3 | 15.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 15 / 3 | 15 / 3 | 15.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=7.gm · 492107 vertices / 655428 edges · 15 complete · 9 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 492107 | 655428 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.011 | 118.863 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.859 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.734 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.828 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 118.832 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 261611 / 230496 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.786 | 118.863 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 261611 / 230496 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 16.128 | 118.863 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 261611 / 230496 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 1.941 | 118.863 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.014 | 118.773 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.551 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.738 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.012 | 118.742 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 261611 / 230496 | 191 / 31 | 190 / 30 | 2 / 2 | k=2, t=7, depth=1 / k=2, t=7, depth=1 | 18.435 | 127.469 | even | - | - | false | - |
| pm-strahler+pre | complete | 261611 / 230496 | 6 / 31 | 5 / 30 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 3.151 | 118.812 | even | - | - | false | - |
| pm-strahler+iter | complete | 261611 / 230496 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 1.450 | 118.598 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 261611 / 230496 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 1.294 | 118.684 | even | - | - | false | - |
| pm-succinct | complete | 261611 / 230496 | 191 / 31 | 190 / 30 | 2 / 2 | bits=7, depth=1 / bits=7, depth=1 | 15.901 | 120.117 | even | - | - | false | - |
| pm-succinct+pre | complete | 261611 / 230496 | 6 / 31 | 5 / 30 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 2.406 | 118.742 | even | - | - | false | - |
| pm-succinct+iter | complete | 261611 / 230496 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 1.366 | 118.730 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 261611 / 230496 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 1.207 | 118.684 | even | - | - | false | - |
| zielonka | complete | 261611 / 230496 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.980 | 118.727 | even | - | - | false | - |
| zielonka+pre | complete | 261611 / 230496 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.962 | 118.797 | even | - | - | false | - |
| zielonka-sym | complete | 261611 / 230496 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 1.311 | 118.664 | even | - | - | false | - |
| zielonka-sym+pre | complete | 261611 / 230496 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 1.101 | 118.594 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 190 / 30 | 190 / 30 | 190.000 / 30.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 5 / 30 | 5 / 30 | 5.000 / 30.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 190 / 30 | 190 / 30 | 190.000 / 30.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 5 / 30 | 5 / 30 | 5.000 / 30.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=7_compact.gm · 49830 vertices / 122701 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 49830 | 122701 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 24358 / 25472 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.752 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 24358 / 25472 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.484 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 24358 / 25472 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 0.618 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 24358 / 25472 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.494 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 24358 / 25472 | 18 / 4 | 17 / 3 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 1.496 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 24358 / 25472 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 0.663 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 24358 / 25472 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.592 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 24358 / 25472 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.573 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 24358 / 25472 | 18 / 4 | 17 / 3 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 1.336 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 24358 / 25472 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.613 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 24358 / 25472 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 0.633 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 24358 / 25472 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.582 | 58.574 | even | true | true | false | - |
| zielonka | complete | 24358 / 25472 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.540 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 24358 / 25472 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.540 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 24358 / 25472 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.571 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 24358 / 25472 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.550 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 17 / 3 | 17 / 3 | 17.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 17 / 3 | 17 / 3 | 17.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=8.gm · 2544209 vertices / 3452747 edges · 12 complete · 12 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2544209 | 3452747 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.065 | 659.684 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.043 | 612.664 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.065 | 659.934 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.039 | 612.598 | - | - | - | - | deadline exceeded |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.023 | 612.734 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | complete | 1598025 / 946184 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 10.509 | 612.547 | even | - | - | false | - |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.026 | 612.672 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | complete | 1598025 / 946184 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 10.480 | 612.625 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.078 | 659.816 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.046 | 612.734 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.067 | 658.738 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.042 | 612.547 | - | - | - | - | deadline exceeded |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.056 | 612.410 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | complete | 1598025 / 946184 | 6 / 38 | 5 / 37 | 2 / 2 | k=2, t=5, depth=1 / k=2, t=5, depth=1 | 19.371 | 612.547 | even | - | - | false | - |
| pm-strahler+iter | complete | 1598025 / 946184 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 5.957 | 612.555 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1598025 / 946184 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 4.958 | 612.559 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.035 | 612.555 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | complete | 1598025 / 946184 | 6 / 38 | 5 / 37 | 2 / 2 | bits=5, depth=1 / bits=5, depth=1 | 14.628 | 612.555 | even | - | - | false | - |
| pm-succinct+iter | complete | 1598025 / 946184 | 4 / 0 | 3 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 6.173 | 612.602 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1598025 / 946184 | 4 / 4 | 3 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 4.949 | 612.684 | even | - | - | false | - |
| zielonka | complete | 1598025 / 946184 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 3.975 | 612.461 | even | - | - | false | - |
| zielonka+pre | complete | 1598025 / 946184 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 3.631 | 612.719 | even | - | - | false | - |
| zielonka-sym | complete | 1598025 / 946184 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 6.346 | 612.609 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1598025 / 946184 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 4.908 | 612.738 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | 1 / 1 | 5 / 37 | 5 / 37 | 5.000 / 37.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | 1 / 1 | 5 / 37 | 5 / 37 | 5.000 / 37.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 3 / 0 | 3 / 0 | 3.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 3 / 3 | 3 / 3 | 3.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLLimitClosuren=8_compact.gm · 196527 vertices / 580276 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 196527 | 580276 | 2 | 1 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 63.598 | - | - | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 63.750 | - | - | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.008 | 63.617 | - | - | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.006 | 63.562 | - | - | - | - | deadline exceeded |
| lifting-adaptive | complete | 137735 / 58792 | 3 / 1 | 2 / 1 | 2 / 1 | H=2, K=2, t=1 / H=1, K=1, t=1 | 2.085 | 63.621 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 137735 / 58792 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.821 | 63.754 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 137735 / 58792 | 2 / 0 | 1 / 0 | 2 / 0 | H=2, K=2, t=1 / H=1, K=1, t=1 | 1.398 | 63.754 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 137735 / 58792 | 2 / 1 | 1 / 1 | 2 / 1 | H=2, K=1, t=0 / H=1, K=1, t=0 | 0.850 | 63.688 | even | - | - | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.007 | 63.621 | - | - | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 63.621 | - | - | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.009 | 63.730 | - | - | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.005 | 63.730 | - | - | - | - | deadline exceeded |
| pm-strahler | complete | 137735 / 58792 | 20 / 4 | 19 / 3 | 2 / 2 | k=2, t=4, depth=1 / k=2, t=4, depth=1 | 13.492 | 63.617 | even | - | - | false | - |
| pm-strahler+pre | complete | 137735 / 58792 | 3 / 4 | 2 / 3 | 2 / 2 | k=2, t=1, depth=1 / k=2, t=1, depth=1 | 1.582 | 63.422 | even | - | - | false | - |
| pm-strahler+iter | complete | 137735 / 58792 | 2 / 0 | 1 / 0 | 2 / 0 | k=1, t=2, depth=1 / k=1, t=2, depth=1 | 0.896 | 63.500 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 137735 / 58792 | 2 / 2 | 1 / 1 | 2 / 2 | k=1, t=1, depth=1 / k=1, t=1, depth=1 | 0.835 | 63.570 | even | - | - | false | - |
| pm-succinct | complete | 137735 / 58792 | 20 / 4 | 19 / 3 | 2 / 2 | bits=4, depth=1 / bits=4, depth=1 | 9.940 | 63.500 | even | - | - | false | - |
| pm-succinct+pre | complete | 137735 / 58792 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 1.253 | 63.559 | even | - | - | false | - |
| pm-succinct+iter | complete | 137735 / 58792 | 3 / 0 | 2 / 0 | 2 / 0 | bits=1, depth=1 / bits=1, depth=1 | 1.282 | 63.555 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 137735 / 58792 | 3 / 4 | 2 / 3 | 2 / 2 | bits=1, depth=1 / bits=1, depth=1 | 0.847 | 63.562 | even | - | - | false | - |
| zielonka | complete | 137735 / 58792 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.705 | 63.613 | even | - | - | false | - |
| zielonka+pre | complete | 137735 / 58792 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.682 | 63.609 | even | - | - | false | - |
| zielonka-sym | complete | 137735 / 58792 | 3 / 1 | 2 / 1 | 2 / 1 | — / — | 0.774 | 63.754 | even | - | - | false | - |
| zielonka-sym+pre | complete | 137735 / 58792 | 2 / 1 | 1 / 1 | 2 / 1 | — / — | 0.688 | 63.625 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| lifting-adaptive+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-adaptive+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| lifting-adaptive+pre+iter | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 1 / 1 | 19 / 3 | 19 / 3 | 19.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-strahler+iter | 1 / 0 | 1 / 0 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 |
| pm-strahler+pre+iter | 1 / 1 | 1 / 1 | 1 / 1 | 1.000 / 1.000 | 0 / 0 | 2 / 2 | 2.000 / 2.000 | 1 / 1 |
| pm-succinct | 1 / 1 | 19 / 3 | 19 / 3 | 19.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+pre | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| pm-succinct+iter | 1 / 0 | 2 / 0 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 0 | 2.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 1 / 1 | 2 / 3 | 2 / 3 | 2.000 / 3.000 | 1 / 1 | 2 / 2 | 2.000 / 2.000 | 2 / 2 |
| zielonka | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |
| zielonka-sym | 1 / 0 | 2 / 1 | 2 / 0 | 2.000 / 0.000 | 1 / 0 | 2 / 1 | 2.000 / 1.000 | 2 / 1 |
| zielonka-sym+pre | 1 / 0 | 1 / 1 | 1 / 0 | 1.000 / 0.000 | 0 / 0 | 2 / 1 | 2.000 / 1.000 | 1 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarLimitClosuren=1.gm · 174667 vertices / 248994 edges · 11 complete · 5 timeout · 8 out of memory · REFERENCE MISMATCH</summary>

Reference mismatches: pm-strahler+pre, pm-strahler+iter, pm-strahler+pre+iter, pm-succinct, pm-succinct+pre, pm-succinct+iter, pm-succinct+pre+iter, zielonka, zielonka+pre, zielonka-sym, zielonka-sym+pre.

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 174667 | 248994 | 17 | 20890720927747 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.288 | 1119.297 | - | false | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.255 | 1119.691 | - | false | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.238 | 1119.668 | - | false | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.485 | 1119.625 | - | false | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | false | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.223 | 1119.492 | - | false | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.179 | 1119.680 | - | false | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.196 | 1119.422 | - | false | - | - | Solver failed: failed to build the Even host U^10_{17,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.180 | 1119.762 | - | false | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | false | - | - | deadline exceeded |
| pm-strahler+pre | complete | 148284 / 26383 | 422 / 749 | 100 / 131 | 9 / 9 | k=3, t=2, depth=8 / k=3, t=2, depth=8 | 3.620 | 58.574 | even | false | false | false | - |
| pm-strahler+iter | complete | 148284 / 26383 | 260 / 0 | 55 / 0 | 10 / 0 | k=3, t=3, depth=9 / k=3, t=3, depth=9 | 1.238 | 58.574 | even | false | false | false | - |
| pm-strahler+pre+iter | complete | 148284 / 26383 | 205 / 0 | 55 / 0 | 9 / 0 | k=3, t=3, depth=8 / k=3, t=3, depth=8 | 1.247 | 58.574 | even | false | false | false | - |
| pm-succinct | complete | 148284 / 26383 | 371 / 1012 | 71 / 159 | 10 / 10 | bits=3, depth=9 / bits=3, depth=9 | 9.921 | 58.574 | even | false | false | false | - |
| pm-succinct+pre | complete | 148284 / 26383 | 263 / 853 | 63 / 159 | 9 / 9 | bits=3, depth=8 / bits=3, depth=8 | 2.316 | 58.574 | even | false | false | false | - |
| pm-succinct+iter | complete | 148284 / 26383 | 288 / 183 | 59 / 24 | 10 / 10 | bits=2, depth=9 / bits=2, depth=9 | 0.924 | 58.574 | even | false | false | false | - |
| pm-succinct+pre+iter | complete | 148284 / 26383 | 234 / 159 | 59 / 24 | 9 / 9 | bits=2, depth=8 / bits=2, depth=8 | 0.882 | 58.574 | even | false | false | false | - |
| zielonka | complete | 148284 / 26383 | 25 / 6 | 11 / 1 | 10 / 6 | — / — | 1.005 | 58.574 | even | false | false | false | - |
| zielonka+pre | complete | 148284 / 26383 | 16 / 6 | 8 / 1 | 7 / 6 | — / — | 0.948 | 58.574 | even | false | false | false | - |
| zielonka-sym | complete | 148284 / 26383 | 25 / 6 | 11 / 1 | 10 / 6 | — / — | 1.896 | 58.574 | even | false | false | false | - |
| zielonka-sym+pre | complete | 148284 / 26383 | 16 / 6 | 8 / 1 | 7 / 6 | — / — | 1.580 | 58.574 | even | false | false | false | - |

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
| pm-strahler+pre | 322 / 618 | 100 / 131 | 13 / 15 | 1.307 / 1.210 | 25 / 17 | 9 / 9 | 9.000 / 9.000 | 3 / 3 |
| pm-strahler+iter | 205 / 0 | 55 / 0 | 15 / 0 | 1.263 / 0.000 | 15 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 150 / 0 | 55 / 0 | 15 / 0 | 1.360 / 0.000 | 15 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct | 300 / 853 | 71 / 159 | 7 / 15 | 1.233 / 1.185 | 38 / 51 | 10 / 10 | 10.000 / 10.000 | 3 / 4 |
| pm-succinct+pre | 200 / 694 | 63 / 159 | 7 / 15 | 1.310 / 1.228 | 32 / 51 | 9 / 9 | 9.000 / 9.000 | 3 / 4 |
| pm-succinct+iter | 229 / 159 | 59 / 24 | 7 / 7 | 1.253 / 1.145 | 33 / 7 | 10 / 10 | 10.000 / 10.000 | 3 / 3 |
| pm-succinct+pre+iter | 175 / 135 | 59 / 24 | 7 / 7 | 1.331 / 1.170 | 30 / 7 | 9 / 9 | 9.000 / 9.000 | 3 / 3 |
| zielonka | 14 / 5 | 5 / 1 | 3 / 1 | 1.714 / 1.000 | 7 / 0 | 4 / 6 | 5.727 / 6.000 | 3 / 1 |
| zielonka+pre | 8 / 5 | 4 / 1 | 3 / 1 | 1.875 / 1.000 | 5 / 0 | 4 / 6 | 5.625 / 6.000 | 2 / 1 |
| zielonka-sym | 14 / 5 | 5 / 1 | 3 / 1 | 1.714 / 1.000 | 7 / 0 | 4 / 6 | 5.727 / 6.000 | 3 / 1 |
| zielonka-sym+pre | 8 / 5 | 4 / 1 | 3 / 1 | 1.875 / 1.000 | 5 / 0 | 4 / 6 | 5.625 / 6.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarLimitClosuren=1_compact.gm · 9585 vertices / 101651 edges · 16 complete · 8 out of memory · REFERENCE MISMATCH</summary>

Reference mismatches: lifting-adaptive, lifting-adaptive+pre, lifting-adaptive+iter, lifting-adaptive+pre+iter, pm-strahler, pm-strahler+pre, pm-strahler+iter, pm-strahler+pre+iter, pm-succinct, pm-succinct+pre, pm-succinct+iter, pm-succinct+pre+iter, zielonka, zielonka+pre, zielonka-sym, zielonka-sym+pre.

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 9585 | 101651 | 13 | 20890720927746 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.317 | 1209.480 | - | false | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.285 | 1209.441 | - | false | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.304 | 1209.359 | - | false | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.120 | 1209.473 | - | false | - | - | (error text not recorded) |
| lifting-adaptive | complete | 8276 / 1309 | 31 / 6 | 10 / 1 | 7 / 6 | H=7, K=2, t=1 / H=7, K=2, t=1 | 2.832 | 58.574 | even | false | false | false | - |
| lifting-adaptive+pre | complete | 8276 / 1309 | 28 / 6 | 10 / 1 | 6 / 6 | H=7, K=2, t=1 / H=7, K=2, t=1 | 2.407 | 58.574 | even | false | false | false | - |
| lifting-adaptive+iter | complete | 8276 / 1309 | 28 / 0 | 10 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 1.052 | 58.574 | even | false | false | false | - |
| lifting-adaptive+pre+iter | complete | 8276 / 1309 | 25 / 0 | 9 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.970 | 58.574 | even | false | false | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.178 | 1209.480 | - | false | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.129 | 1209.500 | - | false | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.118 | 1209.367 | - | false | - | - | Solver failed: failed to build the Even host U^7_{13,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.009 | 1209.492 | - | false | - | - | (error text not recorded) |
| pm-strahler | complete | 8276 / 1309 | 146 / 36 | 34 / 5 | 7 / 8 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 12.739 | 58.574 | even | false | false | false | - |
| pm-strahler+pre | complete | 8276 / 1309 | 140 / 36 | 33 / 5 | 7 / 8 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 11.404 | 58.574 | even | false | false | false | - |
| pm-strahler+iter | complete | 8276 / 1309 | 62 / 0 | 17 / 0 | 7 / 0 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 0.471 | 58.574 | even | false | false | false | - |
| pm-strahler+pre+iter | complete | 8276 / 1309 | 62 / 0 | 17 / 0 | 7 / 0 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 0.463 | 58.574 | even | false | false | false | - |
| pm-succinct | complete | 8276 / 1309 | 77 / 44 | 17 / 7 | 7 / 8 | bits=2, depth=6 / bits=2, depth=7 | 7.077 | 58.574 | even | false | false | false | - |
| pm-succinct+pre | complete | 8276 / 1309 | 86 / 44 | 19 / 7 | 7 / 8 | bits=2, depth=6 / bits=2, depth=7 | 6.332 | 58.574 | even | false | false | false | - |
| pm-succinct+iter | complete | 8276 / 1309 | 45 / 0 | 10 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.597 | 58.574 | even | false | false | false | - |
| pm-succinct+pre+iter | complete | 8276 / 1309 | 45 / 0 | 10 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.574 | 58.574 | even | false | false | false | - |
| zielonka | complete | 8276 / 1309 | 22 / 6 | 11 / 1 | 7 / 6 | — / — | 0.452 | 58.574 | even | false | false | false | - |
| zielonka+pre | complete | 8276 / 1309 | 15 / 6 | 8 / 1 | 6 / 6 | — / — | 0.432 | 58.574 | even | false | false | false | - |
| zielonka-sym | complete | 8276 / 1309 | 22 / 6 | 11 / 1 | 7 / 6 | — / — | 0.462 | 58.574 | even | false | false | false | - |
| zielonka-sym+pre | complete | 8276 / 1309 | 15 / 6 | 8 / 1 | 6 / 6 | — / — | 0.451 | 58.574 | even | false | false | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 21 / 5 | 9 / 1 | 4 / 1 | 1.429 / 1.000 | 4 / 0 | 4 / 6 | 5.100 / 6.000 | 2 / 1 |
| lifting-adaptive+pre | 18 / 5 | 9 / 1 | 4 / 1 | 1.500 / 1.000 | 4 / 0 | 4 / 6 | 4.800 / 6.000 | 2 / 1 |
| lifting-adaptive+iter | 18 / 0 | 9 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 4.800 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 16 / 0 | 8 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 4.889 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | 112 / 31 | 34 / 5 | 13 / 5 | 1.295 / 1.129 | 5 / 1 | 7 / 8 | 7.000 / 8.000 | 2 / 2 |
| pm-strahler+pre | 107 / 31 | 33 / 5 | 13 / 5 | 1.299 / 1.129 | 5 / 1 | 7 / 8 | 7.000 / 8.000 | 2 / 2 |
| pm-strahler+iter | 45 / 0 | 17 / 0 | 9 / 0 | 1.356 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 45 / 0 | 17 / 0 | 9 / 0 | 1.356 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | 60 / 37 | 17 / 7 | 5 / 3 | 1.267 / 1.162 | 8 / 3 | 7 / 8 | 7.000 / 8.000 | 3 / 2 |
| pm-succinct+pre | 67 / 37 | 19 / 7 | 5 / 3 | 1.269 / 1.162 | 9 / 3 | 7 / 8 | 7.000 / 8.000 | 3 / 2 |
| pm-succinct+iter | 35 / 0 | 10 / 0 | 3 / 0 | 1.257 / 0.000 | 5 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 35 / 0 | 10 / 0 | 3 / 0 | 1.257 / 0.000 | 5 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 11 / 5 | 5 / 1 | 3 / 1 | 1.909 / 1.000 | 7 / 0 | 3 / 6 | 4.545 / 6.000 | 3 / 1 |
| zielonka+pre | 7 / 5 | 4 / 1 | 3 / 1 | 2.000 / 1.000 | 5 / 0 | 3 / 6 | 4.625 / 6.000 | 2 / 1 |
| zielonka-sym | 11 / 5 | 5 / 1 | 3 / 1 | 1.909 / 1.000 | 7 / 0 | 3 / 6 | 4.545 / 6.000 | 3 / 1 |
| zielonka-sym+pre | 7 / 5 | 4 / 1 | 3 / 1 | 2.000 / 1.000 | 5 / 0 | 3 / 6 | 4.625 / 6.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarLimitClosuren=2.gm · 1167042 vertices / 1638060 edges · 8 complete · 8 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1167042 | 1638060 | 17 | 6473924464345091 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 3.161 | 1151.148 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.105 | 1537.703 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.099 | 1154.914 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.065 | 1537.625 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | timeout | - / - | - / - | - / - | - / - | - / - | 30.018 | 298.297 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.017 | 298.234 | - | - | - | - | deadline exceeded |
| lifting-adaptive+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.016 | 298.156 | - | - | - | - | deadline exceeded |
| lifting-adaptive+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.019 | 298.297 | - | - | - | - | deadline exceeded |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 3.082 | 1150.977 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 4.248 | 1537.645 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 3.133 | 1154.910 | - | - | - | - | Solver failed: failed to build the Even host U^10_{20,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 4.054 | 1537.688 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.024 | 298.102 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.025 | 298.113 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 1099594 / 67448 | 146 / 0 | 27 / 0 | 10 / 0 | k=4, t=3, depth=9 / k=4, t=3, depth=9 | 9.403 | 298.113 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 1099594 / 67448 | 119 / 0 | 27 / 0 | 9 / 0 | k=4, t=3, depth=8 / k=4, t=3, depth=8 | 9.488 | 298.098 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 298.156 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.028 | 298.168 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 1099594 / 67448 | 0 / 908 | 0 / 189 | 0 / 10 | bits=4, depth=9 / bits=4, depth=9 | 6.223 | 298.113 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 1099594 / 67448 | 0 / 719 | 0 / 189 | 0 / 9 | bits=4, depth=8 / bits=4, depth=8 | 6.113 | 298.117 | even | - | - | false | - |
| zielonka | complete | 1099594 / 67448 | 25 / 6 | 11 / 1 | 10 / 6 | — / — | 4.728 | 298.234 | even | - | - | false | - |
| zielonka+pre | complete | 1099594 / 67448 | 16 / 6 | 8 / 1 | 7 / 6 | — / — | 3.884 | 298.156 | even | - | - | false | - |
| zielonka-sym | complete | 1099594 / 67448 | 25 / 6 | 11 / 1 | 10 / 6 | — / — | 9.697 | 298.164 | even | - | - | false | - |
| zielonka-sym+pre | complete | 1099594 / 67448 | 16 / 6 | 8 / 1 | 7 / 6 | — / — | 7.114 | 298.191 | even | - | - | false | - |

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
| pm-strahler+iter | 119 / 0 | 27 / 0 | 15 / 0 | 1.218 / 0.000 | 5 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-strahler+pre+iter | 92 / 0 | 27 / 0 | 15 / 0 | 1.283 / 0.000 | 5 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 0 / 719 | 0 / 189 | 0 / 27 | 0.000 / 1.261 | 0 / 53 | 0 / 10 | 0.000 / 10.000 | 0 / 4 |
| pm-succinct+pre+iter | 0 / 530 | 0 / 189 | 0 / 27 | 0.000 / 1.355 | 0 / 53 | 0 / 9 | 0.000 / 9.000 | 0 / 4 |
| zielonka | 14 / 5 | 5 / 1 | 3 / 1 | 1.714 / 1.000 | 7 / 0 | 4 / 6 | 5.727 / 6.000 | 3 / 1 |
| zielonka+pre | 8 / 5 | 4 / 1 | 3 / 1 | 1.875 / 1.000 | 5 / 0 | 4 / 6 | 5.625 / 6.000 | 2 / 1 |
| zielonka-sym | 14 / 5 | 5 / 1 | 3 / 1 | 1.714 / 1.000 | 7 / 0 | 4 / 6 | 5.727 / 6.000 | 3 / 1 |
| zielonka-sym+pre | 8 / 5 | 4 / 1 | 3 / 1 | 1.875 / 1.000 | 5 / 0 | 4 / 6 | 5.625 / 6.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarLimitClosuren=2_compact.gm · 62953 vertices / 572688 edges · 12 complete · 4 timeout · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 62953 | 572688 | 13 | 6473924464345090 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.536 | 1301.613 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.590 | 1301.789 | - | - | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.586 | 1301.750 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.612 | 1301.703 | - | - | - | - | (error text not recorded) |
| lifting-adaptive | complete | 60472 / 2481 | 31 / 6 | 10 / 1 | 7 / 6 | H=7, K=2, t=1 / H=7, K=2, t=1 | 9.622 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre | complete | 60472 / 2481 | 28 / 6 | 10 / 1 | 6 / 6 | H=7, K=2, t=1 / H=7, K=2, t=1 | 5.759 | 58.574 | even | - | - | false | - |
| lifting-adaptive+iter | complete | 60472 / 2481 | 28 / 0 | 10 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 4.276 | 58.574 | even | - | - | false | - |
| lifting-adaptive+pre+iter | complete | 60472 / 2481 | 25 / 0 | 9 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 3.745 | 58.574 | even | - | - | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.371 | 1301.484 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.504 | 1301.758 | - | - | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.444 | 1301.684 | - | - | - | - | Solver failed: failed to build the Even host U^7_{15,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.463 | 1301.797 | - | - | - | - | (error text not recorded) |
| pm-strahler | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.003 | 58.574 | - | - | - | - | deadline exceeded |
| pm-strahler+iter | complete | 60472 / 2481 | 146 / 0 | 37 / 0 | 7 / 0 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 1.569 | 58.574 | even | - | - | false | - |
| pm-strahler+pre+iter | complete | 60472 / 2481 | 72 / 0 | 20 / 0 | 7 / 0 | k=2, t=2, depth=6 / k=2, t=2, depth=7 | 0.975 | 58.574 | even | - | - | false | - |
| pm-succinct | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.004 | 58.574 | - | - | - | - | deadline exceeded |
| pm-succinct+iter | complete | 60472 / 2481 | 43 / 0 | 9 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 1.402 | 58.574 | even | - | - | false | - |
| pm-succinct+pre+iter | complete | 60472 / 2481 | 43 / 0 | 9 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.966 | 58.574 | even | - | - | false | - |
| zielonka | complete | 60472 / 2481 | 22 / 6 | 11 / 1 | 7 / 6 | — / — | 0.711 | 58.574 | even | - | - | false | - |
| zielonka+pre | complete | 60472 / 2481 | 15 / 6 | 8 / 1 | 6 / 6 | — / — | 0.711 | 58.574 | even | - | - | false | - |
| zielonka-sym | complete | 60472 / 2481 | 22 / 6 | 11 / 1 | 7 / 6 | — / — | 0.849 | 58.574 | even | - | - | false | - |
| zielonka-sym+pre | complete | 60472 / 2481 | 15 / 6 | 8 / 1 | 6 / 6 | — / — | 0.797 | 58.574 | even | - | - | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 21 / 5 | 9 / 1 | 4 / 1 | 1.429 / 1.000 | 4 / 0 | 4 / 6 | 5.100 / 6.000 | 2 / 1 |
| lifting-adaptive+pre | 18 / 5 | 9 / 1 | 4 / 1 | 1.500 / 1.000 | 4 / 0 | 4 / 6 | 4.800 / 6.000 | 2 / 1 |
| lifting-adaptive+iter | 18 / 0 | 9 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 4.800 / 0.000 | 2 / 0 |
| lifting-adaptive+pre+iter | 16 / 0 | 8 / 0 | 4 / 0 | 1.500 / 0.000 | 4 / 0 | 4 / 0 | 4.889 / 0.000 | 2 / 0 |
| lifting-sym | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-sym+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-strahler+iter | 109 / 0 | 37 / 0 | 14 / 0 | 1.330 / 0.000 | 5 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-strahler+pre+iter | 52 / 0 | 20 / 0 | 13 / 0 | 1.365 / 0.000 | 3 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| pm-succinct+iter | 34 / 0 | 9 / 0 | 3 / 0 | 1.235 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 34 / 0 | 9 / 0 | 3 / 0 | 1.235 / 0.000 | 4 / 0 | 7 / 0 | 7.000 / 0.000 | 2 / 0 |
| zielonka | 11 / 5 | 5 / 1 | 3 / 1 | 1.909 / 1.000 | 7 / 0 | 3 / 6 | 4.545 / 6.000 | 3 / 1 |
| zielonka+pre | 7 / 5 | 4 / 1 | 3 / 1 | 2.000 / 1.000 | 5 / 0 | 3 / 6 | 4.625 / 6.000 | 2 / 1 |
| zielonka-sym | 11 / 5 | 5 / 1 | 3 / 1 | 1.909 / 1.000 | 7 / 0 | 3 / 6 | 4.545 / 6.000 | 3 / 1 |
| zielonka-sym+pre | 7 / 5 | 4 / 1 | 3 / 1 | 2.000 / 1.000 | 5 / 0 | 3 / 6 | 4.625 / 6.000 | 2 / 1 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=1.gm · 36735 vertices / 51267 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 36735 | 51267 | 17 | 1168231104515 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.433 | 1300.422 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.966 | 1081.930 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.432 | 1300.711 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 1.874 | 1081.883 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 36735 / 0 | 21 / 0 | 3 / 0 | 10 / 0 | H=10, K=2, t=1 / H=9, K=2, t=1 | 6.405 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 36735 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 2.608 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 36735 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=10, K=2, t=1 / H=9, K=2, t=1 | 2.792 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 36735 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 1.137 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.307 | 1300.508 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 1.875 | 1082.055 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.276 | 1300.461 | - | true | - | - | Solver failed: failed to build the Even host U^10_{15,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.027 | 1081.934 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 36735 / 0 | 248 / 0 | 41 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 0.537 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 36735 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 0.506 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 36735 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 0.486 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 36735 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 0.466 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 36735 / 0 | 256 / 0 | 45 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 0.579 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 36735 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 0.517 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 36735 / 0 | 86 / 0 | 16 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 0.476 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 36735 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 0.455 | 58.574 | even | true | true | false | - |
| zielonka | complete | 36735 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 0.455 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 36735 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 0.455 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 36735 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 0.567 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 36735 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 0.503 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 18 / 0 | 3 / 0 | 3 / 0 | 1.111 / 0.000 | 1 / 0 | 6 / 0 | 7.667 / 0.000 | 2 / 0 |
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
| pm-succinct | 211 / 0 | 45 / 0 | 5 / 0 | 1.209 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 70 / 0 | 16 / 0 | 3 / 0 | 1.214 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=1_compact.gm · 1264 vertices / 7531 edges · 16 complete · 8 timeout</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 1264 | 7531 | 13 | 1168231104514 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | timeout | - / - | - / - | - / - | - / - | - / - | 31.130 | 1741.465 | - | true | - | - | deadline exceeded |
| lifting+pre | timeout | - / - | - / - | - / - | - / - | - / - | 31.229 | 1735.527 | - | true | - | - | deadline exceeded |
| lifting+iter | timeout | - / - | - / - | - / - | - / - | - / - | 31.228 | 1743.598 | - | true | - | - | deadline exceeded |
| lifting+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.143 | 1709.059 | - | true | - | - | deadline exceeded |
| lifting-adaptive | complete | 1264 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 10.964 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 1264 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 10.924 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 1264 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.477 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 1264 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.424 | 58.574 | even | true | true | false | - |
| lifting-sym | timeout | - / - | - / - | - / - | - / - | - / - | 30.148 | 1775.977 | - | true | - | - | deadline exceeded |
| lifting-sym+pre | timeout | - / - | - / - | - / - | - / - | - / - | 30.148 | 1774.406 | - | true | - | - | deadline exceeded |
| lifting-sym+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.145 | 1771.223 | - | true | - | - | deadline exceeded |
| lifting-sym+pre+iter | timeout | - / - | - / - | - / - | - / - | - / - | 30.144 | 1771.914 | - | true | - | - | deadline exceeded |
| pm-strahler | complete | 1264 / 0 | 30 / 0 | 5 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 1.542 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 1264 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.464 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 1264 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.393 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 1264 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.381 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 1264 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 1264 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.404 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 1264 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.382 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 1264 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.381 | 58.574 | even | true | true | false | - |
| zielonka | complete | 1264 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 1264 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.371 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 1264 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.381 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 1264 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.383 | 58.574 | even | true | true | false | - |

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
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=2.gm · 94631 vertices / 130441 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 94631 | 130441 | 17 | 20890720927747 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.886 | 1337.914 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.928 | 1338.180 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.804 | 1337.648 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.644 | 1338.125 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 94631 / 0 | 21 / 0 | 3 / 0 | 10 / 0 | H=10, K=2, t=1 / H=9, K=2, t=1 | 17.424 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 94631 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 7.103 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 94631 / 0 | 12 / 0 | 2 / 0 | 7 / 0 | H=10, K=2, t=1 / H=9, K=2, t=1 | 7.376 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 94631 / 0 | 6 / 0 | 1 / 0 | 6 / 0 | H=9, K=2, t=1 / H=8, K=2, t=1 | 2.742 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.838 | 1338.195 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.715 | 1338.262 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.673 | 1337.660 | - | true | - | - | Solver failed: failed to build the Even host U^10_{16,10} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.673 | 1338.199 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 94631 / 0 | 248 / 0 | 41 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 0.733 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 94631 / 0 | 159 / 0 | 33 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 0.671 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 94631 / 0 | 192 / 0 | 33 / 0 | 10 / 0 | k=2, t=1, depth=9 / k=2, t=1, depth=9 | 0.610 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 94631 / 0 | 143 / 0 | 31 / 0 | 9 / 0 | k=2, t=1, depth=8 / k=2, t=1, depth=8 | 0.600 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 94631 / 0 | 257 / 0 | 46 / 0 | 10 / 0 | bits=2, depth=9 / bits=2, depth=9 | 0.867 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 94631 / 0 | 126 / 0 | 25 / 0 | 9 / 0 | bits=2, depth=8 / bits=2, depth=8 | 0.712 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 94631 / 0 | 95 / 0 | 17 / 0 | 10 / 0 | bits=1, depth=9 / bits=1, depth=9 | 0.608 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 94631 / 0 | 81 / 0 | 17 / 0 | 9 / 0 | bits=1, depth=8 / bits=1, depth=8 | 0.545 | 58.574 | even | true | true | false | - |
| zielonka | complete | 94631 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 0.557 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 94631 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 0.547 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 94631 / 0 | 18 / 0 | 5 / 0 | 10 / 0 | — / — | 0.845 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 94631 / 0 | 10 / 0 | 4 / 0 | 7 / 0 | — / — | 0.753 | 58.574 | even | true | true | false | - |

| Backend | internal_nodes E / O | width E / O | max_arity E / O | mean_internal_arity E / O | branching_nodes E / O | min_leaf_depth E / O | mean_leaf_depth E / O | strahler E / O |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting+pre+iter | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| lifting-adaptive | 18 / 0 | 3 / 0 | 3 / 0 | 1.111 / 0.000 | 1 / 0 | 6 / 0 | 7.667 / 0.000 | 2 / 0 |
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
| pm-succinct | 211 / 0 | 46 / 0 | 5 / 0 | 1.213 / 0.000 | 22 / 0 | 10 / 0 | 10.000 / 0.000 | 3 / 0 |
| pm-succinct+pre | 101 / 0 | 25 / 0 | 4 / 0 | 1.238 / 0.000 | 12 / 0 | 9 / 0 | 9.000 / 0.000 | 3 / 0 |
| pm-succinct+iter | 78 / 0 | 17 / 0 | 3 / 0 | 1.205 / 0.000 | 9 / 0 | 10 / 0 | 10.000 / 0.000 | 2 / 0 |
| pm-succinct+pre+iter | 64 / 0 | 17 / 0 | 3 / 0 | 1.250 / 0.000 | 8 / 0 | 9 / 0 | 9.000 / 0.000 | 2 / 0 |
| zielonka | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |
| zielonka-sym | 13 / 0 | 3 / 0 | 2 / 0 | 1.308 / 0.000 | 4 / 0 | 4 / 0 | 6.400 / 0.000 | 2 / 0 |
| zielonka-sym+pre | 6 / 0 | 2 / 0 | 2 / 0 | 1.500 / 0.000 | 3 / 0 | 4 / 0 | 5.500 / 0.000 | 2 / 0 |

</details>

<details>
<summary>mlsolver/games/FLCTLStarSimpleLimitClosuren=2_compact.gm · 2861 vertices / 17366 edges · 16 complete · 8 out of memory</summary>

| Vertices | Edges | Distinct priorities | Maximum priority |
| --- | --- | --- | --- |
| 2861 | 17366 | 13 | 20890720927746 |

| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | Height E / O | Parameters E / O | Seconds | Peak RSS MiB | Start winner | Reference | Agrees | Winner disagreement | Detail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lifting | out of memory | - / - | - / - | - / - | - / - | - / - | 2.653 | 1388.523 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.589 | 1388.676 | - | true | - | - | (error text not recorded) |
| lifting+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.660 | 1388.555 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.528 | 1388.605 | - | true | - | - | (error text not recorded) |
| lifting-adaptive | complete | 2861 / 0 | 16 / 0 | 3 / 0 | 7 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.566 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre | complete | 2861 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.485 | 58.574 | even | true | true | false | - |
| lifting-adaptive+iter | complete | 2861 / 0 | 10 / 0 | 2 / 0 | 6 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.506 | 58.574 | even | true | true | false | - |
| lifting-adaptive+pre+iter | complete | 2861 / 0 | 5 / 0 | 1 / 0 | 5 / 0 | H=7, K=2, t=1 / H=7, K=2, t=1 | 0.434 | 58.574 | even | true | true | false | - |
| lifting-sym | out of memory | - / - | - / - | - / - | - / - | - / - | 2.617 | 1388.672 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre | out of memory | - / - | - / - | - / - | - / - | - / - | 2.627 | 1388.672 | - | true | - | - | (error text not recorded) |
| lifting-sym+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.527 | 1388.613 | - | true | - | - | Solver failed: failed to build the Even host U^7_{11,7} |
| lifting-sym+pre+iter | out of memory | - / - | - / - | - / - | - / - | - / - | 2.479 | 1388.656 | - | true | - | - | (error text not recorded) |
| pm-strahler | complete | 2861 / 0 | 30 / 0 | 5 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.776 | 58.574 | even | true | true | false | - |
| pm-strahler+pre | complete | 2861 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.642 | 58.574 | even | true | true | false | - |
| pm-strahler+iter | complete | 2861 / 0 | 25 / 0 | 4 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.423 | 58.574 | even | true | true | false | - |
| pm-strahler+pre+iter | complete | 2861 / 0 | 19 / 0 | 3 / 0 | 7 / 0 | k=2, t=1, depth=6 / k=2, t=1, depth=7 | 0.425 | 58.574 | even | true | true | false | - |
| pm-succinct | complete | 2861 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.527 | 58.574 | even | true | true | false | - |
| pm-succinct+pre | complete | 2861 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.496 | 58.574 | even | true | true | false | - |
| pm-succinct+iter | complete | 2861 / 0 | 34 / 0 | 7 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.414 | 58.574 | even | true | true | false | - |
| pm-succinct+pre+iter | complete | 2861 / 0 | 22 / 0 | 4 / 0 | 7 / 0 | bits=1, depth=6 / bits=1, depth=7 | 0.403 | 58.574 | even | true | true | false | - |
| zielonka | complete | 2861 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka+pre | complete | 2861 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.402 | 58.574 | even | true | true | false | - |
| zielonka-sym | complete | 2861 / 0 | 15 / 0 | 5 / 0 | 7 / 0 | — / — | 0.412 | 58.574 | even | true | true | false | - |
| zielonka-sym+pre | complete | 2861 / 0 | 9 / 0 | 4 / 0 | 6 / 0 | — / — | 0.392 | 58.574 | even | true | true | false | - |

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

