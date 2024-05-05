from collections import deque
import sys
inp = sys.stdin.readline

T = int(inp())

for _ in range(T):
    p = inp().rstrip()
    n = int(inp())
    s = inp().rstrip()
    if n == 0:
        q = deque([])
    elif n == 1:
        q = deque([int(s[1:-1])])
    else:
        q = deque(list(map(int, s[1:-1].split(','))))
    
    TF = True
    rev = 2
    for i in p:
        if i == 'R':
            rev += 1
        else:
            if q:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                TF = False
                break
    if rev % 2 == 1:
        q = deque(reversed(q))

    if TF and q:
        print(f'[{q[0]}', end='')
        for i in range(1, len(q)):
            print(f',{q[i]}', end='')
        print(']')
    elif TF:
        print('[]')
    else:
        print('error')