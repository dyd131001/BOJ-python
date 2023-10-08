t = int(input())

for _ in range(t):
    n = int(input())
    L3 = [0]*n
    L4 = [0]*n

    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))

    L3[0] = L1[0]
    L4[0] = L2[0]
    if n>=2:
        L3[1] = L3[0] +L2[1]
        L4[1] = L4[0] + L1[1]

    for i in range(2,n):
        if i%2 == 0:
            if L3[i-1]+L1[i] > L4[i-2] +L1[i]:
                L3[i] = L3[i-1]+L1[i]
            else:
                L3[i] = L4[i-2] +L1[i]

            if L4[i-1]+L2[i] > L3[i-2] +L2[i]:
                L4[i] = L4[i-1]+L2[i]
            else:
                L4[i] = L3[i-2] +L2[i]

        else:
            if L3[i-1]+L2[i] > L4[i-2] +L2[i]:
                L3[i] = L3[i-1] + L2[i]
            else:
                L3[i] = L4[i-2] + L2[i]

            if L4[i-1]+L1[i] > L3[i-2] +L1[i]:
                L4[i] = L4[i-1]+L1[i]
            else:
                L4[i] = L3[i-2] +L1[i]

    if L3[n-1] > L4[n-1]:
        print(L3[n-1])
    else:
        print(L4[n-1])