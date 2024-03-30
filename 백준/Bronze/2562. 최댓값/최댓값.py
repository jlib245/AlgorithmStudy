a = []
for i in range(9):
    a.append((int(input()), i))
a.sort()
print(a[-1][0], a[-1][1]+1)
    