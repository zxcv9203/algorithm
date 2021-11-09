import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    ans = 1e9 + 1
    k, n = [int(x) for x in input().split()]
    students = [[], [], [], []]
    std = [[], []]
    for j in range(4):
        students[j] = [int(x) for x in input().split()]
    std[0] = [x + y for x in students[0] for y in students[1]]
    std[1] = [x + y  for x in students[2] for y in students[3]]
    std[0].sort()
    std[1].sort()
    length = n * n
    flag = False
    for i in range(length):
        st = 0
        ed = length - 1
        while st <= ed:
            mid = (st + ed) // 2
            tmp = std[0][i] + std[1][mid]
            if tmp == k:
                ans = tmp
                flag = True
                break
            elif tmp < k :
                st = mid + 1
            else :
                ed = mid - 1
            if abs(tmp - k) == abs(ans - k):
                ans = min(ans, tmp)
            elif abs(tmp - k) < abs(ans - k):
                ans = tmp
        if flag == True:
            break
    print(ans)
