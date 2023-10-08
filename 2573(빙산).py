from collections import deque

n, m = map(int, input().split())

d3 = deque()
d4 = deque()
M = []
for i in range(n):
    M.append(list(map(int, input().split())))
    for j in range(m):
        if M[i][j] >= 1:
            d3.append([j, i])

VM = [[False for _ in range(m)]for _ in range(n)]
SM = [[0 for _ in range(m)]for _ in range(n)]

dl = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs1(x, y):  # 바다 수세기
    sc = 0
    if M[y][x] > 0:
        for dll in dl:
            nx = x + dll[1]
            ny = y + dll[0]
            if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                if M[ny][nx] <= 0:
                    sc += 1
            SM[y][x] = sc


def bfs3(x, y):
    if(M[y][x] - (SM[y][x])) <= 0:
        M[y][x] = 0
    else:
        M[y][x] = M[y][x] - (SM[y][x])
        d3.append([x, y])


def bfs2(x, y):
    VM[y][x] = True
    d4.append([x, y])
    while(d4):
        l = d4.popleft()
        for dll in dl:
            nx = l[0] + dll[1]
            ny = l[1] + dll[0]
            if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                if M[ny][nx] > 0 and VM[ny][nx] == False:
                    d4.append([nx, ny])
                    VM[ny][nx] = True


cn = 0

count = 0

si = 1
while True:
    count = 0

    for l in d3:
        if M[l[1]][l[0]] > 0:
            bfs1(l[0], l[1])

    for i in range(len(d3)):
        l = d3.popleft()
        bfs3(l[0], l[1])

    for l in d3:
        if (M[l[1]][l[0]]) > 0 and VM[l[1]][l[0]] == False:
            count += 1
            if count == 1:
                bfs2(l[0], l[1])
            elif count >= 2:
                break

    if count >= 2:
        print(si)
        break
    if count == 0:
        print(count)
        break
    si += 1

    for l in d3:
        if VM[l[1]][l[0]] == True:
            VM[l[1]][l[0]] = False
