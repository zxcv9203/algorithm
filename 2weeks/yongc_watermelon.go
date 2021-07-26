package main

func sol(n int) string {
	var watermelon string
	for i := 1; i <= n; i++ {
		if i % 2 == 1 {
			watermelon += "수"
		} else {
			watermelon += "박"
		}
	}
	return watermelon
}

//func main() {
//	fmt.Println(sol(12))
//}