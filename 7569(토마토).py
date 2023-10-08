from collections import deque
m, n, h = map(int, input().split())
L = [[[*map(int, input().split())] for _ in range(n)] for _ in range(h)]

# 1 익 0 안익 -1없

dl = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

d = deque()


def bfs():
    while d:
        l = d.popleft()
        for dd in dl:
            nx = l[0] + dd[0]
            ny = l[1] + dd[1]
            nz = l[2] + dd[2]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and L[nz][ny][nx] == 0:
                d.append([nx, ny, nz])
                L[nz][ny][nx] = L[l[2]][l[1]][l[0]] + 1


max = 0
im = []

for k in range(h):
    for j in range(n):
        for i in range(m):
            if(L[k][j][i] == 1):
                d.append([i, j, k])
            if(L[k][j][i] == 0):
                im.append([i, j, k])
bfs()
c = 0

for lm in im:
    if L[lm[2]][lm[1]][lm[0]] == 0:
        print('-1')
        c = 1
        break
    else:
        if max < L[lm[2]][lm[1]][lm[0]]:
            max = L[lm[2]][lm[1]][lm[0]]

if c == 0:
    if max == 0 or max == 1:
        print(max)
    else:
        print(max-1)

## 참고
from collections import deque
from sys import stdin

input = stdin.readline


def main():
    width, depth, height = map(int, input().split())
    box = list()

    process = deque()

    for i in range(height):
        plate = list()
        for j in range(depth):
            row = list(map(int, input().split()))
            plate.append(row)
            for k, state in enumerate(row):
                if state == 1:
                    process.append((i, j, k))
        box.append(plate)

    if not process:
        print('-1')
        return

    days = 0
    next_process = deque()
    while process or next_process:
        if not process:
            process, next_process = next_process, deque()
            days += 1
        if not process:
            days -= 1
            break

        x, y, z = process.popleft()

        if x > 0 and box[x-1][y][z] == 0:
            box[x-1][y][z] = 1
            next_process.append((x-1, y, z))
        if x < height-1 and box[x+1][y][z] == 0:
            box[x+1][y][z] = 1
            next_process.append((x+1, y, z))
        if y > 0 and box[x][y-1][z] == 0:
            box[x][y-1][z] = 1
            next_process.append((x, y-1, z))
        if y < depth-1 and box[x][y+1][z] == 0:
            box[x][y+1][z] = 1
            next_process.append((x, y+1, z))
        if z > 0 and box[x][y][z-1] == 0:
            box[x][y][z-1] = 1
            next_process.append((x, y, z-1))
        if z < width-1 and box[x][y][z+1] == 0:
            box[x][y][z+1] = 1
            next_process.append((x, y, z+1))

    not_rippen = False
    for plate in box:
        for row in plate:
            if 0 in row:
                not_rippen = True
                break
        if not_rippen:
            break

    if not_rippen:
        print('-1')
    else:
        print(days)


if __name__ == '__main__':
    main()

