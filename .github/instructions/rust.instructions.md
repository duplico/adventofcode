---
applyTo: "**/*.rs"
---

# Rust Instructions for Advent of Code

## Rust Style for AoC

- Prioritize readability; AoC is about solving puzzles, not production code
- Use `unwrap()` freely - input is trusted, no need for extensive error handling
- Leverage iterators and iterator adapters extensively
- Use pattern matching (`match`, `if let`, `let else`)
- Prefer owned types (`String`, `Vec`) over references for simplicity

## Useful Crates

- **itertools**: Extended iterator methods (`permutations`, `combinations`, `tuple_windows`)
- **regex**: Regular expression parsing
- **nom** or **winnow**: Parser combinators for complex inputs
- **petgraph**: Graph data structures and algorithms
- **rayon**: Parallel iterators (drop-in parallelism)
- **rustc-hash**: Fast hash maps (`FxHashMap`, `FxHashSet`)
- **pathfinding**: A*, Dijkstra, BFS, etc.

## Cargo.toml Starter

```toml
[package]
name = "advent"
version = "0.1.0"
edition = "2024"

[dependencies]
itertools = "0.13"
regex = "1"
rayon = "1.10"
rustc-hash = "2"

[profile.release]
opt-level = 3
lto = true
```

## Input Parsing Patterns

```rust
// Read entire file
let input = std::fs::read_to_string(filename).unwrap();

// Lines as iterator
let lines = input.lines();

// Parse integers per line
let numbers: Vec<i64> = input.lines()
    .map(|l| l.parse().unwrap())
    .collect();

// Parse space-separated integers
let nums: Vec<i64> = line.split_whitespace()
    .map(|n| n.parse().unwrap())
    .collect();

// Grid as Vec<Vec<char>>
let grid: Vec<Vec<char>> = input.lines()
    .map(|l| l.chars().collect())
    .collect();

// Paragraph-separated groups
let groups: Vec<&str> = input.split("\n\n").collect();
```

## Iterator Patterns

```rust
use itertools::Itertools;

// Sliding windows
for (a, b) in numbers.iter().tuple_windows() { }

// All pairs
for (a, b) in items.iter().combinations(2) { }

// Permutations
for perm in items.iter().permutations(items.len()) { }

// Group consecutive
for (key, group) in &items.iter().group_by(|x| **x) { }

// Parallel iteration (rayon)
use rayon::prelude::*;
let sum: i64 = numbers.par_iter().map(|&x| x * 2).sum();
```

## Common Patterns

```rust
// Fast hash maps
use rustc_hash::FxHashMap;
let mut seen: FxHashMap<(i32, i32), bool> = FxHashMap::default();

// BFS template
use std::collections::VecDeque;
let mut queue = VecDeque::new();
queue.push_back((start, 0));
while let Some((pos, dist)) = queue.pop_front() {
    if seen.contains(&pos) { continue; }
    seen.insert(pos);
    // ... add neighbors
}
```

## Running Solutions

```bash
# Debug build (fast compile, slow run)
cargo run -- input.txt

# Release build (slow compile, fast run)
cargo run --release -- input.txt

# Quick iteration
cargo watch -x "run -- sample_input.txt"
```

## CLI Structure

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];
    let part = args.get(2).map(|s| s.as_str()).unwrap_or("1");
    
    match part {
        "1" => part1(filename),
        "2" => part2(filename),
        _ => eprintln!("Unknown part: {}", part),
    }
}
```

## Rust 2024 Edition Features

- Lifetime capture rules improvements
- `gen` blocks for generators (nightly)
- Enhanced async/await patterns
- RPITIT (return position impl trait in traits)
