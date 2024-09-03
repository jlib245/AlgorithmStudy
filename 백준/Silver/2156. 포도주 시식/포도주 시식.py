import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n) :
    wine.append(int(input()))
if n == 1 :
    print(wine[0])
else :
    dp = [[0]*3 for _ in range(n)]
    dp[0] = [0, wine[0], 0]
    dp[1] = [wine[0], wine[1], wine[0]+wine[1]]
    # dp[i][0, 1, 2] i까지 마실 수 있을 때의 최댓값 (안마심, 1연속, 2연속)
    for i in range(2, n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + wine[i]
        dp[i][2] = dp[i-1][1] + wine[i]
    ans = max(dp[n-1])
    print(ans)