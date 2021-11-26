import sys
input = sys.stdin.readline

boggle = []
ans = [0, 0]
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 1 , -1, 0, 0, 1, -1]
score = [0, 0, 0, 1, 1, 2, 3, 5, 11]
visit = [[] for _ in range(4)]
for j in range(4) :
	visit[j] = [False for _ in range(4)]
w = int(input())
word = [input().rstrip() for x in range(w)]
input()
b = int(input())
word.sort()
useWord = [False for _ in range(w)]
ans_string = ""
def safe(x, y):
	return x >= 0 and x < 4 and y >= 0 and y < 4
def bst(string):
	st = 0
	ed = w - 1
	while st <= ed :
		mid = (st + ed) // 2
		if word[mid] == string:
			return mid
		elif word[mid] < string:
			st = mid + 1
		else:
			ed = mid - 1
	return -1

def dfs(x, y, tmp):
	string = "".join(tmp)
	if (len(string) >= 9) :
		return
	search = bst(string)
	if search != -1:
		global ans_string
		if len(string) > len(ans_string):
			ans_string = string
		elif len(string) == len(ans_string) and string < ans_string:
			ans_string = string
		if useWord[search] == False:
			useWord[search] = True;
			ans[1] += 1
			ans[0] += score[len(string)]
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		if safe(nx, ny) and visit[nx][ny] == False:
			visit[nx][ny] = True
			tmp.append(boggle[nx][ny])
			dfs(nx, ny, tmp)
			tmp.pop()
			visit[nx][ny] = False


for i in range(b):
	boggle = []
	for _ in range(4):
		boggle.append(input().rstrip())
	if (i < b - 1):
		input()
	ans[0] = 0
	ans_string = ""
	ans[1] = 0
	tmp = []
	for j in range(4) :
		visit[j] = [False for _ in range(4)]
	useWord = [False for _ in range(w)]
	for x in range(4):
		for y in range(4):
			tmp.append(boggle[x][y])
			visit[x][y] = True
			dfs(x, y, tmp)
			visit[x][y] = False
			tmp.pop()
	print(ans[0], ans_string, ans[1])
