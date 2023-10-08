t = int(input())

for i in range(t):
    tc = 0
    c = 0
    s = input()
    for r in s:
        if 'O' == r:
            c += 1
            tc += c
        else:
            c = 0
    print(tc)
