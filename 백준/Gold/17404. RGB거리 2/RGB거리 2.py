import sys
input = sys.stdin.readline

'''
dp[i][j][k] 시작이 i번째 색이었을 때 j번째 집까지 칠했을 때 k번째 색을 칠한 경우 최소값
'''
N = int(input())

cost = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N-1)] for _ in range(3)]
trash = 1000000000000000
min_ = trash
for i in range(3):
    for c in range(3):
        if i == c :
            dp[i][0][c] = cost[0][c]
        else :
            dp[i][0][c] = trash
    for j in range(1, N-1):
        for k in range(3):
            dp[i][j][k] = min(dp[i][j-1][(k+1)%3], dp[i][j-1][(k+2)%3]) + cost[j][k]
    for c in range(3):
        if i != c :
            nx = min(dp[i][N-2][(c+1)%3], dp[i][N-2][(c+2)%3]) + cost[N-1][c]
            if min_ > nx :
                min_ = nx
                
print(min_)