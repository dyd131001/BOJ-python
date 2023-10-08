import sys
input = sys.stdin.readline

R, C , T = map(int,input().split())

M = [list(map(int,input().split())) for _ in range(R)]
location = []

for i in range(R):
    if M[i][0] == -1:
        location.append((i,0))

d = [(-1,0),(0,-1),(1,0),(0,1)]

def move(row,col):
    count = 0
    for dy, dx in d:
        ny = row + dy
        nx = col + dx
        if ny == location[0][0] and nx == 0:
            continue
        if ny == location[1][0] and nx == 0:
            continue
        if 0 <= ny <= R-1 and 0 <= nx <= C-1:
            count+=1
            MM[ny][nx] += M[row][col]//5
    MM[row][col] += M[row][col] - ((M[row][col]//5) * count)

def move2():
    for i in range(location[0][0]-1, 0,-1):
        ny = i + d[0][0]
        M[i][0] = M[ny][0]
    M[0] = M[0][1:] + [M[1][C-1]]
    for i in range(location[0][0]):
        ny = i + d[2][0]
        M[i][C-1] = M[ny][C-1]
    M[location[0][0]] = [-1,0] + M[location[0][0]][1:C-1]

    for i in range(location[1][0]+1, R-1):
        ny = i + d[2][0]
        M[i][0] = M[ny][0]
    M[R-1] = M[R-1][1:] + [M[R-1][C-1]]
    for i in range(R-1,location[1][0],-1):
        ny = i + d[0][0]
        M[i][C-1] = M[ny][C-1]
    M[location[1][0]] = [-1,0] + M[location[1][0]][1:C-1]


for z in range(T):
    MM = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] >= 5:
                move(i,j)
            else:
                MM[i][j] += M[i][j]
    M = MM
    move2()

print(sum(sum( M[i][j] for j in range(C)) for i in range(R)) + 2)


