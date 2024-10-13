n = int(input())

board = [list(map(int,input().split(" "))) for _ in range(n)]

direction = ['U','D','L','R']

u = []

def export(r,direction,M):
    global u
    if direction == 'L':
        for i in range(n):
            if M[r][i] != 0:
                u.append(M[r][i])
                M[r][i] = 0
    elif direction == 'R':
        for i in range(n-1,-1,-1):
            if M[r][i] != 0:
                u.append(M[r][i])
                M[r][i] = 0
    elif direction == 'U':
        for i in range(n):
            if M[i][r] != 0:
                u.append(M[i][r])
                M[i][r] = 0
    elif direction == 'D':
        for i in range(n-1,-1,-1):
            if M[i][r] != 0:
                u.append(M[i][r])
                M[i][r] = 0

def union():
    if len(u) < 2:
        return
    s_index = 0
    e_index = 1
    count = len(u)-1
    while True:
        if count <= 0:
            break
        if u[s_index] == u[e_index]:
            u.pop(s_index)
            u[s_index] = u[s_index]*2
            count += -1
        s_index += 1
        e_index += 1
        count += -1

def send(r,direction,M):
    global u
    if direction == 'L':
        l = len(u)
        for i in range(l):
            v = u.pop(0)
            M[r][i] = v
    elif direction == 'R':
        l = len(u)
        for i in range(l):
            v = u.pop(0)
            M[r][-(i+1)] = v
    elif direction == 'U':
        l = len(u)
        for i in range(l):
            v = u.pop(0)
            M[i][r] = v
    elif direction == 'D':
        l = len(u)
        for i in range(l):
            v = u.pop(0)
            M[-(i+1)][r] = v

def move(direction, M):
    for i in range(n):
        export(i,direction,M)
        union()
        send(i,direction,M)

def findMax(M):
    return max(map(max,M))

result = 0
def simulate(level):
    global result
    global board
    if level == 5:
        maxValue = findMax(board)
        if maxValue > result:
            result = maxValue
        return

    m = [ b[:] for b in board]
    for d in direction:
        move(d,board)
        simulate(level+1)
        board = [ mm[:] for mm in m]

simulate(0)
print(result)
