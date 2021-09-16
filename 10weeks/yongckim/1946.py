import sys
input = sys.stdin.readline
t = int(input())
for i in range(t) :
	n = int(input())
	human = [list(map(int,input().split())) for i in range(n)]
	human.sort()
	cnt = 1
	rank = human[0][1]
	for i in range(1, n):
		if rank > human[i][1]:
			cnt += 1
			rank = human[i][1]
	print(cnt)
	