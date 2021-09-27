# 이장님 초대 9237

import sys

N = int(input())
day = list(map(int,input().split()))
# day = list(map(int, sys.stdin.readline().spilt())) --> 이거 왜 안됨 ???

day.sort(reverse=True)

max_day = 0

for i in range(0, N):
	if max_day < i+1+day[i]:
		max_day = i+1+day[i]
print(max_day+1)
