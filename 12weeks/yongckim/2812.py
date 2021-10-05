import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = input()

stack = []
for i in range(n):
	while stack and k > 0:
		if stack[len(stack) - 1] < num[i]:
			stack.pop()
			k -= 1
		else:
			break
	stack.append(num[i])
 
for i in range(len(stack) - k) :
    print(stack[i], end="")
 