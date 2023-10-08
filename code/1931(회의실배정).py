import sys
input = sys.stdin.readline

cur = 0
cnt = 0
n = int(input().rstrip())
l = [list(map(int,input().split()))for _ in range(n)]
for s, f in sorted(l,key=lambda x:(x[1],x[0])):
    if cur <= s:
        cur = f
        cnt += 1
print(cnt)
    
