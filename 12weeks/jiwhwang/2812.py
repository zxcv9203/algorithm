import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = list(input())
stack = []
delnum = K

for i in range(N):
    while delnum and stack:
        if (stack[-1] < num[i]):
            # print("stack[-1] = ", stack[-1], " num[i] = ",num[i], sep='')
            stack.pop()
            delnum -= 1
        else:
            break
    stack.append(num[i])
print("".join(stack[:N-K]))
