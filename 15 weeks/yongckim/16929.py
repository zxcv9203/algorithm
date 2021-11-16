import sys
import itertools
input = sys.stdin.readline

CONST_M = 50

ox = 0
oy = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
aaa = "No"

visit = []
[visit.append([]) for x in range(CONST_M)]
[visit[x].append(False) for x in range(CONST_M) for y in range(CONST_M)]

def dfs(x, y, cnt):
	visit[x][y] = True
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if safe(nx, ny):
			if cnt >= 4 and visit[nx][ny] == True and ox == nx and oy == ny:
				global aaa
				aaa = "Yes"
				return
			if visit[nx][ny] == False and dots[x][y] == dots[nx][ny]:
				dfs(nx, ny, cnt + 1)

n, m = [int(x) for x in input().split()]
dots = []
for x in range(n):
	dots.append(input().rstrip())

def safe(x, y):
	return (x >= 0 and x < n and y >= 0 and y < m)



for x in range(n):
	for y in range(m):
		for k in range(CONST_M):
			visit[k][:] = itertools.repeat(False, len(visit))
		ox = x
		oy = y
		dfs(x, y, 1)
		if aaa == "Yes":
			break

print(aaa)
