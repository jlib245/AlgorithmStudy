A = input()
B = input()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
max_ = 0
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            if max_ < dp[i][j] :
                max_ = dp[i][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
ans = dp[len(A)][len(B)]
print(ans)