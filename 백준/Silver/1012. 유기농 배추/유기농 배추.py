import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(r, c) :
    Q = deque([(r, c)])
    while Q :
        r, c = Q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and mtrx[nr][nc] :
                mtrx[nr][nc] = False
                Q.append((nr, nc))
    
ans = []
T = int(input())
for _ in range(T) :
    M, N, K = map(int, input().split())
    mtrx = [[False]*M for _ in range(N)]
    for i in range(K):
        c, r = map(int, input().split())
        mtrx[r][c] = True
    cnt = 0
    for r in range(N) :
        for c in range(M) :
            if mtrx[r][c] :
                mtrx[r][c] = True
                bfs(r, c)
                cnt += 1
    ans.append(cnt)
print(*ans, sep='\n')