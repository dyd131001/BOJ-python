import sys
input = sys.stdin.readline

a = input()
b = input()

cnt = 0
n = 0

while n <= len(a)-len(b):
    if a[n:n + len(b)-1] == b[0:len(b)-1]:
        cnt += 1
        n += len(b)-1
    else:
        n += 1

print(cnt)


a = input()
b = input()
cnt = 0
n = 0
while n <= len(a) - len(b):
    if a[n:n + len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1
print(cnt)
