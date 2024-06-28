import sys
input = lambda : sys.stdin.readline()

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))
dp = [[0]*N for _ in range(N)]
dp[0][0] = lst[0][0]
for i in range(1, N):
    dp[0][i] = dp[0][i-1] * 2 + lst[0][i]
    dp[i][0] = dp[i-1][0] * 2 + lst[i][0]
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])*2 + lst[i][j]

ans = dp[N-1][N-1]
print(ans)