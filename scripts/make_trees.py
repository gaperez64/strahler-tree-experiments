#!/usr/bin/env python3
"""Generate trees and summary.csv for PGSolver files or directories."""

import argparse
import csv
from hashlib import sha256
from pathlib import Path
import shutil
import sys

import gen_decomp as decomp


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backends", help="comma-separated DECOMP.md backend names (default: all)")
    parser.add_argument("--out", type=Path, default=Path("trees"))
    decomp.add_run_arguments(parser)
    parser.add_argument("--no-png", action="store_true")
    parser.add_argument("games", type=Path, nargs="+", metavar="GAME_OR_DIR")
    args = parser.parse_args()
    valid = {backend.name: backend for backend in decomp.BACKENDS}
    names = args.backends.split(",") if args.backends is not None else list(valid)
    unknown = [name for name in names if name not in valid]
    if unknown:
        parser.error(f"unknown backends: {', '.join(unknown)!r}; valid names: "
                     + ", ".join(valid))
    backends = [valid[name] for name in dict.fromkeys(names)]
    build_dir = decomp.validate_run_arguments(parser, args, backends)
    try:
        games = decomp.discover_games([path.resolve() for path in args.games])
        if not games:
            parser.error("no PGSolver games found")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    dot = None if args.no_png else shutil.which(args.dot)
    if not args.no_png and dot is None:
        print(f"warning: Graphviz {args.dot!r} not found; skipping PNGs", file=sys.stderr)
    fields = ["game", "backend", "outcome", "vertices", "edges",
              "distinct_priorities", "maximum_priority"]
    fields += [f"{metric}_{player}" for metric in
               ("won", *decomp.TREE_METRICS, "parameters")
               for player in ("even", "odd")]
    fields.append("tree")
    args.out.mkdir(parents=True, exist_ok=True)
    failed = False
    with (args.out / "summary.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for game in games:
            invalid = None
            try:
                vertices, edges, priorities, maximum = decomp.game_info(game)
            except (OSError, ValueError) as error:
                invalid = decomp.Run("error: " + str(error))
                vertices = edges = priorities = maximum = None
            for backend in backends:
                run = invalid or decomp.run_backend(
                    backend, game, decomp.ROOT, build_dir,
                    args.timeout, args.max_host_leaves, compare_adaptive=False)
                metrics = decomp.run_metrics(backend, run, vertices)
                folder = args.out / game.stem
                decomp.write_run(folder, backend, run, metrics["info"])
                png = folder / (backend.name + ".png")
                if dot and run.dot:
                    source = run.dot.encode("utf-8")
                    png.write_bytes(decomp.render_png(
                        source, sha256(source).hexdigest(), dot))
                else:
                    png.unlink(missing_ok=True)
                row = dict(game=str(game), backend=backend.name, outcome=run.outcome,
                           vertices=vertices, edges=edges, distinct_priorities=priorities,
                           maximum_priority=maximum)
                if metrics["info"] is not None:
                    for p, player in enumerate(("even", "odd")):
                        row[f"won_{player}"] = metrics["won"][p]
                        row[f"parameters_{player}"] = metrics["parameters"][p]
                        for metric in decomp.TREE_METRICS:
                            row[f"{metric}_{player}"] = decomp.format_metric(
                                metric, metrics["info"][p][0][metric])
                    row["tree"] = f"{game.stem}/{backend.name}.dot"
                writer.writerow(row)
                print(f"{game}: {backend.name}: {run.outcome}", file=sys.stderr, flush=True)
                failed |= run.outcome.startswith(("error:", "timeout"))
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
