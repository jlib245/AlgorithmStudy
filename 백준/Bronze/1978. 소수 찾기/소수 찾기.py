N = int(input())
l = [0]*1001
l[1] = 1
for i in range(2, 1000):
    if l[i] == 0:
        a = 2
        while i*a <= 1000:
            l[i*a] = 1
            a += 1
nL = list(map(int, input().split()))
result = 0
for i in nL:
    if l[i] == 0:
        result += 1
print(result)

