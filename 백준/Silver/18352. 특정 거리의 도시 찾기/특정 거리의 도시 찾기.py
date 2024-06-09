from collections import deque
import sys
input = sys.stdin.readline

def bfs(X):
    Q = deque([(X, 0)])
    visit[X] = True
    res = []
    while Q:
        x, d = Q.popleft()
        if d == K:
            res.append(x)
            continue
        for nx in edge[x]:
            if not visit[nx]:
                visit[nx] = True
                Q.append((nx, d+1))
    return sorted(res)

N, M, K, X = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)

visit = [False for _ in range(N+1)]
ans = bfs(X)

if ans:
    print(*ans, sep='\n')
else:
    print(-1)