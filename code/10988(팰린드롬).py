s = input()

n = int(len(s) / 2)
count = 0
for i in range(n):
    if s[i] != s[-i-1]:
        print(0)
        break
    else:
        count += 1
if count == n:
    print(1)
