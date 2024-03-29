lst = []
for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))
lst.sort()
for i in lst:
    print(i[0], i[1])