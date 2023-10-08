import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
Map = [[0 for _ in range(n)] for _ in range(n)]
apple = int(input())
for _ in range(apple):
    y,x = map(int,input().split())
    Map[y-1][x-1] = 2
move_count = int(input())
move_location = [list(map(str,input().split())) for _ in range(move_count)]

d = [[0, 1], [-1, 0], [0, -1], [1,0]]
count = 0
size = 1
Map[0][0] = 1
state = 3
snake = [[0,0]]


def turn(inpo):
    global state
    if inpo == 'D':
        state +=1
        if state == 4:
            state = 0
    elif inpo == 'L':
        state -=1
        if state == -1:
            state = 3
while True:
    if move_location:
        if int(move_location[0][0]) == count:
            turn(move_location[0][1])
            move_location.pop(0)
    count +=1
    nexty = snake[-1][1] + d[state][1]
    nextx = snake[-1][0] + d[state][0]
    size +=1
    if  0 <= nextx  <= n-1 and 0 <= nexty  <= n-1:
        if Map[nexty][nextx] == 0:
            snake.append([nextx,nexty])
            x , y = snake.pop(0)
            size -=1
            Map[nexty][nextx] = 1
            Map[y][x] = 0
        elif Map[nexty][nextx] == 2:
            snake.append([nextx,nexty])
            Map[nexty][nextx] = 1
        else:
            break
    else:
        break

print(count)
