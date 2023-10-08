import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfsrg(i,j):
    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0<= ny <n and 0<= nx <n:
            if not visit[ny][nx]:
                if M[ny][nx] =='R' or M[ny][nx] =='G':
                    visit[ny][nx] = True
                    bfsrg(ny,nx)

def bfsr(i,j):
    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0<= ny <n and 0<= nx <n:
            if not visit[ny][nx]:
                if M[ny][nx] =='R':
                    visit[ny][nx] = True
                    bfsr(ny,nx)

def bfsg(i,j):
    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0<= ny <n and 0<= nx <n:
            if not visit[ny][nx]:
                if M[ny][nx] == 'G':
                    visit[ny][nx] = True
                    bfsg(ny,nx)

def bfsb(i,j):
    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0<= ny <n and 0<= nx <n:
            if not visit[ny][nx]:
                if M[ny][nx] == 'B':
                    visit[ny][nx] = True
                    bfsb(ny,nx)

if __name__ == "__main__":
    n = int(input())
    M = [list(map(str,input())) for _ in range(n)]
    d = [(-1,0),(1,0),(0,1),(0,-1)]

    count = 0
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and M[i][j] == 'B':
                visit[i][j] = True
                bfsb(i,j)
                count+=1
            elif not visit[i][j] and M[i][j] == 'G':
                visit[i][j] = True
                bfsg(i,j)
                count+=1
            elif not visit[i][j] and M[i][j] == 'R':
                visit[i][j] = True
                bfsr(i,j)
                count+=1
    print(count,end=' ')
    count = 0
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if M[i][j] == 'B':
                    visit[i][j] = True
                    bfsb(i,j)
                    count+=1
                else:
                    visit[i][j] = True
                    bfsrg(i,j)
                    count+=1
    print(count)