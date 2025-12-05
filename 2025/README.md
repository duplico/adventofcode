# Advent of Code 2025

Solutions to [Advent of Code 2025](https://adventofcode.com/2025) puzzles.

## Quick Start

```bash
# Create a new day (after installing dependencies below)
just new 02 python

# Add another language to the same day
just new 02 rust

# Run a solution
just run 02 python 1           # day 02, python, part 1
just run 02 python 2 -v        # part 2, verbose
just sample 02 python 1        # part 1 with sample_input.txt
```

## Installing Dependencies

This guide assumes **Debian 12 (Bookworm)** or **Debian 13 (Trixie)**.

### Task Runner: just

[just](https://github.com/casey/just) is a modern command runner used to initialize new days and run solutions.

```bash
# Install prebuilt binary (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin

# Make sure ~/.local/bin is in your PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
just --version
```

Alternative: Install via cargo if you have Rust (see below):

```bash
cargo install just
```

---

## Language Setup

### Python (via uv)

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager from Astral (creators of Ruff). It handles both Python version management and virtual environments.

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart shell or source the env
source ~/.bashrc  # or ~/.zshrc

# Install Python 3.14 (free-threaded build for no-GIL experiments)
uv python install 3.14

# Optionally install the free-threaded variant
uv python install 3.14t

# Verify
uv --version
uv python list
```

**Usage:**

```bash
cd 02/python
uv sync                      # Install dependencies
uv run advent 1 ../input.txt    # Run part 1
```

---

### Rust (via rustup)

[rustup](https://rustup.rs/) is the official Rust toolchain installer.

```bash
# Install rustup and stable Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Follow prompts, then restart shell or:
source ~/.cargo/env

# Verify
rustc --version
cargo --version
```

**Usage:**

```bash
cd 02/rust
cargo run --release -- 1 ../input.txt
```

---

### Go (official binary)

Download the latest Go from [go.dev](https://go.dev/dl/).

```bash
# Download and install (check for latest version at go.dev/dl)
GO_VERSION="1.23.4"
wget "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz"
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf "go${GO_VERSION}.linux-amd64.tar.gz"
rm "go${GO_VERSION}.linux-amd64.tar.gz"

# Add to PATH
echo 'export PATH="/usr/local/go/bin:$HOME/go/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verify
go version
```

**Usage:**

```bash
cd 02/go
go run . 1 ../input.txt
```

---

### Clojure (via official installer)

Clojure uses the [Clojure CLI tools](https://clojure.org/guides/install_clojure) (`clj`/`clojure`).

```bash
# Install Java first (Clojure runs on the JVM)
sudo apt update
sudo apt install -y default-jdk rlwrap  # Installs latest JDK for your Debian version

# Install Clojure CLI tools
curl -L -O https://github.com/clojure/brew-install/releases/latest/download/linux-install.sh
chmod +x linux-install.sh
sudo ./linux-install.sh
rm linux-install.sh

# Verify
java --version
clj --version
```

**Usage:**

```bash
cd 02/clojure
clj -M:run 1 ../input.txt

# Or start a REPL
clj
```

---

### C (GCC from Debian)

Debian's GCC is modern enough for most AoC puzzles.

```bash
sudo apt update
sudo apt install -y build-essential  # Installs gcc, make, etc.

# Verify
gcc --version
```

**Note:** Debian 12 ships GCC 12, Debian 13 ships GCC 14. Some C23 features require GCC 14+. The skeleton uses `-std=c23` but will fall back gracefully on older GCC versions for most code.

**Usage:**

```bash
cd 02/c
make
./advent 1 ../input.txt
```

---

### Tcl

Tcl 8.6 from Debian is sufficient for Advent of Code. ActiveTcl is no longer the recommended distribution.

```bash
# Install from Debian repos (Tcl 8.6)
sudo apt update
sudo apt install -y tcl tcllib

# Verify
tclsh <<< 'puts [info patchlevel]'
```

For Tcl 9.0 (released 2024), you'd need to build from source:

```bash
# Optional: Tcl 9.0 from source
wget https://prdownloads.sourceforge.net/tcl/tcl9.0.0-src.tar.gz
tar xzf tcl9.0.0-src.tar.gz
cd tcl9.0.0/unix
./configure --prefix=/usr/local
make
sudo make install
```

**Usage:**

```bash
cd 02/tcl
tclsh advent.tcl 1 ../input.txt
```

---

### R

R from Debian is sufficient for Advent of Code. We use the `optparse` package for CLI argument parsing.

```bash
# Install from Debian repos
sudo apt update
sudo apt install -y r-base

# Verify
Rscript --version

# Install optparse package
sudo Rscript -e 'install.packages("optparse", repos="https://cloud.r-project.org")'
```

**Usage:**

```bash
cd 02/r
Rscript advent.R 1 ../input.txt
```

---

## Creating a New Day

Once dependencies are installed:

```bash
cd 2025

# See available languages
just langs

# Create day 02 with Python
just new 02 python

# Add Rust to the same day
just new 02 rust

# See what languages a day has
just day-langs 02
```

This will:

1. Create the day directory with shared `input.txt` and `sample_input.txt`
2. Copy the language skeleton to a subdirectory (e.g., `02/python/`)
3. Run any language-specific initialization (e.g., `uv sync` for Python)

## Running Solutions

```bash
# Run with real input (via just)
just run 02 python 1           # day 02, python, part 1
just run 02 python 2 -v        # part 2, verbose
just run 02 rust 1             # same day, different language

# Run with sample input
just sample 02 python 1

# Or run directly in the language directory
cd 02/python
uv run advent 1 ../input.txt         # Python

cd 02/rust
cargo run --release -- 1 ../input.txt # Rust

cd 02/go
go run . 1 ../input.txt               # Go

cd 02/clojure
clj -M:run 1 ../input.txt            # Clojure

cd 02/c
make && ./advent 1 ../input.txt      # C

cd 02/tcl
tclsh advent.tcl 1 ../input.txt      # Tcl

cd 02/r
Rscript advent.R 1 ../input.txt       # R
```

## Interactive REPLs

Some languages support interactive REPLs for exploratory development and debugging:

```bash
# Open a REPL (via just)
just repl 02 python      # Python with advent module pre-loaded
just repl 02 clojure     # Clojure with rebel-readline and advent loaded
just repl 02 tcl         # Basic Tcl shell
just repl 02 r           # R interactive session

# Or start directly
cd 02/python
uv run python -i -c "from advent import *"

cd 02/clojure
clj -M:rebel             # Enhanced REPL with auto-import
```

**Supported languages:** Python, Clojure, Tcl, R

The Clojure REPL uses [rebel-readline](https://github.com/bhauman/rebel-readline) for a better experience and automatically imports all functions from the `advent` namespace via `dev/user.clj`.

## Directory Structure

```plaintext
2025/
├── justfile              # Task runner commands
├── README.md             # This file
├── skel/                 # Project templates
│   ├── python/
│   ├── rust/
│   ├── go/
│   ├── clojure/
│   ├── c/
│   ├── tcl/
│   └── r/
├── 01/                   # Day 01 (old single-language structure)
│   └── ...
├── 02/                   # Day 02 (multi-language structure)
│   ├── input.txt         # Shared puzzle input
│   ├── sample_input.txt  # Shared sample input
│   ├── python/           # Python solution
│   │   ├── pyproject.toml
│   │   └── src/advent/
│   ├── rust/             # Rust solution
│   │   ├── Cargo.toml
│   │   └── src/main.rs
│   └── clojure/          # Clojure solution
│       ├── deps.edn
│       └── src/advent.clj
└── ...
```
