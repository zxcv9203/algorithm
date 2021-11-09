import sys
input = sys.stdin.readline

n = int(input())
solution = [int(x) for x in input().split()]
solution.sort()
low = 2e9 + 1
ans = [solution[0], solution[n - 1]]
for i in range(n - 1):
    st = i + 1
    ed = n - 1
    while st <= ed:
        mid = (st + ed) // 2
        tmp = solution[i] + solution[mid]
        if abs(tmp) < low :
            low = abs(tmp)
            ans[0], ans[1] = solution[i], solution[mid]
        if tmp < 0:
            st = mid + 1
        else:
            ed = mid - 1
     
print(ans[0], ans[1])