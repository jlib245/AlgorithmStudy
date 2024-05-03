import sys
inp = sys.stdin.read

N = int(input())

lst = [0]*10000001
s = ''
while 1:
    i = inp(1)
    if i == ' ' or i == '\n':
        a = int(s)
        if lst[a]:
            print(a)
            break
        else:
            lst[a] = 1
        s = ''
    else:
        s += i