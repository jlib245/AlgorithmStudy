import sys
input = sys.stdin.readline
from collections import deque

def bfs() :
    visit[1] = True
    Q = deque([(1, 0)])
    res = 0
    while Q :
        x,d = Q.popleft()
        for nx, dd in edge[x] :
            nd = d + dd
            if not visit[nx] :
                visit[nx] = True
                Q.append((nx, nd))
                if res < nd :
                    res = nd
    return res
N = int(input())

edge = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B, C = map(int, input().split())
    edge[A].append((B,C))
    edge[B].append((A,C))

visit = [False]*(N+1)
ans = bfs()

print(ans)