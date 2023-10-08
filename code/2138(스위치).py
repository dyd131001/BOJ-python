n = int(input())
s = list(map(int, input()))
t = list(map(int, input()))
s2 = s.copy()
count = 0

for i in range(1, len(s)):
    if s[i-1] != t[i-1]:
        count += 1
        s[i-1] = int(not(s[i-1]))
        s[i] = int(not(s[i]))
        if(i < len(s)-1):
            s[i+1] = int(not(s[i+1]))


if(s == t):
    print(count)
else:
    count = 1

    s2[0] = int(not(s2[0]))
    s2[1] = int(not(s2[1]))

    for i in range(1, len(s2)):
        if s2[i-1] != t[i-1]:
            count += 1
            s2[i-1] = int(not(s2[i-1]))
            s2[i] = int(not(s2[i]))
            if(i < len(s2)-1):
                s2[i+1] = int(not(s2[i+1]))

    if(s2 == t):
        print(count)
    else:
        print(-1)
