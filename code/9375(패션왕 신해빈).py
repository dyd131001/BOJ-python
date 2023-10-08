import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    L = defaultdict(int)
    for _ in range(n):
        name , type = map(str,input().split())
        L[type]+=1
    day = 0
    for item in L.values():
        if day == 0:
            day = (item+1)
        else:
            day *= (item+1)
    if day != 0:
        day-=1
    print(day)
