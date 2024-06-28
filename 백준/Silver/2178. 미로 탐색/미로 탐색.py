import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(N, M):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    Q = deque([(0,0,1)])
    visit[0][0] = True
    while Q:
        r, c, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == N-1 and nc == M-1:
                return d+1
            if 0 <= nr < N and 0<= nc < M and matrx[nr][nc] and not visit[nr][nc] :
                visit[nr][nc] = True
                Q.append((nr,nc,d+1))


N, M = map(int, input().split())
visit = [[False]*M for _ in range(N)]
matrx = [list(map(int, list(input()))) for _ in range(N)]

ans = bfs(N, M)
print(ans)