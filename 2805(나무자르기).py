import sys
input = sys.stdin.readline

n, m = map(int,input().split())
L = list(map(int,input().split()))

maxL = max(L)
minL = 0

while minL <= maxL:
    middle = (minL + maxL)//2
    sumL= sum(i-middle for i in L if i-middle > 0)
    if sumL >= m:
        minL = middle+1
    else:
        maxL = middle-1


print(maxL)

# 200(16) 150 130 100 90