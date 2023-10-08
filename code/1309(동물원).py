
n = int(input())
a1 = 3
a2 = 7
a3 = 17
a4 = 0
for i in range(4,n+1):
    a4 = 2*(a3)+ a2
    a2 = a3
    a3 = a4

if(n == 1):
    print(a1)
elif(n == 2):
    print(a2)
elif(n == 3):
    print(a3)
else:
    print(a4%9901)
