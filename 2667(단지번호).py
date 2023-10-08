n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input())))

count = 0
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(x, y):
    L[y][x] = 0
    global count
    count += 1
    for l in d:
        nx = x + l[1]
        ny = y + l[0]
        if nx >= 0 and nx < n and ny < n and ny >= 0:
            if L[ny][nx] == 1:
                bfs(nx, ny)


count2 = []

for i in range(n):
    for j in range(n):
        if L[i][j] == 1:
            bfs(j, i)
            count2.append(count)
            count = 0

count2.sort()
a = len(count2)
print(a)
for i in range(a):
    print(count2[i])
