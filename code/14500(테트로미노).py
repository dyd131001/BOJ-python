import sys
input = sys.stdin.readline

row , col = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

d = [[0,1],[1,0],[-1,0],[0,-1]]

maxValue = 0
M_m = max(map(max,M))

def dfs(i, j, dsum, cnt):
    global maxValue
    if maxValue >= dsum + M_m*(4-cnt):
        return
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    for z in range(4):
        ny = i+d[z][0]
        nx = j+d[z][1]
        if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = True
                dfs(i, j, dsum + M[ny][nx], cnt+1)
                visited[ny][nx] = False
            visited[ny][nx] = True
            dfs(ny, nx, dsum + M[ny][nx], cnt+1)
            visited[ny][nx] = False

for i in range(row):
    for j in range(col):
        visited[i][j] = True
        dfs(i, j, M[i][j], 1)
        visited[i][j] = False

print(maxValue)


''' 최적화
import sys
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(r,c,idx,total):
    global answer
    if answer >= total + max_val * (3-idx):
        return
    if idx == 3:
        answer = max(answer,total)
        return
    else:
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <=nr < N and 0<=nc <M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r,c,idx+1,total+arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr,nc,idx+1,total+arr[nr][nc])
                visit[nr][nc] = 0
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [([0]*M) for _ in range(N)]
answer = 0
max_val = max(map(max,arr))
for r in range(N):
    for c in range(M):
        visit[r][c] =1
        dfs(r,c,0,arr[r][c])
        visit[r][c] = 0
print(answer)
'''