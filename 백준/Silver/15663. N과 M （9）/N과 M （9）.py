def f():
    if len(l) == M:
        res.add(tuple(l))
        return
    for i in range(len(num)):
        if not i in idxl:
            l.append(num[i])
            idxl.add(i)
            f()
            l.pop()
            idxl.remove(i)
    return

N, M = map(int, input().split())
num = list((map(int , input().split())))
l = []
idxl = set()
res = set()
f()
realres = list(res)
realres.sort()
for i in realres:
    print(*i)