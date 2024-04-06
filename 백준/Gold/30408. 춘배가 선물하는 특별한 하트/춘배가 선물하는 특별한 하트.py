N, M = map(int, input().split())

a = False
set1 = set()
set2 = set()
while N >= M//2:
    set1.add(N)
    if N == 1:
        break
    if N % 2 == 1:
        a = True
        set2.add(N+1)
    N //= 2

if a and M-1 in set1:
        print('YES')
        exit()
elif M in set1:
        print('YES')
        exit()
else:
    print('NO')