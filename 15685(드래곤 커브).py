import sys
input = sys.stdin.readline

n = int(input())
M = [[0 for _ in range(101)] for _ in range(101)]
c_direction = [(0,1),(-1,0),(0,-1),(1,0)]
r_direction = [(0,1),(1,0),(0,0),(1,1)]

def result(y,x):
    count = 0
    for nd in r_direction:
        ny = y + nd[0]
        nx = x + nd[1]
        if M[ny][nx] == 1:
            count+=1
    if count == 4 :
        return True
    return False

def turn(d):
    if d+1 == 4:
        return 0
    else:
        return d+1

def move(cnt, g, d):
    if cnt == g+1 :
        return
    elif cnt == 0:
        curr_d.append(d)
        move(cnt+1, g , d)
    else:
        curr_i = len(curr_d)
        for i in range(curr_i-1,-1,-1):
            curr_d.append(turn(curr_d[i]))
        move(cnt+1, g , d)



for _ in range(n):
    x, y , d ,g = map(int,input().split())
    M[y][x] = 1
    curr_d = []
    move(0,g,d)
    for cd in curr_d:
        ny = y + c_direction[cd][0]
        nx = x + c_direction[cd][1]
        M[ny][nx] = 1
        y = ny
        x = nx

countr = 0
for i in range(100):
    for j in range(100):
        if result(i,j):
            countr+=1
print(countr)

