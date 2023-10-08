import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())

count = 1
cnt = 0
while B >= 5:
    if B%2 == 1:
        count *= A

    A = (A**2) %C
    B = B//2

print(((A**B)*count)%C)


