T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a = 1
    for i in range(N):
        a *= (M-i)
        a //= (i+1)
    print(a)
    