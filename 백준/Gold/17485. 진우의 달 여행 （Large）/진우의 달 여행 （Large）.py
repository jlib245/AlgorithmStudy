'''
dp[i][j] = i행j열
dp[i][j][0] = 좌하단 이동해서 온 경우
dp[i][j][1] = 하단 이동해서 온 경우
dp[i][j][2] = 우하단 이동해서 온 경우
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int,input().split())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))
dp = [[[0]*3 for j in range(M)] for _ in range(N)]
for i in range(M):
    for j in range(3):
        dp[0][i][j] = lst[0][i]
for i in range(1, N):
    for j in range(M):
        plus = lst[i][j]
        if j != M-1:
            a = plus + min(dp[i-1][j+1][1],dp[i-1][j+1][2])
        else :
            a = 10**10
        if j != 0:
            b = plus + min(dp[i-1][j-1][0],dp[i-1][j-1][1])
        else:
            b = 10**10
        dp[i][j][0] = a
        dp[i][j][1] = plus + min(dp[i-1][j][0],dp[i-1][j][2])
        dp[i][j][2] = b
min_ = 10**10
for j in range(M):
    for k in range(3):
        if min_ > dp[N-1][j][k]:
            min_ = dp[N-1][j][k]
ans = min_
print(ans)