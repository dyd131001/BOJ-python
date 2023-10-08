import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def bfs(i,j):
    global count
    for dy, dx in d:
        ny = i + dy
        nx = j + dx
        if 0<= ny <row and 0<= nx <col:
            if M[ny][nx] !='X':
                if M[ny][nx] =='P':
                    count+=1
                M[ny][nx] = 'X'
                bfs(ny,nx)


row, col = map(int,input().split())
M = [list(map(str,input())) for _ in range(row)]
d = [(-1,0),(1,0),(0,1),(0,-1)]
count = 0
for i in range(row):
    for j in range(col):
        if M[i][j] == 'I':
            M[i][j] = 'X'
            bfs(i,j)
            if count == 0:
                print('TT')
            else:
                print(count)
            exit()
