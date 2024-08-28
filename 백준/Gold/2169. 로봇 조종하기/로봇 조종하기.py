import sys
input = sys.stdin.readline

N, M = map(int, input().split())
val = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

dp[0][0] = val[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + val[0][j]

for i in range(1, N):    
    right = [0]*M
    right[0] = dp[i-1][0] + val[i][0]
    for j in range(1, M) :
        right[j] = max(dp[i-1][j], right[j-1]) + val[i][j]
    
    left = [0]*M
    left[-1] = dp[i-1][-1] + val[i][-1]
    for j in range(M-2, -1, -1) :
        left[j] = max(dp[i-1][j], left[j+1]) + val[i][j]
    
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

ans = dp[-1][-1]
print(ans)