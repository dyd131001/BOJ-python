t = int(input())

x = 0
for i in range(t):
    l = list(map(str, input().split()))
    for n in l:
        if n == '@':
            x = x*3
        elif n == '%':
            x = x+5
        elif n == '#':
            x = x-7
        else:
            x = float(n)
    print("%0.2f" %x)
