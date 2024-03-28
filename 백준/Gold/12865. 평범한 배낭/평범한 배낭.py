N, K = map(int, input().split())
a = []
for i in range(N):
    W, V = map(int, input().split())
    a.append((W,V))
dp = [[0]*(K+1)for i in range(N)]
for k in range(K+1):
    if k >= a[0][0]:
        dp[0][k] = a[0][1]
for n in range(1, N):
    for k in range(K+1):
        b = []
        if a[n][0] <= k:
            b.append(dp[n-1][k-a[n][0]] + a[n][1])
        b.append(dp[n-1][k])
        dp[n][k] = max(b)
print(dp[N-1][K])