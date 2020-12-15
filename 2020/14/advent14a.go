package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Hello world!")

	// memory := make(map[uint]uint64)
	var maskBitmask uint64 = 0x00
	var maskValue uint64 = 0x00
	var mem = make(map[uint64]uint64)

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	cmdRexp := regexp.MustCompile(`^(?P<var>mask|mem)(\[(?P<addr>\d+)\])? = (?P<value>[\dX]+)$`)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		match := cmdRexp.FindStringSubmatch(line)
		command := make(map[string]string)
		for i, name := range cmdRexp.SubexpNames() {
			fmt.Printf("%d, %s\n", i, name)
			if i != 0 && name != "" {
				command[name] = match[i]
			}
		}

		switch command["var"] {
		case "mask":
			// Update our mask's mask
			maskBitmaskStr := strings.ReplaceAll(command["value"], "1", "0")
			maskBitmaskStr = strings.ReplaceAll(maskBitmaskStr, "X", "1")
			maskBitmask, _ = strconv.ParseUint(maskBitmaskStr, 2, 36)
			// Update our mask's value
			maskValue, _ = strconv.ParseUint(strings.ReplaceAll(command["value"], "X", "0"), 2, 36)
			fmt.Printf("Write mask bits with  %036b\n", maskBitmask)
			fmt.Printf("Write mask value with %036b\n", maskValue)
		case "mem":
			value, _ := strconv.ParseUint(command["value"], 10, 64)
			addr, _ := strconv.ParseUint(command["addr"], 10, 64)
			value = (value & maskBitmask) | maskValue
			mem[addr] = value
			fmt.Printf("Write to memory value %d at location %d\n", value, addr)
		}
	}

	var memTotal uint64 = 0x00

	for _, value := range mem {
		memTotal += value
	}

	fmt.Printf("Total memory values: %d", memTotal)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
