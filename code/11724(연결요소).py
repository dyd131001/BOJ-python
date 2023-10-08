import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)



n,m = map(int,input().split())
M = [ [] for _ in range(n+1)]
visit = [ False for _ in range(n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    M[i].append(j)
    M[j].append(i)

def dfs(i):
    visit[i] = True
    for j in M[i]:
        if not visit[j]:
            dfs(j)

count = 0
for i in range(1,n+1):
    if not visit[i]:
        count +=1
        dfs(i)

print(count)

