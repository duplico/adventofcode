# Advent of Code Repository Instructions

This repository contains solutions to [Advent of Code](https://adventofcode.com/) puzzles across multiple years.

## ⚠️ Critical: Puzzle Logic Boundary

**DO NOT solve puzzle logic for me.** Unless explicitly asked to help with the actual algorithm or solution approach, focus assistance on:

- Boilerplate code and project setup
- Language features, syntax, and idioms
- Package/library usage and recommendations
- File parsing and input handling
- Command-line argument processing
- Output formatting and visualization
- Build tools, testing, and project management
- Developer experience improvements

When I'm stuck on puzzle logic and explicitly ask for help, prefer giving hints or discussing approaches rather than providing complete solutions.

## Repository Structure

```
adventofcode/
├── YYYY/              # Year folder (2020, 2021, etc.)
│   ├── DD/            # Day folder (01-25)
│   │   ├── advent.py  # Solution file (or language-specific name)
│   │   ├── input.txt  # Puzzle input
│   │   └── sample_input.txt  # Sample/test input
│   └── skel.py        # Template for new days
```

## 2025 Focus

For 2025, the primary languages are **Python** and **Go**, though other languages may be used.

### Python Preferences (2025)

- **Python 3.14** features are encouraged - actively suggest opportunities to use:
  - Free-threaded Python (no-GIL builds) for parallelism where applicable
  - New syntax features and stdlib additions
  - Modern typing features (PEP 695 type parameter syntax, etc.)
- Use the existing CLI pattern with `click` and `rich` (see `skel.py`)
- Prefer modern packages: `rich` for output, `click` for CLI, consider `polars` over pandas, etc.
- Use type hints throughout
- Follow PEP 8, but prioritize readability for puzzle code

### Go Preferences (2025)

- Use Go 1.23+ features where appropriate
- Keep solutions simple and idiomatic
- Use standard library when sufficient; suggest interesting third-party packages when they add value

## Learning Goals

I want to learn new things! Please:

1. **Suggest modern packages/libraries** - Like how `click` and `rich` were used in Day 1, recommend interesting, modern alternatives to common tasks
2. **Highlight new language features** - Especially Python 3.14 and the free-threaded mode
3. **Recommend tools** - Build tools (uv, bazel, make), testing frameworks, linters, formatters
4. **Mention Copilot features** - New capabilities, MCP servers, VS Code integrations
5. **Suggest interesting approaches** - Functional patterns, concurrency, visualization libraries

## Running Solutions

### Python (2025 pattern)

```bash
# Using the click-based CLI
python advent.py 1 input.txt      # Run part 1
python advent.py 2 input.txt      # Run part 2
python advent.py 1 -v input.txt   # Verbose output
python advent.py 1 -vv input.txt  # Very verbose output
```

### Input Handling

- Input files are typically named `input.txt` (real input) or `sample_input.txt` (examples from puzzle description)
- Each line usually needs `.strip()` to remove trailing newlines
- Common patterns: grid parsing, number lists, grouped paragraphs separated by blank lines

## Code Style

- Solutions should be self-contained within their day folder
- Prioritize clarity over extreme optimization (unless the puzzle demands it)
- Include verbose output options for debugging
- Use `rich` formatting for colorful, readable output

## What I Want Help With

✅ **Do help with:**
- Setting up new day folders from the skeleton
- Parsing complex input formats
- Python/Go syntax and features I might not know
- Package recommendations and usage
- Performance optimization techniques (after I have a working solution)
- Testing approaches
- Build and project tooling
- Git operations and workflow

❌ **Don't help with (unless asked):**
- The core puzzle algorithm
- Mathematical insights needed to solve the puzzle
- Optimization tricks specific to the puzzle's answer
