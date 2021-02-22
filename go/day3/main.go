package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := readFile("input.txt")

	// part 1
	part1 := countTrees(3, 1, input)
	fmt.Println("Part 1:", part1)

	// part 2
	s1 := countTrees(1, 1, input)
	s2 := countTrees(5, 1, input)
	s3 := countTrees(7, 1, input)
	s4 := countTrees(1, 2, input)
	fmt.Println("Part 2:", part1*s1*s2*s3*s4)
}

func countTrees(x int, y int, track []string) int {
	xMax := len(track[0])
	treeASCII := int('#')
	trees := 0
	currentPosition := map[string]int{
		"x": 0,
		"y": 0,
	}

	for i := 0; i < len(track); i++ {
		if currentPosition["y"] > len(track) {
			break
		}
		c := track[currentPosition["y"]][currentPosition["x"]%xMax]
		if c == byte(treeASCII) {
			trees++
		}
		currentPosition["x"] += x
		currentPosition["y"] += y
	}

	return trees
}

func readFile(fileName string) []string {
	var data []string
	// Read from file
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}
	return data
}
