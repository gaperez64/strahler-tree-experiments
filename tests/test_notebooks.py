"""Check saved outputs and execute copies with this interpreter's kernel."""

import json
import os
from pathlib import Path
import re
import sys
from time import perf_counter

import pytest

EXAMPLES = Path(__file__).resolve().parents[1] / 'jupyter-examples'
NOTEBOOKS = sorted(EXAMPLES.glob('*.ipynb'))


@pytest.fixture
def executor():
    import importlib.util
    pytest.importorskip('nbclient')
    pytest.importorskip('anywidget')
    spec = importlib.util.spec_from_file_location('execute_notebooks',
                EXAMPLES.parent / 'scripts/execute_notebooks.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_save_is_deterministic_without_a_kernel(executor, tmp_path, monkeypatch):
    import nbformat
    import strahler
    from ipywidgets import VBox, Output, IntSlider, Textarea
    from strahler.widgets import Stepper

    path = tmp_path / 'example.ipynb'
    notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('example()')])
    notebook.metadata.widgets = {'stale': 'state'}
    notebook.cells[0].metadata.execution = {'old': 'timing'}
    nbformat.write(notebook, path)
    kernels = tmp_path / 'kernels'
    spec = kernels / 'strahler-examples'
    spec.mkdir(parents=True)
    argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
    (spec / 'kernel.json').write_text(json.dumps(dict(argv=argv, display_name='test', language='python')))
    model_ids = []

    class Client:
        def __init__(self, notebook, **kwargs):
            self.notebook = notebook
            assert kwargs['timeout'] == 60 and kwargs['record_timing'] is False
            assert kwargs['allow_errors'] is False
            assert kwargs['resources']['metadata']['path'] == str(tmp_path)
            assert kwargs['km'].kernel_spec.argv == argv

        def execute(self, **kwargs):
            assert kwargs['cleanup_kc'] is True and kwargs['env']['PATH'] == os.environ['PATH']
            with strahler.Game.from_text('0 2 0 0,1 "<a&b>"; 1 1 1 1;') as game:
                stepper = Stepper(strahler.trace(game, 'zielonka-sym'))
                stepper.next('check')
                captured = Output(outputs=[nbformat.v4.new_output('stream', name='stdout', text='<captured>')])
                panel = VBox([stepper, stepper.call_tree(), captured,
                              IntSlider(value=4, description='k'), Textarea(value='<input>')])
                self.widget_state = {}
                def collect(widget):
                    self.widget_state[widget.model_id] = widget.get_state()
                    for child in getattr(widget, 'children', ()):
                        collect(child)
                collect(panel)
                model_ids.append(panel.model_id)
                self.notebook.cells[0].execution_count = 1
                self.notebook.cells[0].outputs = [nbformat.v4.new_output(
                    'display_data', data=panel._repr_mimebundle_())]

    monkeypatch.setattr(executor, 'NotebookClient', Client)
    executor.execute_notebook(path, kernels)
    first = path.read_bytes()
    saved = nbformat.read(path, as_version=4)
    assert 'widgets' not in saved.metadata and 'execution' not in saved.cells[0].metadata
    assert saved.cells[0].execution_count == 1
    data = saved.cells[0].outputs[0].data
    assert executor.WIDGET_MIME not in data
    html = data['text/html']
    assert html.count('<svg') == 4
    for text in ('&lt;a&amp;b&gt;', '&lt;captured&gt;', 'k: 4', '&lt;input&gt;', 'algorithm claim:', 'Independent:'):
        assert text in html
    executor.execute_notebook(path, kernels)
    assert model_ids[0] != model_ids[1]
    assert first == path.read_bytes()
    assert not path.with_suffix('.ipynb.tmp').exists()

    def fail(*args, **kwargs):
        raise RuntimeError('execution failed')
    monkeypatch.setattr(Client, 'execute', fail)
    with pytest.raises(RuntimeError, match='execution failed'):
        executor.execute_notebook(path, kernels)
    assert first == path.read_bytes()


def test_freeze_rejects_errors_and_volatile_output(executor):
    import nbformat
    error = nbformat.v4.new_output('error', ename='ValueError', evalue='bad input', traceback=[])
    notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('')])
    notebook.cells[0].outputs = [error]
    with pytest.raises(ValueError, match='Notebook error'):
        executor.freeze_outputs(notebook, {})
    notebook.cells[0].outputs = []
    with pytest.raises(ValueError, match='Notebook error'):
        executor.freeze_outputs(notebook, {'output-widget': {'outputs': [error]}})
    for text in ('/home/someone/build', '<Game at 0x12345678>'):
        notebook.cells[0].outputs = [nbformat.v4.new_output('stream', name='stdout', text=text)]
        with pytest.raises(ValueError, match='Volatile output'):
            executor.freeze_outputs(notebook, {})


def test_six_notebooks_and_version_mismatch(monkeypatch, capsys):
    assert len(NOTEBOOKS) == 6
    import importlib.metadata
    from types import SimpleNamespace
    monkeypatch.setitem(sys.modules, 'strahler', SimpleNamespace(version=lambda: '0.0.1'))
    monkeypatch.setattr(importlib.metadata, 'version', lambda name: '0.0.2')
    setup = ''.join(json.loads(NOTEBOOKS[0].read_text())['cells'][0]['source'])
    with pytest.raises(RuntimeError, match='version mismatch'):
        exec(compile(setup, str(NOTEBOOKS[0]), 'exec'), {})
    assert 'package 0.0.2; libstrahler 0.0.1' in capsys.readouterr().out


@pytest.mark.parametrize('path', NOTEBOOKS, ids=lambda path: path.name)
def test_saved_outputs(path):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    assert 'widgets' not in notebook['metadata']
    counts = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            counts.append(cell['execution_count'])
            assert isinstance(cell['execution_count'], int) and cell['execution_count'] > 0, (
                f'{path}: rerun scripts/execute_notebooks.py')
            assert 'execution' not in cell['metadata']
            assert not list(errors(cell)), path
            for output in cell['outputs']:
                data = output.get('data', {})
                if ('application/vnd.jupyter.widget-view+json' in data or
                    ''.join(data.get('text/plain', [])).startswith('Static widget snapshot;')):
                    assert data.get('image/svg+xml') or data.get('text/html'), path
                if output['output_type'] == 'execute_result':
                    assert output['execution_count'] == cell['execution_count']
            compile(''.join(cell['source']), str(path), 'exec')
    assert counts and all(a < b for a, b in zip(counts, counts[1:])), path
    assert any(cell.get('outputs') for cell in notebook['cells']), path
    first = ''.join(notebook['cells'][0]['source'])
    assert 'import strahler' in first and 'package_version' in first and 'strahler.version()' in first


@pytest.mark.parametrize('path', NOTEBOOKS, ids=lambda path: path.name)
def test_saved_version_is_current(path):
    meson = (EXAMPLES.parent / 'meson.build').read_text(encoding='utf-8')
    version = re.search(r"version\s*:\s*'([^']+)'", meson)[1]
    first = json.loads(path.read_text(encoding='utf-8'))['cells'][0]
    text = ''.join(''.join(output.get('text', [])) for output in first['outputs'])
    assert f'strahler package {version}; libstrahler {version}\n' in text, (
        f'{path}: saved version is stale; rerun scripts/execute_notebooks.py')


def errors(value):
    if isinstance(value, dict):
        if value.get('output_type') == 'error':
            yield value
        for child in value.values():
            yield from errors(child)
    elif isinstance(value, list):
        for child in value:
            yield from errors(child)


@pytest.mark.parametrize('path', NOTEBOOKS, ids=lambda path: path.name)
def test_execute_notebook(path, tmp_path):
    nbformat = pytest.importorskip('nbformat', reason='nbformat is needed for headless notebooks')
    nbclient = pytest.importorskip('nbclient', reason='nbclient is needed for headless notebooks')
    pytest.importorskip('ipykernel')
    pytest.importorskip('anywidget')
    from jupyter_client import KernelManager
    from jupyter_client.kernelspec import KernelSpecManager

    kernels = tmp_path / 'kernels'
    spec = kernels / 'strahler-test'
    spec.mkdir(parents=True)
    (spec / 'kernel.json').write_text(json.dumps(dict(
        argv=[sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        display_name='strahler test venv', language='python')))
    manager = KernelManager(kernel_name='strahler-test',
                            kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(kernels)]))
    notebook = nbformat.read(path, as_version=4)
    client = nbclient.NotebookClient(notebook, km=manager, timeout=60, allow_errors=False,
                                    resources={'metadata': {'path': str(EXAMPLES)}})
    started = perf_counter()
    # Test kernels inherit STRAHLER_LIB/PYTHONPATH from Meson or the wheel job.
    client.execute(cleanup_kc=True, env={**os.environ, 'IPYTHONDIR': str(tmp_path / 'ipython'),
                        'JUPYTER_CONFIG_DIR': str(tmp_path / 'jupyter')})
    elapsed = perf_counter() - started
    assert not list(errors(notebook)), list(errors(notebook))
    print(f'{path.name}: {elapsed:.2f}s')
