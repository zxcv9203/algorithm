package main

import (
	"bufio"
	"fmt"
	"os"
)

var dp [31][31]int

func main() {
	r, w := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var n, m int
	fmt.Fscan(r, &n, &m)
	
}