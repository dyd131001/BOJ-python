n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
V = [[0 for _ in range(n)] for _ in range(n)]
V[0][0] = 1
for j in range(n):
    for i in range(n):
        if V[j][i] == 0:
            continue
        if L[j][i] == 0:
            continue
        else:
            nx = i + L[j][i]
            ny = j + L[j][i]
            if(0 <= ny <= n-1):
                V[ny][i] += V[j][i]
            if(0 <= nx <= n-1):
                V[j][nx] += V[j][i]
print(V[n-1][n-1])
