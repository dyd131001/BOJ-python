import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
B, C = map(int, input().split())
count = n

for i in L:
    if i - B > 0:
        count += ((i - B) + (C-1)) // C


print(count)

'''
왜 count += ((i - B) + (C-1)) // C?
예시
9 // 3 = 3
10 // 3 = 3
11 // 3 = 3
여기서 i-b 가 9일때 3이어야하고
10 부터는 4가 되어야 함.
그래서 9 -> 11 로 옮기고 10 -> 12로 옮겨 원하는 결과가
나오도록 유도
'''