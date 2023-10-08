import sys
input = sys.stdin.readline
from collections import defaultdict

n,m = map(int,input().split())
L = defaultdict(str)
for _ in range(n):
    name, password = map(str,input().split())
    L[name] = password
for _ in range(m):
    print(L[input().rstrip()])