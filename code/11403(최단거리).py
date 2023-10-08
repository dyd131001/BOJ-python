import sys
input = sys.stdin.readline

n= int(input())
M = [ list(map(int,input().split())) for _ in range(n)]
S = [ [ 0 for _ in range(n)] for _ in range(n)]

for k in range(n):
    for i in range(n):
            for j in range(n):
                if M[i][k] == 1:
                    M[i][j] = max(M[i][j], M[k][j])

for i in M:
    for j in i:
        print(j,end=' ')
    print()