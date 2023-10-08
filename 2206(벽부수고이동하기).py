import sys
input = sys.stdin.readline
from collections import deque

ty, tx = map(int,input().split())

M = [list(map(int,input().rstrip())) for _ in range(ty)]

d = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(i,j,k):
    distance = [[[0,0] for _ in range(tx)] for _ in range(ty)]
    distance[i][j][k] = 1
    queue = deque()
    queue.append((i,j,k))
    while queue:
        y,x,z = queue.popleft()
        if y == ty-1 and x == tx-1:
            break
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0<=ny<ty and 0<=nx<tx:
                if not distance[ny][nx][z]:
                    if M[ny][nx] == 0:
                        distance[ny][nx][z] = distance[y][x][z]+1
                        queue.append((ny,nx,z))
                    else:
                        if z == 0:
                            distance[ny][nx][z+1] = distance[y][x][z]+1
                            queue.append((ny,nx,z+1))
    return distance[ty-1][tx-1][z]


r = dfs(0,0,0)
if r==0:
    print(-1)
else:
    print(r)