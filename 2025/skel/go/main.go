package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

var verbose bool

// readLines reads all lines from a file
func readLines(filename string) []string {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error opening file: %v\n", err)
		os.Exit(1)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "Error reading file: %v\n", err)
		os.Exit(1)
	}

	return lines
}

func part1(filename string) {
	lines := readLines(filename)

	if verbose {
		fmt.Printf("Read %d lines from %s\n", len(lines), filename)
	}

	// TODO: Implement solution
	result := 0

	fmt.Printf("Part 1: %d\n", result)
}

func part2(filename string) {
	lines := readLines(filename)

	if verbose {
		fmt.Printf("Read %d lines from %s\n", len(lines), filename)
	}

	// TODO: Implement solution
	result := 0

	fmt.Printf("Part 2: %d\n", result)
}

func main() {
	flag.BoolVar(&verbose, "v", false, "Enable verbose output")
	flag.Parse()

	args := flag.Args()
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s [-v] <part> <filename>\n", os.Args[0])
		os.Exit(1)
	}

	part := args[0]
	filename := args[1]

	switch part {
	case "1":
		part1(filename)
	case "2":
		part2(filename)
	default:
		fmt.Fprintf(os.Stderr, "Unknown part: %s. Use 1 or 2.\n", part)
		os.Exit(1)
	}
}
