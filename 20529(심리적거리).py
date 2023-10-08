import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
from itertools import combinations

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        L = list(map(str,input().split()))
        if n > 32:
            print(0)
        else:
            minv = sys.maxsize
            for L1 in combinations(L,3):
                score = sum(int(s1 != s2) + int(s1 != s3) + int(s2 != s3) for s1,s2,s3 in zip(*L1))
                minv = min(minv,score)
                if minv == 0:
                    break
            print(minv)

