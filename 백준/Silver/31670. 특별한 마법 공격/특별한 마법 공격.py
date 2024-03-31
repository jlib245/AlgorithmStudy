N = int(input())
lst = [0] + list(map(int, input().split()))
dp = [[0]*2 for _ in range(N+1)]
if N == 1:
    print(0)
else:
    dp[1] = [0, lst[1]]
    dp[2] = [lst[1], lst[2]]
    for i in range(3, N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-2][1], dp[i-1][1]) + lst[i]
    print(min(dp[N]))