n = int(input())
L = list(map(int,input().split()))

S = [L[0]]
sn = 1

for i in range(1,n):
    if S[-1] < L[i]:
        S.append(L[i])
        sn+=1
    else:
        if sn == 1:
            S[0] = L[i]
        else:
            if S[-2] < L[i]:
                S[-1] = L[i]
            else:
                for j in range(sn):
                    if S[j] >= L[i]:
                        S[j] = L[i]
                        break

print(len(S))