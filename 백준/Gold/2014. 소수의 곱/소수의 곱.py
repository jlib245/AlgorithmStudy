import sys, heapq
input = sys.stdin.readline

K, N = map(int, input().split())
prime = list(map(int, input().split()))
mul = []
limit = 2**31
for i in range(K):
    heapq.heappush(mul, prime[i])
i = 1
lst = []
prev = -1
while 1 :
    x = heapq.heappop(mul)
    if prev == x :
        continue
    if i == N :
        ans = x
        break 
    prev = x
    for mx in prime :
        nx = x * mx
        if nx < limit :
            heapq.heappush(mul, nx)
    i += 1
print(ans)