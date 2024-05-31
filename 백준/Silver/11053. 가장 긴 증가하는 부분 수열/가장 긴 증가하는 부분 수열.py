N = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, len(lst)):
    max_ = 0
    for j in range(i):
        if lst[i] > lst[j] and max_ < dp[j]:
            max_ = dp[j]
    dp[i] = max_ + 1
print(max(dp))