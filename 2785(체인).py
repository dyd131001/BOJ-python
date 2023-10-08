import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))

L.sort()
i = 0
count = 0
while n > 1:
    L[i] = L[i] - 1
    if(L[i] == 0):
        n -= 2
        count += 1
        i += 1
    else:
        n -= 1
        count += 1

print(count)
