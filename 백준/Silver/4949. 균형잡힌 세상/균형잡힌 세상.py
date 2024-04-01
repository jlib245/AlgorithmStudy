s = ""
while 1:
    a = input()
    if a == ".":
        break
    s += a
l = s.split('.')
l.pop()
for i in l:
    stck = []
    balance = True
    for j in i:
        if j == '(' or j == '[':
            stck.append(j)
        elif j == ']':
            if len(stck) == 0 or len(stck) != 0 and stck.pop() != '[':
                balance = False
                break

        elif j == ')':
            if len(stck) == 0 or len(stck) != 0 and stck.pop() != '(':
                balance = False
                break

    if len(stck) != 0:
        balance = False

    if balance == True:
        print('yes')
    else :
        print('no')