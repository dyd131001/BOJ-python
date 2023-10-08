'''
import sys
input = sys.stdin.readline
from collections import deque

n , m = map(int,input().split())
know = set(list(map(int,input().split()))[1:])
party = [list(map(int,input().split()))[1:] for _ in range(m)]

G = [ [] for _ in range(n+1)]
visit = [ False for _ in range(n+1)]

for p in party:
    for pp in p:
        G[pp] += list(set(p)-{pp})

def bfs():
    L = deque(know)
    for i in know:
        visit[i] = True
    while L:
        nn = L.popleft()
        for nnn in G[nn]:
            if not visit[nnn]:
                visit[nnn] = True
                L.append(nnn)

bfs()

count = 0
for p in party:
    check = 0
    for pp in p:
        if  visit[pp]:
            check =1
            break
    if check == 0:
        count+=1
print(count)
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n , m = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [1 for _ in range(n+1)]

def fp(x):
    if parent[x] == x:
        return x
    parent[x] = fp(parent[x])
    return parent[x]

def ui(i,j):
    x = fp(i)
    y = fp(j)
    if x != y:
        if rank[x] == rank[y]:
            parent[x] = y
            rank[y] +=1
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y

know = list(map(int,input().split()))[1:]
party = [list(map(int,input().split()))[1:] for _ in range(m)]

for i in know[1:]:
    ui(know[0],i)

for p in party:
    for pp in p[1:]:
        ui(p[0],pp)

count = 0
for p in party:
    check = 0
    for pp in p:
        if know:
            if fp(pp) == fp(know[0]):
                check =1
                break
    if check == 0:
        count+=1

print(count)
