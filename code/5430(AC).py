import sys
input = sys.stdin.readline
from collections import deque

t = int(input().rstrip())

for _ in range(t):
    r = 1
    c = input().rstrip()
    Dlen = int(input())

    D= deque(input().rstrip()[1:-1].split(","))
    if Dlen == 0:
        D = []

    ch = 0
    for cm in c:
        if cm == 'R':
            r = r*-1
        else:
            if D:
                if r == 1:
                    D.popleft()
                else:
                    D.pop()
            else:
                print('error')
                ch=1
                break
    if ch ==0:
        if r == -1:
            D.reverse()
            print("[" + ",".join(D) + "]")
        else:
            print("[" + ",".join(D) + "]")