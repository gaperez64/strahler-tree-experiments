#!/usr/bin/env python3
"""Compare checked pg2adot witnesses; Python stdlib only. See docs/disagreements.md."""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
import html
import json
import os
from pathlib import Path
import random
import re
import resource
import shlex
import subprocess
import time


@dataclass(frozen=True)
class Node:
    bound: int
    region: tuple
    top: tuple
    children: tuple  # (attractor, child); child.region is the incoming trap

    def shape(self):
        return tuple(child.shape() for _, child in self.children)

    def canonical(self):
        return [self.bound, self.region, self.top,
                [[a, child.canonical()] for a, child in self.children]]


def metrics(shape):
    if not shape:
        return (1, 1, 1, 1)  # nodes, leaves, height, Strahler
    parts = [metrics(child) for child in shape]
    maximum = max(p[3] for p in parts)
    return (1 + sum(p[0] for p in parts), sum(p[1] for p in parts),
            1 + max(p[2] for p in parts),
            maximum + (sum(p[3] == maximum for p in parts) > 1))


def embeds(small, large):
    """Root/level/order preserving embedding, allowing unused host children."""
    children = iter(large)
    return all(any(embeds(child, host) for host in children) for child in small)


def parse_dot(dot):
    """Parse only the program's classic, unlimited set labels, failing closed."""
    nodes, edges = {}, defaultdict(list)
    for line in dot.splitlines():
        match = re.fullmatch(r'\s*((?:even|odd)(?:_\d+)*) (.*?)\];', line)
        if not match:
            continue
        name, label = match.groups()
        edge = re.match(r'-> ((?:even|odd)(?:_\d+)*) ', label)
        text = html.unescape(re.sub(r'<[^>]*>', '', label))
        sets = [tuple(map(int, s.split(','))) if s else ()
                for s in re.findall(r'= \{([\d,]*)\}', text)]
        if len(sets) != 2 or 'more' in text:
            raise ValueError(f'incomplete set labels: {line}')
        if edge:
            edges[name].append((sets[1], edge[1]))
        else:
            bound = re.search(r'd = (\d+)', text)
            if not bound:
                raise ValueError(line)
            nodes[name] = (int(bound[1]), *sets)

    def visit(name):
        if name not in nodes:
            return None
        bound, region, top = nodes[name]
        return Node(bound, region, top,
                    tuple((a, visit(child)) for a, child in edges[name]))

    for player in ('even', 'odd'):
        if player not in nodes and f'{player}_empty ' not in dot:
            raise ValueError(f'missing {player} root in DOT')
    return tuple(visit(p) for p in ('even', 'odd'))


def game_text(game):
    return f'parity {len(game) - 1};\n' + ''.join(
        f'{v} {p} {o} {",".join(map(str, edges))};\n'
        for v, (p, o, edges) in enumerate(game))


def read_game(path, binary):
    normalized = subprocess.run([str(binary.parent / 'pgfilt'), '--normalize'],
                                input=Path(path).read_text(), text=True,
                                capture_output=True, check=True).stdout
    rows = re.findall(r'^(\d+) (\d+) ([01]) ([\d,]+)(?: .*?)?;',
                      normalized, re.MULTILINE)
    indices = {int(row[0]): i for i, row in enumerate(rows)}
    if not rows:
        raise ValueError(f'no vertices in {path}')
    return tuple((int(p), int(o), tuple(indices[int(v)] for v in e.split(',')))
                 for _, p, o, e in rows)


def random_game(rng, n, h, degree, even_owner=.5, distribution='uniform'):
    weights = {'uniform': [1] * (2 * h),
               'low': list(range(2 * h, 0, -1)),
               'high': list(range(1, 2 * h + 1)),
               'even': [4 if p % 2 == 0 else 1 for p in range(2 * h)],
               'odd': [1 if p % 2 == 0 else 4 for p in range(2 * h)]}[distribution]
    return tuple((rng.choices(range(2 * h), weights)[0],
                  int(rng.random() >= even_owner),
                  tuple(sorted(rng.sample(range(n), min(degree, n)))))
                 for _ in range(n))


def structured_game(family, n, h, player=0):
    rows = []
    for v in range(n):
        if family == 'ladder':
            edges = {v, min(n - 1, v + 1)}
            priority = (v % (2 * h))
        else:  # successive cycles overlap through vertex 0 and their predecessor
            edges = {0, max(0, v - 1), min(n - 1, v + 1)}
            priority = min(2 * h - 1, v)
        rows.append((priority, (v + player) % 2, tuple(sorted(edges))))
    return tuple(rows)


class Runner:
    def __init__(self, binary, timeout):
        self.binary, self.timeout = str(binary), timeout
        self.prefix = shlex.split(os.environ.get('STRAHLER_TEST_WRAPPER', ''))

    @lru_cache(maxsize=2048)
    def run(self, game, algorithm='lifting', extra=()):
        result = subprocess.run(
            [*self.prefix, self.binary, '--labels=sets', f'--max-set-items={len(game)}',
             '--priority-mode=compact', '--stats', f'--algorithm={algorithm}', *extra],
            input=game_text(game), text=True, capture_output=True, timeout=self.timeout)
        if result.returncode:
            raise RuntimeError(result.stderr)
        return parse_dot(result.stdout), result.stderr

    def compare(self, game):
        return self.run(game)[0], self.run(game, 'zielonka')[0]


def differences(left, right):
    flags = set()
    assert (left is None) == (right is None), 'winning regions disagree'
    if left is None:
        return flags
    assert left.region == right.region, 'winning regions disagree'
    a, b = left.shape(), right.shape()
    if a != b:
        flags.add('shape')
    elif left != right:
        flags.add('sets_only')
    if left != right:
        flags.add('decorated')
    for index, metric in enumerate(('nodes', 'leaves', 'height', 'strahler')):
        x, y = metrics(a)[index], metrics(b)[index]
        if x != y:
            flags.add(('lifting' if x > y else 'zielonka') + '_more_' + metric)
    if not embeds(a, b) and not embeds(b, a):
        flags.add('incomparable_shapes')
    return flags


def without_vertices(game, removed):
    keep = [v for v in range(len(game)) if v not in removed]
    index = {v: i for i, v in enumerate(keep)}
    candidate = tuple((game[v][0], game[v][1],
                       tuple(index[w] for w in game[v][2] if w in index)) for v in keep)
    return candidate if candidate and all(e for _, _, e in candidate) else None


def shrink(game, predicate):
    """Chunk deletion followed by a fixed point of single deletions/lowerings.

    The result is 1-minimal for these edits, not a claim of a global minimum.
    Reject edits creating dead ends rather than silently adding new edges.
    """
    width = max(1, len(game) // 2)
    while width:
        changed = False
        for start in range(0, len(game), width):
            candidate = without_vertices(game, set(range(start, min(len(game), start + width))))
            if candidate and predicate(candidate):
                game, changed = candidate, True
                break
        if not changed:
            width //= 2
    while True:
        candidates = [without_vertices(game, {v}) for v in range(len(game))]
        for v, (p, o, edges) in enumerate(game):
            if len(edges) > 1:
                for w in edges:
                    rows = list(game)
                    rows[v] = (p, o, tuple(e for e in edges if e != w))
                    candidates.append(tuple(rows))
            for lower in range(p):
                rows = list(game)
                rows[v] = (lower, o, edges)
                candidates.append(tuple(rows))
        for candidate in candidates:
            if candidate and predicate(candidate):
                game = candidate
                break
        else:
            return game


def cpu_time():
    return sum(getattr(resource.getrusage(who), field)
               for who in (resource.RUSAGE_SELF, resource.RUSAGE_CHILDREN)
               for field in ('ru_utime', 'ru_stime'))


def size(game):
    return len(game), sum(len(e) for _, _, e in game), sum(p for p, _, _ in game)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--binary', type=Path, default=Path('build/pg2adot'))
    parser.add_argument('--seed', type=int, default=20261019)
    parser.add_argument('--n', default='4,8,16,32')
    parser.add_argument('--h', default='2,3,4')
    parser.add_argument('--out-degree', type=int, default=2)
    parser.add_argument('--even-owner', type=float, default=.5)
    parser.add_argument('--priority-distribution', choices=['uniform', 'low', 'high', 'even', 'odd'], default='uniform')
    parser.add_argument('--samples', type=int, default=100)
    parser.add_argument('--cpu-seconds', type=float, default=1200)
    parser.add_argument('--timeout', type=float, default=2)
    parser.add_argument('--output', type=Path, default=Path('/tmp/disagreements.json'))
    parser.add_argument('--examples', nargs='*', type=Path, default=sorted(Path('examples').glob('*.pg')))
    parser.add_argument('--no-shrink', action='store_true')
    args = parser.parse_args()
    ns, hs = [int(x) for x in args.n.split(',')], [int(x) for x in args.h.split(',')]
    if min(ns + hs + [args.out_degree]) < 1 or not 0 <= args.even_owner <= 1:
        parser.error('positive n, h, degree and even-owner in [0,1] required')
    runner = Runner(args.binary.resolve(), args.timeout)
    rng, counts, candidates = random.Random(args.seed), defaultdict(Counter), {}
    started, wall = cpu_time(), time.monotonic()

    def record(game, key):
        try:
            left, right = runner.compare(game)
        except subprocess.TimeoutExpired:
            counts[key]['timeout'] += 1
            return
        except RuntimeError as error:
            if 'more than the limit' not in str(error):
                raise
            counts[key]['host_limit'] += 1
            return
        counts[key]['games'] += 1
        for player in range(2):
            flags = differences(left[player], right[player])
            for flag in sorted(flags):
                counts[key][f'{player}:{flag}'] += 1
                if flag not in candidates or size(game) < size(candidates[flag][0]):
                    candidates[flag] = (game, player)

    for n in ns:
        for h in hs:
            for family in ('ladder', 'nested_cycles'):
                for player in range(2):
                    record(structured_game(family, n, h, player), f'{family}:{n},{h}')
    exhausted = False
    for sample in range(args.samples):
        for n in ns:
            for h in hs:
                if cpu_time() - started >= args.cpu_seconds:
                    exhausted = True
                    break
                record(random_game(rng, n, h, args.out_degree, args.even_owner,
                                   args.priority_distribution), f'random:{n},{h}')
            if exhausted:
                break
        if exhausted:
            break
        if sample % 100 == 0:
            print(f'sample={sample} cpu={cpu_time() - started:.1f}s', flush=True)
    for path in args.examples:
        if path.stat().st_size <= 1_000_000:
            record(read_game(path, args.binary.resolve()), str(path))
        else:
            finished = True
            for algorithm in ('lifting', 'zielonka'):
                try:
                    result = subprocess.run(
                        [str(args.binary.resolve()), f'--algorithm={algorithm}',
                         '--labels=none', '--stats', str(path)],
                        capture_output=True, text=True, timeout=args.timeout)
                    counts[str(path)][f'{algorithm}:exit_{result.returncode}'] += 1
                    finished &= result.returncode == 0
                except subprocess.TimeoutExpired:
                    counts[str(path)][f'{algorithm}:timeout'] += 1
                    finished = False
            if finished:
                record(read_game(path, args.binary.resolve()), str(path))
    examples = {}
    for flag, (game, player) in sorted(candidates.items()):
        if not args.no_shrink:
            def predicate(candidate):
                try:
                    left, right = runner.compare(candidate)
                    return flag in differences(left[player], right[player])
                except subprocess.TimeoutExpired:
                    return False
            game = shrink(game, predicate)
        left, right = runner.compare(game)
        examples[flag] = dict(game=game_text(game), player=player,
                              lifting=[n.canonical() if n else None for n in left],
                              zielonka=[n.canonical() if n else None for n in right])
    report = dict(seed=args.seed, parameters={k: str(v) if isinstance(v, Path) else v
                                            for k, v in vars(args).items() if k != 'examples'},
                  cpu_seconds=cpu_time() - started, wall_seconds=time.monotonic() - wall,
                  counts=dict(counts), counterexamples=examples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(f'wrote {args.output}; cpu={report["cpu_seconds"]:.1f}s', flush=True)


if __name__ == '__main__':
    main()
