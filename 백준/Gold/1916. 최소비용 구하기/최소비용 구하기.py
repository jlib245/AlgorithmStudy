import sys, heapq
input = sys.stdin.readline

INF = 1e8

def dijkstra(start, end):
    H = [(0, start)]
    cost = [INF]*(N+1)
    cost[start] = 0
    while H :
        c, x = heapq.heappop(H)
        if x == end :
            return c
        if c > cost[x]:
            continue
        for nx, dc in edge[x] :
            nc = c + dc
            if cost[nx] > nc :
                cost[nx] = nc
                heapq.heappush(H, (nc, nx))

N = int(input())
M = int(input())

edge = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))

start, end = map(int, input().split())

ans = dijkstra(start, end)
print(ans)