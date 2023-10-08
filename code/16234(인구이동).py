import sys
input = sys.stdin.readline

N , L , R = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(N) ]
d = [[-1,0],[0,-1],[1,0],[0,1]]
day = 0
def bfs(i, j):
    global count
    sumv = 0
    vcount = 0
    visit[i][j] = 1
    b = []
    g = []
    b.append((i,j))
    g.append((i,j))
    vcount+=1
    sumv+=M[i][j]
    while b:
        row , col = b.pop()
        for dd in d:
            ny = row + dd[0]
            nx = col + dd[1]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if visit[ny][nx] == 0:
                    if L <= abs(M[row][col]- M[ny][nx]) <=R:
                        visit[ny][nx] = 1
                        b.append((ny,nx))
                        g.append((ny,nx))
                        vcount+=1
                        sumv+=M[ny][nx]
                        count+=1
    if vcount > 1:
        for r ,c in g:
            M[r][c] = sumv//vcount

while True:
    visit = [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                bfs(i,j)

    if count == 0:
        break
    day+=1

print(day)

