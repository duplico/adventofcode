---
applyTo: "**/*.c,**/*.h"
---

# C Instructions for Advent of Code

## C Style for AoC

- Use C11 or C23 features where appropriate
- Prioritize readability over micro-optimization
- Use meaningful variable names even for puzzle code
- Include comments for non-obvious logic

## C23 Features to Consider

- `nullptr` instead of `NULL`
- `typeof` and `typeof_unqual`
- `#embed` for including binary data
- `constexpr` for compile-time constants
- Digit separators: `1'000'000`
- Binary literals: `0b1010`
- `[[nodiscard]]`, `[[maybe_unused]]` attributes

## Memory Management

- Prefer stack allocation for small, fixed-size data
- Use `malloc`/`free` for dynamic sizes
- Consider arena allocation for complex puzzles
- Always check allocation failures in production, okay to skip for AoC

## Input Parsing Patterns

```c
// Read lines
char line[256];
FILE *f = fopen(filename, "r");
while (fgets(line, sizeof(line), f)) {
    line[strcspn(line, "\n")] = 0;  // Strip newline
    // process line
}
fclose(f);

// Parse integers
int x, y;
sscanf(line, "%d,%d", &x, &y);

// Read entire file
fseek(f, 0, SEEK_END);
long len = ftell(f);
fseek(f, 0, SEEK_SET);
char *content = malloc(len + 1);
fread(content, 1, len, f);
content[len] = '\0';
```

## Useful Patterns

- Use `struct` for grouping related data
- Consider function pointers for part1/part2 dispatch
- Use `enum` for state machines
- `qsort` and `bsearch` from stdlib for sorting/searching

## Compilation

```bash
gcc -std=c23 -Wall -Wextra -O2 -o advent advent.c
# Or with sanitizers for debugging:
gcc -std=c23 -Wall -Wextra -g -fsanitize=address,undefined -o advent advent.c
```

## Suggested Libraries (header-only)

- **stb**: Single-file libraries for various tasks
- **uthash**: Hash table macros
- **vec**: Dynamic arrays
