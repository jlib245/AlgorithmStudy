'''
dp[i][j] = 마지막 자리의 수가 j인 길이 i의 계단수
'''
N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
nam = 10**9
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1]%nam+dp[i-1][j+1]%nam)%nam
res = 0
for i in range(10):
    res = (res + dp[N][i]%nam)%nam
print(res)