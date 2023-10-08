import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
M = [list(map(int,input().split())) for _ in range(n)]
minM = [[0]*3 for _ in range(n)]
minM[0][0] = M[0][0]
minM[0][1] = M[0][1]
minM[0][2] = M[0][2]
for i in range(1,n):
    for j in range(3):
        if j == 0:
            minM[i][0] = M[i][0]+min(minM[i-1][1],minM[i-1][2])
        elif j == 1:
            minM[i][1] = M[i][1]+min(minM[i-1][0],minM[i-1][2])
        else:
            minM[i][2] = M[i][2]+min(minM[i-1][1],minM[i-1][0])

print(min(minM[n-1]))