n = int(input())
dp = [[],[1,0],[1,2]]+[[0]*2 for _ in range(n-2)]
for i in range(3, n+1):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = sum(dp[i-2])*2
print(sum(dp[n])%10007)