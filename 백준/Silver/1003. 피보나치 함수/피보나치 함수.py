T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * (n+1)
    dp[0] = (1, 0)
    if n != 0:
        dp[1] = (0, 1)
    if n > 1:
        for i in range(2, n+1):
            dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])
    print(dp[n][0], dp[n][1])