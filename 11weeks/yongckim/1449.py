import sys
input = sys.stdin.readline
n, l = input().split()
n = int(n)
l = int(l)
pipe = list(map(int,input().split()))
ans = 0
tape = 0
pipe.sort()
for i in pipe :
	if tape < i :
		tape = i + l - 1
		ans += 1
print(ans)