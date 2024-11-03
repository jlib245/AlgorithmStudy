import sys
input = sys.stdin.readline

ans = []
T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1 :
        ans.append(1)
        continue
    elif n == 2 :
        ans.append(2)
        continue
    dp = [[0]*4 for _ in range(n+1)]
    dp[1] = [0, 1, 0, 0]
    dp[2] = [0, 1, 1, 0]
    dp[3] = [0, 1, 1, 1]
    for i in range(4, n+1):
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-2][1]+dp[i-2][2]
        dp[i][3] = sum(dp[i-3])
    res = sum(dp[n])
    ans.append(res)

print(*ans, sep='\n')