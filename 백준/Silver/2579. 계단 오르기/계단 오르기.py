a = [0]
N = int(input())
for i in range(N):
    a.append(int(input()))
dp = [[0]*2 for i in range(N+1)]
dp[1] = [0, a[1]]
if N != 1:
    dp[2] = [a[2], a[1]+a[2]]
    for i in range(3, N+1):
        dp[i][0] = max(dp[i-2]) + a[i]
        dp[i][1] = dp[i-1][0] + a[i]
print(max(dp[N]))