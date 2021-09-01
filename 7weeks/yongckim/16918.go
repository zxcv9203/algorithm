package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r *bufio.Reader
	w *bufio.Writer
	dx = [4]int{-1, 1, 0, 0}
	dy = [4]int{0, 0, -1, 1}
	arr [201][201]rune
	x, y, n int
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

func safe(i, j int) bool {
	return i >= 0 && i < x && j >= 0 && j < y
}

func boom(cp [201][201]rune) [201][201]rune {
	var q Queue

	for t := 2; t <= n; t++ {
		if t % 2 == 0 {
			for i := 0; i < x; i++ {
				for j := 0; j < y; j++ {
					if cp[i][j] == 'O' {
						q.Push(i, j)
					} else {
						cp[i][j] = 'O'
					}
				}
			}
			continue
		}
		for q.Size() > 0 {
			qx, qy := q.Pop()
			cp[qx][qy] = '.'
			for i := 0; i < 4; i++ {
				nx := qx + dx[i]
				ny := qy + dy[i]
				if safe(nx, ny) == true {
					cp[nx][ny] = '.'
				}
			}
		}
	}
	return cp
}

func main() {
	defer w.Flush()
	fmt.Fscan(r, &x, &y, &n)
	for i := 0; i < x; i++ {
		r.Reset(os.Stdin)
		for j := 0; j < y; j++ {
			fmt.Fscanf(r, "%c", &arr[i][j])
		}
	}
	arr = boom(arr)
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			fmt.Fprintf(w,"%c", arr[i][j])
		}
		fmt.Fprintln(w)
	}
}