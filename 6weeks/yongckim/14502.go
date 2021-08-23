package main

import (
	"bufio"
	"fmt"
	"os"
)

type Queue struct {
	x []int
	y []int
}

func (q *Queue) Set(x, y int) {
	q.x = append(q.x, x)
	q.y = append(q.y, y)
}

func (q *Queue) Get() (int, int) {
	x, xs := q.x[0], q.x[1:]
	q.x = xs
	y, ys := q.y[0], q.y[1:]
	q.y = ys
	return x, y
}

func (q *Queue) Empty() bool {
	if len(q.x) == 0 {
		return true
	} else {
		return false
	}

}

func (q *Queue) Size() int {
	return len(q.x)
}

func safe(x, y int) bool {
	return x >= 0 && x < n && y >= 0 && y < m
}

var res [][]int
var n, m int
var q Queue

dx := []int{1, -1, 0, 0}
dy := []int{0, 0, 1, -1}
func bfs() {

}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	res = make([][]int, n)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			tmp := 0
			fmt.Fscan(r, &tmp)
			res[i] = append(res[i], tmp)
			if tmp == 2 {
				q.Set(i, j)
			}
		}
	}
	bfs()
}