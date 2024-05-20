K = int(input())

l = []
maxL = [0, 0]
for i in range(6):
    direction, distance = map(int, input().split())
    l.append((direction, distance))
    a = direction - 2
    if a <= 0:
        if maxL[0] < distance:
            maxL[0] = distance
    else:
        if maxL[1] < distance:
            maxL[1] = distance
A = maxL[0] * maxL[1]

clockDic = {1:3, 2:4, 3:2, 4:1}
clockDir = []
for i in range(6):
    if clockDic[l[i-1][0]] == l[i][0]:
        clockDir.append(True)
    else:
        clockDir.append(False)

for i in range(6):
    if clockDir[i] != clockDir[i-1] and clockDir[i] != clockDir[i-2]:
        minusA = l[i-1][1] * l[i][1]

A -= minusA
res = K * A
print(res)