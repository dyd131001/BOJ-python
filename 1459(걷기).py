x, y, t1, t2 = map(int, input().split())

total = 0

rank = 0
if 2*t1 >= t2:
    rank = 2
else:
    rank = 1

if x > y:
    if rank == 1:
        total = (x+y)*t1
    else:
        if t1 > t2:
            if (x-y) % 2 == 0:
                total = (x-y)*t2 + y*t2
            else:
                total = (x-y-1)*t2+t1 + y*t2
        else:
            total = (x-y)*t1 + y*t2
else:
    if rank == 1:
        total = (y+x)*t1
    else:
        if t1 > t2:
            if (y-x) % 2 == 0:
                total = (y-x)*t2 + x*t2
            else:
                total = (y-x-1)*t2 + t1 + x*t2
        else:
            total = (y-x)*t1 + x*t2

print(total)
