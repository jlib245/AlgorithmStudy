import sys, heapq
input = sys.stdin.readline

def dijkstra(start, end):
    if start == end :
        return 0
    H = []
    distance = [INF]*(N+1)
    heapq.heappush(H, (0, start))
    distance[start] = 0
    while H:
        d, x = heapq.heappop(H)
        if distance[x] < d :
            continue
        if x == end :
            return distance[x]

        for nx, cost in edge[x] :
            if distance[nx] > d + cost :
                distance[nx] = d + cost
                heapq.heappush(H, (distance[nx], nx))
    

N, M, X = map(int, input().split())
INF = 10**9
edge = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b,c))

ans = 0
for i in range(1, N+1):
    res = dijkstra(i, X) + dijkstra(X, i)
    if ans < res:
        ans = res
print(ans)