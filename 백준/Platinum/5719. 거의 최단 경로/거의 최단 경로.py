import sys, heapq
input = sys.stdin.readline
from collections import deque

def dijkstra(S : int , D: int, second : int):
    H = [(0, S)]
    distance = [(INF, list())]*N
    distance[S] = (0, list())

    while H :
        d, x = heapq.heappop(H)

        if x == D :
            if not second :
                Q = deque([D])
                visit = [False]*N
                while Q :
                    x = Q.popleft()
                    for nx, EN in distance[x][1]:
                        edgeVisit[EN] = True
                        if not visit[nx]:
                            visit[nx] = True
                            Q.append(nx)
            return d

        for dd, nx, EN in edge[x] :
            if edgeVisit[EN] :
                continue

            nd = d + dd
            if distance[nx][0] > nd :
                distance[nx] = (nd, [(x, EN)])
                heapq.heappush(H, (nd, nx))
            elif distance[nx][0] == nd :
                distance[nx][1].append((x, EN))
    return -1

ans = []
while 1 :
    N, M = map(int, input().split())
    if N == M == 0 :
        break

    S, D = map(int, input().split())

    edge = [[] for _ in range(N)]
    cnt = 0
    for _ in range(M):
        U, V, P = map(int, input().split())
        edge[U].append((P, V, cnt))
        cnt += 1

    edgeVisit = [False]*M
    INF = 10**9
    dijkstra(S, D, 0)
    ans.append(dijkstra(S, D, 1))

print(*ans, sep='\n')