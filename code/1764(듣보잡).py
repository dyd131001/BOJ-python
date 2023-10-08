import sys
input = sys.stdin.readline

n, m = map(int,input().split())
D = set()
D2 =set()
for _ in range(n):
    D.add(input().rstrip())
for _ in range(m):
    D2.add(input().rstrip())


r = sorted(list(D&D2))
print(len(r))
for i in r:
    print(i)