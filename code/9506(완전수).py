while True:
    n = int(input())
    if n == -1:
        break
    nl = [1]
    c = 2
    con = n/2
    while c <= con+1:
        if n % c == 0:
            nl.append(c)
            if n/c != c:
                nl.append(int(n/c))
            con = (n/c)/2
        c += 1
    sum = 0
    for i in nl:
        sum += i
    if sum == n:
        nl = sorted(nl)
        print(str(n) + " = ", " + ".join(str(x) for x in nl), sep='')
    else:
        print(n, " is NOT perfect.", sep='')
