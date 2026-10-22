"""Execute cleared notebooks with nbclient and this test interpreter's kernel."""

import json
import os
from pathlib import Path
import sys
from time import perf_counter

import pytest

EXAMPLES = Path(__file__).resolve().parents[1] / 'jupyter-examples'
NOTEBOOKS = sorted(EXAMPLES.glob('*.ipynb'))


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
def test_outputs_are_cleared(path):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    assert 'widgets' not in notebook['metadata']
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            assert cell['execution_count'] is None and cell['outputs'] == [], path
            compile(''.join(cell['source']), str(path), 'exec')
    first = ''.join(notebook['cells'][0]['source'])
    assert 'import strahler' in first and 'package_version' in first and 'strahler.version()' in first


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
    client.execute(env={**os.environ, 'IPYTHONDIR': str(tmp_path / 'ipython'),
                        'JUPYTER_CONFIG_DIR': str(tmp_path / 'jupyter')})
    elapsed = perf_counter() - started
    assert not list(errors(notebook)), list(errors(notebook))
    print(f'{path.name}: {elapsed:.2f}s')
