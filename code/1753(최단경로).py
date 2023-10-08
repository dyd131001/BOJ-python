import sys
input = sys.stdin.readline
from heapq import heappop,heappush

v,e = map(int, input().split())
INF = sys.maxsize
start = int(input())
G = [[] for _ in range(v+1)]

def dik(start):
    d = [INF] * (v+1)
    H = []
    heappush(H,(0,start))
    d[start] = 0
    while H:
        value,v1 = heappop(H)
        if d[v1] < value:
            continue
        for value2,v2 in G[v1]:
            nv = value+value2
            if d[v2] > nv:
                d[v2] = nv
                heappush(H,(nv,v2))
    return d

for _ in range(e):
    s,f,val = map(int, input().split())
    G[s].append((val,f))

d = dik(start)

for i in range(1,v+1):
    print("INF" if d[i] >= INF else d[i] )