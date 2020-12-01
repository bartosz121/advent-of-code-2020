package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readFile() []int {
	file, ferr := os.Open("input.txt")
	if ferr != nil {
		panic(ferr)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)
	var data []int

	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		data = append(data, x)
	}

	return data
}

func part1(numbers []int) int {
	var result int = -1
	for _, n1 := range numbers {
		for _, n2 := range numbers {
			if n1+n2 == 2020 {
				fmt.Println(n1, n2, n1*n2)
				result = n1 * n2
				return result
			}
		}
	}
	return result
}

func part2(numbers []int) int {
	var result int = -1
	for _, n1 := range numbers {
		for _, n2 := range numbers {
			for _, n3 := range numbers {
				if n1+n2+n3 == 2020 {
					fmt.Println(n1, n2, n3, n1*n2*n3)
					result = n1 * n2 * n3
					return result
				}
			}
		}
	}
	return result
}

func main() {
	// Read file first
	var input []int = readFile()

	// Part 1
	fmt.Println(part1(input))

	// Part 2
	fmt.Println(part2(input))
}
