import sys
sys.setrecursionlimit(10**6) # 이거 안하면 틀림

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visit,mapp, max_x, max_y):
    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 > nx or nx >= max_x or max_y <= ny or ny < 0:
            continue
        elif visit[nx][ny] == False and mapp[nx][ny] == 1:
            dfs(nx, ny, visit, mapp, max_x, max_y)
        

tc = int(sys.stdin.readline())

for t in range(tc):
    y, x = [int(i) for i in sys.stdin.readline().split()]
    mapp = [[0 for col in range(y)] for row in range(x)]
    visit = [[False for col in range(y)] for row in range(x)]
    for col in range(y):
        line = list(sys.stdin.readline())
        for row in range(x):
            if line[row] == '#':
                mapp[row][col] = 1
            else:
                mapp[row][col] = 0
    # check_mapp(mapp)
    count = 0
    for i in range(x):
        for j in range(y):
            if mapp[i][j] == 1 and visit[i][j] == False:
                dfs(i, j, visit, mapp, x, y)
                count+=1
    print(count)

    

