import sys
input = sys.stdin.readline

N, M = map(int, input().split())
val = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*2 for _ in range(M)] for _ in range(N)]
'''
dp[i][j][k]
    i : row
    j : column
    k : direction
        k == 0 : right
        k == 1 : left
'''
dp[0][0] = [val[0][0], val[0][0]]
impossible = -10**5
for j in range(1, M):
    dp[0][j][0] = dp[0][j-1][0] + val[0][j]
    dp[0][j][1] = impossible
for i in range(1, N):
    # direction == right
    for j in range(M):
        if j == 0 :
            dp[i][j][0] = max(dp[i-1][j]) + val[i][j]
        else :
            dp[i][j][0] = max(max(dp[i-1][j]), dp[i][j-1][0]) + val[i][j]
    # direction == left
    for j in range(M-1, -1, -1) :
        if j == M-1 :
            dp[i][j][1] = max(dp[i-1][j]) + val[i][j]
        else :
            dp[i][j][1] = max(max(dp[i-1][j]), dp[i][j+1][1]) + val[i][j]

ans = max(dp[N-1][M-1])
print(ans)