# Advent of Code - Clojure Solution

## Setup

Requires Clojure CLI tools (`clj`/`clojure`).

## Running

```bash
# Part 1
clj -M:run 1 ../input.txt
clj -M:run 1 ../input.txt -v    # verbose

# Part 2
clj -M:run 2 ../input.txt

# With sample input
clj -M:run 1 ../sample_input.txt
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
;; Load the namespace
(require 'advent)

;; Call functions with namespace prefix
(advent/part1 "../sample_input.txt")
(advent/part2 "../input.txt")

;; Or switch into the namespace
(in-ns 'advent)
(part1 "../sample_input.txt")

;; Reload after editing the file
(require 'advent :reload)
```

## Running Tests

```bash
clj -M:test
```
