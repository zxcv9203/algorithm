import sys
input = sys.stdin.readline
lubic = [list(input().split()) for _ in range(4)]
ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
cnt = 0

def lubic_check(tmp):
	for x in range(4):
		for y in range(4):
			if ans[x][y] != tmp[x][y]:
				return False
	return True
	
def dfs(tmp, move):
	if lubic_check(tmp) == True:
		print(cnt)
		print(move)


dfs(lubic, [])