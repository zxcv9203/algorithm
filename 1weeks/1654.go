package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var k, n int
	io := bufio.NewReader(os.Stdin)

	fmt.Fscan(io, &k, &n)
	cable := make([]int, k)
	for i := 0; i < k; i++ {
		fmt.Fscan(io, &cable[i])
	}
	sort.Ints(cable)
	ed := cable[k - 1]
	for st := 1; st <= ed; {
		mid := (st + ed) / 2
		ret := 0
		for i := 0; i < k; i++ {
			ret += cable[i] / mid
		}
		if ret >= n {
			st = mid + 1
		} else {
			ed = mid - 1
		}
	}
	fmt.Println(ed)
}
