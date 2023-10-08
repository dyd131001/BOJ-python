import sys
input = sys.stdin.readline
import copy


n, m , y, x, c_count = map(int, input().split())

M = [list(map(int,input().split())) for _ in range(n)]
commend = list(map(int,input().split()))
dice = [0 for _ in range(6)]
dice_copy = [0 for _ in range(6)]

d = [[0,1], [0,-1], [-1,0],[1,0]] # 동서북남

def move(c):
    global dice
    if c == 1:
        dice_copy[0] = dice[3]
        dice_copy[2] = dice[0]
        dice_copy[3] = dice[5]
        dice_copy[5] = dice[2]
    elif c == 2:
        dice_copy[0] = dice[2]
        dice_copy[2] = dice[5]
        dice_copy[3] = dice[0]
        dice_copy[5] = dice[3]
    elif c == 3:
        dice_copy[0] = dice[4]
        dice_copy[1] = dice[0]
        dice_copy[4] = dice[5]
        dice_copy[5] = dice[1]
    elif c == 4:
        dice_copy[0] = dice[1]
        dice_copy[1] = dice[5]
        dice_copy[4] = dice[0]
        dice_copy[5] = dice[4]
    dice = copy.deepcopy(dice_copy)

for i in range(c_count):
    ny = y + d[commend[i]-1][0]
    nx = x + d[commend[i]-1][1]
    if 0 <= ny <= n-1 and 0 <= nx <= m-1:
        move(commend[i])
        if M[ny][nx] == 0:
            M[ny][nx] = dice[5]
        else:
            dice[5] = M[ny][nx]
            M[ny][nx] = 0
        print(dice[0])
        x = nx
        y = ny
    else:
        continue
