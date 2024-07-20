import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = []
for _ in range(N):
    m, v = map(int, input().split())
    jewel.append((m,v))
jewel.sort()
bag = []
for _ in range(K):
    c = int(input())
    bag.append(c)
bag.sort()
ans = 0
temp = []
for c in bag:
    while jewel and jewel[0][0] <= c:
        m, v = heapq.heappop(jewel)
        heapq.heappush(temp, -v)
    if temp :
        ans += -heapq.heappop(temp)
    elif not jewel:
        break
print(ans)        