import sys
input = sys.stdin.readline

st = list(input().strip())

one = set(["*","/"])
two = set(["+","-"])
symbol = []
result = ''
for s in st:
    if s.isalpha():
        result +=s
    else:
        if s in one:
            while symbol and symbol[-1] in one:
                result+= symbol.pop()
            symbol.append(s)
        elif s in two:
            while symbol and symbol[-1] != '(':
                    result+= symbol.pop()
            symbol.append(s)
        else:
            if s == '(':
                symbol.append(s)
            if s == ')':
                while symbol and symbol[-1] != '(':
                    result+= symbol.pop()
                symbol.pop()

while symbol:
    result+= symbol.pop()
print(result)




