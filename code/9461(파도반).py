t = int(input())
for _ in range(t):
    L = [0 ,1 , 1 , 1 , 2 , 2]
    n = int(input())
    for i in range(6, n+1):
        L.append(L[i-1]+L[i-5])
    print(L[n])
