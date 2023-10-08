from collections import deque # BFS, DFS의 차이를 알 수 있다.

n, m = map(int, input().split())

M = [list(map(int, input())) for _ in range(n)]

x, y = 0, 0

Q = deque()


def b(x, y):
    dll = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    Q.append([x, y])
    while Q:
        L = Q.popleft()
        x = L[0]
        y = L[1]
        if x == m-1 and y == n-1:
            break
        for dl in dll:
            nx = x + dl[0]
            ny = y + dl[1]
            if nx >= 0 and nx <= m-1 and ny >= 0 and ny <= n-1:
                if M[ny][nx] == 1:
                    Q.append([nx, ny])
                    M[ny][nx] = M[y][x] + 1


b(0, 0)
print(M[n-1][m-1])


def d(x, y, count):
    global min

    if x < 0 or x > m-1 or y < 0 or y > n-1 or min == m+n-2:
        return
    else:
        if y+1 <= n-1:
            if M[y+1][x] == 1:
                M[y][x] = 0
                d(x, y+1, count+1)
                M[y][x] = 1
        if x+1 <= m-1:
            if M[y][x+1] == 1:
                M[y][x] = 0
                d(x+1, y, count+1)
                M[y][x] = 1
        if y-1 >= 0:
            if M[y-1][x] == 1:
                M[y][x] = 0
                d(x, y-1, count+1)
                M[y][x] = 1
        if x-1 >= 0:
            if M[y][x-1] == 1:
                M[y][x] = 0
                d(x-1, y, count+1)
                M[y][x] = 1

    if x == m-1 and y == n-1:
        if min == 0 or min > count:
            min = count
