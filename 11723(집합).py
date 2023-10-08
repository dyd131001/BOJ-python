import sys
input = sys.stdin.readline
n = int(input())
S = set()

for _ in range(n):
    L= list(map(str,input().split()))
    if len(L) != 1:
        value = int(L[1])
        commend = L[0]
        if commend == "add":
            S.add(value)
        elif commend == "remove":
            if value in S:
                S.remove(value)
        elif commend == "check":
            if value in S:
                print(1)
            else:
                print(0)
        else:
            if value in S:
                S.remove(value)
            else:
                S.add(value)

    else:
        if L[0] == "all":
            S = {i for i in range(1,21)}
        else:
            S.clear()


