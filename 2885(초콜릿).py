k = int(input())
n = k
count = 2
count2 = 1
m = 0
f = 0

while count < k:
    if n % 2 == 1 and f == 0:
        m = count2
        f = 1
    n = n//2
    count *= 2
    count2 += 1

if(m == 0):
    print(count, 0)
else:
    print(count, count2 - m + 1)




