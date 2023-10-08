''' 백트래킹
import sys
input = sys.stdin.readline
n = int(input().strip())
c = sys.maxsize
def one(n,cnt):
    global c
    if c < cnt:
        return
    if n == 1:
        c = min(cnt , c)
    else :
        if n%3 == 0:
            one(n//3,cnt+1)
        if n%2 == 0:
            one(n//2,cnt+1)
        one(n-1,cnt+1)

one(n,0)
print(c)
'''

import sys
input = sys.stdin.readline

n = int(input())
def one(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    return min(one(n//3) + n%3 +1, one(n//2) +n%2 +1)

print(one(n))