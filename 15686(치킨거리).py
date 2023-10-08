
import sys
input = sys.stdin.readline
from itertools import combinations

n , m = map(int,input().split())
Map = [ list(map(int,input().split())) for _ in range(n)]
Home = []
Food = []

for i in range(n):
    for j in range(n):
        if Map[i][j] == 0:
            continue
        if Map[i][j] == 1:
            Home.append([i,j])
            continue
        if Map[i][j] ==2:
            Food.append([i,j])


print(min( sum( min( abs(x-x1) + abs(y-y1) for x, y in select) for x1, y1 in Home) for select in combinations(Food,m)))


'''
def gen_combinations(arr, n):
    result =[]

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        print("첫번째 for문 시작 i : " + str(i) + ' ' + str(n))
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n-1):
            print("두번째 for문 시작 i : " + str(i))
            print( str(elem) +' '+str(C))
            result.append([elem]+C)

    return result

print(gen_combinations([1, 2 ,3, 4, 5],2))
'''

import sys
input = sys.stdin.readline
from itertools import combinations

n , m = map(int,input().split())
Map = [ list(map(int,input().split())) for _ in range(n)]
Home = []
Home_index = 0
Food = []
Food_index = 0
sum_min = 999999

for i in range(n):
    for j in range(n):
        if Map[i][j] == 0:
            continue
        if Map[i][j] == 1:
            Home.append([i,j])
            Home_index+=1
            continue
        if Map[i][j] ==2:
            Food.append([i,j])
            Food_index+=1


index_list = [i for i in range(Food_index)]

for z in combinations(index_list, m):
    temp = 0
    for i in range(Home_index):
        min_cost = 999999
        for j in z:
            min_cost = min(min_cost,abs(Home[i][0] - Food[j][0]) + abs(Home[i][1] - Food[j][1]))
        temp += min_cost
        if (temp > sum_min):
            break
    if temp < sum_min:
        sum_min = temp


print(sum_min)

