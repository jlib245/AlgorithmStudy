def f(n):
    if len(l) == M:
        print(*l)
        return 
    for i in range(n,N+1):
        l.append(i)
        f(i)
        l.pop()
    return

N, M = map(int, input().split())

l = []
f(1)