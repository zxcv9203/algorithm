package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	dx = [4]int{-1, 1, 0, 0}
	dy = [4]int{0, 0, -1, 1}
	n int
	high int
	ans int = 1
	locate [100][100]int
)

func safe(x, y int) bool {
	return x >= 0 && x < n && y >= 0 && y < n
}

func dfs(idx, x,  y int, visit *[100][100]bool) {
	visit[x][y] = true

	for i := 0; i < 4; i++ {
		nx := x + dx[i]
		ny := y + dy[i]
		if safe(nx, ny) == true && visit[nx][ny] == false && locate[nx][ny] > idx{
			dfs(idx, nx, ny, visit)
		}
	}
}

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &locate[i][j])
			if high < locate[i][j] {
				high = locate[i][j]
			}
		}
	}
	for i := 0; i < high; i++ {
		var visit [100][100]bool
		cnt := 0
		for j := 0; j < n; j++ {
			for l := 0; l < n; l++ {
				if visit[j][l] == false && locate[j][l] > i {
					dfs(i, j, l, &visit)
					cnt++
				}
			}
		}
		if ans < cnt {
			ans = cnt
		}
	}
	fmt.Fprintln(w, ans)
}