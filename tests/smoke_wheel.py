"""Run with an installed wheel's Python, outside the source tree."""

from importlib.metadata import version
from pathlib import Path
import sys

import strahler


assert Path(strahler.__file__).resolve().is_relative_to(Path(sys.prefix).resolve())
assert strahler.version() == version('strahler') == sys.argv[1]
with strahler.Game.from_text('parity 1; 0 2 0 0 "even"; 1 1 1 1 "odd";') as game:
    for algorithm in ('zielonka', 'zielonka-sym', 'lifting', 'lifting-sym'):
        result = strahler.decompose(game, algorithm)
        assert result.complete and result.regions == (frozenset({0}), frozenset({1}))
        for player in (0, 1):
            checked = strahler.check(game, result.trees[player], player,
                                    subgame=result.regions[player])
            assert checked.ok and checked.condition is strahler.Condition.OK
        run = strahler.trace(game, algorithm)
        assert run.state(-1).trees == result.trees
        assert all(actual.ok == event['is_attractor_decomposition']
                   for event, actual in run.check_claims())
    for options in ({'player': 'even'}, {'args': ['--player=odd']}):
        try:
            strahler.trace(game, **options)
        except ValueError:
            pass
        else:
            raise AssertionError('single-player trace was accepted')
    assert strahler.progress_measures(game, algorithm='succinct')['rounds']
assert strahler.genstree(k=2, h=3, t=1)
assert strahler.pms_tree('0|1|')
try:
    strahler.Game.from_text('bad')
except strahler.InputError:
    pass
else:
    raise AssertionError('invalid input was accepted')
print(f'Installed strahler {strahler.version()}: smoke test passed')
