package main

import (
	"bufio"
	"fmt"
	"os"
)
const M int = 1e3
var dp[M] int

func ioInit() (*bufio.Reader, *bufio.Writer){
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	return r, w
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func main() {
	var n int
	var seq []int
	var ans int
	r, w := ioInit()
	defer w.Flush()

	fmt.Fscan(r, &n)

	for i := 0; i < n; i++ {
		tmp := 0
		fmt.Fscan(r, &tmp)
		seq = append(seq, tmp)
	}
	for i, _ := range seq {
		dp[i] = 1
		for j := 0; j < i; j++ {
			if seq[i] > seq[j] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
		ans = max(dp[i], ans)
	}
	fmt.Fprintln(w, ans)
}
