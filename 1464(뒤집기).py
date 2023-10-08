L = input()
n = len(L)

temp = ''
s = 0
i = 0
j = 1
state = -1  # 0 오름차순 중 1 내림차순 중

for z in range(n-1):
    if L[i] > L[j]:
        if state == -1:
            state = 0  # DBA..
        if state == 1:  # ABC.. B
            if(L[0] >= L[j]):  # BCD..A , 이거나 ACD..A 이러면 뒤집어야지
                temp = L[s:j]
                temp = temp[::-1] + L[j:]
                L = temp
                state = 0
            else:  # ABC.. B 이때 뒤집으면 이상해짐
                state = 1
        i += 1
        j += 1
    elif L[i] < L[j]:  # A < B 1 >>< 1 CSA D
        if state == -1:
            state = 1  # ABD..
        if state == 0:
            temp = L[s:j]
            temp = temp[::-1] + L[j:]
            L = temp
            state = 1
        i += 1
        j += 1
    else:  # 같을땐 이전과 상태가 같다
        i += 1
        j += 1

if L[0] >= L[n-1]:
    L = L[::-1]

print(L)

####2

# 무조껀 제일 작은애를 만나면 뒤집어야됌
# 내가 제일 작은애면 다음턴에 뒤집어야됨

#temp = L[s:j]
#temp = temp[::-1] + L[j:]
#L = temp
L = input()
n = len(L)

temp = ''
s = 0
i = 0
j = 1
state = L[i]

for z in range(n-1):
    if state > L[j]:
        if state == L[0]:
            temp = L[s:j]
            temp = temp[::-1] + L[j:]
            L = temp
        state = L[j]
        i += 1
        j += 1
    elif state < L[j]:
        if L[0] == state:
            i += 1
            j += 1
        elif L[i] == state:
            temp = L[s:j]
            temp = temp[::-1] + L[j:]
            L = temp
            i += 1
            j += 1
    else:
        if L[0] == state:
            temp = L[s:j]
            temp = temp[::-1] + L[j:]
            L = temp
        i += 1
        j += 1

if L[0] >= L[n-1]:
    L = L[::-1]

print(L)
