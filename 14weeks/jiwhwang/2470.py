import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()
min_s = 1e10

if N == 2:
    print(arr[0], arr[1])
    exit(0)

for i in range(N-1):
    start = i+1
    end = N-1

    while(start <= end):
        mid = (start + end) // 2
        s = arr[i] + arr[mid]

        if abs(s) < min_s:
            idx1, idx2, min_s = i, mid, abs(s)
           
        if s < 0:
            start = mid+1
        else:
            end = mid-1
print(arr[idx1], arr[idx2])
        


