import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
maxv = 0
maxn = 0
G = [[] for _ in range(n+1)]
for i in range(n):
    t = list(map(int,input().split()))[:-1]
    for j in range(1,len(t)-1,2):
        G[t[0]].append((t[j],t[j+1]))


def dfs(i,value):
    global maxv
    global maxn
    for nextnode, nvalue in G[i]:
        if not visit[nextnode]:
            visit[nextnode] = True
            dfs(nextnode, value+nvalue)
            if maxv < value+nvalue:
                maxv = value+nvalue
                maxn = nextnode


visit = [False for _ in range(n+1)]
visit[1] = True
dfs(1,0)
visit = [False for _ in range(n+1)]
visit[maxn] = True
dfs(maxn,0)
print(maxv)
