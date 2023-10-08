S = input()
T = input()

tn = len(T)

while len(S) != len(T):
    if T[-1] == "A":
        T = T[:len(T)-1]

    else:
        temp = T[:len(T)-1]
        T = temp[::-1]



if T == S:
    print("1")
else:
    print("0")
