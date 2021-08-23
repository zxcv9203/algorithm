package main

import (
	"bufio"
	"fmt"
	"os"
)

var n, k int
var a [150]int
var visit [150]int

func dfs(idx int) {

}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n, &k)
	dfs(0)
}