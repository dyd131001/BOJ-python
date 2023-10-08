
n, m = map(int, input().split())
t = int(input())

m = m+t

ad = 0

if m >= 60:
    ad = m//60
    m = m % 60

n += ad
if n >= 24:
    n = n % 24

print(n, m)
