n, m = map(int, input().split())

L = list(map(int, input().split()))
L.sort()

L1 = []
L2 = []
for i in L:
    if i > 0:
        L1.append(i)
    else:
        L2.append(i)

count = m-1
sum = 0
max1 = 0
max2 = 0
for i in range(len(L1)):
    if(i == 0):
        max1 = L1[-1]
    if(count != m-1):
        count += 1
    else:
        sum += L1[-i-1] * 2
        count = 0

count = m-1
for i in range(len(L2)):
    if(i == 0):
        max2 = -L2[0]
    if(count != m-1):
        count += 1
    else:
        sum += L2[i] * -2
        count = 0

if max1 > max2:
    sum -= max1
else:
    sum -= max2
print(sum)
