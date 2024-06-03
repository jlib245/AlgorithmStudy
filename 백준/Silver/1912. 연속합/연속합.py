n = int(input())
lst = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = lst[0]
for i in range(1, n):
    if dp[i-1] <= 0:
        dp[i] = lst[i]
    else:
        dp[i] = dp[i-1] + lst[i]

max_ = dp[0]
for i in range(1, n):
    if max_ < dp[i]:
        max_ = dp[i]

print(max_)