T = int(input())

for _ in range(T):
    s = input()
    stck = []
    a = True
    for i in s:
        if i == '(':
            stck.append(i)
        elif stck != []:
            if stck[-1] == '(':
                stck.pop()
            else:
                print('NO')
                a = False
                break
        else:
            print('NO')
            a = False
            break
            
    if a == True and stck == []:
        print('YES')
    elif a == True:
        print('NO')
        