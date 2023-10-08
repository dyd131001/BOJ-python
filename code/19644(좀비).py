import sys
input = sys.stdin.readline

L = int(input())  # 거리
ML, MK = map(int, input().split())  # 사거리 ,공격력
C = int(input())  # 어뢰 개수
KN = 0
J = []
J2 = []
for i in range(L):
    a = int(input())
    J.append(a)
    J2.append(1)


i = 0
count = 0
j = ML-1

Li = 0  # 목숨
while True:

    if i-ML+1 >= 0 and i-ML+1 <= L-1:
        if J2[i-ML+1] == 0:
            count -= 1

    if i == L:
        break
    if C == 0 and MK*(KN+1) < J[i]:
        Li = 1
        break
    elif C != 0 and MK*(KN+1) < J[i]:
        if KN >= 1:
            if KN == j - count:
                KN -= 1
            if ML > 1:
                count += 1
                J2[i] = 0
        C -= 1
    else:
        if KN < j - count:
            KN += 1
    i += 1

if Li == 0:
    print("YES")
else:
    print("NO")

 # 2 2 2 2 2 2 2
  # 2 2 2 2 2 2 2
   #  x x x x x x x
    #   2 2 2 2 2 2 2
    #    2 2 2 2 2 2 2
    #     2 2 2 2 2 2 2
    #            이기점부터 값내려주자
