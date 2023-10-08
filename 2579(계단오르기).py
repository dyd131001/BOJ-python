n = int(input())
L= []
for _ in range(n):
    L.append(int(input()))

L2 =[0]*n


if n > 2:
    L2[0] = L[0]
    L2[1] = L[0]+L[1]
    if L[0]+L[2] > L[1]+L[2]:
        L2[2] = L[0]+L[2]
    else :
        L2[2] = L[1]+L[2]

    for i in range(3,n):
        if L[i] + L[i-1] + L2[i-3] > L[i] + L2[i-2]:
            L2[i] = L[i] + L[i-1] + L2[i-3]
        else:
            L2[i] = L[i] + L2[i-2]

    print(L2[n-1])
elif n == 2:
    print(L[0]+L[1])
else:
    print(L[0])
