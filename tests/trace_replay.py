"""Compatibility import for trace regressions and their tiny C checker."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'python'))
from strahler._replay import Replay, check_input, vertices

__all__ = ['Replay', 'check_input', 'vertices']
