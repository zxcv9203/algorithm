import sys
input = sys.stdin.readline

n = int(input())
conn = list(map(int, input().split()))
city = list(map(int, input().split()))
mn = city[0]
ans = 0

for i in range(n - 1) :
	mn = min(mn, city[i])
	ans += mn * conn[i]
print(ans)