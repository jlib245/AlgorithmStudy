def f(a):
    res = [None]*2
    res[0] = a[1]
    res[1] = a[0]
    return res
a = list()
for i in range(int(input())):
    x, y = map(int, input().split())
    a.append((x,y))
a.sort(key = f)
for i in range(len(a)):
    print(a[i][0],a[i][1])
    