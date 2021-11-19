# n과 m(3)

import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()

dfs()
