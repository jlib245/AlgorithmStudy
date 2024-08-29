import sys, heapq
input = sys.stdin.readline

n = int(input())
ho = [sorted((map(int, input().split()))) for _ in range(n)]
d = int(input())

H = []
L = []
for h, o in ho :
    heapq.heappush(L, (h-d, h))
    heapq.heappush(L, (h, h+d))
    heapq.heappush(L, (o-d, o))
    heapq.heappush(L, (o, o+d))
    heapq.heappush(H, (o, h))

ans = 0
cnt = 0
put = []
for i in range(len(L)) :
    x, y = heapq.heappop(L)
    while put :
        h, o = heapq.heappop(put)
        if x <= h :
            heapq.heappush(put, (h, o))
            break
        else :
            cnt -= 1
    while H:
        o, h = heapq.heappop(H)
        if o > y :
            heapq.heappush(H, (o, h))
            break 
        if x <= h :
            heapq.heappush(put, (h, o))
            cnt += 1
    if ans < cnt :
        ans = cnt
print(ans)