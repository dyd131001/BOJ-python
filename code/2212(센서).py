n = int(input())
m = int(input())

L = list(map(int, input().split()))
if (n <= m):
    print(0)
else:
    L.sort()
    L2 = []
    for i in range(n-1):
        L2.append(L[i+1] - L[i])

    L2.sort(reverse=True)
    for i in range(m-1):
        L2[i] = 0

    sum = 0
    for i in L2:
        sum += i
    print(sum)
