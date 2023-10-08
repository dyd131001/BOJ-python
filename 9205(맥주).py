from collections import deque


def bfs(x, y):
    c = 0
    d.append([x, y])
    while d:
        bl = d.popleft()
        if abs(tx - bl[0]) + abs(ty - bl[1]) <= 1000:
            c = 1
            print("happy")
            break
        for i in range(n):
            if abs(PL[i][0] - bl[0]) + abs(PL[i][1] - bl[1]) <= 1000 and vP[i+1] == False:
                vP[i+1] = True
                d.append([PL[i][0], PL[i][1]])
    if c == 0:
        print("sad")


t = int(input())

for _ in range(t):
    d = deque()
    n = int(input())
    hx, hy = map(int, input().split())
    vP = [False for _ in range(n+1)]
    PL = []
    for _ in range(n):
        px, py = map(int, input().split())
        PL.append([px, py])
    tx, ty = map(int, input().split())
    bfs(hx, hy)
