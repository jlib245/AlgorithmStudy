from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(start):
    Q = deque([start])
    nv = [[True]*M for i in range(N)]
    onePiece = []
    while Q:
        r, c= Q.popleft()
        nv[r][c] = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and lst[nr][nc] == 'L': 
                visit[nr][nc] = True
                Q.append((nr,nc))
                onePiece.append((nr,nc, 0))
    max_ = 0
    for i in onePiece:
        sr, sc, sd = i
        re = deque([i])
        cv = []
        for i in nv:
            cv.append(i[::])
        cv[sr][sc] = True
        while re:
            r, c, d = re.popleft()
            if max_ < d:
                max_ = d
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <=nc < M and not cv[nr][nc] and lst[nr][nc] == 'L':
                    cv[nr][nc] = True
                    re.append((nr,nc,d+1))
    return max_

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(input())
visit = [[False]*M for _ in range(N)]
max_ = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j] and lst[i][j] == 'L':
            visit[i][j] = True
            a = bfs((i,j))
            if max_ < a:
                max_ = a
print(max_)