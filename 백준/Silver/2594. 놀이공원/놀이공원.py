N = int(input())
lst = []
for i in range(N):
    a = tuple(map(int, input().split()))
    start = (a[0]//100, a[0]%100)
    end = (a[1]//100, a[1]%100)
    lst.append((start, end))
Time = [True]*24*60
for start, end in lst:
    for i in range(start[0]*60+start[1]-10, end[0]*60+end[1]+10):
        if 10*60 <= i < 24*60:
            Time[i] = False

res = 0
cnt = 0
for i in range(10*60, 22*60):
    if Time[i] :
        cnt += 1
    else:
        if res < cnt:
            res = cnt
        cnt = 0
if res < cnt:
    res = cnt
print(res)