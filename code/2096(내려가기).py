n = int(input())

a = list(map(int, input().split()))

MAX = [0, 0 ,0]
MAX2 = [0, 0 ,0]
MIN = [0,0,0]
MIN2 = [0,0,0]


for i in range(3):
    MAX[i] = a[i]
    MIN[i] = a[i]
if n > 1:
    a = list(map(int, input().split()))
for i in range(1, n):
    for j in range(3):
        if(j == 0):
            if MAX[0] > MAX[1]:
                MAX2[j] = a[j]+MAX[0]
            else:
                MAX2[j] = a[j]+MAX[1]
            if MIN[0] > MIN[1]:
                MIN2[j] = a[j]+MIN[1]
            else:
                MIN2[j] = a[j]+MIN[0]
        elif(j == 1):
            MAX2[j] = a[j]+max(MAX)
            MIN2[j] = a[j]+min(MIN)
        else:
            if MAX[1] > MAX[2]:
                MAX2[j] = a[j]+MAX[1]
            else:
                MAX2[j] = a[j]+MAX[2]
            if MIN[1] > MIN[2]:
                MIN2[j] = a[j]+MIN[2]
            else:
                MIN2[j] = a[j]+MIN[1]
    for k in range(3):
        MAX[k] = MAX2[k]
        MIN[k] = MIN2[k]
    if i != n-1:
        a = list(map(int, input().split()))

print(max(MAX),min(MIN))

