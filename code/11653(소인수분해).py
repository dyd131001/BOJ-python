import math
c = 0
n = int(input())
m = round(math.sqrt(n))

while True:
    if n == 1:
        print('')
        break
    if n == 2:
        print(int(n))
        break
    for z in range(2, m+1):  # range 범위 (1 <= n+1)
        if n % z == 0:
            n = n/z
            m = round(math.sqrt(n))
            print(z)
            break
        if z >= m:
            c = 1
            print(int(n))
            break
    if c == 1:
        c = 0
        break
