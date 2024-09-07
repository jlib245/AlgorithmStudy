import sys, heapq
input = sys.stdin.readline

N = int(input())
H = []
ans = []
for _ in range(N) :
    x = int(input())
    if x :
        heapq.heappush(H, (abs(x), x//abs(x)))
    else :
        if H :
            a, b = heapq.heappop(H)
            ans.append(a*b)
        else :
            ans.append(0)
print(*ans, sep='\n')