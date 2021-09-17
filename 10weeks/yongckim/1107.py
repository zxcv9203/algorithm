import sys
input = sys.stdin.readline
n = int(input())
t = int(input())
cnt = abs(100 - n)
button = [True for i in range(10)]
tmp = list(map(int, input().split()))
for i in tmp :
	button[i] = False
for i in range(1000001) :
	flag = True
	target = str(i)
	for num in target :
		if button[int(num)] == False :
			flag = False
			break
	if flag == True :
		cnt = min(cnt, len(target) + abs(i - n))
print(cnt)