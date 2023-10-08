s1 = input()
s2 = input()

s1n = len(s1)
s2n = len(s2)
D = [[0 for _ in range(s1n+1)] for _ in range(s2n+1)]
max = 0
for i in range(1, s2n+1):
    for j in range(1, s1n+1):
        if s1[j-1] == s2[i-1]:
            D[i][j] = D[i][j]+D[i-1][j-1] + 1
            if D[i][j] > max:
                max = D[i][j]

print(max)
