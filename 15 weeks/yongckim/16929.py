import sys
input = sys.stdin.readline

CONST_M = 50

ox = 0
oy = 0
ok = "No"
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visit = []
[visit.append([]) for x in range(CONST_M)]
[visit[x].append(False) for x in range(CONST_M) for y in range(CONST_M)]

n, m = [int(x) for x in input().split()]
dots = []
for x in range(n):
	dots.append(input().rstrip())

def safe(x, y):
	return (x >= 0 and x < n and y >= 0 and y < m)

def dfs(x, y, cnt):
	visit[x][y] = True
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if safe(nx, ny):
			if ox == nx and oy == ny:
				ok = "Yes"
				return
			if visit[nx][ny] == False and dots[x][y] == dots[nx][ny]:
				dfs(nx, ny, cnt + 1)

for x in range(n):
	for y in range(m):
		ox = x
		oy = y
		dfs(x, y, 0)
		if ok == "Yes":
			break
print(ok)
