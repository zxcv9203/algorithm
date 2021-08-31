package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r *bufio.Reader
	w *bufio.Writer
	n int
	ans int = 1e9
	nations int = 1
	field [101][101]int
	visit [101][101]bool
	dx = [4]int{-1, 1, 0, 0}
	dy = [4]int{0, 0, -1, 1}
)

type Queue struct {
	x []int
	y []int
}

func (q *Queue) Push(x, y int) {
	q.x = append(q.x, x)
	q.y = append(q.y, y)
}

func (q *Queue) Pop() (int, int) {
	x, xs := q.x[0], q.x[1:]
	q.x = xs
	y, ys := q.y[0], q.y[1:]
	q.y = ys
	return x, y
}

func (q *Queue) Size() int {
	return len(q.x)
}


func init() {
	r, w = bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
}

func safe(x, y int) bool {
	return x >= 0 && x < n && y >= 0 && y < n
}

func dfs(x, y int) {
	visit[x][y] = true
	field[x][y] = nations
	for i := 0; i < 4; i++ {
		nx := x + dx[i]
		ny := y + dy[i]
		if safe(nx, ny) && visit[nx][ny] == false && field[nx][ny] != 0 {
			dfs(nx, ny)
		}
	}
}

func bfs(nation, ret int) {
	var q Queue

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			visit[i][j] = false
			if field[i][j] == nation {
				q.Push(i, j)
				visit[i][j] = true
			}
		}
	}
	size := q.Size()
	for size > 0 {
		size = q.Size()
		for s := 0; s < size; s++ {
			qx, qy := q.Pop()
			for i := 0; i < 4; i++ {
				nx := qx + dx[i]
				ny := qy + dy[i]
				if safe(nx, ny) == false {
					continue
				}
				if field[nx][ny] != 0 && field[nx][ny] != nation {
					if ans > ret{
						ans = ret
						return
					}
				} else if visit[nx][ny] == false && field[nx][ny] == 0 {
					visit[nx][ny] = true
					q.Push(nx, ny)
				}
			}
		}
		ret++
	}
}

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &field[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if visit[i][j] == false && field[i][j] != 0{
				dfs(i, j)
				nations++
			}
		}
	}
	for i := 1; i < nations; i++ {
		bfs(i, 0)
	}
	fmt.Println(ans)
}