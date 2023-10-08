import sys
input = sys.stdin.readline

n, m = map(int,input().split())
N = list(map(int,input().split()))
N2 = N[:]

for i in range(1,n):
    N2[i] += N2[i-1]

for _ in range(m):
    s, f = map(int,input().split())
    if s == 1:
        print(N2[f-1])
    else:
        print(N2[f-1] - N2[s-2])