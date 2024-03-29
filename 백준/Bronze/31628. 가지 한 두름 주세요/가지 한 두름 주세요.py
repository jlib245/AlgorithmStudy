lst = []
for i in range(10):
    lst.append(input().split())
bk = 0
for i in range(10):
    if bk == 1:
        break
    n = 0
    previous = lst[i][0]
    now = lst[i][0]
    for j in range(1, 10):
        now = lst[i][j]
        if previous != now:
            break
        n += 1
        previous = now
    if n == 9:
        bk = 1
for i in range(10):
    if bk == 1:
        break
    n = 0
    previous = lst[0][i]
    now = lst[0][i]
    for j in range(1, 10):
        now = lst[j][i]
        if previous != now:
            break
        n += 1
        previous = now
    if n == 9:
        bk = 1
print(bk)