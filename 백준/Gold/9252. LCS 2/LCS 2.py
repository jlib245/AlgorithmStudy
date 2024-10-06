A = ['']+list(input())
B = ['']+list(input())
'''
dp[i][j] = i행 j열까지 갔을 때 최댓값
'''
N = len(A)
M = len(B)
dp = [[0]*(M) for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if A[i] == B[j] :
            dp[i][j] = dp[i-1][j-1] +1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

cnt = dp[N-1][M-1]
print(cnt)
if cnt :
    res = ""
    i, j = N-1, M-1
    while i != 0 and j != 0:
        if dp[i][j] == dp[i][j-1]:
            j -= 1
        elif dp[i][j] == dp[i-1][j] :
            i -= 1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            res += B[j]
            i -= 1
            j -= 1
        else :
            j -= 1
    print(res[::-1])