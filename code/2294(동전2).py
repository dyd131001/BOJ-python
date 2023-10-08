n , t = map(int,input().split())

L = [0 for _ in range(t+1)]
nL = []
for i in range(n):
    a = int(input())
    nL.append(a)
nL.sort()

for m in nL:
    for i in range(m, t+1):
        if L[i] == 0:
            if L[i-m] == 0:
                if i-m == 0:
                    L[i] = L[i-m]+1
            else:
                L[i] = L[i-m]+1
        else:
            if L[i-m] == 0:
                if i-m == 0:
                    if L[i-m]+1 < L[i]:
                        L[i] = L[i-m]+1
            else:
                if L[i-m]+1 < L[i]:
                    L[i] = L[i-m]+1

if L[t] == 0:
    print('-1')
else:
    print(L[t])



