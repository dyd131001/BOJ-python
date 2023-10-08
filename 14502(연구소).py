import sys
input = sys.stdin.readline
from collections import deque

row , col = map(int, input().split())
M = [list(map(int,input().split())) for _ in range(row)]
virus = []

d = ((1,0),(-1,0),(0,1),(0,-1))
result = 0
maxV = 0
zeroc  = 0
for i in range(row):
            for j in range(col):
                if M[i][j] == 0:
                    zeroc+=1
                if M[i][j] == 2:
                    virus.append((i,j))

def bfs():
    count = zeroc-3 # 바이러스 개수 - 3
    M_copy = [ [0] * col for _ in range(row)]
    two = deque(virus)
    while two:
        L = two.popleft()
        for dl in d:
            ny = L[0] + dl[0]
            nx = L[1] + dl[1]
            if 0 <= ny <= row-1 and 0 <= nx <= col-1:
                if M[ny][nx] == 0 and M_copy[ny][nx] == 0:
                    M_copy[ny][nx] =2
                    two.append((ny,nx))
                    count -=1
    return count


def wall(cnt):
    global maxV
    if cnt == 3:
        result = bfs()
        maxV = max(result,maxV)
    else:
        for i in range(row):
            for j in range(col):
                if M[i][j] == 0:
                    M[i][j] = 1
                    wall(cnt+1)
                    M[i][j] = 0
wall(0)
print(maxV)


''' 속도개선을 위해 deepcopy를 사용하지 않고 빈칸을 탐색으로 새는게 아니라 빼서 샌다.
속도를 위해 튜플을 쓰고 deque로 가져온다. 이러면 deepcopy 느낌이 됨
import sys
input = sys.stdin.readline

from collections import deque

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            empty.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))

l = len(empty)


def dfs(n,s, lst):
    global ans
    if n==3:
        for i in lst:
            arr[empty[i][0]][empty[i][1]]=1
        cnt = bfs()
        ans = max(ans, cnt)
        for i in lst:
            arr[empty[i][0]][empty[i][1]]=0
        return


    for i in range(s,l):
        dfs(n+1, i+1, lst+[i])


def bfs():
    q = deque(virus)
    v = [[0]*M for _ in range(N)]
    cnt = l-3
    for ci,cj in virus:
        v[ci][cj]=1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and arr[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj))
                cnt -=1
    return cnt

ans = 0
dfs(0,0,[])
print(ans)

'''
