L = [int(input()) for _ in range(6)]
L1 = 0
L2 = 0
L3 = 0

count = L[5]
if L[4] != 0:
    count += L[4]
    L1 += 11*L[4]
    L[4] = 0

if L[3] != 0:
    count += L[3]
    L2 += 5*L[3]
    L[3] = 0


while L[2] != 0:
    if L3 == 0:
        L3 += 4
        L[2] -= 1
        L3 -= 1
        count += 1
    else:
        L3 -= 1
        L[2] -= 1

if L3 != 0:
    if L3 == 3:
        L2 += 5
        L1 += 7
    elif L3 == 2:
        L2 += 3
        L1 += 6
    else:
        L2 += 1
        L1 += 5


if L2 >= L[1]:
    sub = L2 - L[1]
    L1 += sub*4
    L[1] = 0
    L2 = 0
else:
    L[1] = L[1] - L2
    L2 = 0

while L[1] != 0:
    if L2 == 0:
        L2 += 9
        L[1] -= 1
        L2 -= 1
        count += 1
    else:
        L2 -= 1
        L[1] -= 1


if L2 != 0:
    L1 += 4*L2
    L2 = 0


if L1 < L[0]:
    L[0] = L[0] - L1
    L1 = 0

    while L[0] != 0:
        if L1 == 0:
            L1 += 36
            L1 -= 1
            L[0] -= 1
            count += 1
        else:
            L1 -= 1
            L[0] -= 1
    print(count)
else:
    print(count)
