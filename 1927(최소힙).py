import sys
input = sys.stdin.readline
import heapq

l = []
n = int(input())
for _ in range(n):
    m = int(input())
    if m == 0:
        if l:
            print(heapq.heappop(l))
        else:
            print(0)
    else:
        heapq.heappush(l,m)