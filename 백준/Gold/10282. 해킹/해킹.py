import sys, heapq
input = sys.stdin.readline

def bfs(c) :
    H = [(0, c)]
    visit = [False]*(n+1)
    max_ = 0
    cnt = 0
    while H:
        t, x = heapq.heappop(H)
        if visit[x] :
            continue
        visit[x] = True
        cnt += 1
        if max_ < t :
            max_ = t
        for nx, dt in edge[x]:
            nt = t + dt
            heapq.heappush(H, (nt, nx))
    return cnt, max_

T = int(input())
ans = []
for _ in range(T):
    n, d, c = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        edge[b].append((a, s))
    ans.append(tuple(bfs(c)))

for t in ans :
    print(*t)