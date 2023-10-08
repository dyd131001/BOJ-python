n = int(input())

L = list(map(int, input().split()))
R = []
L.sort()

for i in range(n):
    R.append(L[i] + L[-i-1])

R.sort()
print(R[0])
