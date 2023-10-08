from collections import deque


def bfs(s, t):
    L.append([s, 0])
    while L:
        t1 = L.popleft()
        nx = 0
        for i in range(1, 4):
            if i == 1:
                nx = t1[0]*2
            elif i == 2:
                nx = t1[0]+1
            else:
                nx = t1[0]-1

            if nx <= k+1 and nx > 0:
                if visit[nx] == False:
                    visit[nx] = True
                    L.append([nx, t1[1]+1])
                if nx == t:
                    return t1[1]+1


n, k = map(int, input().split())
if k <= n:
    print(n-k)
else:
    visit = [False]*(k+2)
    L = deque()
    print(bfs(n, k))
