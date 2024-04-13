n = int(input())
l = [(0,0), (1,1)]

if n > 0:
    l.append((1,1))
    for i in range(3, n+1):
        b = l[i-1][0]*l[i-1][1] + l[i-2][0]*l[i-2][1]
        if b > 0:
            c = 1
        elif b == 0:
            c = 0
        else :
            c = -1
        l.append((c, abs(b)%1000000000))

elif n < 0:
    l.append((-1, 1))
    for i in range(3, -n+1):
        b = l[i-2][0]*l[i-2][1] - l[i-1][0] * l[i-1][1]
        if b > 0:
            c = 1
        elif b == 0:
            c = 0
        else :
            c = -1
        l.append((c, abs(b)%1000000000))

print(l[abs(n)][0])
print(l[abs(n)][1])