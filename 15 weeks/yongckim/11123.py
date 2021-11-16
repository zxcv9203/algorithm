import sys
import itertools
sys.setrecursionlimit(10000)
input = sys.stdin.readline
CONST_M = 101
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visit = []
pasture = []
cnt = 0
[visit.append([]) for x in range(CONST_M)]
[visit[x].append(False) for x in range(CONST_M) for y in range(CONST_M)]
[pasture.append([]) for x in range(CONST_M)]
[pasture[x].append('.') for x in range(CONST_M) for y in range(CONST_M)]
def safe(x, y):
	return (x >= 0 and x < h and y >= 0 and y < w)
def dfs(x, y):
	if pasture[x][y] == '.':
		return 0
	visit[x][y] = True
	for i in range(4):
		nx = dx[i] + x
		ny = dy[i] + y
		if safe(nx, ny) :
			if visit[nx][ny] == False and pasture[nx][ny] == '#':
				visit[nx][ny] = True
				dfs(nx, ny)
	return 1
t = int(input())
for i in range(t):
	cnt = 0
	for x in range(CONST_M):
		visit[x][:] = itertools.repeat(False, len(visit))
	h, w = [int(x) for x in input().split()]
	for x in range(h):
		tmp = input()
		for y in range(w):
			pasture[x][y] = tmp[y]
	for x in range(h):
		for y in range(w):
			if visit[x][y] == False:
				cnt += dfs(x, y)
	print(cnt)
