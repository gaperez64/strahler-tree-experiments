#!/usr/bin/env python3
"""Resolve the build version without third-party modules or network access."""

import os
from pathlib import Path
import re
import subprocess
import sys


def validate(version):
    # Canonical PEP 440 syntax, including epochs, pre/post/dev and local versions.
    if not re.fullmatch(
        r'(?:[0-9]+!)?[0-9]+(?:\.[0-9]+)*(?:(?:a|b|rc)[0-9]+)?'
        r'(?:\.post[0-9]+)?(?:\.dev[0-9]+)?'
        r'(?:\+[a-z0-9]+(?:\.[a-z0-9]+)*)?', version
    ):
        raise ValueError(f'Invalid version {version!r}; use a canonical PEP 440 version')
    return version


def from_describe(description):
    match = re.fullmatch(
        r'v([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9]+)-g([0-9a-f]+))?(-dirty)?',
        description,
    )
    if not match:
        raise ValueError(f'Invalid Git version {description!r}; release tags must be vX.Y.Z')
    major, minor, patch, distance, commit, dirty = match.groups()
    version = f'{major}.{minor}.{patch}'
    if distance:
        version = f'{major}.{minor}.{int(patch) + 1}.dev{distance}+g{commit}'
    if dirty:
        version += '.dirty' if '+' in version else '+dirty'
    return validate(version)


def get_version(source):
    if 'STRAHLER_VERSION' in os.environ:
        return validate(os.environ['STRAHLER_VERSION'])
    # A source copy must never inherit an enclosing repository's tags.
    if (source / '.git').exists():
        try:
            result = subprocess.run(
                ['git', '-C', str(source), 'describe', '--tags', '--match', 'v[0-9]*', '--dirty'],
                capture_output=True, text=True, check=False,
            )
        except OSError:
            pass
        else:
            if result.returncode == 0:
                return from_describe(result.stdout.strip())
    frozen = source / 'VERSION'
    if frozen.is_file():
        return validate(frozen.read_text(encoding='utf-8').strip())
    archival = source / '.git_archival.txt'
    if archival.is_file():
        description = archival.read_text(encoding='utf-8').strip()
        if description and not description.startswith('$Format:'):
            return from_describe(description)
    raise ValueError('Cannot determine Strahler version. Fetch Git tags, use an sdist or '
                     'Git archive with version metadata, or set STRAHLER_VERSION (PEP 440).')


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3 and sys.argv[1] == '--dist':
            (Path(os.environ['MESON_DIST_ROOT']) / 'VERSION').write_text(
                validate(sys.argv[2]) + '\n', encoding='utf-8')
        else:
            print(get_version(Path(__file__).resolve().parents[1]))
    except (OSError, ValueError) as error:
        sys.exit(f'strahler version: {error}')
