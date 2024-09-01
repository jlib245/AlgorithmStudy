import sys, heapq
input = sys.stdin.readline

def bfs():
    INF = 10**6
    H = [(0, 0)]
    visit = [INF]*N
    visit[0] = True
    while H :
        d, x = heapq.heappop(H)
        if x == N-1 :
            return d
        
        if line[x] == -1 :
            nx = x + 1
            nd = d + 1
            if nd < visit[nx] :
                visit[nx] = nd
                heapq.heappush(H, (nd, nx))
        else :
            portalColor, destination = portal[line[x]]
            nx = destination
            nd = d
            if nd < visit[nx] :
                visit[nx] = nd
                heapq.heappush(H, (nd, nx))
            if portalColor :
                nx = x + 1
                nd = d + 1
                if nd < visit[nx] :
                    visit[nx] = nd
                    heapq.heappush(H, (nd, nx))
    return -1

N, C = map(int, input().split())
line = [-1]*N
portal = []
for i in range(C) :
    t, a, b = map(int, input().split())
    line[a] = len(portal)
    portal.append((t, b))
print(bfs())