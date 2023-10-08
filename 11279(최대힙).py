import sys
input = sys.stdin.readline
import heapq

n= int(input())
L = []
for _ in range(n):
    num = int(input())
    if num !=0:
        heapq.heappush(L,-num)
    else:
        if L:
            print(-heapq.heappop(L))
        else:
            print(0)