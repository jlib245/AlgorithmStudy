import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [(0, 0)]+[tuple(map(int, input().split())) for _ in range(K)]

#dp[i][j] = i번째 과목까지 셌을 때 공부시간 j시간을 초과하지 않는 과목 중요도 최대 합
dp = [[0]*(N+1) for i in range(K+1)]
for i in range(K+1):
    for j in range(N+1):
        dp[i][j] = dp[i-1][j]
        w, t = lst[i]
        if j >= t :
            dp[i][j] = max(dp[i][j], dp[i-1][j-t]+w)

print(dp[K][N])