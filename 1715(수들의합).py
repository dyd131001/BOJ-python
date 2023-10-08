import heapq

n = int(input())
L = []
for _ in range(n):
    heapq.heappush(L, int(input()))

sum = 0
for _ in range(n-1):
    n1 = heapq.heappop(L)
    n2 = heapq.heappop(L)
    sum += n1 + n2
    heapq.heappush(L, n1+n2)

print(sum)
