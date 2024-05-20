def f(i : int):
    if len(l) == M:
        print(*l)
        return
    for nx in range(i, len(num)):
        l.append(num[nx])
        f(nx)
        l.pop()
    return

N, M = map(int, input().split())
num = list(set(map(int, input().split())))
num.sort()
l = []
f(0)