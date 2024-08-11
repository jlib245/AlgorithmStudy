from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def dijkstra(s, e):
    min_ = [INF]*(N+1)
    min_[s] = 0
    Q = deque([(s, 0)])
    while Q :
        x, d = Q.popleft()
        for nx, dd in edge[x] :
            nd = d + dd
            if min_[nx] > nd :
                min_[nx] = nd
                Q.append((nx, nd))
    return min_[e]
N, E = map(int ,input().split())
edge = [[] for _ in range(N+1)]
INF = 10**9
for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))
    edge[b].append((a, c))
v1, v2 = map(int, input().split())
v1v2 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2v1 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
ans = min(v1v2, v2v1)
if ans >= INF :
    print(-1)
else :
    print(ans)