package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, k int
var a [150]int


func dfs(player, cnt int) {
	if player == k {
		fmt.Println(cnt)
		return
	} else if cnt == n {
		fmt.Println(-1)
		return
	}
	dfs(a[player], cnt + 1)
}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n, &k)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &a[i])
	}
	dfs(0, 0)
}