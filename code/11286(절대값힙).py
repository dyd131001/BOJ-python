import sys
input = sys.stdin.readline
import heapq

n= int(input())
L = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(L,(num,1))
    elif num < 0:
        heapq.heappush(L,(-num,0))
    else:
        if L:
            hn = heapq.heappop(L)
            if hn[1] == 0:
                print(-hn[0])
            else:
                print(hn[0])
        else:
            print(0)