'''
import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
L = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

for i in range(n+1):
    L[i].sort()

vi = [0 for _ in range(n+1)]


def d(v):
    vi[v] = 1
    for i in L[v]:
        if vi[i] == 0:
            print(i, end=' ')
            d(i)


print(v, end=' ')
d(v)
print()
deq = deque()
vi2 = [0 for _ in range(n+1)]


def b(v):
    deq.append(v)
    print(v, end=' ')
    vi2[v] = 1
    while deq:
        nl = deq.popleft()
        for a in L[nl]:
            if vi2[a] == 0:
                deq.append(a)
                print(a, end=' ')
                vi2[a] = 1


b(v)
print()
'''


''' 최적화한 남의 코드
아이디어:
- DFS
  stack 사용
  재귀함수+visited 배열(boolean)
- BFS
  큐 사용
  while loop 사용+visited 배열(boolean)
시간복잡도:
- O(V+E)

import sys
input = sys.stdin.readline

def dfs(point, visited, edge, dfs_list):
    visited[point] = True
    dfs_list.append(str(point))
    
    for v in edge[point]:
        if visited[v] == False:
            dfs(v, visited, edge, dfs_list)

def bfs(point, visited, edge, bfs_list):
    queue = [point]
    visited[point] = True
    
    while queue:
        visit_v = queue.pop(0)
        bfs_list.append(str(visit_v))
        
        for v in edge[visit_v]:
            if visited[v] == False:
                visited[v] = True
                queue.append(v)
    
    return bfs_list

n, m, start = map(int, input().split())

edge = [[] for _ in range(n+1)]
visitied = [False] * (n+1)
dfs_list = []

for k in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)

edge_sorted = []
for e in edge:
    edge_sorted.append(sorted(e))

dfs(start, visitied, edge_sorted, dfs_list)
dfs_result = " ".join(dfs_list)
print(dfs_result)

visitied = [False] * (n+1)
bfs_list = []
bfs_result = bfs(start, visitied, edge_sorted, bfs_list)
print(" ".join(bfs_result))

'''


import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int,input().split())
gragh = [[] for _ in range(n+1)]
DFS_visit = [False for _ in range(n+1)]
BFS_visit = [False for _ in range(n+1)]
queue = deque()
result = [[],[]]

for _ in range(m):
    s,f = map(int,input().split())
    gragh[s].append(f)
    gragh[f].append(s)

def DFS(v):
    DFS_visit[v] = True
    result[0].append(str(v))
    for i in sorted(gragh[v]):
        if DFS_visit[i] == False:
            DFS(i)

def BFS(v):
    queue.append(v)
    BFS_visit[v] = True
    while queue:
        s = queue.popleft()
        result[1].append(str(s))
        for i in sorted(gragh[s]):
            if BFS_visit[i] == False:
                queue.append(i)
                BFS_visit[i] = True

DFS(v)
BFS(v)
print(*result[0])
print(*result[1])
