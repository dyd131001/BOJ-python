import sys
input = sys.stdin.readline

n = int(input())
sum = 0
L = []
for _ in range(n):
    L.append(int(input()))
L.sort()

for j in range(1, n+1):
    if L[j-1] > j:
        sum += L[j-1] - j
    else:
        sum += j - L[j-1]

print(sum)
