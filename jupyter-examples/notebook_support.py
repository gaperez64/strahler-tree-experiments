"""Offline presentation helpers for examples using the public strahler API."""

from html import escape
from pathlib import Path

import strahler
from IPython.display import HTML, display
from ipywidgets import Button, HBox, Output, Textarea, VBox
from strahler.widgets import Stepper

HERE = Path(__file__).resolve().parent
BACKENDS = ('zielonka', 'zielonka-sym', 'lifting', 'lifting-sym')


def metrics_table(results):
    rows = []
    for name, result in results.items():
        for player, metrics in enumerate(result.metrics['trees']):
            rows.append([name, 'Even' if player == 0 else 'Odd',
                         *(metrics[key] for key in ('nodes', 'leaves', 'height', 'strahler')),
                         len(result.regions[player]), result.complete, len(result.unresolved)])
    table(['backend', 'player', 'nodes', 'leaves', 'height', 'Strahler', 'residual won', 'complete', 'unresolved'], rows)


def table(headers, rows):
    def cells(tag, row):
        return ''.join(f'<{tag}>{escape(str(value))}</{tag}>' for value in row)
    display(HTML('<table><thead><tr>' + cells('th', headers) + '</tr></thead><tbody>' +
                 ''.join('<tr>' + cells('td', row) + '</tr>' for row in rows) + '</tbody></table>'))


def comparison(text, coordinates=None):
    """Show both recursive algorithms with linked views and clickable call trees."""
    game = strahler.Game.from_text(text)
    steppers = [Stepper(strahler.trace(game, algorithm), coordinates) for algorithm in BACKENDS[:2]]
    for stepper in steppers:
        stepper.next('call')
    return VBox([HBox(steppers), HBox([stepper.call_tree() for stepper in steppers])])


def close_views(widget):
    """Release widget comms and recordings when an editor or slider replaces them."""
    for child in getattr(widget, 'children', ()):
        close_views(child)
    widget.close()


def editor(text, solve=comparison):
    """Parse and solve PGSolver text; keep parser diagnostics visible."""
    field = Textarea(value=text, description='PGSolver', layout={'width': '100%', 'height': '200px'})
    button = Button(description='Parse and solve', button_style='primary')
    output = Output()
    rendered = None
    def run(_):
        nonlocal rendered
        with output:
            output.clear_output(wait=True)
            if rendered is not None:
                close_views(rendered)
                rendered = None
            try:
                rendered = solve(field.value)
                display(rendered)
            except (strahler.StrahlerError, ValueError) as error:
                print(f'Cannot solve this input: {error}')
    button.on_click(run)
    run(None)
    return VBox([field, button, output])


def call_count_plot(counts):
    """Draw a self-contained SVG plot with a logarithmic call-count axis."""
    from math import log10
    colours = {'zielonka': '#1d4ed8', 'zielonka-sym': '#b45309'}
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" '
             'aria-label="Recursive calls on H k, logarithmic scale"><rect width="760" height="340" fill="white"/>']
    for power in range(6):
        y = 280 - power * 48
        parts.append(f'<path d="M65 {y}H700" stroke="#cbd5e1"/><text x="5" y="{y+4}">10^{power}</text>')
    for name, values in counts.items():
        points = ' '.join(f'{75+i*85},{280-log10(value)*48}' for i, value in enumerate(values))
        parts.append(f'<polyline fill="none" stroke="{colours[name]}" stroke-width="3" points="{points}"/>')
    for i, k in enumerate(range(2, 17, 2)):
        parts.append(f'<text x="{75+i*85}" y="305">{k}</text>')
    parts.append('<text x="330" y="330">k (5k vertices)</text>')
    parts.append('<text x="80" y="20" fill="#1d4ed8">zielonka</text><text x="250" y="20" fill="#b45309">zielonka-sym</text></svg>')
    display(HTML(''.join(parts)))
