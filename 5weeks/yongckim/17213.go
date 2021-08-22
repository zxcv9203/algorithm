package main

import (
	"bufio"
	"fmt"
	"os"
)

var dp [31][31]int
var n, m int


func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	for i := 0; i < n; i++ {
		dp[i][i] = 1
	}
	for i := 0; i < m; i++ {
		dp[0][i] = 1
	}
	for i := 1; i < n; i++ {
		for j := i + 1; j < m; j++ {
			for k := 0; k < j; k++ {
				dp[i][j] += dp[i - 1][k]
			}
		}
	}
	fmt.Fprintln(w, dp[n - 1][m - 1])
}