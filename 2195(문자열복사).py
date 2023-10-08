a2 = input()
b = input()

bl = len(b)
make = 0
count = 0

while True:
    if make == len(b):
        break
    maxc = 0
    bi = make
    bj = bi + 1
    ai = 0
    aj = 1
    while True:
        if ai >= len(a2):
            break
        while True:
            if aj >= len(a2)+1:
                ai += 1
                break
            if b[bi:bj] == a2[ai:aj]:
                if aj-ai > maxc:
                    maxc = aj-ai
                bj += 1
                aj += 1
            else:
                ai += 1
                aj = ai+1
                bj = bi+1
                break
    make += maxc
    count += 1
print(count)
