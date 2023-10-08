import sys
input = sys.stdin.readline


str1 = list(map(str,input().rstrip()))
str2 = list(map(str,input().rstrip()))
l1 = len(str1)
l2 = len(str2)
L = [0 for _ in range(l2+1)]

for i in range(1,l1+1):
    pre = 0
    for j in range(1,l2+1):
        if pre < L[j]:
            pre = L[j]
        elif str1[i-1] == str2[j-1]:
            L[j] =pre+1
        else:
            L[j] = max(L[j-1],L[j])
    print(L)
print(L[l2])
