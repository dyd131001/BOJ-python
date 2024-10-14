from collections import deque

N,L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]


def countRight(start):
    chunk = deque()
    chunk.append((board[start][0],1))
    for i in range(1, N):
        c = chunk.pop()
        if c[0] == board[start][i]:
            chunk.append((c[0],c[1]+1))
        else:
            chunk.append(c)
            chunk.append((board[start][i],1))
    return chunk

def countDown(start):
    chunk = deque()
    chunk.append((board[0][start],1))
    for i in range(1, N):
        c = chunk.pop()
        if c[0] == board[i][start]:
            chunk.append((c[0],c[1]+1))
        else:
            chunk.append(c)
            chunk.append((board[i][start],1))
    return chunk


def divide(L,chunk):
    newChunk = []
    while chunk:
        c = chunk.popleft()
        divideResult = c[1]//L
        if divideResult >= 1:
            for _ in range(c[1]//L):
                newChunk.append((c[0],L))
        else:
            newChunk.append((c[0],1))
    return newChunk

def union(L,chunk):
    if len(chunk) == 1:
        return True
    count = len(chunk)-1
    while True:
        if count <= 0:
            if len(chunk) == 1:
                return True
        if chunk[0][0]+1 == chunk[1][0]:
            if chunk[0][1] == L:
                    chunk.pop(0)
                    count-=1
            else:
                return False
        elif chunk[0][0] == chunk[1][0]+1:
            if chunk[1][1] == L:
                    chunk.pop(0)
                    newChunk = chunk.pop(0)
                    chunk.insert(0,(newChunk[0],0))
                    count-=1
            else:
                return False
        elif chunk[0][0] == chunk[1][0]:
                chunk.pop(0)
                count-=1
        else:
            return False

def simulation():
    result = 0
    for i in range(N):
        if union(L,divide(L,countRight(i))):
            result += 1
        if union(L,divide(L,countDown(i))):
            result += 1
    print(result)

simulation()
