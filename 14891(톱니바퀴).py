import sys
input = sys.stdin.readline

def switch(s, d):
    if d == 1:
        IL[s-1] -= 1
        if IL[s-1] == -1:
            IL[s-1] = 7
    else:
        IL[s-1] = (IL[s-1]+1) % 8

L = [input().split() for _ in range(4)]
IL = [0 for _ in range(4)]
S = [0 for _ in range(3) ]

n = int(input())
W = [ list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(3):
        if L[j][0][(IL[j]+2)%8] == L[j+1][0][(IL[j+1]-2)]:
            S[j] = 1
        else:
            S[j] = 0

    if W[i][0] == 1:
        switch(1,W[i][1])
        if S[0] == 0:
            switch(2,W[i][1]*(-1))
            if S[1] == 0:
                switch(3,W[i][1])
                if S[2] == 0:
                    switch(4,W[i][1]*(-1))
    if W[i][0] == 2:
        switch(2,W[i][1])
        if S[0] == 0:
            switch(1,W[i][1]*(-1))
        if S[1] == 0:
            switch(3,W[i][1]*(-1))
            if S[2] == 0:
                switch(4,W[i][1])

    if W[i][0] == 3:
        switch(3,W[i][1])
        if S[2] == 0:
            switch(4,W[i][1]*(-1))
        if S[1] == 0:
            switch(2,W[i][1]*(-1))
            if S[0] == 0:
                switch(1,W[i][1])

    if W[i][0] == 4:
        switch(4,W[i][1])
        if S[2] == 0:
            switch(3,W[i][1]*(-1))
            if S[1] == 0:
                switch(2,W[i][1])
                if S[0] == 0:
                    switch(1,W[i][1]*(-1))

total = 0
if L[0][0][IL[0]] == '1':
    total +=1
if L[1][0][IL[1]] == '1':
    total +=2
if L[2][0][IL[2]] == '1':
    total +=4
if L[3][0][IL[3]] == '1':
    total +=8

print(total)

'''
퍼팩트 풀이
배워야할거 배열 인덱싱, 카피 반복문 범위, 배열 더하기
<= <
import sys
input = sys.stdin.readline


west = 6
east = 2

wheel = [list(map(int, input().strip())) for _ in range(4)]

k = int(input())

def move(idx, direction):
    if(direction == 1):
        wheelCopy[idx] = [wheel[idx][7]] + wheel[idx][:7]
    elif(direction == -1):
        wheelCopy[idx] = wheel[idx][1:] + [wheel[idx][0]]
    

for _ in range(k):
    num, direction = map(int, input().split())

    num -= 1 # index를 [1-4]에서 [0-3]으로 조정

    wheelCopy = [wheel[i][:] for i in range(4)]

    for i in range(num-1, -1, -1):
        if(wheel[i][east] != wheel[i+1][west]):
            move(i, direction * (-1) ** (num-1-i+1))
        else:
            break

    for i in range(num+1, 4):
        if(wheel[i][west] != wheel[i-1][east]):
            move(i, direction * (-1) ** (i-num))
        else:
            break

    move(num, direction)

    wheel = [wheelCopy[i][:] for i in range(4)]

print(sum([wheel[i][0] * (2 ** i) for i in range(4)]))

'''