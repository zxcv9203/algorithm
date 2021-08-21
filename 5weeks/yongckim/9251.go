package main

import (
	"bufio"
	"fmt"
	"os"
)
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var s1, s2 string
	dp := [1001][1001]int{}
	fmt.Fscan(r, &s1, &s2)
	s1Len, s2Len := len(s1), len(s2)
	for i := 1; i <= s1Len; i++ {
		for j := 1; j <= s2Len; j++ {
			if s1[i - 1] == s2[j - 1] {
				dp[i][j] = dp[i - 1][j - 1] + 1
			} else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
			}
		}
	}
	fmt.Fprintln(w, dp[s1Len][s2Len])
}
