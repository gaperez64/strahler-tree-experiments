"""Check inline ESM and compare its geometry with the static SVGs."""

import ast
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest
from xml.etree import ElementTree as ET

SOURCE = Path(__file__).resolve().parents[1] / 'python/strahler/widgets.py'


def frontend():
    return next(ast.literal_eval(node.value) for node in ast.parse(SOURCE.read_text()).body
                if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == '_ESM'
                                                       for t in node.targets))


def test_no_remote_frontend_dependencies():
    javascript = frontend()
    assert 'import ' not in javascript and 'fetch(' not in javascript
    assert 'https://' not in javascript
    assert 'http://' not in javascript.replace('http://www.w3.org/2000/svg', '')
    assert 'innerHTML' not in javascript


def test_inline_esm_syntax(tmp_path):
    node = shutil.which('node')
    if not node:
        if os.environ.get('CI'):
            pytest.fail('Node is required to check inline widget ESM syntax in CI')
        pytest.skip('node is not installed; inline ESM syntax check unavailable')
    source = tmp_path / 'widgets.mjs'
    source.write_text(frontend(), encoding='utf-8')
    subprocess.run([node, '--check', str(source)], check=True, capture_output=True, text=True)


@pytest.mark.parametrize('kind', ['game', 'boxes', 'tree'])
@pytest.mark.parametrize('fixture', ['fig1', 'h4'])
def test_svg_geometry_matches_frontend(tmp_path, kind, fixture):
    node = shutil.which('node')
    if not node:
        if os.environ.get('CI'):
            pytest.fail('Node is required for widget layout comparisons in CI')
        pytest.skip('node is not installed; widget layout comparison unavailable')
    pytest.importorskip('anywidget')
    import strahler
    from strahler.widgets import GameView, TreeView
    from otj22 import hk

    root = SOURCE.parents[2]
    text = (root / 'tests/games/otj22-fig1.gm').read_text() if fixture == 'fig1' else hk(4)
    with strahler.Game.from_text(text) as game:
        view = (GameView(game) if kind == 'game' else
                TreeView(strahler.decompose(game, 'zielonka').trees[0], mode=kind))
        if kind == 'game':
            view.highlight(game.vertices[:2], '#abc', 'layer')
            view.selected = game.vertices[0]
            view.hovered = [game.vertices[-1]]
        fields = ('kind', 'data', 'highlights', 'hovered', 'selected', 'mode')
        state = {key: getattr(view, key) for key in fields}
        source = tmp_path / 'widgets.mjs'
        source.write_text(frontend(), encoding='utf-8')
        runner = tmp_path / 'compare.mjs'
        runner.write_text('''
import renderer from './widgets.mjs';
class Element {
  constructor(tag) { this.tag=tag; this.attrs={}; this.children=[]; this.style={}; this.classList={add(){}}; }
  set textContent(value) { this.text=String(value); }
  get textContent() { return this.text??''; }
  setAttribute(k,v) { this.attrs[k]=String(v); }
  append(child) { this.children.push(child); }
  replaceChildren() { this.children=[]; }
  contains() { return false; }
}
globalThis.document={createElement:tag=>new Element(tag),createElementNS:(_,tag)=>new Element(tag)};
const state=JSON.parse(process.argv[2]), el=new Element('div');
renderer.render({model:{model_id:'fixture',get:key=>state[key],on(){}},el});
const groups=[], edges=[];
function visit(e) {
  if(e.attrs['data-vertex']!==undefined || e.attrs['data-path']!==undefined) {
    const id=e.attrs['data-vertex'] ?? e.attrs['data-path'];
    groups.push([id,e.children.filter(c=>['rect','circle','text'].includes(c.tag)).map(c=>[c.tag,c.attrs,c.textContent??''])]);
  }
  if(e.tag==='line' || e.tag==='path' && e.attrs['marker-end']) edges.push([e.tag,e.attrs]);
  e.children.forEach(visit);
}
visit(el);
console.log(JSON.stringify({groups,edges}));
''', encoding='utf-8')
        result = subprocess.run([node, str(runner), json.dumps(state)], check=True,
                                capture_output=True, text=True)
        actual = json.loads(result.stdout)
        svg = ET.fromstring(view._static_svg())
        groups, edges = [], []
        for element in svg.iter():
            tag = element.tag.split('}')[-1]
            key = element.get('data-vertex', element.get('data-path'))
            if key is not None:
                groups.append([key, [[e.tag.split('}')[-1], e.attrib, e.text or ''] for e in element
                                     if e.tag.split('}')[-1] in ('rect', 'circle', 'text')]])
            if tag == 'line' or tag == 'path' and 'marker-end' in element.attrib:
                edges.append([tag, element.attrib])

        def normalized(rows):
            # JS and Python may print the same float differently.
            import re
            def attributes(attrs):
                return {key: ([float(n) for n in re.findall(r'-?\d+(?:\.\d+)?(?:e[+-]?\d+)?', value)]
                              if key in ('d', 'x', 'y', 'x1', 'x2', 'y1', 'y2', 'cx', 'cy',
                                         'r', 'rx', 'width', 'height', 'stroke-width') else
                              value.replace('arrow-fixture', 'strahler-arrow')) for key, value in attrs.items()}
            return [[row[0], attributes(row[1]), *row[2:]] for row in rows]

        for expected_group, actual_group in zip(sorted(groups), sorted(actual['groups']), strict=True):
            assert expected_group[0] == actual_group[0]
            assert normalized(expected_group[1]) == normalized(actual_group[1])
        expected_edges = sorted(normalized(edges), key=str)
        actual_edges = sorted(normalized(actual['edges']), key=str)
        for expected, observed in zip(expected_edges, actual_edges, strict=True):
            assert expected[0] == observed[0]
            assert expected[1].keys() == observed[1].keys()
            for key, value in expected[1].items():
                assert observed[1][key] == (pytest.approx(value) if isinstance(value, list) else value)
