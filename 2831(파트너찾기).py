n = int(input())
M = list(map(int, input().split()))
W = list(map(int, input().split()))

M.sort()
W.sort()
mi = 0
wi = 1

count = 0
while True:
    if mi >= len(M):
        break
    if wi > len(W):
        break
    if M[mi] >= 0:
        break
    if W[-wi] < 0:
        break
    if M[mi]*(-1) > W[-wi]:
        count += 1
        mi += 1
        wi += 1
    else:
        wi += 1

mi = 1
wi = 0

while True:
    if wi >= len(W):
        break
    if mi > len(M):
        break
    if W[wi] >= 0:
        break
    if M[-mi] < 0:
        break
    if W[wi]*(-1) > M[-mi]:
        count += 1
        wi += 1
        mi += 1
    else:
        mi += 1

print(count)
