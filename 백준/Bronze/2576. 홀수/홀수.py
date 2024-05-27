res = 0
min_ = 100
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        res += n
        if min_ > n:
            min_ = n
if res == 0:
    print(-1)
else:
    print(res)
    print(min_)