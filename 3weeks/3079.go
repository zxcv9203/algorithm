package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	n, m := 0, 0
	var audit []int
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &n, &m)
	for i := 0; i < n; i++ {
		tmp := 0
		fmt.Fscan(io, &tmp)
		audit = append(audit, tmp)
	}
	sort.Ints(audit)
	st, ed := 0, m * audit[n - 1]
	ans := ed
	for st <= ed {
		mid := (st + ed) / 2
		sum := 0
		for i := 0; i < n; i++ {
			sum += mid / audit[i]
		}
		if sum >= m {
			ans = min(ans, mid)
			ed = mid - 1
		} else {
			st = mid + 1
		}
	}
	fmt.Println(ans)
}