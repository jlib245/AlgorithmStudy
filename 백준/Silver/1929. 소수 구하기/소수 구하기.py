M, N = map(int, input().split())
no = [0]*(N+1)
no[0], no[1] = [1, 1]
for i in range(2, N):
    a = 1
    while 1:
        a += 1
        b = i * a
        if b > N:
            break
        no[b] = 1
for i in range(M, N+1):
    if no[i] == 0:
        print(i)