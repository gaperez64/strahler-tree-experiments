"""Offline SVG notebook widgets. Install ``strahler[notebooks]`` to use them.

GameView(game, coordinates=None), TreeView(tree, game_view=None, mode='boxes'),
and Stepper(trace, coordinates=None). No frontend dependencies or remote URLs.
"""

from html import escape
import json
from math import hypot, isfinite
import re
from xml.etree import ElementTree as ET

try:
    import anywidget
    import traitlets as t
    from ipywidgets import VBox, HBox, Layout
except ImportError as error:
    raise ImportError('Notebook views need: pip install "strahler[notebooks]"') from error

from . import Node
from ._widget_state import TraceCursor

__all__ = ['GameView', 'TreeView', 'Stepper']

_CSS = """
.strahler { font: 14px system-ui, sans-serif; color: #182538; background: #fff;
  padding: 8px; border: 1px solid #b7c4d3; border-radius: 6px; overflow: auto; }
.strahler button, .strahler select, .strahler textarea { font: inherit; margin: 3px; }
.strahler button { cursor: pointer; } .strahler button:focus-visible,
.strahler [tabindex]:focus-visible { outline: 3px solid #2563eb; }
.strahler svg { min-width: 300px; max-width: 100%; }
.strahler text { fill: #182538; font: 12px system-ui, sans-serif; }
.strahler pre { white-space: pre-wrap; max-height: 240px; overflow: auto; }
.strahler .current { background: #fef08a; } .strahler .badge { padding: 6px; border-left: 5px solid #b45309; }
.strahler .ok { border-color: #15803d; } .strahler .timeline { width: 100%; height: 36px; }
"""

_ESM = r"""
const NS = 'http://www.w3.org/2000/svg';
function element(tag, text, parent) {
  const e = document.createElement(tag);
  if (text !== null) e.textContent = text;
  if (['button','input','select'].includes(tag)) e.setAttribute('data-control',text || tag);
  if (parent) parent.append(e);
  return e;
}
function svgElement(tag, attrs, parent) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  parent.append(e);
  return e;
}
function interactive(e, label, action) {
  e.setAttribute('tabindex', '0'); e.setAttribute('role', 'button');
  e.setAttribute('aria-label', label);
  e.onclick = event => { event.stopPropagation(); action(); };
  e.onkeydown = event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); event.stopPropagation(); action(); } };
}
function game(model, el) {
  const d = model.get('data'), sets = model.get('highlights'), hovered = model.get('hovered');
  const svg = svgElement('svg', {viewBox: '0 0 800 500', role: 'group', 'aria-label': 'Parity game. Circles Even, squares Odd.'}, el);
  const markerID = 'arrow-' + model.model_id;
  const defs = svgElement('defs', {}, svg);
  const marker = svgElement('marker', {id: markerID, viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto-start-reverse'}, defs);
  svgElement('path', {d: 'M 0 0 L 10 5 L 0 10 z', fill: '#64748b'}, marker);
  const points = new Map(d.vertices.map(v => [v.id, v.xy]));
  for (const [a, b] of d.edges) {
    const [x, y] = points.get(a), [u, v] = points.get(b), dx = u-x, dy = v-y;
    const len = Math.hypot(dx, dy) || 1, r = 23;
    const path = a === b ? `M ${x-10} ${y-18} C ${x-65} ${y-85} ${x+65} ${y-85} ${x+10} ${y-18}` :
      `M ${x+dx*r/len} ${y+dy*r/len} Q ${(x+u)/2-dy*.12} ${(y+v)/2+dx*.12} ${u-dx*r/len} ${v-dy*r/len}`;
    svgElement('path', {d: path, fill: 'none', stroke: '#64748b', 'marker-end': `url(#${markerID})`}, svg);
  }
  for (const vertex of d.vertices) {
    const [x, y] = vertex.xy, group = svgElement('g', {'data-vertex':vertex.id}, svg);
    let fill = '#fff';
    for (const set of sets) if (set.vertices.includes(vertex.id)) fill = set.colour;
    const hot = hovered.includes(vertex.id), selected = model.get('selected') === vertex.id;
    const attrs = {fill, stroke: hot ? '#c026d3' : selected ? '#dc2626' : '#182538', 'stroke-width': hot || selected ? 4 : 1.5};
    svgElement(vertex.owner === 0 ? 'circle' : 'rect', vertex.owner === 0 ? {...attrs, cx:x, cy:y, r:20} : {...attrs, x:x-20, y:y-20, width:40, height:40}, group);
    svgElement('text', {x, y:y+4, 'text-anchor':'middle'}, group).textContent = vertex.priority;
    svgElement('text', {x, y:y+37, 'text-anchor':'middle'}, group).textContent = vertex.name || String(vertex.id);
    svgElement('title', {}, group).textContent = `${vertex.name || vertex.id}: priority ${vertex.priority}, ${vertex.owner === 0 ? 'Even' : 'Odd'}`;
    interactive(group, `Select vertex ${vertex.name || vertex.id}`, () => { model.set('selected', vertex.id); model.save_changes(); });
  }
  const legend = element('div', 'Circle: Even · Square: Odd · ', el);
  for (const set of sets) { const label = element('span', `${set.name}  `, legend); label.style.backgroundColor = set.colour; }
}
function tree(model, el) {
  const select = element('select', null, el);
  select.setAttribute('aria-label', 'Tree layout');
  for (const value of ['boxes', 'tree']) { const o = element('option', value === 'boxes' ? 'H/T/S boxes' : 'Node-link tree', select); o.value = value; }
  select.value = model.get('mode');
  select.onchange = () => { model.set('mode', select.value); model.save_changes(); };
  const root = model.get('data');
  if (!root) { element('p', '∅ — empty tree', el); return; }
  const hover = (e, n) => {
    e.setAttribute('data-path', JSON.stringify(n.path));
    e.onpointerenter = e.onfocus = () => { model.set('hovered', n.vertices); model.save_changes(); };
    e.onpointerleave = e.onblur = () => { model.set('hovered', []); model.save_changes(); };
    interactive(e, `Tree node ${n.label}`, () => {
      if (JSON.stringify(model.get('selected')) === JSON.stringify(n.path)) {
        model.send({command:'select',path:n.path});
      } else { model.set('selected', n.path); model.save_changes(); }
    });
  };
  if (select.value === 'boxes') {
    const [width, height] = root.extent.boxes;
    const svg = svgElement('svg', {viewBox:`0 0 ${width} ${height}`, role:'group', 'aria-label':'H/T/S boxes'}, el);
    const visit = (n, parent) => {
      const [x,y,w,h] = n.box;
      const outer = svgElement('g', {}, parent); hover(outer, n);
      svgElement('rect', {x,y,width:w,height:h,fill:'#fff',stroke:'#64748b'}, outer);
      svgElement('text', {x:x+6,y:y+18,style:'font-weight:bold'}, outer).textContent=n.label;
      const offsets = {S:[6,28,w-12,h-34],T:[12,56,w-24,h-68],H:[18,h-46,w-36,28]};
      const colours = {S:'#ffedd5',T:'#dcfce7',H:'#dbeafe'};
      for (const part of ['S', 'T', 'H']) {
        const [dx,dy,width,height]=offsets[part];
        svgElement('rect', {x:x+dx,y:y+dy,width,height,fill:colours[part],stroke:'#64748b',class:`part-${part}`}, outer);
        svgElement('text', {x:x+dx+6,y:y+dy+18}, outer).textContent=`${part}: ${n[part].join(', ') || '∅'}`;
      }
      for (const child of n.children) visit(child, outer);
    };
    visit(root, svg);
  } else {
    const nodes = [], edges = [];
    const visit = n => {
      for (const child of n.children) visit(child);
      const [x,y]=n.xy;
      const row={n,x,y}; nodes.push(row);
      for (const c of n.children) edges.push([row,{x:c.xy[0],y:c.xy[1]}]);
    };
    visit(root);
    const [width,height]=root.extent.tree;
    const svg = svgElement('svg', {viewBox:`0 0 ${width} ${height}`, role:'group', 'aria-label':'Ordered tree'}, el);
    for (const [a,b] of edges) svgElement('line', {x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:'#94a3b8'}, svg);
    for (const {n,x,y} of nodes) {
      const g = svgElement('g', {}, svg); hover(g,n);
      svgElement('rect', {x:x-58,y:y-17,width:116,height:34,rx:5,fill:'#dbeafe',stroke:'#64748b'},g);
      svgElement('text',{x,y:y+4,'text-anchor':'middle'},g).textContent=n.label;
      svgElement('title',{},g).textContent=`${n.label}: ${n.vertices.join(', ')}`;
    }
  }
}
function controls(model, el) {
  const d = model.get('data');
  const send = (command, extra={}) => model.send({command,...extra});
  for (const [label, command] of [['Back','back'],['Step','step'],['Run to end','end']]) {
    element('button',label,el).onclick = () => send(command);
  }
  const kinds = element('select',null,el); kinds.setAttribute('aria-label','Next event kind');
  for (const k of d.kinds) element('option',k,kinds).value=k;
  kinds.value = model.get('next_kind');
  kinds.onchange = () => { model.set('next_kind', kinds.value); model.save_changes(); };
  element('button','Next event of kind',el).onclick = () => send('next',{kind:kinds.value});
  for (const kind of ['call','return','check']) if(d.kinds.includes(kind)) {
    element('button','Next '+kind,el).onclick=()=>send('next',{kind});
  }
  const slider = element('input',null,el); slider.type='range'; slider.min=0; slider.max=d.length-1; slider.value=d.index;
  slider.style.width='100%'; slider.setAttribute('aria-label','Trace position');
  slider.onchange=()=>send('seek',{index:Number(slider.value)});
  element('div','Timeline (sampled): hover a tick for its event name; purple means check.',el);
  const timeline=svgElement('svg',{viewBox:'0 0 1000 32',class:'timeline',role:'img','aria-label':'Event timeline; purple ticks mark checks'},el);
  // A bounded number of ticks keeps 100k-event traces cheap to render.
  for (const tick of d.ticks) {
    const x=1000*tick.index/Math.max(1,d.length-1);
    const line=svgElement('line',{x1:x,x2:x,y1:0,y2:tick.kind==='check'?30:14,stroke:tick.kind==='check'?'#a21caf':'#94a3b8'},timeline);
    svgElement('title',{},line).textContent=`${tick.index}: ${tick.kind}`;
    line.onclick=()=>send('seek',{index:tick.index});
  }
  svgElement('line',{x1:1000*d.index/Math.max(1,d.length-1),x2:1000*d.index/Math.max(1,d.length-1),y1:0,y2:32,stroke:'#dc2626','stroke-width':3},timeline);
  element('strong',`${d.index} / ${d.length-1}: ${d.event.event}`,el);
  element('pre',JSON.stringify(d.event,null,2),el);
  element('strong','Call stack',el);
  element('pre',d.stack.join('\n') || '(outside recursive calls)',el);
  element('p',d.note,el);
  const code=element('div',null,el);
  d.pseudocode.forEach((line,i)=>{const row=element('pre',`${i+1}. ${line}`,code);if(i===d.line)row.className='current';});
  for (const badge of d.badges) {
    const box=element('div',null,el); box.className='badge'+(badge.ok?' ok':'');
    const claim=badge.claim;
    element('div',`${badge.player===0?'Even':'Odd'} — algorithm claim: `+(claim?`${claim.event.is_attractor_decomposition?'✔':'✘'} at step ${claim.index}, path ${JSON.stringify(claim.event.path)}, G={${claim.event.subgame.join(',')}}`:'no check event yet'),box);
    element('div',`Independent: ${badge.ok?'✔':'✘'} ${badge.status} on G={${badge.domain.join(',')}}; condition ${badge.condition}; path ${JSON.stringify(badge.path)}; vertex ${badge.vertex === null ? '—' : badge.vertex}. ${badge.message}`,box);
    if(badge.problems.length)element('pre','Materializer: '+JSON.stringify(badge.problems),box);
  }
}
export default { render({model,el}) {
  el.classList.add('strahler');
  const draw=()=>{
    const focused=el.contains(document.activeElement)?document.activeElement:null;
    const attribute=focused && focused.hasAttribute('data-vertex')?'data-vertex':'data-control';
    const active=focused?focused.getAttribute(attribute):null;
    el.replaceChildren();
    const kind=model.get('kind'); if(kind==='game')game(model,el);else if(kind==='tree')tree(model,el);else controls(model,el);
    if(active!==null){const node=Array.from(el.querySelectorAll(`[${attribute}]`)).find(e=>e.getAttribute(attribute)===active);if(node)node.focus();}
  };
  const fields=model.get('kind')==='game'?['data','highlights','hovered','selected']:['data','mode'];
  for(const field of fields)model.on('change:'+field,draw);
  draw();
  return ()=>{for(const field of fields)model.off('change:'+field,draw);};
}};
"""


def _svg(parent, tag, attrs=None, text=None):
    element = ET.SubElement(parent, tag, {k: str(v) for k, v in (attrs or {}).items()})
    if text is not None:
        element.text = str(text)
    return element


def _svg_root(width, height, label):
    return ET.Element('svg', xmlns='http://www.w3.org/2000/svg',
                      viewBox=f'0 0 {width} {height}', width=str(width), height=str(height),
                      role='img', attrib={'aria-label': label, 'fill': '#182538',
                      'style': 'max-width:100%;height:auto;background:white;font:12px system-ui,sans-serif'})


def _svg_colour(colour):
    # SVG paint URLs could fetch external content; accept only plain colours.
    return colour if isinstance(colour, str) and re.fullmatch(
        r'#[\da-fA-F]{3,8}|[a-zA-Z]+|(?:rgb|hsl)a?\([\d.% ,+-]+\)', colour) else '#fff'


def _tree_layout(tree):
    root = _tree_data(tree)
    if root is None:
        return None
    leaf = depth = 0

    def measure(n, level):
        nonlocal leaf, depth
        sizes = [measure(c, level + 1) for c in n['children']]
        if sizes:
            x = sum(c['xy'][0] for c in n['children']) / len(sizes)
        else:
            leaf += 1
            x = leaf * 130
        n['xy'] = [x, 35 + level * 85]
        depth = max(depth, level)
        # Reserve eight pixels per character for the nested box labels.
        labels = [len(str(n['label'])) * 8 + 12] + [
            len(f"{p}: {', '.join(map(str, n[p])) or '∅'}") * 8 + inset
            for p, inset in [('S', 24), ('T', 36), ('H', 48)]]
        width = max(150, *labels, sum(w for w, h in sizes) + max(0, len(sizes)-1)*8 + 36)
        height = 130 + (max(h for w, h in sizes) + 8 if sizes else 0)
        n['box'] = [0, 0, width, height]
        return width, height

    def place(n, x, y):
        n['box'][:2] = [x, y]
        for child in n['children']:
            place(child, x + 18, y + 84)
            x += child['box'][2] + 8

    width, height = measure(root, 0)
    place(root, 5, 5)
    root['extent'] = dict(boxes=[width + 10, height + 10],
                          tree=[max(300, (leaf + 1)*130), 100 + depth*85])
    return root


class _View(anywidget.AnyWidget):
    _esm = _ESM
    _css = _CSS
    kind = t.Unicode().tag(sync=True)
    data = t.Any(allow_none=True).tag(sync=True)
    hovered = t.List(t.Int()).tag(sync=True)
    highlights = t.List(t.Dict()).tag(sync=True)
    selected = t.Any(allow_none=True).tag(sync=True)
    mode = t.Enum(['boxes', 'tree'], default_value='boxes').tag(sync=True)
    next_kind = t.Unicode('call').tag(sync=True)

    def _repr_mimebundle_(self, **kwargs):
        bundle = super()._repr_mimebundle_(**kwargs)
        if bundle is None:
            return None
        data = bundle[0] if isinstance(bundle, tuple) else bundle
        if self.kind in ('game', 'tree'):
            data.update({'image/svg+xml': self._static_svg(),
                         'text/plain': 'Parity game' if self.kind == 'game' else 'Ordered tree'})
        return bundle


class GameView(_View):
    """Parity game; coordinates map external IDs to (x, y), scaled to the view.

    The default deterministic layout groups vertices by input priority.
    ``highlight(vertices, colour, name)`` replaces a named highlight layer.
    ``selected`` is the clicked external vertex ID (or None).
    """

    def __init__(self, game, coordinates=None, **kwargs):
        self.game = game
        vertices = game.vertices
        # shortcut: JS numbers have 53-bit precision; use string IDs if larger games need them.
        if any(abs(v) > 2**53 - 1 for v in vertices):
            raise ValueError('SVG views require vertex IDs at most 2**53 - 1; renumber this game')
        if coordinates is None:
            levels = sorted(set(game.priority.values()), reverse=True)
            coordinates = {}
            for row, priority in enumerate(levels):
                group = [v for v in vertices if game.priority[v] == priority]
                for col, v in enumerate(group):
                    coordinates[v] = (col * 2 - len(group) + 1, row * 2)
        if set(coordinates) != set(vertices):
            raise ValueError('coordinates must contain every external vertex ID exactly once')
        if any(len(xy) != 2 or not all(isfinite(x) for x in xy) for xy in coordinates.values()):
            raise ValueError('coordinates must be finite (x, y) pairs')
        xs = [xy[0] for xy in coordinates.values()] or [0]
        ys = [xy[1] for xy in coordinates.values()] or [0]
        def scale(value, values, extent):
            return 60 + (value - min(values)) / (max(values) - min(values) or 1) * extent
        data = dict(vertices=[dict(id=v, name=game.names[v], priority=game.priority[v],
                                  owner=game.owner[v], xy=[scale(coordinates[v][0], xs, 680),
                                                         scale(coordinates[v][1], ys, 360)])
                              for v in vertices], edges=game.edges)
        super().__init__(kind='game', data=data, **kwargs)

    def highlight(self, vertices, colour='#bfdbfe', name='selection'):
        vertices = sorted(set(vertices))
        if not set(vertices) <= set(self.game.vertices):
            raise ValueError('highlight contains an unknown vertex')
        self.highlights = [s for s in self.highlights if s['name'] != name] + [
            dict(name=name, vertices=vertices, colour=colour)]

    def _static_svg(self):
        svg = _svg_root(800, 520, 'Parity game. Circles Even, squares Odd.')
        marker = _svg(_svg(svg, 'defs'), 'marker', dict(
            id='strahler-arrow', viewBox='0 0 10 10', refX=9, refY=5,
            markerWidth=6, markerHeight=6, orient='auto-start-reverse'))
        _svg(marker, 'path', dict(d='M 0 0 L 10 5 L 0 10 z', fill='#64748b'))
        points = {v['id']: v['xy'] for v in self.data['vertices']}
        for a, b in self.data['edges']:
            x, y = points[a]
            u, v = points[b]
            dx, dy = u-x, v-y
            length = hypot(dx, dy) or 1
            path = (f'M {x-10} {y-18} C {x-65} {y-85} {x+65} {y-85} {x+10} {y-18}'
                    if a == b else f'M {x+dx*23/length} {y+dy*23/length} '
                    f'Q {(x+u)/2-dy*.12} {(y+v)/2+dx*.12} {u-dx*23/length} {v-dy*23/length}')
            _svg(svg, 'path', {'d': path, 'fill': 'none', 'stroke': '#64748b',
                              'marker-end': 'url(#strahler-arrow)'})
        for vertex in self.data['vertices']:
            x, y = vertex['xy']
            group = _svg(svg, 'g', {'data-vertex': vertex['id']})
            fill = '#fff'
            for layer in self.highlights:
                if vertex['id'] in layer['vertices']:
                    fill = layer['colour']
            hot = vertex['id'] in self.hovered
            selected = self.selected == vertex['id']
            attrs = dict(fill=_svg_colour(fill), stroke='#c026d3' if hot else '#dc2626' if selected else '#182538')
            attrs['stroke-width'] = 4 if hot or selected else 1.5
            if vertex['owner'] == 0:
                _svg(group, 'circle', dict(attrs, cx=x, cy=y, r=20))
            else:
                _svg(group, 'rect', dict(attrs, x=x-20, y=y-20, width=40, height=40))
            name = vertex['name'] or str(vertex['id'])
            _svg(group, 'text', {'x': x, 'y': y+4, 'text-anchor': 'middle'}, vertex['priority'])
            _svg(group, 'text', {'x': x, 'y': y+37, 'text-anchor': 'middle'}, name)
            _svg(group, 'title', text=f"{name}: priority {vertex['priority']}, {'Even' if vertex['owner'] == 0 else 'Odd'}")
        _svg(svg, 'text', dict(x=8, y=490), 'Circle: Even · Square: Odd')
        x = 8
        for layer in self.highlights:
            width = len(layer['name']) * 8 + 12
            _svg(svg, 'rect', dict(x=x, y=496, width=width, height=20, fill=_svg_colour(layer['colour'])))
            _svg(svg, 'text', dict(x=x+4, y=510), layer['name'])
            x += width + 4
        return ET.tostring(svg, encoding='unicode')


def _tree_data(tree, path=(), label=None):
    if isinstance(tree, Node):
        tree = tree.to_dict()
    if isinstance(tree, str):
        tree = json.loads(tree)
    if tree is None:
        return None
    if 'schema' in tree or ('tree' in tree and 'children' not in tree):
        return _tree_data(tree['tree'], path, label)
    children = []
    for i, child in enumerate(tree.get('children', [])):
        child_label = None
        if child is not None and 'node' in child:
            child_label, child = child['label'], child['node']
        node = _tree_data(child, path + (i,), child_label)
        if node is not None:
            children.append(node)
    vertices = set(tree.get('vertices') or [])
    for part in 'HTS':
        vertices.update(tree.get(part, []))
    for child in children:
        vertices.update(child['vertices'])
    name = tree.get('label', label)
    if name is None:
        name = 'ε' + ''.join(str(i + 1) for i in path)
        if 'h' in tree:
            name += f" (h={tree['h']})"
    return dict(label=name or 'ε', path=list(path), vertices=sorted(vertices),
                children=children, **{part: tree.get(part, []) for part in 'HTS'})


class TreeView(_View):
    """H/T/S Node/dict, genstree document, or PR #31 prefix-tree JSON.

    Assign ``tree`` to refresh. Hover propagates to the linked GameView.
    ``mode`` is 'boxes' or 'tree'; selected is a zero-based child-index path.
    """

    def __init__(self, tree=None, game_view=None, mode='boxes', **kwargs):
        self.game_view = game_view
        super().__init__(kind='tree', data=_tree_layout(tree), mode=mode, **kwargs)
        self.observe(self._hover, names='hovered')

    @property
    def tree(self):
        return self.data

    @tree.setter
    def tree(self, value):
        self.data = _tree_layout(value)

    def _hover(self, change):
        if self.game_view is not None:
            self.game_view.hovered = change['new']

    def _static_svg(self):
        if self.data is None:
            svg = _svg_root(300, 40, 'Empty tree')
            _svg(svg, 'text', dict(x=8, y=24), '∅ — empty tree')
        else:
            svg = _svg_root(*self.data['extent'][self.mode],
                            'H/T/S boxes' if self.mode == 'boxes' else 'Ordered tree')

            def visit(n, parent):
                if self.mode == 'boxes':
                    x, y, w, h = n['box']
                    group = _svg(parent, 'g', {'data-path': json.dumps(n['path'], separators=(',', ':'))})
                    _svg(group, 'rect', dict(x=x, y=y, width=w, height=h, fill='#fff', stroke='#64748b'))
                    _svg(group, 'text', dict(x=x+6, y=y+18, style='font-weight:bold'), n['label'])
                    for part, dx, dy, width, height, colour in [
                        ('S', 6, 28, w-12, h-34, '#ffedd5'),
                        ('T', 12, 56, w-24, h-68, '#dcfce7'),
                        ('H', 18, h-46, w-36, 28, '#dbeafe')]:
                        _svg(group, 'rect', dict(x=x+dx, y=y+dy, width=width, height=height,
                                                fill=colour, stroke='#64748b', **{'class': f'part-{part}'}))
                        _svg(group, 'text', dict(x=x+dx+6, y=y+dy+18),
                             f"{part}: {', '.join(map(str, n[part])) or '∅'}")
                    for child in n['children']:
                        visit(child, group)
                else:
                    x, y = n['xy']
                    for child in n['children']:
                        u, v = child['xy']
                        _svg(svg, 'line', dict(x1=x, y1=y, x2=u, y2=v, stroke='#94a3b8'))
                        visit(child, svg)
                    group = _svg(svg, 'g', {'data-path': json.dumps(n['path'], separators=(',', ':'))})
                    _svg(group, 'rect', dict(x=x-58, y=y-17, width=116, height=34, rx=5,
                                            fill='#dbeafe', stroke='#64748b'))
                    _svg(group, 'text', {'x': x, 'y': y+4, 'text-anchor': 'middle'}, n['label'])
                    _svg(group, 'title', text=f"{n['label']}: {', '.join(map(str, n['vertices']))}")

            visit(self.data, svg)
        return ET.tostring(svg, encoding='unicode')


_PLAIN = [
    'McNZEven(G, h, ε, ω)  [McNZOdd exchanges players]',
    'If G is empty, return ∅ (paper base: h=0 before priority normalization)',
    'G₁ ← G; i ← 0',
    'Repeat:',
    '  i ← i+1; H_i ← priority-h vertices in G_i',
    '  A_i ← Attr_Even^G_i(H_i)',
    '  G′_i ← G_i \\ A_i',
    '  U′_i ← McNZOdd(G′_i, h−1, ω·i, ε)',
    '  A′_i ← Attr_Odd^G_i(U′_i)',
    '  S_Odd(ω·i) ← A′_i \\ U′_i; G_{i+1} ← G_i \\ A′_i',
    'Until G_{i+1} = G_i',
    'H_Even(ε) ← H_i; T_Even(ε) ← A_i \\ H_i',
    'Return G_i',
]
_MEMORY = [
    'McNZFastEven(G, h, ε, ω)  [McNZFastOdd exchanges players]',
    'If the Even candidate at ε restricted to G is an AD:',
    '  Set S_Odd(ω) to G; return G',
    'If the Odd candidate at ω restricted to G is an AD:',
    '  Set S_Even(ε) to G; return ∅',
    'G₁ ← G; i ← 0',
    'Repeat with the next child ω·i:',
    '  H_i ← priority-h vertices; A_i ← Attr_Even^G_i(H_i)',
    '  Set/Move top fibres using A_i and H_i',
    '  Remove the escaping attractor from the retained child (entry correction)',
    '  G′_i ← the resulting child core in G_i',
    '  U′_i ← McNZFastOdd(G′_i, h−1, ω·i, ε)',
    '  S′_i ← Attr_Odd^G_i(U′_i)',
    '  Set S_Odd(ω·i) to S′_i \\ U′_i',
    '  Move S′_i to at least S_Even(ε)',
    '  G_{i+1} ← G_i \\ S′_i',
    'Until the Even candidate restricted to G_{i+1} is an AD',
    'Return G_{i+1}  [corrected residual index]',
]
_LIFTING = [
    'Build the Strahler host for each player',
    'Initialize the least priority-compatible H/T/S labels',
    'Short-lift an unstable vertex to its next valid label',
    'End the round; repeat until labels stabilize',
    'Adaptive host: raise t and repeat if needed',
    'Iterative shaving: attract certified winners; restart on the residual',
    'Materialize and independently check the resulting certificates',
]


def _controls_html(data):
    def paragraph(text):
        return '<p>' + escape(text) + '</p>'
    html = paragraph(f"{data['index']} / {data['length']-1}: {data['event']['event']}")
    for badge in data['badges']:
        claim = badge['claim']
        player = 'Even' if badge['player'] == 0 else 'Odd'
        text = (f"{claim['event']['is_attractor_decomposition']} at step {claim['index']}, "
                f"path {claim['event']['path']}, G={claim['event']['subgame']}"
                if claim else 'no check event yet')
        html += paragraph(f'{player} — algorithm claim: {text}')
        html += paragraph(f"Independent: {'✔' if badge['ok'] else '✘'} {badge['status']} "
                          f"on G={badge['domain']}; condition {badge['condition']}; "
                          f"path {badge['path']}; vertex {badge['vertex']}. {badge['message']}")
        if badge['problems']:
            html += paragraph('Materializer: ' + json.dumps(badge['problems']))
    return html


class Stepper(VBox):
    """Recorded trace with step/back/next/end/seek and independent badges.

    ``state`` is the public package State. ``verify(player)`` checks the current
    candidate and restriction; ``badges`` keeps recorded claims separately.
    ``call_tree()`` returns a TreeView whose selected call jumps this Stepper.
    Keep trace.game open for as long as the widget is used.
    """

    def __init__(self, run, coordinates=None, checkpoint_interval=None, **kwargs):
        self.run = run
        self.cursor = TraceCursor(run, checkpoint_interval)
        self.game_view = GameView(run.game, coordinates)
        self.tree_views = tuple(TreeView(game_view=self.game_view) for _ in range(2))
        self.controls = _View(kind='controls')
        self.controls.next_kind = 'call' if 'call' in self.cursor.kinds else 'lift'
        self.controls.on_msg(self._message)
        super().__init__(children=[self.controls, self.game_view, HBox(self.tree_views,
                         layout=Layout(overflow='auto'))], **kwargs)
        self.seek(0)

    def _repr_mimebundle_(self, **kwargs):
        bundle = super()._repr_mimebundle_(**kwargs)
        bundle['text/plain'] = f"Step {self.index}: {self.state.event['event']}"
        bundle['text/html'] = (_controls_html(self.controls.data) + self.game_view._static_svg() +
                               ''.join(view._static_svg() for view in self.tree_views))
        return bundle

    @property
    def index(self):
        return self.cursor.index

    def seek(self, index):
        self.state = self.cursor.seek(index)
        self.badges = [self.cursor.badge(p) for p in range(2)]
        for view, tree in zip(self.tree_views, self.state.trees):
            view.tree = tree
        self.game_view.highlights = []
        self.game_view.highlight(self.cursor.subgame, '#dbeafe', 'current subgame')
        colours = {'G_i': '#dbeafe', 'A_i': '#bbf7d0', 'H_i': '#fef08a', "U′_i": '#fed7aa', 'side attractor': '#e9d5ff'}
        if self.cursor.stack:
            sets = self.cursor.stack[-1]['sets']
            for name, colour in colours.items():
                if name in sets:
                    self.game_view.highlight(sets[name], colour, name)
        frames = []
        backend = self.run.events[0]['algorithm']
        memory = backend.endswith('-sym')
        procedure = 'UnivFast' if backend == 'lifting-sym' else ('McNZFast' if memory else 'McNZ')
        for frame in self.cursor.stack:
            event = frame['event']
            player = 'Even' if event['player'] == 0 else 'Odd'
            frames.append(f"{procedure}{player}(G={event['subgame']}, h={event['h']}, ε={event['paths'][0]}, ω={event['paths'][1]})")
        event = self.state.event
        kind = event['event']
        code = _MEMORY if memory else _PLAIN
        if backend == 'lifting-sym':
            code = list(_MEMORY)
            code[0] = 'UnivFastEven(G, h, ε, ω)  [UnivFastOdd exchanges players]'
            code[16] = 'Continue through all host children; finish with short-lift certification'
        # Trace events group multiple C statements; highlight a semantic block.
        if memory:
            frame = self.cursor.stack[-1] if self.cursor.stack else {}
            previous = frame.get('last_attractor', {})
            lower = frame.get('event', {}).get('player')
            if kind == 'check':
                line = 16 if previous else (1 if event['player'] == lower else 3)
            elif kind == 'attractor':
                line = 7 if event['kind'] == 'top' else (9 if event['player'] == lower else 12)
            elif kind in ('set', 'move', 'labels'):
                line = 8 if previous.get('kind') == 'top' else (9 if previous.get('player') == lower else 14)
            else:
                line = 17 if kind == 'return' else 0
        else:
            line = {'call': 0, 'attractor': 5 if event.get('kind') == 'top' else 8,
                    'set': 11, 'move': 9, 'return': 12}.get(kind, 0)
        if backend == 'lifting':
            code = _LIFTING
            line = {'lift': 2, 'labels': 2, 'round_end': 3, 'result': 6}.get(kind, 0)
            if kind == 'phase':
                line = {'labels_reset': 1, 't_raised': 4, 'shave_applied': 5,
                        'dominion_certified': 6}.get(event['phase'], 0)
        note = 'Yellow marks the current semantic block, not a one-to-one C source line.'
        if memory:
            note += ' Entry correction: allow the higher player’s S fibre (root S = TOP), and remove the escaping attractor before recursion; see docs/symmetric.md.'
        self.controls.data = dict(index=self.index, length=len(self.run), event=event,
                                  stack=frames, badges=self.badges, kinds=list(self.cursor.kinds),
                                  pseudocode=code, line=line, ticks=self.cursor.ticks, note=note)
        return self.state

    def step(self):
        return self.seek(min(self.index + 1, len(self.run) - 1))

    def back(self):
        return self.seek(max(0, self.index - 1))

    def next(self, kind='call'):
        return self.seek(self.cursor.next_index(kind))

    def end(self):
        return self.seek(len(self.run) - 1)

    def verify(self, player):
        return self.cursor.verify(player)

    def _message(self, widget, content, buffers):
        command = content.get('command')
        if command == 'seek':
            self.seek(content['index'])
        elif command == 'next':
            self.next(content['kind'])
        elif command in ('step', 'back', 'end'):
            getattr(self, command)()

    def call_tree(self):
        nodes, roots = {}, []
        indices = {}
        for call in self.cursor.calls:
            e = call['event']
            node = dict(label=f"#{call['index']} {'E' if e['player'] == 0 else 'O'} h={e['h']}",
                        vertices=e['subgame'], children=[])
            if call['parent'] is None:
                path = (len(roots),)
                roots.append(node)
            else:
                parent, parent_path = nodes[call['parent']]
                path = parent_path + (len(parent['children']),)
                parent['children'].append(node)
            nodes[call['index']] = node, path
            indices[path] = call['index']
        view = TreeView(dict(label='calls', children=roots), game_view=self.game_view, mode='tree')
        def jump(change):
            if tuple(change['new'] or ()) in indices:
                self.seek(indices[tuple(change['new'])])
        view.observe(jump, names='selected')
        view.on_msg(lambda widget, content, buffers: jump(dict(new=content['path']))
                    if content.get('command') == 'select' else None)
        return view
