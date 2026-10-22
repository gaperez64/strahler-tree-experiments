"""Python widget/comm behaviour; frontend rendering is a separate browser check."""

from pathlib import Path
import pytest
import strahler

pytest.importorskip('anywidget', reason='install strahler[notebooks] for widget tests')
from strahler.widgets import GameView, TreeView, Stepper
from otj22 import hk

ROOT = Path(__file__).resolve().parents[1]


def test_game_state_sync_and_coordinates():
    with strahler.Game.from_text('10 2 0 10,42 "a";42 1 1 42;') as game:
        view = GameView(game)
        assert view.data == GameView(game).data
        assert view.selected is None
        view.selected = 42
        assert view.get_state()['selected'] == 42
        view.highlight([10], '#abc', 'domain')
        view.highlight([42], '#def', 'domain')
        assert view.highlights == [dict(name='domain', colour='#def', vertices=[42])]
        with pytest.raises(ValueError, match='unknown'):
            view.highlight([0])
        with pytest.raises(ValueError, match='every'):
            GameView(game, {10: (0, 0)})
        with pytest.raises(ValueError, match='finite'):
            GameView(game, {10: (0, 0), 42: (float('inf'), 1)})
        explicit = GameView(game, {10: (0, 0), 42: (1, 2)})
        assert explicit.data['vertices'][0]['xy'] == [60, 60]


def test_tree_json_and_linked_hover():
    with strahler.Game.from_file(ROOT / 'tests/games/otj22-fig1.gm') as game:
        view = GameView(game)
        tree = TreeView(strahler.decompose(game, 'zielonka').trees[0], view)
        tree.hovered = [0, 1]
        assert view.hovered == [0, 1]
        tree.mode = 'tree'
        assert tree.get_state()['mode'] == 'tree'
        tree.tree = strahler.genstree(2, 3, 1)
        assert tree.data['children']
        tree.tree = strahler.pms_tree('0,e|1,e|')
        assert len(tree.data['children']) == 2
        measures = strahler.progress_measures(game)
        tree.tree = measures['rounds'][-1]['trees'][0]
        assert tree.data['vertices']
        tree.tree = None
        assert tree.data is None


@pytest.mark.parametrize('tree', [None, {'tree': None},
    {'schema': 'strahler-decomp/1', 'tree': None},
    {'schema': 'strahler-tree/1', 'tree': None},
    {'schema': 'strahler-pm/1', 'tree': None},
    {'parameters': {'k': 1, 't': 1}, 'tree': None}, 'null', '{"tree": null}'])
def test_empty_tree_documents(tree):
    view = TreeView(tree)
    assert view.data is None
    view.tree = {'h': 0, 'H': [], 'T': [], 'S': [], 'children': []}
    assert view.data is not None  # An empty node still has a tree shape.
    view.tree = tree
    assert view.data is None


@pytest.mark.parametrize('algorithm', ['zielonka', 'zielonka-sym'])
def test_stepper_controls_and_call_tree(algorithm):
    with strahler.Game.from_text(hk(4)) as game:
        run = strahler.trace(game, algorithm)
        view = Stepper(run, checkpoint_interval=11)
        assert view.index == 0
        assert [badge['condition'] for badge in view.controls.data['badges']] == [
            view.verify(player).condition.name for player in range(2)]
        view.next('call')
        call = view.index
        assert view.controls.data['stack']
        view.step()
        view.back()
        assert view.index == call
        view._message(view.controls, dict(command='next', kind='return'), [])
        assert view.state.event['event'] == 'return'
        view._message(view.controls, dict(command='end'), [])
        assert view.state.trees == run.result.trees
        assert all(view.verify(p).ok for p in range(2))
        assert [badge['condition'] for badge in view.controls.data['badges']] == ['OK', 'OK']
        tree = view.call_tree()
        tree.selected = [0]
        assert view.index == call
        view._message(view.controls, dict(command='seek', index=0), [])
        assert view.index == 0
        assert view.controls.data['badges'][0]['claim'] is None


def test_replacing_notebook_panels_closes_owned_comms():
    import importlib.util
    from ipywidgets import VBox
    spec = importlib.util.spec_from_file_location('notebook_support', ROOT / 'jupyter-examples/notebook_support.py')
    support = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(support)
    with strahler.Game.from_text(hk(2)) as game:
        stepper = Stepper(strahler.trace(game, 'zielonka'))
        call_tree = stepper.call_tree()
        panel = VBox([stepper, call_tree])
        support.close_views(panel)
        assert panel.comm is None and call_tree.comm is None
        assert stepper.comm is None and stepper.game_view.comm is None
        assert all(tree.comm is None for tree in stepper.tree_views)
