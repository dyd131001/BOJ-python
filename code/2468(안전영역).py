import sys
sys.setrecursionlimit(10**7)
n = int(input())
M = [[*map(int, input().split())] for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]  # false 맨땅

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
count = 0


def dfs(x, y, k):
    visit[y][x] = True
    for dl in d:
        ny = y + dl[0]
        nx = x + dl[1]
        if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1:
            if(visit[ny][nx] == False and M[ny][nx] > k):
                dfs(nx, ny, k)


max = 0
for k in range(1, 101):
    count = 0
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False and M[i][j] > k:
                dfs(j, i, k)
                count += 1
    if max < count:
        max = count
    if count == 0:
        break

if max == 0:
    print('1')
else:
    print(max)
