''' 처음짠 코드

import sys
input = sys.stdin.readline

day = int(input().rstrip())

maxlist = [0 for _ in range(day+1)]
daylist = [[]]
for i in range(day):
    daylist.append(list(map(int,input().split())))

for i in range(day):
    now = day-i
    next = (now + daylist[now][0]-1)
    if next < day:
        if now+1 <= day:
            if maxlist[next+1] + daylist[now][1] > maxlist[now+1]:
                maxlist[now] = maxlist[next+1] + daylist[now][1]
            else:
                maxlist[now] = maxlist[now+1]
        else:
            maxlist[now] = maxlist[next+1] + daylist[now][1]
    elif next == day:
        if now+1 <= day:
            if daylist[now][1] > maxlist[now+1]:
                maxlist[now] = daylist[now][1]
            else:
                maxlist[now] = maxlist[now+1]
        else:
            maxlist[now] = daylist[now][1]
    else:
        if now+1 <= day:
            maxlist[now] = maxlist[now+1]

print(maxlist[1])

'''
'''
해당 코드를 생각해보면 now+1이 인덱스 참조 오류가 뜰걸 생각하고
next+1이 인덱스 참조 오류가 뜰걸 생각해서 하나하나 예외처리를 했는데
만약 maxlist칸을 한칸 더만들고 0으로만 초기화하면 결과가 같다는것을 생각하지 못했다.
'''

import sys
input = sys.stdin.readline

day = int(input())

maxlist = [0 for _ in range(day+2)]
daylist = [[]]
for i in range(day):
    daylist.append(list(map(int,input().split())))

for i in range(day):
    now = day-i
    next = now + daylist[now][0]-1
    if next > day:
        maxlist[now] = maxlist[now+1]
    else:
        maxlist[now] = max(maxlist[now+1], daylist[now][1] + maxlist[next+1])

print(maxlist[1])