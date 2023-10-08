import sys
input = sys.stdin.readline
from collections import deque

def D(num):
    return (num*2)%10000
def S(num):
    if num-1 >= 0:
        return num-1
    else:
        return 9999
def L(num):
    d1 = num//1000
    d2 = (num//100)%10
    d3 = (num//10)%10
    d4 = num%10
    return ((d2 * 10 + d3) * 10 + d4) * 10 + d1
def R(num):
    d1 = num//1000
    d2 = (num//100)%10
    d3 = (num//10)%10
    d4 = num%10
    return ((d4 * 10 + d1) * 10 + d2) * 10 + d3

def F(num):
    return ((D(num),"D"),(S(num),"S"),(L(num),"L"),(R(num),"R"))
def bfs(n,t):
    visit = [False] * 10000
    DD= deque()
    DD.append((n,""))
    visit[n] = True
    while DD:
        Dn, Ds = DD.popleft()
        for i,fn in F(Dn):
            if not visit[i]:
                if i == t:
                    return Ds+fn
                visit[i] = True
                DD.append((i,Ds+fn))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 , s2 = map(int, input().split())
        print(bfs(s1,s2))
