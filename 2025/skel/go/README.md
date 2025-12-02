# Advent of Code - Go Solution

## Running

```bash
# Run directly
go run . 1 input.txt
go run . 2 input.txt -v

# Build and run
go build -o advent .
./advent 1 input.txt
./advent -v 2 input.txt
```

## Build optimized

```bash
go build -ldflags="-s -w" -o advent .
```
