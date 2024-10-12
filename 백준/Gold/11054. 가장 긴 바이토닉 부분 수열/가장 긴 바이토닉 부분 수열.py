N = int(input())
S = list(map(int, input().split()))

# dp[i][j] : i 인덱스까지 갔을 때 S[i]로 끝나는 증가하는 : 0, 증가했다감소하는 : 1 부분수열의 최대 길이
dp = [[0]*2 for _ in range(N)]
dp[0] = [1, 1]
ans = 1
for i in range(1, N) :
    max_ = [1, 1]
    for j in range(i) :
        if S[i] > S[j] :
            if max_[0] < dp[j][0] + 1:
                max_[0] = dp[j][0] + 1
        elif S[i] < S[j] :
            if max_[1] < max(dp[j]) + 1 :
                max_[1] = max(dp[j]) + 1
    if ans < max(max_) :
        ans = max(max_)
    dp[i] = max_
print(ans)