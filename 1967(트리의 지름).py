import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
G = [[] for _ in range(n+1)]
leaf = set()
maxv = 0
maxi = 0
for _ in range(n-1):
    s, f , v = map(int,input().split())
    G[s].append((f,v))
    G[f].append((s,v))

for i in range(1,n+1):
    if len(G[i]) == 1:
        leaf.add(i)

def dfs(start,sumv):
    visit[start] = True
    if start in leaf:
        global maxv
        global maxi
        if maxv < sumv:
                maxv = sumv
                maxi = start
    else:
        for f, v in G[start]:
            if not visit[f]:
                dfs(f,sumv+v)

leaf.discard(1)
visit = [False]*(n+1)
dfs(1,0)
leaf.discard(maxi)
visit = [False]*(n+1)
dfs(maxi,0)

print(maxv)

''' 좋은 코드
# ???

import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n+1)]
max_dist = 0

for _ in range(n-1):
    node, child, weight = map(int,input().split())
    graph[node].append((child,weight))
    
def dfs(start, dist):
    global max_dist
    first, second= 0, 0
    for adj_node, weight in graph[start]:
        temp = dfs(adj_node, weight)
        
        if first <= second:
            first  = max(first , temp)
        else:
            second = max(second, temp)

    max_dist = max(max_dist, first + second)
    return max(first+dist , second+dist)

dfs(1, 0)
print(max_dist)'''


'''import sys
input = sys.stdin.readline
from heapq import heappush,heappop
n = int(input())
INF = int(10e9)
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, f , v = map(int,input().split())
    G[s].append((v,f))
    G[f].append((v,s))

def dik(start):
    d = [INF] * (n+1)
    H = []
    d[start] = 0
    heappush(H,(0,start))
    maxi = 0
    maxv = 0
    while H:
        value, v1= heappop(H)
        if d[v1] < value:
            continue
        for value2, v2 in G[v1]:
            nvalue = value2 + value
            if d[v2] > nvalue:
                d[v2] = nvalue
                if maxv < nvalue:
                    maxi = v2
                    maxv = nvalue
                heappush(H,(nvalue,v2))
    return (maxi,maxv)

mi,mv = dik(1)
mi,mv= dik(mi)
print(mv)'''


import sys
input = sys.stdin.readline
n = int(input())

G = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, f , v = map(int,input().split())
    G[s].append((v,f))
    G[f].append((v,s))

def dik(start):
    visit = [-1] * (n+1)
    visit[start] = 0
    H = []
    H.append(start)
    maxi = 0
    maxv = 0
    while H:
        v1= H.pop()
        for value, v2 in G[v1]:
            if visit[v2] == -1:
                visit[v2] = visit[v1]+value
                H.append(v2)
                if visit[v1]+value > maxv:
                    maxi = v2
                    maxv = visit[v1]+value
    return (maxi,maxv)

mi,mv = dik(1)
mi,mv= dik(mi)
print(mv)