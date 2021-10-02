import sys

n = int(input())
chain = list(map(int, sys.stdin.readline().split()))
gori = 0

chain.sort()
for i, value in enumerate(chain):
    cnt = n - i - 1
    gori += value
    if gori >= cnt :
					print(cnt)
					break