import sys
from heapq import heappush, heappop
input = sys.stdin.readline


n = int(input())
m = int(input())
INT = int(10e9)
G = [[] for _ in range(n+1)]
for i in range(m):
    s, f, value = map(int,input().split())
    G[s].append((value,f))

def dik(start,finish):
    d = [INT] *(n+1)
    H  = []
    d[start] = 0
    H.append((0,start))
    while H:
        cost, node = heappop(H)
        if d[node] < cost:
            continue
        for cost2, node2 in G[node]:
            nextcost = cost+cost2
            if nextcost < d[node2]:
                d[node2] = nextcost
                heappush(H,(nextcost,node2))
    return d[finish]

s,f = map(int, input().split())
print(dik(s,f))