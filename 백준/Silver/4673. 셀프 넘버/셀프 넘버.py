r = [0]*10001
for i in range(10001):
    for j in str(i):
        i += int(j)
    if i <= 10000:
        r[i] = 1
for i in range(10001):
    if r[i] == 0:
        print(i)