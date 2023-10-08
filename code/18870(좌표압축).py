import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

L = list(map(int,input().split()))
L2= sorted(list(set(L)))
size = len(L2)

def find(s,f,t):
    m = (s+f)//2
    if s <= f:
        if t == L2[m]:
            print(m,end=' ')
        elif L2[m] < t:
            find(m+1,f,t)
        else:
            find(s,m-1,t)


for num in L:
	find(0,size-1,num)
