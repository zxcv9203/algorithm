# n과 m(2)

import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

s = []

def backtracking():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    s.sort()
    for i in range(1, n+1):
        if i not in s and (len(s) == 0 or s[len(s)-1] < i):
            s.append(i)
            backtracking()
            s.pop()


backtracking()

