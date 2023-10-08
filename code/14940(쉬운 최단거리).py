import sys
input = sys.stdin.readline
from collections import deque

row , col = map(int,input().split())
d = [(-1,0),(1,0),(0,1),(0,-1)]
M = [list(map(int,input().split())) for _ in range(row)]
visit = [[0 for _ in range(col)] for _ in range(row)]

def bfs(i,j):
    D = deque()
    D.append((i,j))
    visit[i][j] = 1
    while D:
        y , x = D.popleft()
        for dy ,dx in d:
            ny = y +dy
            nx = x +dx
            if 0 <= nx <= col-1 and 0 <= ny <= row-1:
                if M[ny][nx] != 0 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[y][x]+1
                    D.append((ny,nx))

for r in range(row):
    for c in range(col):
        if M[r][c] == 2:
            bfs(r,c)
            break

for r in range(row):
    for c in range(col):
        if visit[r][c] !=0:
            print(str(visit[r][c]-1) + ' ',end='')
        else:
            if M[r][c] == 0:
                print(str(visit[r][c]) + ' ',end='')
            else:
                print(str(visit[r][c]-1) + ' ',end='')
    print()
