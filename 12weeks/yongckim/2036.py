import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for i in range(n)]
ans = 0
rever = []
nums.sort()
for i, value in enumerate(nums) :
    if value > 0 :
        rever = nums[i:]
        nums = nums[:i]
        break
rever.sort(reverse=True)
n_len = len(nums)
r_len = len(rever)
for i in range(0, r_len, 2) :
	if i + 1 >= r_len :
		ans += rever[i]
		break
	if rever[i] == 1 or rever[i + 1] == 1:
		ans += rever[i] + rever[i + 1]
	else :
		ans += rever[i] * rever[i + 1]
for i in range(0, n_len, 2) :
    if i + 1 >= n_len :
        ans += nums[i]
        break
    ans += nums[i] * nums[i + 1]
print(ans)