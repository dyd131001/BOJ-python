from collections import deque

F, S, G, U, D = map(int, input().split())


visit = [False] * (F+1)
dx = [U, -D]
count = 0

d = deque()


def bfs(n, t):
    visit[n] = True
    d.append([n, 0])
    if n == t:
        return 0
    while d:
        x = d.popleft()
        for k in dx:
            nx = x[0] + k
            if nx >= 1 and nx <= F:
                if visit[nx] == False:
                    visit[nx] = True
                    d.append([nx, x[1]+1])
                if nx == t:
                    return x[1]+1
    return -1


count = bfs(S, G)
if count == -1:
    print("use the stairs")
else:
    print(count)
