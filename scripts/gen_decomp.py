#!/usr/bin/env python3
"""Regenerate decomp/ and DECOMP.md from the built, verified game tools."""

import argparse
from dataclasses import dataclass
from itertools import combinations
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Backend:
    name: str
    binary: str
    options: tuple[str, ...]


BACKENDS = (
    Backend("lifting", "pg2adot", ("--algorithm=lifting",)),
    Backend("lifting-adaptive", "pg2adot",
            ("--algorithm=lifting", "--adaptive-t")),
    Backend("lifting-sym", "pg2adot", ("--algorithm=lifting-sym",)),
    Backend("pm-strahler", "pg2pmdot", ("--algorithm=strahler",)),
    Backend("pm-succinct", "pg2pmdot", ("--algorithm=succinct",)),
    Backend("zielonka", "pg2adot", ("--algorithm=zielonka",)),
    Backend("zielonka-sym", "pg2adot", ("--algorithm=zielonka-sym",)),
)
MAX_SET_ITEMS = 8
# Per-game label overrides belong here if a DOT approaches 2 MB.
GAME_LABELS = {}
# Local release runs exceeded 60 s for each pair, with and without preprocessing.
SKIP_RUNS = {
    ("cabp_swp.ehoa.pg", "lifting-adaptive", False): 60,
    ("cabp_swp.ehoa.pg", "lifting-adaptive", True): 60,
    ("cabp_swp.ehoa.pg", "pm-strahler", False): 60,
    ("cabp_swp.ehoa.pg", "pm-strahler", True): 60,
}
HEADER = re.compile(r"parity\s+\d+\s*;")
VERTEX = re.compile(
    r'(\d+)\s+(\d+)\s+[01]\s+(\d+(?:\s*,\s*\d+)*)\s*'
    r'(?:"(?:\\.|[^"\\])*"\s*)?;'
)


def discover_games(root):
    """Recognize games by their first nonempty line, whatever the suffix."""
    games = []
    for path in sorted((root / "examples").rglob("*")):
        if path.is_file():
            with path.open(encoding="utf-8", errors="replace") as stream:
                first = next((line.strip() for line in stream
                              if line.strip()), "")
            if HEADER.fullmatch(first):
                games.append(path)
    stems = [path.stem for path in games]
    if len(stems) != len(set(stems)):
        raise ValueError("games must have unique stems under examples/")
    return games


def game_info(path):
    """Count records; the header can mean maximum ID or vertex count."""
    vertices = edges = 0
    priorities = set()
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A\s*parity\s+\d+\s*;", "", text)
    text = re.sub(r"\A\s*start\s+\d+\s*;", "", text)
    end = 0
    for match in VERTEX.finditer(text):
        if text[end:match.start()].strip():
            raise ValueError("invalid PGSolver vertex record")
        vertices += 1
        priorities.add(int(match[2]))
        edges += match[3].count(",") + 1
        end = match.end()
    if text[end:].strip():
        raise ValueError("invalid PGSolver vertex record")
    return vertices, edges, len(priorities), max(priorities, default=0)


def stable_stats(stderr, root, build_dir):
    """Keep stderr in order, dropping timing lines/fields and local paths."""
    stderr = stderr.replace(str(build_dir), "build").replace(str(root), ".")
    lines = []
    timing = r"(?:\w*time\w*|elapsed\w*|seconds|duration\w*)"
    for line in stderr.splitlines():
        if re.match(r"\s*(?:wall[ -]?time|cpu[ -]?time|time|timing|elapsed|"
                    r"duration|seconds)\b", line, re.IGNORECASE):
            continue
        line = re.sub(rf"\s*\b{timing}=\S+", "", line, flags=re.IGNORECASE)
        if line.strip():
            lines.append(line.rstrip())
    return "".join(line + "\n" for line in lines)


@dataclass
class Run:
    outcome: str
    stats: str = ""
    dot: str = ""
    leaves: str = ""


def invoke(command, game, root, build_dir, timeout):
    try:
        with game.open("rb") as stream:
            result = subprocess.run(
                command, stdin=stream, capture_output=True, text=True,
                encoding="utf-8", errors="replace", cwd=root, timeout=timeout,
                env={**os.environ, "LC_ALL": "C", "LANG": "C"},
            )
    except subprocess.TimeoutExpired:
        raise SystemExit(
            f"{game.name}: safety timeout after {timeout:g} s for "
            f"{' '.join(command)}; measure locally and add this "
            "(game, backend, pre) pair to the SKIP_RUNS skip list in "
            "scripts/gen_decomp.py"
        ) from None
    except OSError:
        return Run(f"error: cannot execute {Path(command[0]).name}")
    stats = stable_stats(result.stderr, root, build_dir)
    if re.search(r"more than (?:the limit|\d+ leaves)", stats):
        return Run("host limit", stats)
    if result.returncode:
        first = stats.splitlines()[0] if stats else "process failed"
        return Run("error: " + first, stats)
    match = re.search(r"\bresult=(complete|partial)\b", stats)
    if not match:
        return Run("error: missing result statistics", stats)
    return Run(match[1], stats, result.stdout)


def run_backend(backend, pre, game, root, build_dir, timeout, limit):
    if (game.name, backend.name, pre) in SKIP_RUNS:
        seconds = SKIP_RUNS[game.name, backend.name, pre]
        return Run(f"skipped (> {seconds:g} s locally)")
    command = [str(build_dir / backend.binary), *backend.options,
               "--player=both", "--stats",
               "--labels=" + GAME_LABELS.get(game.stem, "sets"),
               f"--max-set-items={MAX_SET_ITEMS}"]
    if backend.binary == "pg2adot" and backend.name.startswith("lifting"):
        command.append(f"--max-host-leaves={limit}")
    if pre:
        command.extend(("--shave=all", "--compress"))
    run = invoke(command, game, root, build_dir, timeout)
    if run.outcome not in ("complete", "partial"):
        return run
    if "--adaptive-t" in backend.options:
        incremental = invoke(
            [arg.replace("--adaptive-t", "--adaptive-t=incremental")
             for arg in command], game, root, build_dir, timeout)
        if incremental.outcome not in ("complete", "partial"):
            return Run(incremental.outcome, run.stats + incremental.stats)
        assert (run.outcome == incremental.outcome and
                run.dot == incremental.dot), (
            f"{game.name}: cold/incremental adaptive trees differ (pre={pre})")
    if backend.binary == "pg2pmdot":
        leaves = invoke(command + ["--format=leaves"], game, root, build_dir,
                        timeout)
        if leaves.outcome not in ("complete", "partial"):
            return Run(leaves.outcome, leaves.stats)
        assert run.stats == leaves.stats, "DOT/leaf runs disagree"
        run.leaves = leaves.dot
    return run


def player_stats(stats):
    players = []
    for player in ("even", "odd"):
        match = re.search(rf"^(?:\S+ )?{player}: (.+)$", stats, re.MULTILINE)
        players.append(dict(re.findall(r"(\w+)=(\S+)", match[1]))
                       if match else {})
    return players


def tree_info(dot, pm):
    """Read our ordered DOT trees; exclude synthetic and shaved nodes."""
    names = r"n\d+" if pm else r"(?:even|odd)(?:_\d+)*"
    nodes = dict(re.findall(rf"^  ({names}) \[label=(.*);$",
                            dot, re.MULTILINE))
    children = {name: [] for name in nodes}
    for parent, child in re.findall(r"^  (\w+) -> (\w+)(?: \[.*\])?;\s*$",
                                    dot, re.MULTILINE):
        if parent in nodes and child in nodes:
            children[parent].append(child)
    result = []
    for player in ("even", "odd"):
        root = next((name for name, label in nodes.items()
                     if (label.startswith('"' + player.title() + " (")
                         if pm else name == player)), None)
        if root is None or "no non-top measures" in nodes[root]:
            result.append(((0, 0, 0, 0), ()))
            continue
        order, stack = [], [root]
        while stack:
            name = stack.pop()
            order.append(name)
            stack.extend(reversed(children[name]))
        metrics = {}
        for name in reversed(order):
            parts = [metrics[child] for child in children[name]]
            if not parts:
                metrics[name] = (1, 1, 1, 1)
            else:
                maximum = max(part[3] for part in parts)
                metrics[name] = (
                    1 + sum(part[0] for part in parts),
                    sum(part[1] for part in parts),
                    1 + max(part[2] for part in parts),
                    maximum + (sum(part[3] == maximum for part in parts) > 1),
                )
        result.append((metrics[root], tuple(len(children[n]) for n in order)))
    return result


def pair(values):
    return " / ".join(map(str, values))


def generate(root, destination, build_dir, timeout, limit):
    lines = [
        "# Decompositions\n\n"
        "Generated by `scripts/gen_decomp.py`; **do not hand-edit**. "
        "Methods come from "
        "[the reviewed template](scripts/decomp_methods.md).\n\n",
        (root / "scripts/decomp_methods.md").read_text(encoding="utf-8"),
        "\n## Inventory\n\n",
        "Regenerate with release tools (`--buildtype=release`): "
        "`python3 scripts/gen_decomp.py`. "
        f"Defaults: {timeout:g} s "
        f"safety timeout per subprocess; {limit} host leaves; sets capped at "
        f"{MAX_SET_ITEMS} IDs. `+pre` adds `--shave=all --compress`. "
        "Each adaptive result is checked against incremental adaptive; "
        "identical DOT is stored once. PM leaf streams keep raw order.\n\n",
        "Metrics and parameters are **Even / Odd**. Heights count nodes. "
        "Empty trees have zero metrics; synthetic, shaved and unresolved "
        "nodes are excluded. AD metrics describe residual decompositions; "
        "PM metrics describe occupied measure prefix trees (including their "
        "extra root), not minimum game Strahler numbers. Won sizes include "
        "shaved vertices; partial rows give certified lower bounds. "
        "Unknown winners are `?`. Every backend is attempted on every game "
        "except measured slow pairs in `SKIP_RUNS` in "
        "`scripts/gen_decomp.py`; their skip outcomes are fixed by the table. "
        "Host-leaf limits remain outcomes, without vertex cutoffs. "
        "A safety timeout aborts generation; measure locally and add the "
        "pair to the skip list.\n\n",
    ]
    disagreements = []
    for game in discover_games(root):
        vertices, edges, priorities, maximum = game_info(game)
        print(f"{game.relative_to(root)} ({vertices} vertices)", flush=True)
        folder = destination / "decomp" / game.stem
        folder.mkdir(parents=True)
        records = []
        for backend in BACKENDS:
            for pre in (False, True):
                name = backend.name + ("+pre" if pre else "")
                run = run_backend(backend, pre, game, root,
                                  build_dir, timeout, limit)
                (folder / (name + ".stats")).write_text(
                    f"outcome: {run.outcome}\n" + run.stats, encoding="utf-8")
                info = won = parameters = None
                if run.dot:
                    pm = backend.binary == "pg2pmdot"
                    info = tree_info(run.dot, pm)
                    stats = player_stats(run.stats)
                    assert (all(stats) or vertices == 0 or
                            "residual=0" in run.stats)
                    shaved = [int(re.search(rf"shaved_{p}=(\d+)",
                                            run.stats)[1])
                              if f"shaved_{p}=" in run.stats else 0
                              for p in ("even", "odd")]
                    won = tuple(int(s.get("non_top" if pm else "region",
                                          s.get("dominion", 0))) + shaved[p]
                                for p, s in enumerate(stats))
                    if run.outcome == "complete":
                        assert sum(won) == vertices, "incomplete regions"
                        assert all(r["won"] == won for r in records
                                   if r["run"].outcome == "complete"), (
                                       f"{game.name}: winning sizes disagree")
                    parameters = pair(
                        ", ".join(f"{key}={s[key]}" for key in
                                  ("H", "K", "k", "t", "bits", "depth")
                                  if key in s)
                        or "—" for s in stats)
                    (folder / (name + ".dot")).write_text(
                        run.dot, encoding="utf-8")
                    if pm:
                        (folder / (name + ".leaves")).write_text(
                            run.leaves, encoding="utf-8")
                records.append(dict(name=name, backend=backend, pre=pre,
                                    run=run, info=info, won=won,
                                    parameters=parameters))
                print(f"  {name}: {run.outcome}", flush=True)
        complete = next((r["won"] for r in records
                         if r["run"].outcome == "complete"), ("?", "?"))
        lines.extend([
            f"\n### {game.name}\n\n",
            "| Vertices | Edges | Distinct priorities | Maximum priority | "
            "Won (Even / Odd) |\n| ---: | ---: | ---: | ---: | --- |\n",
            f"| {vertices} | {edges} | {priorities} | {maximum} | "
            f"{pair(complete)} |\n\n",
            "| Backend | Outcome | Won E / O | Nodes E / O | Leaves E / O | "
            "Height E / O | Strahler E / O | Parameters E / O | Tree |\n",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n",
        ])
        for record in records:
            name, run, info = record["name"], record["run"], record["info"]
            link = f"decomp/{game.stem}/{name}"
            columns = [f"[{name}]({link}.stats)", run.outcome]
            if info is None:
                columns.extend(["—"] * 7)
            else:
                columns.append(pair(record["won"]))
                columns.extend(pair(part[0][i] for part in info)
                               for i in range(4))
                columns.append(record["parameters"])
                columns.append(f"[DOT]({link}.dot)")
                if run.leaves:
                    columns[-1] += f" · [leaves]({link}.leaves)"
            lines.append("| " + " | ".join(columns) + " |\n")
        for left, right in combinations(records, 2):
            if (left["pre"] != right["pre"] or
                    left["backend"].binary != right["backend"].binary or
                    left["run"].outcome != "complete" or
                    right["run"].outcome != "complete"):
                continue
            for player, (a, b) in enumerate(zip(left["info"], right["info"])):
                if a[1] != b[1]:
                    changed = [label for i, label in enumerate(
                        ("nodes", "leaves", "height", "Strahler"))
                        if a[0][i] != b[0][i]]
                    player_name = "Even" if player == 0 else "Odd"
                    detail = "; " + ", ".join(changed) if changed else ""
                    disagreements.append(
                        f"| {game.name} | {player_name} | {left['name']} | "
                        f"{right['name']} | ordered shape{detail} |\n")
    lines.extend([
        "\n## Tree disagreements\n\n",
        "Compare complete ordered, unlabelled shapes within each tree family "
        "and preprocessing mode. Different sets on equal shapes are excluded; "
        "truncated labels cannot establish set equality. AD and PM trees have "
        "different meanings, so are not compared to each other. For comparing "
        "of full vertex sets and smaller witnesses, see "
        "[the disagreement study](docs/disagreements.md).\n\n",
        "| Game | Player | Backend A | Backend B | Differences |\n",
        "| --- | --- | --- | --- | --- |\n",
        *(disagreements or ["| — | — | — | — | No shape disagreements |\n"]),
    ])
    (destination / "DECOMP.md").write_text("".join(lines), encoding="utf-8")


def output_files(root):
    return {path.relative_to(root): path.read_bytes()
            for path in (root / "decomp").rglob("*") if path.is_file()} | (
                {Path("DECOMP.md"): (root / "DECOMP.md").read_bytes()}
                if (root / "DECOMP.md").is_file() else {})


def sync_outputs(root, generated, check):
    old, new = output_files(root), output_files(generated)
    stale = sorted(path for path in old.keys() | new.keys()
                   if old.get(path) != new.get(path))
    if check:
        for path in stale:
            print(f"stale: {path}")
        if stale:
            print("Regenerate: python3 scripts/gen_decomp.py")
        return bool(stale)
    for path in stale:
        target = root / path
        if path in new:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(generated / path, target)
        else:
            target.unlink()
    size = sum(len(data) for path, data in new.items()
               if path.parts[0] == "decomp")
    print(f"decomp/: {size} bytes; {len(stale)} files updated")
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, default=Path("build"))
    parser.add_argument("--timeout", type=float, default=600)
    parser.add_argument("--max-host-leaves", type=int, default=10_000)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("--timeout must be finite and positive")
    if args.max_host_leaves <= 0:
        parser.error("--max-host-leaves must be positive")
    build_dir = args.build_dir.resolve()
    for binary in {backend.binary for backend in BACKENDS}:
        if not os.access(build_dir / binary, os.X_OK):
            parser.error(f"missing {binary}; run meson compile first")
    with tempfile.TemporaryDirectory(prefix="gen-decomp-") as directory:
        generated = Path(directory)
        generate(ROOT, generated, build_dir, args.timeout,
                 args.max_host_leaves)
        return sync_outputs(ROOT, generated, args.check)


if __name__ == "__main__":
    raise SystemExit(main())
