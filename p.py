'''import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))

dp  = [1] * (n)
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''
import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))
dp = [0]
for i in arr:
    if i > dp[-1]:
        dp.append(i)
    else:
        start = 0
        end = len(dp)-1
        while end-start != 1:
            mid = (start+end)//2
            if i > dp[mid]:
                start = mid
            else:
                end = mid
        dp[end] = i

print(len(dp)-1)

