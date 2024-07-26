import sys, heapq
input = sys.stdin.readline

def dijkstra(K) :
    H = [(0, K)]
    while H :
        w, x = heapq.heappop(H)
        if visit[x] :
            continue

        visit[x] = True
        SP[x] = w
        for dw, nx in edge[x] :
            nw = w + dw
            heapq.heappush(H, (nw, nx))
    return

V, E = map(int, input().split())

K = int(input())

edge = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    edge[u].append((w, v))

visit = [False]*(V+1)
SP = [0]*(V+1)

dijkstra(K)
for i in range(1, V+1) :
    if visit[i] :
        print(SP[i])
    else :
        print("INF")