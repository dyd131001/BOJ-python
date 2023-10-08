import sys
input = sys.stdin.readline

T = {}

n = int(input())

for _ in range(n):
    s,*string = list(map(str,input().split()))
    T[s] = string

def pre(start):
    if start != '.':
        print(start,end='')
        pre(T[start][0])
        pre(T[start][1])

def inorder(start):
    if start != '.':
        inorder(T[start][0])
        print(start,end='')
        inorder(T[start][1])

def po(start):
    if start != '.':
        po(T[start][0])
        po(T[start][1])
        print(start,end='')

pre('A')
print()
inorder('A')
print()
po('A')