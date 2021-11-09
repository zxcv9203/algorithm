import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
st = 0
ed = k
ans = 0
while st <= ed :
    total = 0
    mid = (st + ed) // 2
    for i in range(1, n+1):
        total += min(mid//i, n)
    if total < k:
        st = mid + 1
    else:
        ans, ed = mid, mid - 1
print(ans)