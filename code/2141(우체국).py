# 직관적으로 무게를 생각하면 편하다

n = int(input())
L = []
sum = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum += b
    L.append([a, b])

if(sum % 2 == 0):
    sum //= 2
else:
    sum = sum // 2 + 1

L.sort(key=lambda x: x[0])
sum2 = 0
i = 0

while True:
    sum2 += L[i][1]
    if(sum2 >= sum):
        print(L[i][0])
        break
    i += 1
