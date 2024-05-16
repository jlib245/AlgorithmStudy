import sys
input = sys.stdin.readline

N = int(input())

cost = [[] for _ in range(N+1)]
for i in range(1, N+1):
    cost[i] = (list(map(int,input().split())))

dp = [[0]*3 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N]))