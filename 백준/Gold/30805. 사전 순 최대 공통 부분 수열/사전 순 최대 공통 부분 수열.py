import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = [-1]+list(map(int, input().split()))
M = int(input())
B = [-1]+list(map(int, input().split()))

dp = [[tuple()]*(M+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        if A[i] == B[j]:
            base = dp[i-1][j-1]
            a = []
            lst = [dp[i][j], (A[i], )]
            for pi in range(len(base)):
                a.append(base[pi])
                lst.append(tuple(a+[A[i]]))
            dp[i][j] = max(lst)
print(len(dp[N][M]))
if len(dp[N][M]):
    print(*dp[N][M])