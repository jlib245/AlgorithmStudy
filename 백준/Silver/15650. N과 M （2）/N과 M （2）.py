def f(n) :
    if len(l) == M:
        print(*l)
        return
    for i in range(n+1,N+1):
        l.append(i)
        f(i)
        l.pop()
    return

N, M = map(int, input().split())

num = [i for i in range(N+1)]
l = []
f(0)