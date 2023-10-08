import sys
input = sys.stdin.readline
from collections import deque
import copy

# 빈칸 - 감시구역 = 사각지대

row , col = map(int,input().split())
M = [ list(map(int,input().split())) for _ in range(row)]
cctv_d = [[[0], [1] ,[2] ,[3]],
        [[0, 1], [2 , 3]],
        [[0, 2], [0 , 3],[1, 2],[1,3]],
        [[0,1,2], [0,1,3],[0,2,3],[1,2,3]],
        [[0,1,2,3]]]
zero = 0
cctv = []
cctv_c = 0
max_v = 0

for i in range(row):
    for j in range(col):
        if M[i][j] == 0:
            zero +=1
        if 1<= M[i][j] <=5:
            cctv.append((M[i][j],i,j))
            cctv_c +=1

def move(d,t,visit):
    # 왼쪽
    count = 0
    for a in d:
        if a == 0:
            for i in range(t[2]-1,-1,-1):
                if visit[t[1]][i] == 6:
                    break
                if visit[t[1]][i] == 0:
                    visit[t[1]][i] = 1
                    count +=1
        elif a == 1:
            for i in range(t[2]+1, col):
                if visit[t[1]][i] == 6:
                    break
                if visit[t[1]][i] == 0:
                    visit[t[1]][i] = 1
                    count +=1
        elif a == 2:
            for i in range(t[1]-1,-1,-1):
                if visit[i][t[2]] == 6:
                    break
                if visit[i][t[2]] == 0:
                    visit[i][t[2]] = 1
                    count +=1
        else:
            for i in range(t[1]+1, row):
                if visit[i][t[2]] == 6:
                    break
                if visit[i][t[2]] == 0:
                    visit[i][t[2]] = 1
                    count +=1
    return count

def dfs(cnt , value, arr):
    global max_v
    if cnt == cctv_c:
        max_v = max(value,max_v)
    else:
        for d2 in cctv_d[cctv[cnt][0]-1]:
            visit = copy.deepcopy(arr)
            c_value = move(d2,cctv[cnt],visit)
            dfs(cnt+1, value + c_value,visit)


dfs(0,0,M)
print(zero - max_v)

''' set을 이용하여 카메라의 각 모양을 집합으로 만들고 합집합한다. 0번 카메라가 1번유형이면 4부분을 cctv_list[0]에 넣어놓고 dfs로 다 더한다.
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
graph = []
# 1~5가 cctv, 0은 빈칸, 6은 벽
cctv_list = []
total = 0
answer = [-1]
d_dict = {
    1:[[0],[1],[2],[3]],
    2:[[0,1],[2,3]],
    3:[[0,2],[0,3],[1,2],[1,3]],
    4:[[0,1,2],[0,1,3],[2,3,0],[2,3,1]],
    5:[[0,1,2,3]]
}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def watch(now,d_list): # 색칠용
    cur_set = set([])
    x = now[0]
    y = now[1]
    for d in d_list:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0>nx or 0>ny or N<=nx or M<=ny:
                break
            elif graph[nx][ny]==6:
                break
            elif graph[nx][ny]==0:
                cur_set.add((nx,ny))
    return cur_set
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            total+=1 # 비춰야 할 사각지대 갯수  
        if 1<=graph[i][j]<=5:
            cctv_list.append([watch((i,j),d_list) for d_list in d_dict[graph[i][j]]])

def dfs(depth,watched_set): # 조합만들기 - 최종 watched_set을 점점 완성해가는것
    if depth==len(cctv_list):
        answer[0]=max(answer[0],len(watched_set))
        return
    for one_set in cctv_list[depth]:
        dfs(depth+1,watched_set|one_set)
dfs(0,set([]))
print(total-answer[0])

'''