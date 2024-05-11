s = input()
boom = input()
lst = []

for i in range(len(s)):
    lst += s[i]
    if len(lst) >= len(boom) :
        Boo = True
        for i in range(1, len(boom)+1):
            if lst[-i] != boom[-i]:
                Boo = False
                break
        if Boo :
            for _ in range(len(boom)):
                lst.pop()
if len(lst) :
    for i in lst:
        print(i, end='')
else :
    print("FRULA")