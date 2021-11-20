import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
r, c, n = [int(x) for x in input().split()]
bomber = [list(input().rstrip()) for x in range(r)]
dq = deque()
def safe(x, y) :
	return x >= 0 and x < r and y >= 0 and y < c

def bomSet():
	for x in range(r):
		for y in range(c):
			if bomber[x][y] == 'O':
				dq.append((x, y))
			else :
				bomber[x][y] = 'O'

def bomPrint():
	for x in range(r):
		for y in range(c):
			print(bomber[x][y], end="")
		print()

def boom():
	while dq:
		x, y = dq.popleft()
		bomber[x][y] = '.'
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if safe(nx, ny) == True and bomber[nx][ny] == 'O':
				bomber[nx][ny] = '.'
i = 1
while i <= n:
	if i % 2 == 0:
		bomSet()
	else :
		boom()
	i += 1
bomPrint()