import sys

row, col = list(map(int, sys.stdin.readline().split()))

gameboard = [[0 for c in range(col)] for r in range(row)]
visit = [[False for c in range(col)] for r in range(row)]

for r in range(row):
    line = list(sys.stdin.readline()) 
    for c in range(col):
        gameboard[r][c] = line[c]

connect_x = [-1, 1, 0, 0]
connect_y = [0, 0, -1, 1]
find = False

def find_cycle(r, c, start_r, start_c, color, cnt):
    global find

    
    for i in range(4):
        nr = r + connect_x[i]
        nc = c + connect_y[i]
        
        if find == True:
            return True
        if nr < 0 or nc < 0 or nr >= row or nc >= col:
            continue
        if cnt >= 4 and start_r == nr and start_c == nc:
            find = True
            return True
        if color == gameboard[nr][nc] and visit[nr][nc] == False:
            visit[nr][nc] = True
            find_cycle(nr, nc, start_r, start_c, color, cnt+1)
            visit[nr][nc] = False


for r in range(row):
    for c in range(col):
        start_r = r
        start_c = c
        visit[start_r][start_c] = True
        find = find_cycle(r, c, start_r, start_c, gameboard[start_r][start_c],1)
if find:
    print('Yes')
else:
    print('No')
