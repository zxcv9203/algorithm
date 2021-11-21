import sys
import time
input = sys.stdin.readline
usleep = lambda x: time.sleep(x/1000000.0)

CONST_M = 10
# 루빅의 사각형 예제
# 1 2 15 4
# 7 8 3 6
# 9 10 5 12
# 13 14 11 16
# 다음상황에서 2 3 3 이라고 할 경우
# 세로의 3번째 열인 15 3 5 11을 3번 돌리는 것입니다.
# 이렇게 3번을 돌리면 다음과 같은 형태가 될 것입니다.
# 1 2 3 4
# 7 8 5 6
# 9 10 11 12
# 13 14 15 16
# 위의 상황에서 가로줄의 2번째 값을 2번 돌리면 다음과 같이 정답이 나옵니다.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# 값을 입력받음
lubic = [list(map(int,input().split())) for _ in range(4)]

# 원하는 형태를 저장한 리스트
ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# 원하는 형태로 되기위해 몇번 움직여야 하는지
ans_cnt = 8

# 원하는 형태로 만들기 위해 돌린 방법
# {가로, 세로(1, 2)} {몇번째인지} {돌린횟수} 와 같은 형태
rotation = []
[rotation.append([]) for x in range(CONST_M)]
[rotation[x].append(0) for x in range(CONST_M) for y in range(3)]
tmp_rotation = []
[tmp_rotation.append([]) for x in range(CONST_M)]
[tmp_rotation[x].append(0) for x in range(CONST_M) for y in range(3)]
# 사각형 안에 정답에 맞지 않는 원소의 개수를 카운트하는 함수
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
	diff = lubic_check()
	if diff == 0:
		global ans_cnt
		ans_cnt = cnt
		for i in range(cnt):
			rotation[i][0] = tmp_rotation[i][0]
			rotation[i][1] = tmp_rotation[i][1]
			rotation[i][2] = tmp_rotation[i][2]
		return
	# 답과 다른 형태의 값이 나올 경우 돌려야할 횟수를 예측
	change = diff / 4
	# 만약 정확히 떨어지는 상황이 아니라면 돌려야할 횟수를
	# 하나 추가해 소수점을 올림 처리함
	if change % 4 != 0:
		change += 1
	# 현재 답보다 움직임에 예측되는 값이 크다면 더 이상 실행할 필요가 없음
	prediction = cnt + change
	if prediction >= ans_cnt:
		return
	for l in range(1, 3):
		for x in range(4):
			for r in range(1, 3):
				tmp_rotation[cnt][0] = l
				tmp_rotation[cnt][1] = x + 1
				tmp_rotation[cnt][2] = r
				rotate_lubic(l, x, r, True)
				#time.sleep(3)
				#for i in range(4):
				#	print(lubic[i])
				dfs(cnt + 1)
				rotate_lubic(l, x, r, False)
				#for i in range(4):
				#	print(lubic[i])
				#print()


	
	


dfs(0)
print(ans_cnt)
for i in range(ans_cnt):
	print(rotation[i][0], rotation[i][1], rotation[i][2])