import sys, heapq
input = sys.stdin.readline

N = int(input())

H = []
res = []
for _ in range(N):
    x = int(input())
    if x > 0 :
        heapq.heappush(H, -x)
    else :
        if H :
            res.append(-heapq.heappop(H))
        else :
            res.append(0)
            
print(*res, sep='\n')