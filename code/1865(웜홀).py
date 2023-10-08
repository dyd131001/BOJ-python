import sys
input = sys.stdin.readline
INF = 100000

def ford(start):
    d = [INF]*(n+1)
    d[start] = 0
    for i in range(n):
        for s,e,time in edge:
            if d[s] + time < d[e]:
                d[e] = d[s] + time
                if i == n-1:
                    return -1
                print(d)
    return 1


TC= int(input())

for _ in range(TC):
    n, m , w= map(int,input().split())
    edge = set()
    checknode = [False] * (n+1)
    for _ in range(m):
        s, e, time = map(int,input().split())
        edge.add((s,e,time))
        edge.add((e,s,time))

    for _ in range(w):
        s, e, time = map(int,input().split())
        edge.add((s,e,-time))


    print("NO" if ford(1) == 1 else "YES")

'''
import sys
input = sys.stdin.readline

TC= int(input())

for _ in range(TC):
    n, m , w= map(int,input().split())
    G = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e, time = map(int,input().split())
        G[s].append((e,time))
        G[e].append((s,time))

    for _ in range(w):
        s, e, time = map(int,input().split())
        G[s].append((e,-time))

    cost = [0] * (n+1)
    min_cost = [0] * (n+1)
    *arr, =  range(1,n+1)
    visit = set()
    min_index =[]
    rc = 1
    for _ in range(n):
        temp = tuple(arr)
        if temp in visit:
            break
        visit.add(temp)
        while arr:
            index = arr.pop()
            for st, value in G[index]:
                if cost[index] + value < min_cost[st]:
                    min_cost[st] = cost[index] + value
                    min_index.append(st)
        if min_index:
            for z in min_index:
                cost[z] = min_cost[z]
        else:
            break
        arr, min_index = min_index, arr

    if arr:
        rc = 0
    print("NO" if rc == 1 else "YES")



'''