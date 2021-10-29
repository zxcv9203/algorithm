import sys
N = int(input())
K = int(input())

s = 0
e = K
answer = 0
while (s <= e):
    mid = (s+e) // 2 
    count = 0
    for i in range(1, N+1):
        count = count + min(N, mid//i)
    
    if count < K:
        s = mid+1
    else:
        answer = mid
        e = mid-1

print(answer)
