N, K = map(int, input().split())

res = 1
for i in range(K):
    res = res * (N-i) // (i+1)

print(res)