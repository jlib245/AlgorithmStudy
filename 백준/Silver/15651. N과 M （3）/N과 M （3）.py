def f(lst = list(), m = int(), n = int(), M = int()):
    if m == M:
        for i in lst:
            print(i, end = ' ')
        print('')
        return
    for i in range(1, n+1):
        lst.append(i)
        f(lst, m+1, n, M)
        lst.pop()
N, M = map(int, input().split())
f([], 0, N, M)