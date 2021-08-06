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
	z []int
}

func (q *Queue) Set(x, y, z int) {
	q.x = append(q.x, x)
	q.y = append(q.y, y)
	q.z = append(q.z, z)
}

func (q *Queue) Get() (int, int, int) {
	x, xs := q.x[0], q.x[1:]
	q.x = xs
	y, ys := q.y[0], q.y[1:]
	q.y = ys
	z, zs := q.z[0], q.z[1:]
	q.z = zs
	return x, y, z
}

func (q *Queue) Empty() bool {
	if len(q.x) == 0 && len(q.y) == 0 && len(q.z) == 0 {
		return true
	} else {
		return false
	}
}

func (q *Queue) Size() int {
	return len(q.x)
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

func boxInput(box [][][]int, visit [][][]bool, q Queue, io *bufio.Reader) ([][][]int, [][][]bool, Queue) {
	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				fmt.Fscan(io, &box[i][j][k])
				if box[i][j][k] == 1 {
					q.Set(j, k, i)
				}
				if box[i][j][k] == -1 {
					visit[i][j][k] = true
				}
			}
		}
	}
	return box, visit, q
}

func safe(qx, qy, qz int) bool {
	return qx >= 0 && qx < m && qy >= 0 && qy < n && qz >= 0 && qz < h
}

func visitCheck(ans int, visit [][][]bool) int {
	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				if visit[i][j][k] == false {
					return -1
				}
			}
		}
	}
	return ans
}

func bfs(q Queue, visit [][][]bool, box [][][]int) {
	ans := -1
	size := 0
	for q.Empty() == false {
		size = q.Size()
		ans++
		for i := 0; i < size; i++ {
			qx, qy, qz := q.Get()
			for j := 0; j < 6; j++ {
				qx += dx[j]
				qy += dy[j]
				qz += dz[j]
				if safe(qx, qy, qz) == false {
					continue
				}
				fmt.Println(qz, qx, qy)
				if visit[qz][qx][qy] == false && box[qz][qx][qy] == 0 {
					visit[qz][qx][qy] = true
					q.Set(qx, qy, qz)
				}
			}
		}
	}
	//ans = visitCheck(ans, visit)
	fmt.Println(visit)
	fmt.Println(ans)
}

func main() {
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &n, &m, &h)
	box, visit := boxInit()
	var q Queue
	box, visit, q = boxInput(box, visit, q, io)
	bfs(q, visit, box)
}