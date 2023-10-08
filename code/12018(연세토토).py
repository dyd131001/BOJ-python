import sys
input = sys.stdin.readline

n, m = map(int, input().split())
minL = []

for _ in range(n):
    p, max = map(int, input().split())
    if p < max:
        minL.append(1)
        input()
    else:
        L = list(map(int, input().split()))
        L.sort()
        minL.append(L[p-max])

minL.sort()
i = 0
while True:
    if i == n:
        break
    m -= minL[i]
    if m < 0:
        break
    i += 1

print(i)
