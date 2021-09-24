import sys
input = sys.stdin.readline
n = int(input())
tree = list(map(int,input().split()))
ans = 2
cnt = 0
tree.sort(reverse=True)
for i in tree :
	ans = max(ans, i + cnt + 2)
	cnt += 1
print(ans)