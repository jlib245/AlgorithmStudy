import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
'''
dp[i] : i칸으로 끝나는 최대 증가 부분 수열
'''
dp = [0]*N
prev = [-1]*N
dp[0] = 1
for i in range(1, N):
    max_ = 1
    for j in range(i):
        if A[i] > A[j] and max_ < dp[j] + 1 :
            max_ = dp[j] + 1
            prev[i] = j
    dp[i] = max_

maxPoint = 0
cnt = 0
for i in range(N):
    if cnt < dp[i] :
        cnt = dp[i]
        maxPoint = i

ans = [0]*cnt

print(cnt)
while cnt :
    cnt -= 1
    ans[cnt] = A[maxPoint]
    maxPoint = prev[maxPoint]
print(*ans)