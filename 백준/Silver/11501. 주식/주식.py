import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    nxt = 0
    res = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if price[i] < nxt :
            cnt += 1
            res += nxt - price[i]
        elif price[i] > nxt :
            cnt = 0
            nxt = price[i]
    ans.append(res)
print(*ans, sep='\n')