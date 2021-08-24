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

var n, m int
var ans int
var dx = []int{1, -1, 0, 0}
var dy = []int{0, 0, 1, -1}

func safe(x, y int) bool {
	return x >= 0 && x < n && y >= 0 && y < m
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func safetyZone(res [9][9]int) {
	safety := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if res[i][j] == 0 {
				safety++
			}
		}
	}
	ans = max(ans, safety)
}

func bfs(res [9][9]int, q Queue) {
	for q.Empty() == false {
		size := q.Size()
		for i := 0; i < size; i++ {
			qx, qy := q.Get()
			for j := 0; j < 4; j++ {
				nx := qx + dx[j]
				ny := qy + dy[j]
				if safe(nx, ny) && res[nx][ny] == 0 {
					q.Set(nx, ny)
					res[nx][ny] = 2
				}
			}
		}
	}
	safetyZone(res)
}

func dfs(res *[9][9]int, q *Queue, i, j, cnt int) {
	if cnt == 3 {
		bfs(*res, *q)
		return
	}
	if i == n {
		return
	}
	if res[i][j] == 0 {
		res[i][j] = 1
		if j + 1 >= m {
			dfs(res, q, i+1, 0, cnt+1)
		} else {
			dfs(res, q, i, j + 1, cnt + 1)
		}
		res[i][j] = 0
	}
	if j + 1 >= m {
		dfs(res, q, i+1, 0, cnt)
	} else {
		dfs(res, q, i, j + 1, cnt)
	}
}


func sol(res [9][9]int, q Queue, i, j int) {
	dfs(&res, &q, i, j, 0)
}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var q Queue
	var res [9][9]int

	fmt.Fscan(r, &n, &m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(r, &res[i][j])
			if res[i][j] == 2 {
				q.Set(i, j)
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if res[i][j] == 0 {
				sol(res, q, i, j)
			}
		}
	}
	fmt.Fprintln(w, ans)
}
