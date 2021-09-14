n = int(input())

card = [list(map(int,input().split())) for i in range(n)]
score = 0
ans = 10
for i in range(n):
	for j in range(5):
		for k in range(j + 1, 5):
			for l in range(k + 1, 5):
				ret = (card[i][j] + card[i][k] + card[i][l]) % 10
				if score <= ret :
					score = ret
					ans = i + 1
print(ans)