import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = [list(map(int,input().split()))for _ in range(n)]
r = [0,0]
def search(y,x,size):
    c = l[y][x]
    s = size//2
    for i in range(y,y+size):
        for j in range(x,x+size):
            if l[i][j] !=c:
                search(y,x,s)
                search(y+s,x,s)
                search(y,x+s,s)
                search(y+s,x+s,s)
                return
    r[c] += 1

search(0,0,n)
print(r[0])
print(r[1])