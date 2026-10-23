"""Version discovery in real temporary repositories and source archives."""

import importlib.util
from io import BytesIO
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('version', ROOT / 'ci/version.py')
version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(version)


class VersionTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix='strahler version ')
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        env = patch.dict(os.environ)
        env.start()
        self.addCleanup(env.stop)
        os.environ.pop('STRAHLER_VERSION', None)

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def repository(self):
        self.git('init', '-q')
        self.git('config', 'user.name', 'Version test')
        self.git('config', 'user.email', 'version@example.invalid')
        self.git('config', 'commit.gpgsign', 'false')
        self.git('config', 'tag.gpgsign', 'false')
        self.git('config', 'core.abbrev', '7')
        (self.root / 'tracked').write_text('original\n')
        self.git('add', 'tracked')
        self.git('commit', '-qm', 'initial')
        self.git('tag', 'v0.3.1')

    def test_exact_tag(self):
        self.repository()
        self.assertEqual(version.get_version(self.root), '0.3.1')
        self.git('tag', '-d', 'v0.3.1')
        self.git('tag', '-a', 'v0.4.0', '-m', 'release')
        self.assertEqual(version.get_version(self.root), '0.4.0')

    def test_commits_after_tag(self):
        self.repository()
        for _ in range(2):
            self.git('commit', '--allow-empty', '-qm', 'next')
        commit = self.git('rev-parse', '--short', 'HEAD')
        self.assertEqual(version.get_version(self.root), f'0.3.2.dev2+g{commit}')

    def test_dirty(self):
        self.repository()
        (self.root / 'tracked').write_text('changed\n')
        self.assertEqual(version.get_version(self.root), '0.3.1+dirty')
        self.git('commit', '--allow-empty', '-qm', 'next')
        commit = self.git('rev-parse', '--short', 'HEAD')
        self.assertEqual(version.get_version(self.root), f'0.3.2.dev1+g{commit}.dirty')

    def test_environment_override(self):
        self.repository()
        for value in ('0.4.0', '0.4.0rc1', '1!0.4.0.post1.dev2+build.3'):
            with self.subTest(value=value):
                os.environ['STRAHLER_VERSION'] = value
                self.assertEqual(version.get_version(self.root), value)
        for value in ('', 'bad', '0.4.0; echo bad', '0.4.0\n', '0.4.0+bad/path'):
            with self.subTest(value=value):
                os.environ['STRAHLER_VERSION'] = value
                with self.assertRaisesRegex(ValueError, 'PEP 440'):
                    version.get_version(self.root)

    def test_archival_fallback(self):
        self.repository()
        for name in ('.gitattributes', '.git_archival.txt'):
            shutil.copyfile(ROOT / name, self.root / name)
        self.git('add', '.gitattributes', '.git_archival.txt')
        self.git('commit', '-qm', 'archive metadata')
        for tagged in (False, True):
            if tagged:
                self.git('tag', 'v0.4.0')
            expected = version.get_version(self.root)
            archive = subprocess.check_output(['git', '-C', str(self.root), 'archive', 'HEAD'])
            with tarfile.open(fileobj=BytesIO(archive)) as tar:
                metadata = tar.extractfile('.git_archival.txt').read()
            with tempfile.TemporaryDirectory() as copied:
                source = Path(copied)
                (source / '.git_archival.txt').write_bytes(metadata)
                self.assertEqual(version.get_version(source), expected)

    def test_frozen_version(self):
        (self.root / 'VERSION').write_text('0.3.2.dev19+g1234567.dirty\n')
        shutil.copyfile(ROOT / '.git_archival.txt', self.root / '.git_archival.txt')
        self.assertEqual(version.get_version(self.root), '0.3.2.dev19+g1234567.dirty')
        os.environ['STRAHLER_VERSION'] = '0.4.0'
        self.assertEqual(version.get_version(self.root), '0.4.0')

    def test_git_takes_precedence_over_frozen_version(self):
        self.repository()
        (self.root / 'VERSION').write_text('99.0.0\n')
        self.assertEqual(version.get_version(self.root), '0.3.1')

    def test_unavailable_git(self):
        self.repository()
        for failure in (FileNotFoundError('git'), subprocess.CompletedProcess(
                ['git'], 128, '', 'fatal: detected dubious ownership')):
            with self.subTest(failure=failure):
                with patch.object(version.subprocess, 'run', side_effect=(
                        failure if isinstance(failure, Exception) else None), return_value=failure):
                    (self.root / '.git_archival.txt').write_text('v0.4.0\n')
                    self.assertEqual(version.get_version(self.root), '0.4.0')
                    (self.root / 'VERSION').write_text('0.5.0\n')
                    self.assertEqual(version.get_version(self.root), '0.5.0')
                    (self.root / 'VERSION').unlink()

    def test_no_metadata_fails(self):
        shutil.copyfile(ROOT / '.git_archival.txt', self.root / '.git_archival.txt')
        with self.assertRaisesRegex(ValueError, 'Fetch Git tags'):
            version.get_version(self.root)
        (self.root / 'ci').mkdir()
        shutil.copyfile(ROOT / 'ci/version.py', self.root / 'ci/version.py')
        result = subprocess.run([sys.executable, str(self.root / 'ci/version.py')],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('STRAHLER_VERSION', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_no_tags_fails(self):
        self.repository()
        self.git('tag', '-d', 'v0.3.1')
        with self.assertRaisesRegex(ValueError, 'Fetch Git tags'):
            version.get_version(self.root)

    def test_dist_freezes_configured_version(self):
        env = dict(os.environ, MESON_DIST_ROOT=str(self.root))
        subprocess.run([sys.executable, str(ROOT / 'ci/version.py'), '--dist', '0.4.0'],
                       env=env, check=True)
        self.assertEqual(version.get_version(self.root), '0.4.0')


if __name__ == '__main__':
    unittest.main()
