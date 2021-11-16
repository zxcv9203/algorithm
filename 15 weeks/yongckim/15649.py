import sys
input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
ans = []
visit = []
[ans.append(0) for x in range(m)]
[visit.append(False) for x in range(1, n+2)]
def dfs(depth) :
	if depth == m:
		[print(x, end= " ") for x in ans]
		print()
		return
	for i in range(1, n+1):
		if (visit[i] == False):
			ans[depth] = i;
			visit[i] = True
			dfs(depth+1)
			visit[i] = False
dfs(0)
