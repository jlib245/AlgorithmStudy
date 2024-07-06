N, K = map(int, input().split())
lst = [0] + list(map(int, input().split()))
hap = [0]*(N+1)
for i in range(1, N+1):
    hap[i] = hap[i-1] + lst[i]
max_ = 0
res = []
for i in range(K, N+1):
    res.append(hap[i] - hap[i-K])
ans = max(res)
print(ans)