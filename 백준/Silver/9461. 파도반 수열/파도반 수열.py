for _ in range(int(input())):
    N = int(input())
    P = [0,1,1,1,2,2,3,4,5,7,9]
    if N <= 10:
        print(P[N])
        continue
    for i in range(11, N+1):
        P.append(P[i-5] + P[i-1])
    print(P[N])