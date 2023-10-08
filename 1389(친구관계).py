import sys
input = sys.stdin.readline
from collections import deque
n , m = map(int,input().split())
G = [[] for _ in range(5001)]
P = set()
for _ in range(m):
    i , j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)
    P.add(i)
    P.add(j)
r = []
minv = sys.maxsize
for i in P:
    visit = [ False for _ in range(5001)]
    v = deque()
    v.append((i,1))
    visit[i] = True
    sumc = 0
    while v:
        p, c = v.popleft()
        for friend in G[p]:
            if not visit[friend]:
                v.append((friend,c+1))
                visit[friend] = True
                sumc += c
    if sumc <= minv:
        minv = sumc
        r.append((i,sumc))

rr = []
for i , j in r:
    if j == minv:
        rr.append(i)

print(min( i for i in rr))

