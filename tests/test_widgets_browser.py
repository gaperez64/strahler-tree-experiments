"""Render the packaged inline ESM offline, with a small anywidget model stub."""

from pathlib import Path

import pytest
import strahler

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None

from otj22 import hk

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('kind', 'data', 'hovered', 'highlights', 'selected', 'mode', 'next_kind')


@pytest.fixture(scope='module')
def browser():
    if sync_playwright is None:
        print('Browser tests skipped: playwright is not importable')
        pytest.skip('playwright is not importable')
    with sync_playwright() as playwright:
        # Missing browsers or launch failures are failures, not skipped coverage.
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    errors, requests = [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
    page.route('**/*', lambda route: (requests.append(route.request.url), route.abort()))
    yield page
    page.close()
    assert not errors, errors
    assert not requests, f'Widgets attempted network access: {requests}'


def mount(page, *widgets):
    """Round-trip saved traits and custom messages through the Python widgets."""
    from strahler.widgets import _ESM, _CSS
    by_id = {widget.model_id: widget for widget in widgets}

    def snapshots():
        return [dict(id=widget.model_id, state={field: getattr(widget, field) for field in FIELDS})
                for widget in widgets]

    def update(model_id, changes, message):
        widget = by_id[model_id]
        for field, value in changes.items():
            setattr(widget, field, value)
        if message is not None:
            widget._handle_custom_msg(message, [])
        return snapshots()

    page.expose_function('updatePython', update)
    page.evaluate('''async ({source, css, snapshots}) => {
      const url = URL.createObjectURL(new Blob([source], {type:'text/javascript'}));
      const renderer = (await import(url)).default;
      URL.revokeObjectURL(url);
      const style = document.createElement('style'); style.textContent = css;
      document.head.append(style);
      window.models = [];
      window.pending = Promise.resolve();
      const sync = snapshots => snapshots.forEach(({state}, i) => models[i].update(state));
      for (const {id, state} of snapshots) {
        const listeners = {}, changes = {};
        const model = {
          model_id:id, state, saved:0, sent:[],
          get(key) { return state[key]; },
          set(key, value) { changes[key] = value; this.update({[key]:value}); },
          on(event, callback) { (listeners[event] ||= new Set()).add(callback); },
          off(event, callback) { listeners[event]?.delete(callback); },
          update(patch) {
            for (const [key,value] of Object.entries(patch)) {
              if (JSON.stringify(state[key]) === JSON.stringify(value)) continue;
              state[key] = value;
              for (const callback of listeners['change:'+key] || []) callback();
            }
          },
          save_changes() {
            this.saved++;
            const patch = {...changes};
            for (const key of Object.keys(changes)) delete changes[key];
            return window.pending = updatePython(id, patch, null).then(sync);
          },
          send(message) {
            this.sent.push(message);
            return window.pending = updatePython(id, {}, message).then(sync);
          }
        };
        models.push(model);
        const el = document.createElement('div'); el.id = 'widget-'+(models.length-1);
        document.body.append(el);
        renderer.render({model, el});
      }
    }''', dict(source=_ESM, css=_CSS, snapshots=snapshots()))


@pytest.mark.parametrize('text', [(ROOT / 'tests/games/otj22-fig1.gm').read_text(), hk(4)],
                         ids=['fig1', 'h4'])
def test_game_render_and_selection(page, text):
    from strahler.widgets import GameView
    with strahler.Game.from_text(text) as game:
        view = GameView(game)
        mount(page, view)
        assert page.locator('svg').count() == 1
        assert page.locator('[data-vertex]').count() == len(game.vertices)
        assert page.locator('g > circle').count() == sum(p == 0 for p in game.owner.values())
        assert page.locator('g > rect').count() == sum(p == 1 for p in game.owner.values())
        assert page.locator('path[marker-end]').count() == len(game.edges)
        vertex = game.vertices[-1]
        page.locator(f'[data-vertex="{vertex}"]').click()
        page.evaluate('window.pending')
        assert view.selected == vertex
        assert page.evaluate('models[0].get("selected")') == vertex
        assert page.locator(f'[data-vertex="{vertex}"] > :first-child').get_attribute('stroke') == '#dc2626'
        page.locator(f'[data-vertex="{game.vertices[0]}"]').focus()
        page.keyboard.press('Enter')
        page.evaluate('window.pending')
        assert view.selected == game.vertices[0]


def nodes(root):
    return [] if root is None else [root] + [n for child in root['children'] for n in nodes(child)]


@pytest.mark.parametrize('mode', ['boxes', 'tree'])
@pytest.mark.parametrize('kind', ['decomposition', 'strahler', 'prefix', 'measures', 'empty'])
def test_tree_render_and_interaction(page, mode, kind):
    from strahler.widgets import GameView, TreeView
    with strahler.Game.from_file(ROOT / 'tests/games/otj22-fig1.gm') as game:
        data = dict(decomposition=strahler.decompose(game, 'zielonka').trees[0],
                    strahler=strahler.genstree(2, 3, 1), prefix=strahler.pms_tree('0,e|1,e|'),
                    measures=strahler.progress_measures(game)['rounds'][-1]['trees'][0],
                    empty={'tree': None})[kind]
        game_view = GameView(game)
        view = TreeView(data, game_view, mode=mode)
        mount(page, game_view, view)
        tree = page.locator('#widget-1')
        expected = nodes(view.data)
        assert len(expected) == dict(decomposition=5, strahler=17, prefix=5, measures=7, empty=0)[kind]

        def counts():
            boxes = view.mode == 'boxes'
            assert tree.locator('svg').count() == (1 if expected else 0)
            assert tree.locator('svg g[role="button"]').count() == len(expected)
            assert tree.locator('svg line').count() == (0 if boxes else max(0, len(expected)-1))
            for part in 'HTS':
                assert tree.locator(f'.part-{part}').count() == (len(expected) if boxes else 0)

        counts()
        if not expected:
            assert 'empty tree' in tree.inner_text()
            return
        # Select a child to catch bubbling through nested parent boxes.
        child = expected[1]
        target = tree.locator('[data-path="' + str(child['path']).replace(' ', '') + '"]')
        # Hit the node center; SVG group corners can be outside its rounded rectangle.
        position = {'x': 2, 'y': 2} if mode == 'boxes' else None
        target.hover(position=position)
        page.evaluate('window.pending')
        assert view.hovered == game_view.hovered == child['vertices']
        assert page.evaluate('models[1].get("hovered")') == child['vertices']
        for vertex in child['vertices']:
            assert page.locator(f'[data-vertex="{vertex}"] > :first-child').get_attribute('stroke') == '#c026d3'
        target.click(position=position)
        page.evaluate('window.pending')
        assert view.selected == child['path']
        target.focus()
        page.keyboard.press('Enter')
        page.evaluate('window.pending')
        assert page.evaluate('models[1].sent.at(-1)') == dict(command='select', path=child['path'])
        page.mouse.move(0, 0)
        tree.get_by_role('combobox').focus()
        page.evaluate('window.pending')
        assert game_view.hovered == []
        tree.get_by_role('combobox').select_option('tree' if mode == 'boxes' else 'boxes')
        page.evaluate('window.pending')
        counts()


@pytest.mark.parametrize('algorithm', ['zielonka', 'zielonka-sym'])
def test_stepper_render_and_navigation(page, algorithm):
    from strahler.widgets import Stepper
    with strahler.Game.from_file(ROOT / 'tests/games/otj22-fig1.gm') as game:
        stepper = Stepper(strahler.trace(game, algorithm))
        calls = stepper.call_tree()
        mount(page, stepper.controls, stepper.game_view, *stepper.tree_views, calls)
        controls = page.locator('#widget-0')

        def check_state():
            assert page.evaluate('models[0].get("data").index') == stepper.index
            assert controls.locator('.badge').count() == 2
            assert controls.locator('pre.current').count() == 1
            assert page.locator('#widget-1 [data-vertex]').count() == 10
            assert controls.locator('.timeline line').count() == len(stepper.cursor.ticks) + 1
            for i, view in enumerate(stepper.tree_views, 2):
                for part in 'HTS':
                    assert page.locator(f'#widget-{i} .part-{part}').count() == len(nodes(view.data))
            for player, badge in enumerate(stepper.badges):
                text = controls.locator('.badge').nth(player).inner_text()
                assert badge['status'] in text
                assert f"condition {stepper.verify(player).condition.name}" in text

        check_state()
        for label in ['Next call', 'Step', 'Back', 'Next return'] + (['Next check'] if algorithm.endswith('-sym') else []):
            controls.get_by_role('button', name=label, exact=True).click()
            page.evaluate('window.pending')
            check_state()
        kind = 'labels' if algorithm.endswith('-sym') else 'set'
        controls.get_by_role('combobox', name='Next event kind').select_option(kind)
        page.evaluate('window.pending')
        assert stepper.controls.next_kind == kind
        controls.get_by_role('button', name='Next event of kind', exact=True).click()
        page.evaluate('window.pending')
        assert stepper.state.event['event'] == kind
        check_state()
        # Seek through distinct tree-building prefixes and the final certificates.
        for index in [len(stepper.run)//3, 2*len(stepper.run)//3, len(stepper.run)-1]:
            controls.get_by_role('slider').evaluate('''(slider, index) => {
              slider.value = index; slider.dispatchEvent(new Event('change', {bubbles:true}));
            }''', index)
            page.evaluate('window.pending')
            assert stepper.index == index
            check_state()
        controls.get_by_role('button', name='Run to end', exact=True).click()
        page.evaluate('window.pending')
        assert stepper.state.trees == stepper.run.result.trees
        assert all(badge['ok'] for badge in stepper.badges)
        assert [len(nodes(view.data)) for view in stepper.tree_views] == [5, 0]
        # Click a call twice: selected-path sync and custom-message paths both jump.
        first = page.locator('#widget-4 [data-path="[0]"]')
        for _ in range(2):
            first.click()
            page.evaluate('window.pending')
            assert stepper.index == stepper.cursor.calls[0]['index']
            check_state()
