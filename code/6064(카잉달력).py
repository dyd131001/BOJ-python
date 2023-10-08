import sys
input = sys.stdin.readline

T = int(input())
def solve(M,N,tx,ty):
    k = tx
    ch = 0
    while k <= M*N:
        if (k-tx)%M == 0 and (k-ty)%N == 0:
            ch =1
            print(k)
            break
        k += M
    if ch == 0:
        print(-1)

for _ in range(T):
    M,N,tx,ty = map(int,input().split())
    solve(M,N,tx,ty)