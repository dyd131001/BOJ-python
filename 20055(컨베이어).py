
'''
import sys
input = sys.stdin.readline
from collections import deque

# deque random aceess O(n)
# list del index 0 O(n)

def process(n, k, a):
    belt = a
    robots = [False for x in range(0, n)]
    zero = 0
    count = 0

    while True:
        belt, robots, zero = step(belt, robots, zero)
        count = count + 1

        if zero >= k:
            break

    return count


def step(b, r, z):
    # step 1
    b[:0] = b.pop(),
    r[:0] = r.pop(),
    # b.append(b.pop(0))
    # r.append(r.pop(0))

    # step 2-0
    if r[-1]:
        r[-1] = False

    # step 2
    for x in range(len(r)-1, 0, -1):
        if r[x] and b[x+1] > 0 and not r[x+1]:
            r[x+1], r[x] = r[x], r[x+1]
            b[x+1] = b[x+1] - 1

            if b[x+1] == 0:
                z = z + 1

    # step 2-2
    if r[-1]:
        r[-1] = False

    # step 3
    if b[0] > 0:
        r[0] = True
        b[0] = b[0] - 1

        if b[0] == 0:
            z = z + 1

    return b, r, z

a, b = map(int, input().split())
arr = list(map(int, input().split()))


t = process(a, b, arr)
print(t)
'''

'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
C = list(map(int,input().split()))
location = []
count0 = 0
result = 0

def move():
    for i , v in enumerate(location):
        location[i]+=1
    return [C[-1]] + C[:(2*n)-1]

def delete():
    if location:
        if location[0] == n-1:
            location.pop(0)

while True:
    result += 1
    C = move()
    delete()
    for i , v in enumerate(location):
        if C[v+1] >= 1:
            if i == 0:
                location[i] +=1
                C[v+1] -=1
                if C[v+1] == 0:
                    count0 +=1
                continue
            if location[i-1] != v+1:
                location[i] +=1
                C[v+1] -=1
                if C[v+1] == 0:
                    count0 +=1
    delete()

    if C[0] != 0:
        location.append(0)
        C[0] -= 1
        if C[0] == 0:
            count0 +=1
    if count0 >= k:
        break
    

print(result)
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
C = list(map(int,input().split()))

robots = [False for _ in range(n)]
count0 = 0
result = 0



def delete():
    if robots[-1] == True:
        robots[-1] = False

while True:
    result += 1
    C[:0] = [C.pop()]
    robots[:0] = [robots.pop()]

    delete()
    for x in range(n-1, 0, -1):
        if robots[x] == True:
            if C[x+1] >= 1:
                if not robots[x+1]:
                    robots[x+1], robots[x] = robots[x] , robots[x+1]
                    C[x+1] -=1
                    if C[x+1] == 0:
                        count0 +=1
    delete()

    if C[0] != 0:
        robots[0] = True
        C[0] -= 1
        if C[0] == 0:
            count0 +=1

    if count0 >= k:
        break

print(result)