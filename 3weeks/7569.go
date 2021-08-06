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
	if len(q.x) == 0 {
		return true
	} else {
		return false
	}
}

func (q *Queue) Size() int {
	return len(q.x)
}

func boxInit() [][][]int {
	box := make([][][]int, h)
	for i := 0; i < h; i++ {
		box[i] = make([][]int, m)
		for j := 0; j < m; j++ {
			box[i][j] = make([]int, n)
		}
	}
	return box
}

func boxInput(box [][][]int, q Queue, io *bufio.Reader) ([][][]int, Queue) {
	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				fmt.Fscan(io, &box[i][j][k])
				if box[i][j][k] == 1 {
					q.Set(j, k, i)
				}
			}
		}
	}
	return box, q
}

func safe(x, y, z int) bool {
	return x >= 0 && x < m && y >= 0 && y < n && z >= 0 && z < h
}

func boxCheck(ans int, box [][][]int) int {
	for i := 0; i < h; i++ {
		for j := 0; j < m; j++ {
			for k := 0; k < n; k++ {
				if box[i][j][k] == 0 {
					return -1
				}
			}
		}
	}
	return ans
}

func bfs(q Queue, box [][][]int) {
	ans := -1
	size := 0
	for q.Empty() == false {
		size = q.Size()
		ans++
		for i := 0; i < size; i++ {
			qx, qy, qz := q.Get()
			for j := 0; j < 6; j++ {
				x := qx + dx[j]
				y := qy + dy[j]
				z := qz + dz[j]
				if safe(x, y, z) == false {
					continue
				}
				if box[z][x][y] == 0 {
					box[z][x][y] = 1
					q.Set(x, y, z)
				}
			}
		}
	}
	ans = boxCheck(ans, box)
	fmt.Println(ans)
}

func main() {
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &n, &m, &h)
	box := boxInit()
	var q Queue
	box, q = boxInput(box, q, io)
	bfs(q, box)
}