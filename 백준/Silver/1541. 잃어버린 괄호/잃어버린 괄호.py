l = input().split('-')
c = []
for i in l:
    c.append(sum(map(int, i.split('+'))))
result = c[0]
for i in range(1, len(c)):
    result -= c[i]
print(result)