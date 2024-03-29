import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    q = input().split()
    if q[0] == 'push':
        lst.append(int(q[1]))
    elif q[0] == 'pop':
        if lst != []:
            print(lst[0])
            lst = lst[1:]
        else:
            print(-1)
    elif q[0] == 'size':
        print(len(lst))
    elif q[0] == 'empty':
        if lst == []:
            print(1)
        else:
            print(0)
    elif q[0] == 'back':
        if lst == []:
            print(-1)
        else:
            print(lst[-1])
    else:
        if lst == []:
            print(-1)
        else:
            print(lst[0])