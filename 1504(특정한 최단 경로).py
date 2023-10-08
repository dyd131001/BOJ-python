import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, e = map(int,input().split())
INF = int(1e9)

G = [[] for _ in range(n+1)]
for _ in range(e):
    a, b ,c = map(int,input().split())
    G[a].append((b,c))
    G[b].append((a,c))

def dik(start):
    distance = [INF] * (n+1)
    V = []
    heappush(V,(start,0))
    distance[start] = 0
    while V:
        t,v = heappop(V)
        if distance[t] < v:
            continue

        for t2,v2 in G[t]:
            if distance[t2] > v+v2:
                distance[t2] = v+v2
                heappush(V,(t2,v+v2))
    return distance

v1 ,v2 = map(int,input().split())
d1 = dik(1)
dv1 = dik(v1)
dv2 = dik(v2)
r1 = d1[v1]+dv1[v2]+dv2[n]
r2 = d1[v2]+dv2[v1]+dv1[n]

r = min(r1,r2)
if r >= INF:
    print(-1)
else:
    print(r)