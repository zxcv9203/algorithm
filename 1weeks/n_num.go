package main

func solution(a int, b int) int64 {
	ans := 0
	if a > b {
		a, b = b, a
	}
	for i := a; i <= b; i++ {
		ans += i
	}
	return int64(ans)
}