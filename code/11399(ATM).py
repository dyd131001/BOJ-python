import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int,input().split()))
L.sort()
print(sum( sum( j for j in L[0:i+1]) for i in range(n)))


