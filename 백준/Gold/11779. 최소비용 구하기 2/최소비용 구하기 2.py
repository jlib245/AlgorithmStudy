import sys, heapq
input = lambda : sys.stdin.readline()

def dijkstra(s, e):
    INF = 10**9
    cost = [INF]*(n+1)
    cost[s] = 0
    H = [(0, s, [s])]
    while H :
        d, x, r = heapq.heappop(H)
        if x == e :
            return (d, len(r), r)
        for nx, dd in edge[x] :
            nd = d + dd
            if cost[nx] > nd :
                cost[nx] = nd
                heapq.heappush(H, (nd, nx, r+[nx]))
n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((b, c))

s, e = map(int, input().split())
d, cnt, route = dijkstra(s, e)
print(d)
print(cnt)
print(*route)