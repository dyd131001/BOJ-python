import sys
input = sys.stdin.readline

n, m = map(int, input().split())

L = [list(map(int, input().split())) for _ in range(n)]
L.sort(key=lambda x: x[0])

x = L[0][0]
SC = 0

for S, F in L:

    if x <= S:
        x = S
    elif x > F:
        continue

    if (F-x) % m != 0:
        count = (F-x)//m+1
        SC += count
        x += m*count
    else:
        count = (F-x)//m
        x += m*count
        SC += count

print(SC)
