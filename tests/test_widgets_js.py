"""Check the inline ESM without importing optional Python widget dependencies."""

import ast
import os
from pathlib import Path
import shutil
import subprocess

import pytest

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
