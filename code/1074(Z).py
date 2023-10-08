## 편하게 좌표를 옮겨본다.n의 크기 , 최대값을 누적해가며 계산해보자.
import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())
check = 0

def search(n,s,f,min,max):
    global check
    if check == 1:
        return
    if n == 1:
        if r ==s[0] and c == s[1]:
            print(min)
            check =1
        elif r ==s[0] and c == s[1]+1:
            print(min+1)
            check =1
        elif r ==s[0]+1 and c == s[1]:
            print(min+2)
            check =1
        else:
            print(min+3)
            check =1

    else:
        num = 2**(n-1) * 2**(n-1)
        if s[0]<= r <= (s[0] + f[0])//2  and s[1]<= c <= (s[1] + f[1])//2  :
            search(n-1,(s[0],s[1]), ((s[0] + f[0])//2 ,(s[1] + f[1])//2), min , min+num-1)
        elif s[0]<= r <= (s[0] + f[0])//2 and (s[1] + f[1])//2 +1 <= c <= f[1]:
            search(n-1,(s[0],(s[1] + f[1])//2+1),((s[0] + f[0])//2,f[1]), min +num, min+num*2-1)
        elif (s[0] + f[0])//2 +1 <= r <=  f[0] and s[1]<= c <= (s[1] + f[1])//2:
            search(n-1,((s[0] + f[0])//2+1 ,s[1]),(f[0],(s[1] + f[1])//2),min+num*2,min+num*3-1)
        elif (s[0] + f[0])//2 +1 <= r <= f[0] and (s[1] + f[1])//2 +1 <= c <= f[1]:
            search(n-1,((s[0] + f[0])//2+1,(s[1] + f[1])//2+1),(f[0],f[1]),min+num*3,min+num*4-1)


search(N,(0,0),(2**N-1,2**N-1),0,(2**N) * (2**N)-1)


'''
import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())

M = [[0, 1],[2 ,3]]
result = 0
while True:
    if N == 1:
        result += M[r][c]
        break
    else:
        maxv = 2**(N-1) * 2**(N-1)
        s_index = 2**(N-1)
        if 0 <= r < s_index and 0 <= c < s_index:
            result = result
        elif 0 <= r < s_index and s_index <= c < s_index*2: #2
            c-= s_index
            result += maxv
        elif s_index <= r < s_index*2 and 0 <= c < s_index : #3
            r-= s_index
            result += maxv*2
        else:
            c-= s_index
            r-= s_index
            result += maxv*3
        N-=1

print(result)
'''