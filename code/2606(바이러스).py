n = int(input())
m = int(input())
M = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    M[a].append(b)
    M[b].append(a)

count = 0


def dfs(num):
    global count
    count += 1
    visit[num] = True
    for i in M[num]:
        if visit[i] == False:
            dfs(i)


dfs(1)
print(count-1)
# for j in range(1, n+1):
#   if(visit[j] == False):
#      count += 1
#     dfs(j)

# print(count)
