import sys
input = sys.stdin.readline

n = int(input())


L = [(1,0), (0,1)]
for i in range(2,41):
    L.append((L[i-1][0] + L[i-2][0],L[i-1][1] + L[i-2][1]))

for _ in range(n):
    t = int(input())
    print(str(L[t][0])+" "+str(L[t][1]))
