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

var maskBitmaskStr string
var maskBitmask uint64 = 0x00
var maskValue uint64 = 0x00
var mem = make(map[uint64]uint64)
var cmdRexp = regexp.MustCompile(`^(?P<var>mask|mem)(\[(?P<addr>\d+)\])? = (?P<value>[\dX]+)$`)

func partOneCmd(command map[string]string) {
	switch command["var"] {
	case "mask":
		// Update our mask's mask
		maskBitmaskStr = strings.ReplaceAll(command["value"], "1", "0")
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

func setFloatingMem(addr string, val uint64) {
	if strings.Contains(addr, "X") {
		// The string is floating, need to resolve the ambiguity:
		setFloatingMem(strings.Replace(addr, "X", "1", 1), val)
		setFloatingMem(strings.Replace(addr, "X", "0", 1), val)
	} else {
		// The string is fixed, need to set values:
		address, _ := strconv.ParseUint(addr, 2, 36)
		mem[address] = val
	}
}

func partTwoCmd(command map[string]string) {
	switch command["var"] {
	case "mask":
		maskBitmaskStr = command["value"]
	case "mem":
		value, _ := strconv.ParseUint(command["value"], 10, 64)
		addr, _ := strconv.ParseUint(command["addr"], 10, 64)
		addrStr := strconv.FormatUint(addr, 2)
		addrStr = strings.Repeat("0", len(maskBitmaskStr)-len(addrStr)) + addrStr
		// TODO: Not this:
		addrStrFloating := ""
		for i := 0; i < len(maskBitmaskStr); i++ {
			if maskBitmaskStr[i] == '0' {
				addrStrFloating += string([]byte{addrStr[i]})
			} else {
				addrStrFloating += string([]byte{maskBitmaskStr[i]})
			}
		}

		setFloatingMem(addrStrFloating, value)
	}
}

func main() {
	inputFile := "sample_input.txt"

	if len(os.Args) > 3 || len(os.Args) == 1 {
		panic("Expected: advent14 {1|2} [input.txt]")
	} else if len(os.Args) == 3 {
		inputFile = os.Args[2]
	}

	adventPart := os.Args[1]

	file, err := os.Open(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		match := cmdRexp.FindStringSubmatch(line)
		command := make(map[string]string)
		for i, name := range cmdRexp.SubexpNames() {
			// fmt.Printf("%d, %s\n", i, name)
			if i != 0 && name != "" {
				command[name] = match[i]
			}
		}

		switch adventPart {
		case "1":
			partOneCmd(command)
		case "2":
			partTwoCmd(command)
		default:
			panic("No such part for day 14!")
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
