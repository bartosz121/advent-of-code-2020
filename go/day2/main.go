package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var validPasswordsPart1 int = 0
	var validPasswordsPart2 int = 0
	for scanner.Scan() {
		tmp := strings.Split(scanner.Text(), " ")
		password := tmp[2]
		targetChar := string(tmp[1][0])
		charCount := strings.Count(password, targetChar)

		tmpMaxMin := strings.Split(tmp[0], "-")

		min, err := strconv.Atoi(tmpMaxMin[0])
		if err != nil {
			panic(err)
		}

		max, err := strconv.Atoi(tmpMaxMin[1])
		if err != nil {
			panic(err)
		}

		// Part 1
		if charCount >= min && charCount <= max {
			validPasswordsPart1++
		}

		// Part 2
		pos1 := string(password[min-1])
		pos2 := string(password[max-1])

		if (pos1 == targetChar) != (pos2 == targetChar) {
			validPasswordsPart2++
		}
	}

	fmt.Println(validPasswordsPart1)
	fmt.Println(validPasswordsPart2)
}
