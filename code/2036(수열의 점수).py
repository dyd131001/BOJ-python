import sys
input = sys.stdin.readline
n = int(input())
L1 = []
L2 = []
len1 = 0
len2 = 0
for _ in range(n):
    a = int(input())
    if a > 0:
        L1.append(a)
        len1 += 1
    else:
        L2.append(a)
        len2 += 1

L1.sort(reverse=True)
L2.sort()

sum = 0


if len1 % 2 != 0:
    sum += L1[-1]
if len2 % 2 != 0:
    sum += L2[-1]
for i in range(len1//2):
    sum += L1[i*2] * L1[i*2+1]
    if L1[i*2+1] == 1:
        sum += 1
for i in range(len2//2):
    sum += L2[i*2] * L2[i*2+1]

print(sum)
