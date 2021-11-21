import sys
input = sys.stdin.readline

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
lubic = [list(input().split()) for _ in range(4)]

# 원하는 형태를 저장한 리스트
ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# 원하는 형태로 되기위해 몇번 움직여야 하는지
ans_cnt = 0

# 원하는 형태로 만들기 위해 돌린 방법
# {가로, 세로(1, 2)} {몇번째인지} {돌린횟수} 와 같은 형태
rotate = []

# 사각형 안에 정답에 맞지 않는 원소의 개수를 카운트하는 함수
def lubic_check():
	cnt = 0
	for x in range(4):
		for y in range(4):
			if ans[x][y] != lubic[x][y]:
				cnt += 1
	return True
	
def dfs(cnt):
	diff = lubic_check()
	if diff == 0:
		global ans_cnt
		ans_cnt = cnt
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
	for k in range(1, 3):
		for i in range(4):
			for j in range(1, 3):
				rotate.append([])
	
	


dfs(0)
print(ans_cnt)
for i in range(ans_cnt):
	print(rotate[i][0], rotate[i][1], rotate[i][2])