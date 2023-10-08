def s(c):
    if c == '#':
        return 0
    elif c == '*':
        return 1


t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int, input()))
    L2 = list(map(s, input()))
    count1 = 0
    count2 = 0
    r = 0

    if L[0] == 1:
        L3 = L2.copy()
        if L3[0] == 0 and L3[1] == 0:
            L3[0] = 0
            L3[1] = 1

        for i in range(1, n-1):
            if L3[i-1] + L3[i] == L[i] and L3[i+1] == 0:
                L3[i+1] = 0
            elif L3[i-1] + L3[i] > L[i]:
                r = 1
                break
            else:
                L3[i+1] = 1

        if L[n-1] == L3[n-1] + L3[n-2]:
            r = 0
        else:
            r = 1

        if r == 0:
            for i in L3:
                count1 += i

        r = 0
        if L2[0] == 0 and L2[1] == 0:
            L2[0] = 1
            L2[1] = 0
        for i in range(1, n-1):
            if L2[i-1] + L2[i] == L[i] and L2[i+1] == 0:
                L2[i+1] = 0
            elif L2[i-1] + L2[i] > L[i]:
                r = 1
                break
            else:
                L2[i+1] = 1

        if L[n-1] == L2[n-1] + L2[n-2]:
            r = 0
        else:
            r = 1

        if r == 0:
            for i in L2:
                count2 += i

        if count1 > count2:
            print(count1)
        else:
            print(count2)

    else:
        if L[0] == 0:
            L2[0] = 0
            L2[1] = 0
        elif L[0] == 2:
            L2[0] = 1
            L2[1] = 1
        for i in range(1, n-1):
            if L2[i-1] + L2[i] == L[i] and L2[i+1] == 0:
                L2[i+1] = 0
            elif L2[i-1] + L2[i] > L[i]:
                r = 1
                break
            else:
                L2[i+1] = 1

        if L[n-1] == L2[n-1] + L2[n-2]:
            r = 0
        else:
            r = 1

        if r == 0:
            for i in L2:
                count2 += i
        print(count2)
