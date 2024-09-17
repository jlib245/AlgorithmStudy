import sys, heapq
input = sys.stdin.readline

def bfs():
    if N == K :
        return 0
    H = [(0, N)]
    INF = 10**5+1
    visit = [INF]*INF
    while H :
        d, x = heapq.heappop(H)
        lst = [(d, 2*x), (d+1, x-1), (d+1, x+1)]
        for nd, nx in lst :
            if nx == K :
                return nd
            if 0 <= nx < INF and visit[nx] > nd :
                visit[nx] = nd
                heapq.heappush(H, (nd, nx))

N, K = map(int, input().split())
ans = bfs()
print(ans)