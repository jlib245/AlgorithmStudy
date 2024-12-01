import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T) :
    N = int(input())
    coin = list(map(int,input().split()))
    M = int(input())
    
    # dp[i][j] 금액이 i를 만들기 위해 j번째 동전까지 사용하는 모든 방법의 수
    dp = [[0]*N for _ in range(M+1)]
    # 가장 작은 동전보다 작은 i는 의미 x
    s = coin[0]
    for i in range(s, M+1) :
        for j in range(N) :
            if i > coin[j] :
                if j == 0 :
                    dp[i][j] = dp[i-coin[j]][j]
                else :
                    dp[i][j] = dp[i][j-1] + dp[i-coin[j]][j]
            elif i == coin[j] :
                dp[i][j] = dp[i][j-1] + 1
            else :
                # 정렬되어 있기 때문에 이후는 의미x, 이전 인덱스 복사
                dp[i][j] = dp[i][j-1]
    
    res = dp[M][N-1]
    ans.append(res)

print(*ans, sep='\n')