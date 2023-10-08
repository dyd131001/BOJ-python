
n , m = map(int, input().split())
r,c,d = map(int, input().split())


dl = [[-1,0],[0,1],[1,0],[0,-1]]
M = [list(map(int, input().split())) for _ in range(n)]
VM = [[False for _ in range(m)]for _ in range(n)]
count = 0

def turn(x):
    if x == 0:
        return 2
    if x == 1:
        return 3
    if x == 2:
        return 0
    if x == 3:
        return 1

def turn2(x):
    if x-1 == -1:
        return 3
    return x-1

def bfs(x, y, d):
    global count
    while True:
        c = 0
        if M[y][x] == 0 and VM[y][x] == False:
            count+=1
            VM[y][x] =True

        cd = turn2(d)
        while True:
            nx = x + dl[cd][1]
            ny = y + dl[cd][0]
            if 0 <= ny <= n and 0 <= nx <= m and M[ny][nx] == 0 and VM[ny][nx] == False:
                x = nx
                y = ny
                d = cd
                c = 1
                break
            if cd == d :
                break
            cd = turn2(cd)

        if c == 0:
            cd = turn(d)
            lx = x + dl[cd][1]
            ly = y + dl[cd][0]
            if 0 <= ly <= n and 0 <= lx <= m and M[ly][lx] == 0:
                x = lx
                y = ly
            else:
                break

bfs(c,r,d)
print(count)