n = int(input())
o1, o2 = map(int, input().split())

tl = int(input())
L = [int(input()) for _ in range(tl)]

D = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(tl)]


def dfs(cnt, open1, open2):
    if(cnt == tl):  # 깊이 제한
        return 0
    else:
        if D[cnt][open1][open2] != 0:
            return D[cnt][open1][open2]
        else:
            left = dfs(cnt+1, L[cnt], open2) + abs(L[cnt]-open1)
            right = dfs(cnt+1, open1, L[cnt]) + abs(L[cnt]-open2)
            if left < right:
                D[cnt][open1][open2] = left
            else:
                D[cnt][open1][open2] = right
            return D[cnt][open1][open2]


print(dfs(0, o1, o2))
