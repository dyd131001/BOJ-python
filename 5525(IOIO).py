import sys
input = sys.stdin.readline
n = int(input())
strlen = int(input())
T = input()

count = 0
score = 0
last = 'O'
for s in T:
    if s == "I":
        if last == "O":
            score+=1
            if score >= n+1:
                count+=1
        else:
            score=1
    else:
        if last == "O":
            score=0
    last = s


print(count)