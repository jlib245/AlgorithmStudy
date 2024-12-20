import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N += 1
M += 1

K = int(input())

dp = [[0]*M for _ in range(N)]
able = [[[1]*2 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    if a != c :
        able[min(a, c)][b][0] = 0
    else :
        able[a][min(b, d)][1] = 0

dp[0][0] = 1
for j in range(1, M):
    dp[0][j] = dp[0][j-1] * able[0][j-1][1]
for i in range(1, N):
    dp[i][0] = dp[i-1][0] * able[i-1][0][0]
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j]*able[i-1][j][0] + dp[i][j-1]*able[i][j-1][1]

ans = dp[N-1][M-1]
print(ans)