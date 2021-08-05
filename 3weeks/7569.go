package main

import (
	"bufio"
	"fmt"
	"os"
)

var dx = []int{-1, 1, 0, 0, 0, 0}
var dy = []int{0, 0, 0, 0, -1, 1}
var dz = []int{0, 0, -1, 1, 0, 0}
var n, m, h int

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
	if len(q.x) == 0 && len(q.y) == 0 {
		return true
	} else {
		return false
	}
}

func boxInit() ([][][]int, [][][]bool) {
	box := make([][][]int, h)
	visit := make([][][]bool, h)
	for i := 0; i < h; i++ {
		box[i] = make([][]int, m)
		visit[i] = make([][]bool, m)
		for j := 0; j < m; j++ {
			box[i][j] = make([]int, n)
			visit[i][j] = make([]bool, n)
		}
	}
	return box, visit
}

func boxInput(box [][][]int, visit [][][]bool, q []Queue, io *bufio.Reader) ([][][]int, [][][]bool, []Queue) {
	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				fmt.Fscan(io, &box[i][j][k])
				if box[i][j][k] == 1 {
					q[i].Set(j, k)
				}
				if box[i][j][k] == -1 {
					visit[i][j][k] = true
				}
			}
		}
	}
	return box, visit, q
}

func qEmpty(q []Queue) bool {

}

func bfs(q []Queue) {
	ans := -1
	for qEmpty(q) == false {

	}

}

func main() {
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &n, &m, &h)
	box, visit := boxInit()
	q := make([]Queue, h)
	box, visit, q = boxInput(box, visit, q, io)
	bfs(q)
}