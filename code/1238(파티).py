import sys
input = sys.stdin.readline
from heapq import heappop, heappush
INF = int(1e9)
n, m , t = map(int,input().split())
G = [[] for _ in range(n+1)]
Gr = [[] for _ in range(n+1)]


for i in range(m):
    s, f, v = map(int,input().split())
    G[s].append((f,v))
    Gr[f].append((s,v))

def dik(start,G):
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


dist = dik(t, G)
reversed_dist = dik(t, Gr)

sum_list = [x+y for x,y, in zip(dist,reversed_dist)]
print(max(sum_list[1:]))