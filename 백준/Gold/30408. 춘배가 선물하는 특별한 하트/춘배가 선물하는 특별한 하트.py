N, M = map(int, input().split())

set1 = set()
a = False
while N > M//2:
    set1.add(N)
    if N == 1:
        break
    if N % 2 == 1:
        a = True
    N //= 2

if a and M-1 in set1 or M in set1:
        print('YES')
        exit()
else:
    print('NO')