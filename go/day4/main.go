package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	var rawPassport []string
	var passportStrings [][]string
	part1 := 0
	part2 := 0
	input := readFile("input.txt")
	for i, a := range input {
		if len(a) == 0 {
			passportStrings = append(passportStrings, rawPassport)
			// clear passport slice
			rawPassport = nil
			continue
		}
		rawPassport = append(rawPassport, a)
		//TODO edge case where last passport from input is not passed to check make it more elegenat later
		if i == len(input)-1 {
			passportStrings = append(passportStrings, rawPassport)
		}
	}

	var passport []string
	for _, p := range passportStrings {
		passport = nil
		for _, v := range p {
			if strings.Contains(v, " ") {
				for _, k := range strings.Split(v, " ") {
					passport = append(passport, k)
				}
			} else {
				passport = append(passport, v)
			}
		}
		// passport validated ready to work
		if checkIfPassportValid(passport) {
			part1++
			// adding dash at the end to make things easier in part2
			if checkIfPassportMeetsRules(strings.Join(passport, "-") + "-") {
				part2++
			}
		}
	}
	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// Return true if passport is valid
func checkIfPassportValid(passport []string) bool {
	passportFields := []string{
		// ignore "cid"
		"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",
	}

	for _, field := range passportFields {
		if !strings.Contains(strings.Join(passport, " "), field) {
			return false
		}
	}
	return true
}

func checkIfPassportMeetsRules(passport string) bool {
	byr := passport[strings.Index(passport, "byr")+4:][:strings.Index(passport[strings.Index(passport, "byr")+4:], "-")]
	iyr := passport[strings.Index(passport, "iyr")+4:][:strings.Index(passport[strings.Index(passport, "iyr")+4:], "-")]
	eyr := passport[strings.Index(passport, "eyr")+4:][:strings.Index(passport[strings.Index(passport, "eyr")+4:], "-")]
	hgt := passport[strings.Index(passport, "hgt")+4:][:strings.Index(passport[strings.Index(passport, "hgt")+4:], "-")]
	hcl := passport[strings.Index(passport, "hcl")+4:][:strings.Index(passport[strings.Index(passport, "hcl")+4:], "-")]
	ecl := passport[strings.Index(passport, "ecl")+4:][:strings.Index(passport[strings.Index(passport, "ecl")+4:], "-")]
	pid := passport[strings.Index(passport, "pid")+4:][:strings.Index(passport[strings.Index(passport, "pid")+4:], "-")]
	// fmt.Println(byr, byrRule(byr))
	// fmt.Println(iyr, iyrRule(iyr))
	// fmt.Println(eyr, eyrRule(eyr))
	// fmt.Println(hgt, hgtRule(hgt))
	// fmt.Println(hcl, hclRule(hcl))
	// fmt.Println(ecl, eclRule(ecl))
	// fmt.Println(pid, pidRule(pid))
	// fmt.Println("---------------------------------------------------")
	return byrRule(byr) && iyrRule(iyr) && eyrRule(eyr) && hgtRule(hgt) && hclRule(hcl) && eclRule(ecl) && pidRule(pid)
}

func byrRule(s string) bool {
	year, err := strconv.Atoi(s)
	if err != nil {
		return false
	}
	if 1920 <= year && year <= 2002 {
		return true
	}
	return false
}

func iyrRule(s string) bool {
	year, err := strconv.Atoi(s)
	if err != nil {
		return false
	}
	if 2010 <= year && year <= 2020 {
		return true
	}
	return false
}

func eyrRule(s string) bool {
	year, err := strconv.Atoi(s)
	if err != nil {
		return false
	}
	if 2020 <= year && year <= 2030 {
		return true
	}
	return false
}

func hgtRule(s string) bool {
	l := len(s)
	if len(s[:l-2]) == 0 {
		return false
	}
	n, err := strconv.Atoi(s[:l-2])
	if err != nil {
		return false
	}
	u := s[l-2:]

	if u == "cm" || u == "in" {
		if u == "cm" {
			return 150 <= n && n <= 193
		} else if u == "in" {
			return 59 <= n && n <= 76
		}
	}
	return false
}

func hclRule(s string) bool {
	if s[0] == '#' {
		for _, c := range s[1:] {
			if !(unicode.IsDigit(c) || (c >= 'a' || c <= 'f')) {
				return false
			}
		}
		return true
	}
	return false
}

func eclRule(s string) bool {
	ecl := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	for _, t := range ecl {
		if t == s {
			return true
		}
	}
	return false
}

func pidRule(s string) bool {
	if len(s) != 9 {
		return false
	}
	for _, c := range s {
		if !(c >= '0' || c <= 9) {
			return false
		}
	}
	return true
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
