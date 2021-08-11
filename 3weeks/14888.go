package main

import (
	"bufio"
	"fmt"
	"os"
)

type operator struct {
	sum int
	sub int
	mul int
	div int
}

var op operator

var n int
var num []int
var maxAns int = -1e9
var minAns int = 1e9

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func dfs(op operator, idx ,total int) {
	if idx == n {
		maxAns = max(maxAns, total)
		minAns = min(minAns, total)
		return
	}
	if op.sum > 0 {
		op.sum--
		dfs(op, idx + 1, total + num[idx])
		op.sum++
	}
	if op.sub > 0 {
		op.sub--
		dfs(op, idx + 1, total - num[idx])
		op.sub++
	}
	if op.mul > 0 {
		op.mul--
		dfs(op, idx + 1, total * num[idx])
		op.mul++
	}
	if op.div > 0 {
		op.div--
		dfs(op, idx + 1, total / num[idx])
		op.div++
	}

}
func main() {
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &n)
	for i := 0; i < n; i++ {
		tmp := 0
		fmt.Fscan(io, &tmp)
		num = append(num, tmp)
	}
	fmt.Fscan(io, &op.sum, &op.sub, &op.mul, &op.div)
	dfs(op, 1, num[0])
	fmt.Println(maxAns)
	fmt.Println(minAns)

}