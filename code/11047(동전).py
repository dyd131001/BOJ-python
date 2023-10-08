import sys
input = sys.stdin.readline

n, t = map(int,input().split())
L = [ int(input()) for _ in range(n)]
r = 0
for i in range(n-1,-1,-1):
    if t == 0:
        break
    if t >= L[i]:
        r += t // L[i]
        t = t % L[i]
print(r)