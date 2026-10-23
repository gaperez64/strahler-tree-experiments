"""Python widget/comm behaviour; frontend rendering is a separate browser check."""

from pathlib import Path
from xml.etree import ElementTree as ET
import pytest
import strahler

pytest.importorskip('anywidget', reason='install strahler[notebooks] for widget tests')
from strahler.widgets import GameView, TreeView, Stepper
from otj22 import hk

ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://www.w3.org/2000/svg'}
WIDGET_MIME = 'application/vnd.jupyter.widget-view+json'


def bundle(view):
    result = view._repr_mimebundle_()
    return result[0] if isinstance(result, tuple) else result


def test_game_svg_fallback():
    with strahler.Game.from_text('10 2 0 10,42 "<a&b>";42 1 1 42;') as game:
        view = GameView(game)
        view.highlight([10, 42], '#abc', '<layer>')
        view.highlight([42], '#def', 'last')
        view.selected = 10
        view.hovered = [42]
        data = bundle(view)
        assert WIDGET_MIME in data and data['text/plain'] == 'Parity game'
        svg = ET.fromstring(data['image/svg+xml'])
        groups = svg.findall('s:g', NS)
        assert len(groups) == len(game.vertices)
        assert [g[0].tag for g in groups] == ['{' + NS['s'] + '}' + tag for tag in ('circle', 'rect')]
        assert [g[0].get('fill') for g in groups] == ['#abc', '#def']
        assert [g[0].get('stroke') for g in groups] == ['#dc2626', '#c026d3']
        assert all(g[0].get('stroke-width') == '4' for g in groups)
        assert len(svg.findall('s:path', NS)) == len(game.edges)
        assert '<a&b>' in ''.join(svg.itertext())
        assert '&lt;a&amp;b&gt;' in data['image/svg+xml']
        assert data['image/svg+xml'] == bundle(GameView(game, highlights=view.highlights,
                                                       selected=10, hovered=[42]))['image/svg+xml']
        view.highlight([10], 'url(https://example.com/paint)', 'external')
        assert 'https://' not in bundle(view)['image/svg+xml']


@pytest.mark.parametrize('mode', ['boxes', 'tree'])
def test_tree_svg_fallback(mode):
    view = TreeView(dict(label='<a&b>', H=[10], T=[42], S=[], children=[
        dict(label='child', H=[42], children=[])]), mode=mode)
    data = bundle(view)
    assert WIDGET_MIME in data and data['text/plain'] == 'Ordered tree'
    svg = ET.fromstring(data['image/svg+xml'])
    assert len(svg.findall('.//s:g[@data-path]', NS)) == 2
    assert '<a&b>' in ''.join(svg.itertext())
    assert '&lt;a&amp;b&gt;' in data['image/svg+xml']
    if mode == 'boxes':
        for part, colour in [('H', '#dbeafe'), ('T', '#dcfce7'), ('S', '#ffedd5')]:
            shapes = svg.findall(f'.//s:rect[@class="part-{part}"]', NS)
            assert len(shapes) == 2 and all(s.get('fill') == colour for s in shapes)
    else:
        assert len(svg.findall('.//s:rect', NS)) == 2
        assert len(svg.findall('s:line', NS)) == 1
        assert view.data['xy'] == [130.0, 35]
        assert view.data['children'][0]['xy'] == [130, 120]
    view.tree = None
    assert '∅ — empty tree' in ''.join(ET.fromstring(bundle(view)['image/svg+xml']).itertext())


def test_stepper_static_fallback_and_call_tree():
    with strahler.Game.from_text(hk(2)) as game:
        view = Stepper(strahler.trace(game, 'zielonka-sym'))
        view.next('check')
        data = bundle(view)
        assert WIDGET_MIME in data
        html = ET.fromstring('<div>' + data['text/html'] + '</div>')
        assert len(html.findall('s:svg', NS)) == 3
        text = ''.join(html.itertext())
        assert f'{view.index} / {len(view.run)-1}: check' in text
        for badge in view.badges:
            assert badge['condition'] in text and badge['status'] in text
        calls = view.call_tree()
        assert ET.fromstring(bundle(calls)['image/svg+xml']).findall('.//s:g', NS)
        view.end()
        assert data['text/html'] != bundle(view)['text/html']


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
