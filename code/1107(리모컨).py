import sys
input = sys.stdin.readline
target = str(input().strip())
tn = int(target)
n = int(input())

if n != 0:
    nL = set(map(str,input().split()))
else:
    nL = set()

mincount = abs(100-int(target))

for num in range(1000001):
    strnum = str(num)
    strlen = len(strnum)
    if strlen >= mincount :
        break
    for cnt , sn in enumerate(strnum):
        if sn in nL:
            break
        elif cnt+1 == strlen:
            mincount = min(mincount, abs(num - tn)+strlen)
print(mincount)