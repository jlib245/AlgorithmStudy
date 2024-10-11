import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
'''
dp[i] : i칸으로 끝나는 최대 감소 부분 수열
'''
dp = [0]*N
dp[0] = 1
for i in range(1, N):
    max_ = 1
    for j in range(i):
        if A[i] < A[j] and max_ < dp[j] + 1 :
            max_ = dp[j] + 1
    dp[i] = max_
print(max(dp))