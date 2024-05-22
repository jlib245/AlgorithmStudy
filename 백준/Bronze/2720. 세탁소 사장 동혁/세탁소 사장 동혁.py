T = int(input())
for _ in range(T):
    C = int(input())
    
    Q = C//25
    C %= 25

    D = C // 10
    C %= 10

    N = C // 5
    P = C % 5
    
    res = [Q, D, N, P]
    print(*res)