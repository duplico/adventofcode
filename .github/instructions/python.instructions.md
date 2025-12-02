---
applyTo: "**/*.py"
---

# Python Instructions for Advent of Code

## Modern Python Style

- Use Python 3.14 features when appropriate
- Always include type hints for function signatures
- Use `match` statements for complex conditionals
- Prefer f-strings for string formatting
- Use walrus operator (`:=`) when it improves readability
- Consider dataclasses or named tuples for structured data

## Free-Threaded Python (No-GIL)

When parallelism could help (e.g., processing independent puzzle parts):
- Suggest `concurrent.futures.ThreadPoolExecutor` patterns
- Mention when free-threaded Python could provide speedups
- Note that GIL removal enables true parallelism in CPU-bound code

## Preferred Packages

- **CLI**: `click` (already in use)
- **Output**: `rich` for colored/formatted console output
- **Data**: `polars` for dataframe operations if needed
- **Parsing**: `parse` or `regex` for complex pattern matching
- **Math**: `sympy` for symbolic math, `numpy` for numerical
- **Graphs**: `networkx` for graph algorithms
- **Visualization**: `matplotlib`, `plotly`, or `rich` progress bars

## Input Parsing Patterns

```python
# Standard file reading
with open(filename, 'r') as f:
    lines = [line.strip() for line in f]

# Grid parsing
grid = [list(line.strip()) for line in open(filename)]

# Numbers per line
numbers = [int(line.strip()) for line in open(filename)]

# Paragraph-separated groups
groups = open(filename).read().strip().split('\n\n')
```

## CLI Pattern (from skel.py)

Use the established click pattern:
- `@cli.command(name='1')` for part 1
- `@cli.command(name='2')` for part 2  
- `@common_options` decorator for filename and verbose flags
- Use `console.print()` with rich markup for output

## Verbose Output

- `-v`: Show key intermediate steps
- `-vv`: Show detailed trace/debug info
- Use `if verbose >= 1:` and `if verbose >= 2:` patterns
