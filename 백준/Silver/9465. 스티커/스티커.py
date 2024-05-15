import sys
input = sys.stdin.readline

T = int(input())

res = []
for t in range(T):
    n = int(input())

    lst = [[]]
    for i in range(2):
        lst.append([0]+list(map(int, input().split())))
        
    if n == 1:
        res.append(max(lst[1][1], lst[2][1]))
        continue
        
    dp = [[0]*3 for _ in range(n+1)]
    dp[1] = [0,lst[1][1],lst[2][1]]
    for i in range(2, n+1):
        dp[i][1] = max(dp[i-1][2], dp[i-2][2]) + lst[1][i]
        dp[i][2] = max(dp[i-1][1], dp[i-2][1]) + lst[2][i]

    res.append(max(dp[n]))

print(*res, sep='\n')