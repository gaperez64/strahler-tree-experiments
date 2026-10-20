# Strahler tree experiments

Command-line tools for building Strahler trees and computing attractor
decompositions and progress measures of parity games, based on
[The Strahler Number of a Parity Game](https://arxiv.org/pdf/2003.08627).

## Build

Requires Meson 1.4+, Ninja, a C23 compiler (Clang 18+, GCC 14+, or recent Apple Clang), and a C++20 compiler.
Boost enables `lenstree`; Graphviz renders DOT and enables DOT syntax tests. macOS: `brew install boost graphviz meson ninja`.

```sh
meson setup build
meson compile -C build
meson test -C build --print-errorlogs
```

Executables go in `build/`. Release binaries for `linux-x86_64` and
`macos-arm64` are attached to [GitHub releases](https://github.com/vfluegel/strahler-tree-experiments/releases).

## Commands

| Command | What it does |
| --- | --- |
| `genstree` | Generate a Strahler tree, count its leaves, or print DOT. |
| `lenstree` | Count leaves or look up a leaf with the Boost-based implementation. |
| `pms2dot` | Convert progress-measure branches from standard input to a DOT prefix tree. |
| `pgfilt` | Check a PGSolver game from standard input; print statistics or normalize it. |
| `pg2adot` | Compute and verify attractor decompositions; write DOT. |
| `pg2pmdot` | Compute Strahler or succinct progress measures; write DOT or leaf streams. |
| `str-tree` | Check p-level successors in a compiled-in example tree. |

`pg2adot` and `pg2pmdot` read a PGSolver file; `-` or no filename reads
standard input. For example:

```sh
./build/pg2adot --algorithm=lifting --adaptive-t game.pg > decomposition.dot
./build/pg2adot --algorithm=zielonka --shave=all --compress game.pg > decomposition.dot
./build/pg2pmdot --algorithm=strahler --shave=all --compress game.pg > measures.dot
./build/pg2pmdot --algorithm=succinct --labels=sets game.pg > measures.dot
dot -Tsvg decomposition.dot > decomposition.svg
```

`--shave=all` removes simple dominions before solving. `--compress` merges
consecutive distinct priorities of the same parity. Sample games are in
[tests/games/](tests/games/).

Run `<cmd> --help` for the full option list (in `genstree`, `-h` is the
height). [lenstree](docs/developing.md#lenstree) and
[str-tree](docs/developing.md#str-tree) have no help; see their notes instead.

[DECOMP.md](DECOMP.md) has example trees for every backend. See [docs/](docs/)
for research notes and [docs/developing.md](docs/developing.md) for detailed
command behavior, tree notation, and development instructions.

## License

[MIT](LICENSE) covers the original CLI, public interface, tree output,
shared modules and tests, with the exception below.

### NOTICE

`src/pm_lift.c`, `src/pm_solve.c`, `src/pm_internal.h`, `src/strpm.c`, and
`src/sspm.c` derive from [Oink](https://github.com/trolando/oink) and
[Vanessa Flügel's fork](https://github.com/vfluegel/oink), branch `print-pms`
(checkout `51c2640fe650fd18d9331cfe5133cf3605a98c31`; tree printing introduced
in `504081d`). Copyright 2017-2018 Tom van Dijk, Johannes Kepler University Linz.
Ported to C23 and modified for tree output, these files remain Apache-2.0;
see [LICENSE-APACHE-2.0](LICENSE-APACHE-2.0). Relicensing them to MIT requires
the copyright holders' consent, which has not been obtained.
