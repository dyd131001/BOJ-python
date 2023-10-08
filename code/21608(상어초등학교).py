## 필요한 정보를 모두 모으고 정렬로 우선순위를 정하는 사고방식이 필요했다.
## 정렬을 통해 원하는 것을 찾을 수 있다.
## 매우 어렵게 느껴진다면 잘못된 접근법을 사용하고 있는 것이다.
## 맵에서 상하좌우를 사용하는 문제라면 꼭 방향을 정의할 것

''' 모범답안
n = int(input())
data = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            # 빈자리가 있다면
            if data[i][j] == 0:
                prefer, empty = 0, 0
                
                # 동서남북 방향 확인하여 
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                     
                    # 범위내에 있을 때
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 주위에 있다면 더해준다.
                        if data[nx][ny] in student[1:]:
                            prefer += 1
                            
                        # 빈자리가 있다면 더해준다.
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))
    # 정렬
    available.sort(key= lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] in students[data[i][j] - 1]:
                    count += 1

        answer += score[count]

print(answer)

'''

# 좋아하는 학생 수 , 비어있는 칸 높은순, 행, 열 낮은순

import sys
input = sys.stdin.readline

n = int(input())
seat = [[0 for _ in range(n)]for _ in range(n)]
students = [list(map(int,input().split())) for _ in range(n**2)]
d = [[-1, 0],[1, 0],[0, 1],[0, -1]]

for student in students:
    standard = []
    for row in range(n):
        for col in range(n):
            love = 0
            empty = 0
            if seat[col][row] == 0:
                for d1 in d:
                    nextx = row + d1[0]
                    nexty = col + d1[1]
                    if 0 <= nextx <= n-1 and 0 <= nexty <= n-1:
                        if seat[nexty][nextx] == 0:
                            empty +=1
                        elif seat[nexty][nextx] in student:
                            love +=1
                standard.append([row, col, love, empty])
    standard.sort(key= lambda x:(-x[2], -x[3], x[0],x[1]))
    seat[standard[0][1]][standard[0][0]] = student[0]

students.sort()
score = [0 , 1 , 10, 100, 1000]
result = 0
for row in range(n):
    for col in range(n):
        count = 0
        for d1 in d:
            nextx = row + d1[0]
            nexty = col + d1[1]
            if 0 <= nextx <= n-1 and 0 <= nexty <= n-1:
                if seat[nexty][nextx] in students[seat[col][row]-1]:
                    count +=1
        result += score[count]

print(result)

'''
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_area(class_, now_favorite):
  check_x = 0
  check_y = 0
  check_cnt = -1
  check_favorite_cnt = -1
  for x in range(N):
    for y in range(N):
      if not class_[x][y]:
        cnt = 0
        favorite_cnt = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < N and 0 <= ny < N:
            if not class_[nx][ny]:
              cnt += 1
            else:
              if class_[nx][ny] in now_favorite:
                favorite_cnt += 1
        if check_favorite_cnt < favorite_cnt:
          check_x = x
          check_y = y
          check_favorite_cnt = favorite_cnt
          check_cnt = cnt
        elif check_favorite_cnt == favorite_cnt:
          if check_cnt < cnt:
            check_x = x
            check_y = y
            check_cnt = cnt
  return check_x, check_y

def solution():
  class_ = [[[] for _ in range(N)] for _ in range(N)]
  for number in data:
    x, y = find_area(class_, data[number])
    class_[x][y] = number
  res = 0
  for x in range(N):
    for y in range(N):
      cnt = 0
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if class_[nx][ny] in data[class_[x][y]]:
            cnt += 1
      res += int(10**(cnt-1))
  return res

if __name__ == "__main__":
  N = int(input())
  data = dict()
  for _ in range(N**2):
    v = list(map(int,input().split()))
    data[v[0]] = v[1:]
  print(solution())
'''