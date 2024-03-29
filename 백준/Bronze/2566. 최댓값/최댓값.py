lst = []
for i in range(9):
    lst.append(list(map(int, input().split())))
    maxL = max(lst[i])
    a = lst[i].index(maxL)
    lst[i].append((maxL, i+1, a+1))
mL = lst[0][9]
for i in range(1, 9):
    c = lst[i][9]
    if c[0] > mL[0]:
        mL = c
print(mL[0])
print(mL[1], mL[2])