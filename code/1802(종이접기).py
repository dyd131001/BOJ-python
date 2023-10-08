
import sys
import math
sys.setrecursionlimit(10**7)


def s(start, f, L):
    if start >= f:
        return True

    left = start
    right = f
    mid = (start + f) // 2

    while True:
        if L[left] == L[right]:
            return False
        left += 1
        right -= 1
        if left >= right:
            break

    return s(0, mid-1, L)


t = int(input())

for _ in range(t):
    L = input()
    f = len(L)-1

    if(f % 2 != 0):
        print("NO")
        continue

    r = s(0, f, L)

    if r == True:
        print("YES")
    else:
        print("NO")
