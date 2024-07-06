N = input()
if len(N) == 1:
    N = '0' + N
a = N
a = a[1] + str(int(a[0])+int(a[1]))[-1]
cnt = 1
while a != N:
    cnt += 1
    a = a[1] + str(int(a[0])+int(a[1]))[-1]
print(cnt)