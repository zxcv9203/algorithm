import sys
import queue
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
r, c, n = [int(x) for x in input().split()]
bomber = []
[bomber.append(input().rstrip()) for x in range(r)]
qx = queue.Queue()
qy = queue.Queue()

def bomLocation():
	for x in range(r):
		for y in range(c):
			if bomber[x][y] == 'O':
				qx.put(x)
				qy.put(y)

def bomPrint():
	for x in range(r):
		print(bomber[x])

bomLocation()
bomPrint()
while qx.empty() == False and qy.empty() == False:
	print(qx.get(), qy.get())