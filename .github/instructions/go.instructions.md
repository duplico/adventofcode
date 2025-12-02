---
applyTo: "**/*.go"
---

# Go Instructions for Advent of Code

## Go Style for AoC

- Keep solutions simple and readable
- Use Go 1.23+ features (iterators, range-over-func, etc.)
- Prefer standard library, but suggest interesting packages when valuable
- Use `fmt.Printf` for verbose output with format verbs

## Interesting Go Features to Consider

- Generic functions for reusable utilities
- `slices` and `maps` packages for common operations
- `cmp` package for comparison functions
- Range-over-func iterators (Go 1.23+)
- Structured logging with `slog`

## Suggested Packages

- **CLI**: `cobra` or `flag` (stdlib)
- **Output**: `fatih/color` for colored output
- **Data structures**: `golang.org/x/exp/slices`, `golang.org/x/exp/maps`

## Input Parsing Patterns

```go
// Read all lines
file, _ := os.Open(filename)
scanner := bufio.NewScanner(file)
var lines []string
for scanner.Scan() {
    lines = append(lines, scanner.Text())
}

// Read entire file
data, _ := os.ReadFile(filename)
content := string(data)
```

## Project Structure

Each day can be a standalone `main` package or part of a larger module.
