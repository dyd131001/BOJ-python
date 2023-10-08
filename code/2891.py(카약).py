import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
sl = list(map(int, input().split()))
r = list(map(int, input().split()))

L = [1 for _ in range(n)]
for i in sl:
    L[i-1] = 0
for i in r:
    L[i-1] += 1

sum = 0

for i in range(n):
    if L[i] == 2:
        if i == 0:
            if L[i+1] == 0:
                L[i+1] = 1
            sum += 1
        elif i == n-1:
            if L[i-1] == 0:
                sum += 2
            else:
                sum += 1
        else:
            if L[i-1] == 0:
                sum += 2
            elif L[i+1] == 0:
                L[i+1] = 1
                sum += 1
            else:
                sum += 1
    elif L[i] == 1:
        sum += 1

print(n-sum)
