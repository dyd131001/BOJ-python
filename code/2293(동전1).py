
n, t = map(int,input().split())

T = [0 for _ in range(t+1)]
L = []
T[0] =1
for _ in range(n):
    a = int(input())
    L.append(a)
L.sort()

for i in L:
    for j in range(i,t+1):
        if j-i >= 0:
            T[j] += T[j-i]

print(T[t])

