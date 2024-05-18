import sys
input = sys.stdin.readline

N = int(input())

wall = [[1]*(N+1)]
for _ in range(N):
    wall.append([1] + list(map(int, input().split())))

dp = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]
dp[1][2] = [1, 0, 0]
for i in range(1, N+1):
    for j in range(3, N+1):
        if not wall[i][j] :
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
            if not(wall[i-1][j] or wall[i][j-1]):
                dp[i][j][1] = sum(dp[i-1][j-1])

print(sum(dp[N][N]))

'''
dp[i][j] = i행 j열에 갈 수 있는 경우의 수
dp[i][j][0] = 가로 = dp[i][j-1][0] + dp[i][j-1][1]
dp[i][j][1] = 대각선 = sum(dp[i-1][j-1])
dp[i][j][2] = 세로 = dp[i-1][1] + dp[i-1][2]
'''