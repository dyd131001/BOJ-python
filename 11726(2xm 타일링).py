import sys
input = sys.stdin.readline

n = int(input())

L = [1,1,2]
a = 1
b = 1
c = 2

if n >= 3:
    for i in range(3,n+1):
        a = b
        b = c
        c = a+b
    print(c%10007)
else:
    if n == 1:
        print(a)
    else:
        print(c)

