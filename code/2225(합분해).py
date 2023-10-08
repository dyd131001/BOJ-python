n, k = map(int, input().split())

L = [[0 for _ in range(k+1)]for _ in range(n+1)]

for i in range(1, k+1):
    for j in range(n+1):
        if i == 1:
            L[j][i] = 1
        else:
            if j != 0:
                L[j][i] += L[j-1][i] + L[j][i-1]
            else:
                L[j][i] += L[j][i-1]

print(L[n][k] % 1000000000)
