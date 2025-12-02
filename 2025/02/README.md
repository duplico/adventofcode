# Advent of Code - Clojure Solution

## Setup

Requires Clojure CLI tools (`clj`/`clojure`).

## Running

```bash
# Part 1
clj -M:run 1 input.txt
clj -M:run 1 input.txt -v    # verbose

# Part 2
clj -M:run 2 input.txt
```

## REPL Development

```bash
# Start a REPL (with nREPL for editor integration)
clj -M:repl

# Or plain REPL
clj
```

Then in the REPL:

```clojure
(require '[advent :refer :all])
(part1 "sample_input.txt")
(part2 "input.txt")
```

## Running Tests

```bash
clj -M:test
```
