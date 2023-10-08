a, b, c = map(int, input().split())
ac, bc, cc = 0, 0, 0

if a > b:
    ac += 1
else:
    bc += 1

if b > c:
    bc += 1
else:
    cc += 1

if c > a:
    cc += 1
else:
    ac += 1

if ac == 1:
    print(a)
elif bc == 1:
    print(b)
else:
    print(c)
