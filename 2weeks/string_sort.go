package main

import (
	"sort"
)


func solution(strings []string, n int) []string {
	sort.Slice(strings, func(i, j int) bool {
		if strings[i][n] != strings[j][n] {
			return strings[i][n] < strings[j][n]
		}
		return strings[i] < strings[j]
	})
	return strings
}
//
//func main() {
//	strings := []string{"car", "bed", "sun"}
//	solution(strings, 1)
//	for _, value := range strings {                                   test code
//		fmt.Println(value)
//	}
//}