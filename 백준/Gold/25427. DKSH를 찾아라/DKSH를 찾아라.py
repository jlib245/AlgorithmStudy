N = int(input())
S = list(input())
dp = [[0]*4 for _ in range(N)]
if S[0] == 'D' :
    dp[0] = [1, 0, 0, 0]
for i in range(1, N) :
    dp[i] = dp[i-1][::]
    if S[i] == 'D' :
        dp[i][0] += 1
    elif S[i] == 'K' :
        dp[i][1] += dp[i-1][0] 
    elif S[i] == 'S' :
        dp[i][2] += dp[i-1][1] 
    elif S[i] == 'H' :
        dp[i][3] += dp[i-1][2]

ans = dp[N-1][3]
print(ans)