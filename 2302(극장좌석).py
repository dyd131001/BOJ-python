n = int(input())
n2 = int(input())

L2 = [1, 1, 2]
L2L = 2

L = []
for i in range(n2):
    a = int(input())
    L.append(a)

sum = 1
index = 0

if n2 != 0:
    if L[0] == 1:
        sum = 1
        index = L[0]
    else:
        if (L[0] - 1) > L2L:
            for j in range((L[0] - 1)-L2L):
                L2.append(L2[L2L] + L2[L2L-1])
                L2L += 1
        sum = L2[L[0]-1]
        index = L[0]


for i in range(1, n2):
    if (L[i]-1 - index) > L2L:
        for j in range((L[i]-1 - index)-L2L):
            L2.append(L2[L2L] + L2[L2L-1])
            L2L += 1
    sum = sum * L2[(L[i]-1 - index)]
    index = L[i]


if index < n:
    if ((n-index)) > L2L:
        for j in range((n-index)-L2L):
            L2.append(L2[L2L] + L2[L2L-1])
            L2L += 1
    sum = sum * L2[(n-index)]


print(sum)
