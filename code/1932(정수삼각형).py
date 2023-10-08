import sys
input = sys.stdin.readline


n = int(input())
dp = list(map(int,input().split()))
d = [-1 , 0]
for i in range(n-1):
    cost = list(map(int,input().split()))
    dp2 = []
    for j , c in enumerate(cost):
        maxv = 0
        for k in d:
            nextj = j + k
            if 0 <= nextj <= i:
                if maxv < dp[nextj]:
                    maxv = dp[nextj]
        dp2.append(maxv+c)
    dp = dp2

print(max(dp))