import sys
input = sys.stdin.readline

num = [1, 1, 2, 4]

for i in range(4,12):
    num.append(num[i-1] + num[i-2] + num[i-3])

t = int(input())
for _ in range(t):
    n = int(input())
    print(num[n])

