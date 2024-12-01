import sys, heapq
input = sys.stdin.readline

def dijkstra(s, e) :
    INF = 10**9
    visit = [0]*(N+1)
    H = [(-INF, s)]
    while H :
        d, x = heapq.heappop(H)
        d = -d

        if x == e :
            return d

        for nx, cd in edge[x] :
            nd = min(d, cd)
            if visit[nx] < nd :
                visit[nx] = nd
                heapq.heappush(H, (-nd, nx))    

N, M = map(int, input().split())

edge = [[] for _ in range(1+N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A].append((B,C))
    edge[B].append((A,C))

s, e = map(int, input().split())

ans = dijkstra(s,e)
print(ans)