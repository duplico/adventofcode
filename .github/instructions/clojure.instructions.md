---
applyTo: "**/*.clj,**/*.cljs,**/*.cljc,**/*.edn"
---

# Clojure Instructions for Advent of Code

## Clojure Style for AoC

- Embrace functional programming and immutability
- Use threading macros (`->`, `->>`, `as->`) for clarity
- Leverage lazy sequences for large datasets
- Use destructuring liberally
- Prefer pure functions; isolate side effects

## Core Functions to Remember

```clojure
;; Sequence operations
(map f coll)
(filter pred coll)
(reduce f init coll)
(partition n coll)
(partition-by f coll)
(group-by f coll)
(frequencies coll)
(take n coll) (drop n coll)
(take-while pred coll)

;; Transformations
(into {} coll)  ; convert to map
(into [] coll)  ; convert to vector
(into #{} coll) ; convert to set

;; Useful
(iterate f x)        ; infinite sequence
(cycle coll)         ; infinite repetition
(interleave a b)
(zipmap keys vals)
```

## Input Parsing Patterns

```clojure
;; Read lines
(def lines (clojure.string/split-lines (slurp filename)))

;; Parse integers per line
(def numbers (map #(Integer/parseInt %) lines))

;; Parse space-separated integers
(defn parse-ints [line]
  (map #(Integer/parseInt %) (clojure.string/split line #"\s+")))

;; Paragraph-separated groups
(def groups (clojure.string/split (slurp filename) #"\n\n"))

;; Grid as vector of vectors
(def grid (mapv vec lines))
```

## REPL-Driven Development

- Use the REPL interactively to explore solutions
- `(def sample (slurp "sample_input.txt"))` for quick testing
- Use `comment` blocks for scratch work
- `(time expr)` to measure performance

## Useful Libraries

- **clojure.set**: Set operations (union, intersection, difference)
- **clojure.string**: String manipulation
- **clojure.math.combinatorics**: Permutations, combinations
- **instaparse**: Parser generator for complex inputs

## Running Solutions

```bash
# With Clojure CLI
clj -M advent.clj input.txt

# With Leiningen
lein run input.txt

# Or in REPL
(load-file "advent.clj")
(part1 "input.txt")
```
