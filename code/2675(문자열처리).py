t = int(input())

for i in range(t):
    n, s = map(str, input().split())
    re = ""
    for c in s:
        re += c*int(n)
    print(re)
