package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var n int
	dp := [117]int{1, 1, 1, 2}
	fmt.Fscan(r, &n)
	for i := 3; i < n; i++ {
		dp[i] = dp[i - 1] + dp[i - 3]
	}
	fmt.Fprintln(w, dp[n - 1])
}
