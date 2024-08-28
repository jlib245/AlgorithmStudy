import sys
input = sys.stdin.readline

N = int(input())

INF = 10**8
W = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not W[i][j] :
            W[i][j] = INF

# dp[i][j] = 이미 방문한 도시들의 집합 i, 현재 있는 도시 j, 지금까지의 최소비용
dp = [[INF]*N for _ in range(2**N)]
dp[1][0] = 0

MAX = 2**N-1
for i in range(1, MAX) :
    # j == 다음 목적지
    for j in range(1, N) :
        if not (i & (1 << j)) :
            min_ = INF
            # k == 원래 있던 곳
            for k in range(N) :
                if i & (1 << k) :
                    a = dp[i][k] + W[k][j]
                    if min_ > a :
                        min_ = a
            dp[i|(1 << j)][j] = min_

ans = INF
for i in range(1, N) : 
    if ans > dp[MAX][i] + W[i][0] :
        ans = dp[MAX][i] + W[i][0]

print(ans)