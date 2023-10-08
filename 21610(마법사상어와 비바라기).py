# 음수도 나머지 연산이 된다.
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

M = [list(map(int,input().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
location = [list(map(int,input().split())) for _ in range(m)]
cloud = []
cloud.append([n-1,0])
cloud.append([n-1,1])
cloud.append([n-2,0])
cloud.append([n-2,1])


d = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
d2 = [[-1,-1],[-1,1],[1,1],[1,-1]]

def move(direction,count):
    for _ in range(count):
        for i in range(len(cloud)):
            nexty = cloud[i][0] + d[direction-1][0]
            nextx = cloud[i][1] + d[direction-1][1]
            if 0 <= nextx <= n-1 and 0 <= nexty <= n-1:
                cloud[i][0] = nexty
                cloud[i][1] = nextx
            else :
                if nextx < 0:
                    nextx = n + nextx
                elif nextx > n-1:
                    nextx = nextx - n
                if nexty < 0:
                    nexty = n +nexty
                elif nexty > n-1:
                    nexty = nexty - n
                cloud[i][0] = nexty
                cloud[i][1] = nextx

for de in location:
    move(de[0],de[1])
    for l in cloud:
        visit[l[0]][l[1]] = 1
        M[l[0]][l[1]]+=1

    while True:
        if not cloud:
            break
        l2 = cloud.pop()
        wc = 0
        for lo in d2:
            nexty = l2[0] + lo[0]
            nextx = l2[1] + lo[1]
            if 0 <= nextx <= n-1 and 0 <= nexty <= n-1:
                if M[nexty][nextx] > 0:
                    wc+=1
        M[l2[0]][l2[1]]+=wc



    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                if M[i][j] >= 2:
                    cloud.append([i,j])
                    M[i][j] -=2
            elif visit[i][j] == 1:
                visit[i][j] = 0
res = 0
for i in M:
    res += sum(i)
print(-7 % 8)
print(res)