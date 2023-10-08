import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

def bfs(s):
    find =defaultdict(int)
    un, dn = map(int,input().split())
    for _ in range(un + dn):
        st , f = map(int,input().split())
        find[st] = f
    L = deque()
    L.append((s,0))
    visit = [False] * (101)
    visit[s] = True
    while L:
        x,cnt = L.popleft()
        for i in range(1,7):
            nx = x + i
            if nx <= 100:
                if not visit[nx]:
                    visit[nx] = True
                    if find[nx] and not visit[find[nx]]:
                        visit[find[nx]] = True
                        L.append((find[nx],cnt+1))
                    elif not find[nx]:
                        L.append((nx,cnt+1))
                        if nx == 100:
                            return cnt+1

if __name__ == "__main__":
    print(bfs(1))