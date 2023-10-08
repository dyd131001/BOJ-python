import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n-1, -1, -1):
        if(max <= L[i]):
            max = L[i]
        else:
            count += max - L[i]
    print(count)