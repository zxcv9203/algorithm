package main

import (
	"bufio"
	"fmt"
	"os"
)

var visit[] bool
var network[][] bool
type Queue struct {
	items []int
}

func (q *Queue) Set (value int) {
	q.items = append(q.items, value)
}

func (q *Queue) Get() int {
	item, items := q.items[0], q.items[1:]
	q.items = items
	return item
}

func (q *Queue) Empty() bool {
	if len(q.items) == 0 {
		return true
	} else {
		return false
	}
}

func bfs(n, computer int) {
	ans := 0
	q := Queue{}
	q.Set(n)
	visit[n] = true
	for q.Empty() == false {
		n = q.Get()
		for i := 1; i <= computer; i++ {
			if visit[i] == false && network[n][i] == true {
				q.Set(i)
				visit[i] = true
				ans++
			}
		}
	}
	fmt.Println(ans)
}

func main() {
	var computer, link int
	io := bufio.NewReader(os.Stdin)
	fmt.Fscan(io, &computer, &link)
	network = make([][]bool, computer + 1)
	visit = make([]bool, computer + 1)
	for i := 1; i <= computer; i++ {
		network[i] = make([]bool, computer + 1)
	}
	for i := 0; i < link; i++ {
		a, b := 0, 0
		fmt.Fscan(io, &a, &b)
		network[a][b] = true
		network[b][a] = true
	}
	bfs(1, computer)
}