n, k = map(int, input().split())

L = [list(map(int, input().split())) for _ in range(n)]
L.sort(key=lambda x: x[0], reverse=True)
L.sort(key=lambda x: x[1])

value = 0
cost = 0
index = 0
se = 1
while True:
    if index >= n:
        break
    if value >= k:
        break
    value += L[index][0]
    if L[index][1] == cost:
        se += 1
    else:
        se = 1
    cost = L[index][1]
    index += 1

while True:
    if index >= n:
        break
    if cost*se > L[index][1] and cost != L[index][1]:
        cost = L[index][1]
        se = 1
        break
    index += 1


if value >= k:
    print(cost * se)
else:
    print("-1")
