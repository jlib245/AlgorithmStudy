lst = []
for i in range(int(input())):
    lst.append(tuple(map(int, input().split())))
lst.sort()
for i in lst:
    for j in range(2):
        print(i[j], end=' ')
    print('')