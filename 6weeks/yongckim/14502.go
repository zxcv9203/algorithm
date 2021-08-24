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

func checkRes(res [9][9]int) {
	fmt.Println()
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Print(res[i][j], " ")
		}
		fmt.Println()
	}
}
func checkVisit(res [9][9]bool) {
	fmt.Println()
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Print(res[i][j], " ")
		}
		fmt.Println()
	}
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

func bfs(res [9][9]int, q Queue, visit [9][9]bool) {
	for q.Empty() == false {
		size := q.Size()
		for i := 0; i < size; i++ {
			qx, qy := q.Get()
			for j := 0; j < 4; j++ {
				nx := qx + dx[j]
				ny := qy + dy[j]
				if safe(nx, ny) && res[nx][ny] != 1 && visit[nx][ny] == false{
					q.Set(nx, ny)
					visit[nx][ny] = true
					res[nx][ny] = 2
				}
			}
		}
	}
	safetyZone(res)
}



func dfs(res *[9][9]int, q *Queue, visit *[9][9]bool, i, j, cnt int) {
	if cnt == 3 {
		bfs(*res, *q, *visit)
		return
	}
	if i == n {
		return
	}
	if res[i][j] == 0 {
		res[i][j] = 1
		visit[i][j] = true
		if j + 1 >= m {
			dfs(res, q, visit, i+1, 0, cnt+1)
		} else {
			dfs(res, q, visit, i, j + 1, cnt + 1)
		}
		res[i][j] = 0
		visit[i][j] = false
	}
	if j + 1 >= m {
		dfs(res, q, visit, i+1, 0, cnt)
	} else {
		dfs(res, q, visit, i, j + 1, cnt)
	}
}


func sol(res [9][9]int, q Queue, visit [9][9]bool, i, j int) {
	dfs(&res, &q, &visit, i, j, 0)
}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var q Queue
	var res [9][9]int
	var visit [9][9]bool

	fmt.Fscan(r, &n, &m)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(r, &res[i][j])
			if res[i][j] == 2 {
				q.Set(i, j)
			}
			if res[i][j] == 1 {
				visit[i][j] = true
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if res[i][j] == 0 {
				sol(res, q, visit, i, j)
			}
		}
	}
	fmt.Println(ans)
}
