package main

import (
	"bufio"
	"fmt"
	"os"
)

var dp[21][21][21] int

func funny(a, b, c int) int {
	if a <= 0 || b <= 0 || c <= 0 {
		return 1
	}
	if a > 20 || b > 20 || c > 20 {
		return funny(20, 20, 20)
	}
	if dp[a][b][c] != 0 {
		return dp[a][b][c]
	}
	if a < b && b < c {
		dp[a][b][c] = funny(a, b, c - 1) + funny(a, b - 1, c - 1) - funny(a, b - 1, c)
	} else {
		dp[a][b][c] = funny(a - 1, b, c) + funny(a - 1, b - 1, c) + funny(a - 1, b, c - 1) - funny(a - 1, b - 1, c - 1)
	}
	return dp[a][b][c]
}

func main() {
	io, wr := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer wr.Flush()
	a, b, c := 0, 0, 0
	for true {
		fmt.Fscan(io, &a, &b, &c)
		if a == -1 && b == -1 && c == -1 {
			break
		}
		fmt.Fprintf(wr, "w(%d, %d, %d) = %d\n", a, b, c, funny(a, b, c))
	}
}
