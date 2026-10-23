"""Ownership and signatures for the stable C ABI (implementation detail)."""

import ctypes as C
from ctypes.util import find_library
import os
from pathlib import Path
import re
import sysconfig


class StrahlerError(RuntimeError):
    """Native failure; ``status`` retains the CLI/API exit code."""

    def __init__(self, message, status):
        super().__init__(message)
        self.status = status


class InputError(StrahlerError, ValueError):
    """Invalid game, tree, or CLI option."""


Callback = C.CFUNCTYPE(C.c_int, C.c_void_p, C.c_void_p, C.c_size_t)
_library = None


def library():
    global _library
    if _library is None:
        override = os.environ.get('STRAHLER_LIB')
        directory = (Path(override) if override else
                     Path(__file__).resolve().parent.parent / '.strahler.mesonpy.libs')
        if not override and not directory.is_dir():
            directory = Path(sysconfig.get_path('platlib')) / '.strahler.mesonpy.libs'
        if directory.is_dir():
            candidates = [directory / name for name in
                          ('libstrahler.so', 'libstrahler.dylib')]
            candidates.extend(sorted(directory.glob('libstrahler.so.*')))
            candidates.extend(sorted(directory.glob('libstrahler.*.dylib')))
            path = next((p for p in candidates if p.is_file()), None)
            if path is None:
                raise ImportError(f'libstrahler not found in {directory}; set STRAHLER_LIB')
        elif override:
            path = directory
        else:
            path = None
        name = str(path.resolve()) if path else find_library('strahler')
        if name is None:
            raise ImportError('libstrahler not found; set STRAHLER_LIB')
        lib = C.CDLL(name)
        try:
            lib.strahler_version.argtypes = []
            lib.strahler_version.restype = C.c_char_p
            native_version = lib.strahler_version()
        except AttributeError as error:
            raise ImportError('libstrahler is missing strahler_version (expected ABI 0.3.x)') from error
        # The pre-1.0 ABI is compatible only within the 0.3 release series.
        if re.fullmatch(rb'0\.3\.[0-9]+', native_version or b'') is None:
            raise ImportError(f'Unsupported libstrahler ABI {native_version!r}; expected 0.3.x')
        pointer = C.c_void_p
        output = C.POINTER(pointer)
        args = C.POINTER(C.c_char_p)
        signatures = {
            'game_parse': [C.c_char_p, C.c_size_t, output, output],
            'game_summary': [pointer, output, output],
            'decompose': [pointer, args, C.c_int, Callback, pointer, output, output],
            'progress_measures': [pointer, args, C.c_int, output, output],
            'check': [pointer, C.c_char_p, C.c_int, C.c_char_p, C.c_int, output, output],
            'materialize_partial': [pointer, C.c_char_p, C.c_int, output, output],
            'genstree': [C.c_int, C.c_int, C.c_int, output, output],
            'pms_tree': [C.c_char_p, C.c_size_t, args, C.c_int, output, output],
        }
        try:
            for name, signature in signatures.items():
                function = getattr(lib, 'strahler_' + name)
                function.argtypes = signature
                function.restype = C.c_int
            for name in ('free', 'game_free'):
                function = getattr(lib, 'strahler_' + name)
                function.argtypes = [pointer]
                function.restype = None
        except AttributeError as error:
            raise ImportError(f'libstrahler ABI 0.3.x is missing a required symbol: {error}') from error
        _library = lib
    return _library


def call(name, *arguments, handle=False):
    lib = library()
    value, error = C.c_void_p(), C.c_void_p()
    try:
        status = getattr(lib, 'strahler_' + name)(
            *arguments, C.byref(value), C.byref(error))
        if status:
            message = C.string_at(error).decode('utf-8', 'replace').strip() if error.value else 'Native allocation failure'
            exception = InputError if status in (2, 3) else StrahlerError
            if status == 6:
                raise MemoryError(message)
            raise exception(message, status)
        if handle:
            result = value
            value = C.c_void_p()
            return result
        return C.string_at(value).decode('utf-8')
    finally:
        if value.value:
            lib.strahler_free(value)
        if error.value:
            lib.strahler_free(error)


def options(args, keywords, algorithm=None):
    flags = [] if algorithm is None else [f'--algorithm={algorithm}']
    for key, value in keywords.items():
        flag = '--' + key.replace('_', '-')
        if value is True:
            flags.append(flag)
        elif value is not False and value is not None:
            flags.append(f'{flag}={os.fspath(value) if isinstance(value, os.PathLike) else value}')
    flags.extend(args or ())
    if any(not isinstance(flag, str) or '\0' in flag for flag in flags):
        raise ValueError('Options must be strings without NUL bytes')
    return (C.c_char_p * len(flags))(*(flag.encode('utf-8') for flag in flags))
