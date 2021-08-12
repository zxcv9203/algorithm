package main

import (
	"bufio"
	"fmt"
	"os"
)

const M int = 501
var dp[M][M] int
var tri[M][M] int
var n int

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
func main() {
	var ans int
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 1; i <= n; i++ {
		for j := 1; j <= i; j++ {
			fmt.Fscan(r, &tri[i][j])
		}
	}
	dp[1][1] = tri[1][1]
	for i := 2; i <= n; i++ {
		for j := 1; j <= i; j++ {
			dp[i][j] = tri[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])
		}
	}
	for i := 1; i <= n; i++ {
		ans = max(ans, dp[n][i])
	}
	fmt.Fprintln(w, ans)
}