import sys
input = sys.stdin.readline
from collections import deque

def bfs(s : int, e : int) -> int :
    Q = deque([(s, 0)])
    visit = [False]*(N+1)
    visit[s] = True
    while Q :
        x, d = Q.popleft()
        for nx, dd in lst[x] :
            if not visit[nx] :
                visit[nx] = True
                nd = d + dd
                Q.append((nx, nd))
                if nx == e :
                    return nd

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

ans = []
for _ in range(M):
    a, b = map(int, input().split())
    ans.append(bfs(a, b))

print(*ans, sep='\n')