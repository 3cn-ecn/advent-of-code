package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}

func part1() int {
	dat, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	sum := 0
	for _, line := range lines {
		digits := []int{}
		for _, c := range line {
			if unicode.IsDigit(c) {
				digits = append(digits, int(c-'0'))
			}
		}
		sum += digits[0]*10 + digits[len(digits)-1]
	}
	return sum
}

func part2() int {
	map_ := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	dat, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(dat), "\n")
	sum := 0
	for _, line := range lines {
		digits := []int{}
		buff := ""
		for _, c := range line {
			buff += string(c)
			if unicode.IsDigit(c) {
				digits = append(digits, int(c-'0'))
				buff = ""
			} else if len(buff) >= 3 {
				for i := 0; i < len(buff)-2; i++ {
					if _, ok := map_[buff[i:]]; ok {
						digits = append(digits, map_[buff[i:]])
						buff = ""
					}
				}
			}
			fmt.Println(digits)
		}
		sum += digits[0]*10 + digits[len(digits)-1]
	}
	return sum
}
