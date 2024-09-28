import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs(sr, sc):
    if visit[sr][sc] :
        return 0
    visit[sr][sc] = True
    Q = deque([(sr, sc)])
    if floor[sr][sc] == '|' :
        dr = 1
        dc = 0
    else :
        dr = 0
        dc = 1
    while Q :
        r, c = Q.popleft()
        nr = r + dr
        nc = c + dc
        if nr < N and nc < M and floor[r][c] == floor[nr][nc] :
            Q.append((nr, nc))
            visit[nr][nc] = True
    return 1

N, M = map(int, input().split())

floor = [input() for _ in range(N)]
visit = [[False]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        ans += bfs(i, j)
print(ans)