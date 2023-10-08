import sys
input = sys.stdin.readline

n= int(input())
L = [0, 1, 3]

if n <= 2:
    print(L[n])
else:
    for i in range(3,n+1):
        L.append( (L[i-1] + 2*L[i-2]) %10007)
    print(L[n])