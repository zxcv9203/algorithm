# 2036  score of the sequence
import sys
input = sys.stdin.readline

n = int(input())

neg = []
pos = []
for i in range(n):
	num = int(input())
	if (num > 0):
		pos.append(num)
	else:
		neg.append(num)

score = 0

pos.sort(reverse=True)
neg.sort() # 오름차순으로 정렬해야 됨 음수는

for i in range(0, len(pos), 2):
	if i == len(pos)-1:
		score += pos[i]
	elif pos[i] == 1 or pos[i+1] == 1:
		score += pos[i] + pos[i+1]
	else:
		score += pos[i] * pos[i+1]

for i in range(0, len(neg), 2):
	if i == len(neg)-1:
		score += neg[i]
	else:
		score += neg[i] * neg[i+1]

print(score)
