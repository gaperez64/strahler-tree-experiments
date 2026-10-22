# Strahler tree notebooks

Setup instructions for exploring parity games with the Python API and
JupyterLab. This checkout currently has no `.ipynb` notebooks, data, or helpers.

Prebuilt wheels exist for **Linux x86_64** (glibc 2.28+) and **macOS on Apple
silicon (arm64, macOS 11.0+)**. On any other machine, follow
[From a checkout](#from-a-checkout). You need Python 3.10 or newer.

## From a release

Download `strahler-notebooks-<version>.zip` from the
[releases page](https://github.com/vfluegel/strahler-tree-experiments/releases),
replacing `<version>` in the commands below with its version (without `v`).
The zip contains both wheels and everything in `jupyter-examples/` at the
release tag, including any notebooks, data, and helpers present there.
`requirements.txt` uses `--find-links ./wheels` to find the matching strahler
wheel; notebook dependencies are downloaded from PyPI.

Run these commands from the directory containing the download. After
unzipping, run installation and JupyterLab from inside the unzipped directory
so that `./wheels` resolves correctly.

### With venv and pip

```sh
unzip strahler-notebooks-<version>.zip
cd strahler-notebooks-<version>
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Use JupyterLab's file browser to open or create a notebook. Later sessions
only need `source .venv/bin/activate` and `jupyter lab`. Run `deactivate` to
leave the environment.

### With uv

```sh
unzip strahler-notebooks-<version>.zip
cd strahler-notebooks-<version>
uv venv
uv pip install -r requirements.txt
uv run --no-project jupyter lab
```

For a temporary environment, from the unzipped directory:

```sh
uv run --no-project --with-requirements requirements.txt jupyter lab
```

### Colab or a single wheel

Each wheel is also attached to the release on its own. For Linux x86_64,
replace both occurrences of `<version>` in this notebook cell:

```python
%pip install https://github.com/vfluegel/strahler-tree-experiments/releases/download/v<version>/strahler-<version>-py3-none-manylinux_2_28_x86_64.whl
```

For Apple silicon, download
`strahler-<version>-py3-none-macosx_11_0_arm64.whl` instead.
Use `strahler.version()` to read the loaded library's version and
`strahler.check(game, tree, player)` to check a candidate decomposition.
To check that the library matches the release you downloaded:

```python
import strahler
assert strahler.version() == "<version>", "Install the wheel from this notebook release"
```

## From a checkout

You need a C23 compiler (GCC 14+, Clang 18+, or recent Apple Clang), a C++20
compiler, and the build dependencies listed in the
[top-level README](https://github.com/vfluegel/strahler-tree-experiments#build).
The package builds libstrahler through meson-python. An editable install
rebuilds it on import after a C source changes.

### With venv and pip

```sh
git clone https://github.com/vfluegel/strahler-tree-experiments.git
cd strahler-tree-experiments
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install meson-python meson ninja
python -m pip install --no-build-isolation -e .
python -m pip install -r jupyter-examples/requirements.txt
jupyter lab jupyter-examples/
```

### With uv

```sh
git clone https://github.com/vfluegel/strahler-tree-experiments.git
cd strahler-tree-experiments
uv venv
uv pip install meson-python meson ninja
uv pip install --no-build-isolation -e .
uv pip install -r jupyter-examples/requirements.txt
uv run --no-project jupyter lab jupyter-examples/
```

## Notebooks

Open or create an `.ipynb` file in JupyterLab. Each release zip includes
everything in `jupyter-examples/` at release time, including any notebook
data and helpers.
