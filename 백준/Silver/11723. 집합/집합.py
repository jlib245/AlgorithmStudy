import sys
input = sys.stdin.readline
S = set()
for i in range(int(input())):
    q = input().rstrip().split()
    z = q[0]
    if z == 'add':
        S.add(int(q[1]))
    elif z == 'remove':
        S.discard(int(q[1]))
    elif z == 'check':
        a = int(q[1])
        if a in S:
            print(1)
        else:
            print(0)
    elif z == 'toggle':
        a = int(q[1])
        if a in S:
            S.remove(a)
        else:
            S.add(a)
    elif z == 'all':
        S = set(range(1, 21))
    else:
        S = set()