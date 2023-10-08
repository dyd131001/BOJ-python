D = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,  2, 2, 2, 1,
     2, 2, 2, 2, 2,  2, 2]

s = list(map(int,input()))
n = len(s)
D2 = [0 for _ in range(n+1)]
D2[0] = 1

i = 0
c = 0

if(s[0] == 0):
    c=1
    print('0')
else:
    D2[1] = 1
    for j in range(1,n):
        if s[i]*10 + s[j] <= 26:
            if D[s[i]*10 + s[j]] == 2:
                if j == n-1:
                    D2[j+1] = D2[j-1] + D2[j]
                else:
                    if s[j+1] == 0:
                        D2[j+1] = D2[j]
                    else:
                        D2[j+1] = D2[j-1] + D2[j]
            elif D[s[i]*10 + s[j]] == 1:
                D2[j+1] = D2[j]
            else:
                c = 1
                print('0')
                break
        else:
            if s[j] == 0:
                c = 1
                print('0')
                break
            else:
                D2[j+1] = D2[j]
        i+=1

if c == 0:
    print(D2[n]%1000000)