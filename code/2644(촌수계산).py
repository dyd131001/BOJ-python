from collections import deque

n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
L = [[] for _ in range(n+1)]
visit = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)


d = deque()
count = 0


def bfs(t1, t2):
    count = 0
    visit[t1] = True
    d.append([t1, 0])
    while d:
        t1l = d.popleft()
        for s2 in L[t1l[0]]:
            if s2 == t2:
                visit[s2] = True
                count = t1l[1]+1
                break
            if visit[s2] == False:
                visit[s2] = True
                d.append([s2, t1l[1]+1])

    return count


count = bfs(t1, t2)

if visit[t2] == True:
    print(count)
else:
    print('-1')