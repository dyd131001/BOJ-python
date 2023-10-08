n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x2 = x
        y2 = y
    else:
        x2 = y
        y2 = x

    while x2 % y2 != 0:
        t = x2 % y2
        x2 = y2
        y2 = t

    print(int(x*y/y2))
