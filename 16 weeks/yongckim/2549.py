import sys
input = sys.stdin.readline

CONST_M = 8
lubic = [list(map(int,input().split())) for _ in range(4)]
ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
ans_cnt = 8
rotation = []
[rotation.append([]) for x in range(CONST_M)]
[rotation[x].append(0) for x in range(CONST_M) for y in range(3)]
tmp_rotation = []
[tmp_rotation.append([]) for x in range(CONST_M)]
[tmp_rotation[x].append(0) for x in range(CONST_M) for y in range(3)]

def lubic_check():
	cnt = 0
	for x in range(4):
		for y in range(4):
			if ans[x][y] != lubic[x][y]:
				cnt += 1
	return cnt

def rotate_lubic(line, idx, rotate, status):
	rotate_arr = [0, 0, 0, 0]
	if line == 1:
		if status == True:
			for i in range(4):
				rotate_arr[(i + rotate) % 4] = lubic[idx][i]
			for i in range(4):
				lubic[idx][i] = rotate_arr[i]
		else:
			rotate = 4 - rotate
			for i in range(4):
				rotate_arr[(i + rotate) % 4] = lubic[idx][i]
			for i in range(4):
				lubic[idx][i] = rotate_arr[i]
	else:
		if status == True:
			for i in range(4):
				rotate_arr[(i + rotate) % 4] = lubic[i][idx]
			for i in range(4):
				lubic[i][idx] = rotate_arr[i]
		else:
			rotate = 4 - rotate
			for i in range(4):
				rotate_arr[(i + rotate) % 4] = lubic[i][idx]
			for i in range(4):
				lubic[i][idx] = rotate_arr[i]
				

def dfs(cnt):
	global ans_cnt
	diff = lubic_check()
	if diff == 0 and cnt < ans_cnt:
		ans_cnt = cnt
		for i in range(cnt):
			rotation[i][0] = tmp_rotation[i][0]
			rotation[i][1] = tmp_rotation[i][1]
			rotation[i][2] = tmp_rotation[i][2]
		return
	change = diff // 4
	if change % 4 != 0:
		change += 1
	prediction = cnt + change
	if prediction > ans_cnt:
		return
	for l in range(1, 3):
		for x in range(4):
			for r in range(1, 4):
				tmp_rotation[cnt][0] = l
				tmp_rotation[cnt][1] = x + 1
				tmp_rotation[cnt][2] = r
				rotate_lubic(l, x, r, True)
				dfs(cnt + 1)
				rotate_lubic(l, x, r, False)

dfs(0)
print(ans_cnt)
for i in range(ans_cnt):
	print(rotation[i][0], rotation[i][1], rotation[i][2])