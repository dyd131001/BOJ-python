n = int(input())
for _ in range(n):
    s = input()
    sn = len(s)
    i = 0
    c = 0
    while True:
        if i >= sn//2:
            break
        if s[i] == s[-i-1]:
            c += 1
        else:
            temp1 = s[i+1: sn-i]
            temp2 = s[i:sn-i-1]
            if temp1 == temp1[::-1]:
                print("1")
                break
            elif temp2 == temp2[::-1]:
                print("1")
                break
            else:
                print("2")
                break
        i += 1

    if c == sn//2:
        print("0")
