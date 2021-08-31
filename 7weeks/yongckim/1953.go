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
	hate [101][]int
	visit [101]int
	team [2][]int
)

func dfs(player, num int) {
	visit[player] = num
	for _, hater := range hate[player] {
		if visit[hater] == 0{
			dfs(hater, num * -1)
		}
	}
}

func main() {
	r,w = bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 1; i <= n; i++ {
		param := 0
		fmt.Fscan(r, &param)
		for j := 0; j < param; j++{
			tmp := 0
			fmt.Fscan(r, &tmp)
			hate[i] = append(hate[i], tmp)
			hate[tmp] = append(hate[tmp], i)
		}
	}
	for i := 1; i <= n; i++ {
		if visit[i] == 0 {
			dfs(i, 1)
		}
	}

	for i := 1; i <= n; i++ {
		if visit[i] == 1 {
			team[0] = append(team[0], i)
		} else {
			team[1] = append(team[1], i)
		}
	}
	fmt.Fprintln(w, len(team[0]))
	for _, player := range team[0] {
		fmt.Fprint(w, player, " ")
	}
	fmt.Fprintln(w)
	fmt.Fprintln(w, len(team[1]))
	for _, player := range team[1] {
		fmt.Fprint(w, player, " ")
	}
	fmt.Fprintln(w)
}