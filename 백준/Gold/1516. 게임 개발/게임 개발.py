from collections import deque
import sys
input = sys.stdin.readline


def update(i):
    if not cal[i] :
        if not lst[i]:
            cal[i] = True
            return time[i]
        else:
            preMax = 0
            for nx in lst[i]:
                a = update(nx)
                if preMax < a:
                    preMax = a
            cal[i] = True
            time[i] += preMax
            return time[i]
    else:
        return time[i]


N = int(input())

lst = [[] for _ in range(N+1)]

time = [0 for _ in range(N+1)]
cal = [False for _ in range(N+1)]
for i in range(1, N+1):
    q = deque(list(map(int, input().split())))
    t = q.popleft()
    time[i] = t
    while 1:
        pre = q.popleft()
        if pre == -1:
            break
        lst[i].append(pre)

for i in range(1, N+1):
    update(i)

for i in range(1, N+1):
    print(time[i])