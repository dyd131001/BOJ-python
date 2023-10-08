import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(row)]
visit = [[0 for _ in range(col)] for _ in range(row)]
T = deque()
d = [(-1, 0),(1,0),(0,-1),(0,1)]
day = 0
zero = 0

def bfs():
    maxd = 0
    while T:
        cday ,i, j = T.popleft()
        for dy, dx in d:
            ny = i + dy
            nx = j + dx
            if 0 <= ny <= row-1 and 0 <= nx <= col-1:
                if M[ny][nx] == 0 and visit[ny][nx] == 0:
                    M[ny][nx] = 1
                    visit[ny][nx] = 1
                    T.append((cday+1,ny,nx))
                    maxd = max(cday+1,maxd)
    return maxd

for i in range(row):
    for j in range(col):
        if M[i][j] == 1:
            T.append((0,i,j))
            visit[i][j] =1

check = 0

day = bfs()
for mM in M:
    if 0 in mM:
        print(-1)
        check = 1
        break
if check == 0:
    print(day)






