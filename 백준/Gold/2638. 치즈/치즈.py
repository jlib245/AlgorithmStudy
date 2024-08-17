import sys
input = lambda : sys.stdin.readline()
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def emptyBFS(r, c, t):
    visit[r][c] = 0
    cheeze[r][c] = 0
    emptyVisit[r][c] = True
    res = [(r, c, t)]
    Q = deque([(r, c)])
    while Q :
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not visit[nr][nc] and not emptyVisit[nr][nc]:
                emptyVisit[nr][nc] = True
                res.append((nr, nc, t))
                Q.append((nr, nc))
    return res
    
def bfs(empty):
    max_ = 0
    Q = deque(empty)
    while Q :
        r, c, t = Q.popleft()
        if max_ < t :
            max_ = t
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and cheeze[nr][nc]:
                visit[nr][nc] -= 1
                if visit[nr][nc] <= 2:
                    a = emptyBFS(nr, nc, t+1)
                    for tup in a :
                        Q.append(tup)
    return max_
N, M = map(int, input().split())
cheeze = []
visit = [[4]*M for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M) :
        if not row[j]:
            visit[i][j] = 0
    cheeze.append(row)
Q = deque([(0,0)])
empty = [(0,0,0)]
emptyVisit = [[False]*M for i in range(N)]
emptyVisit[0][0] = True
while Q :
    r, c = Q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not cheeze[nr][nc]and not emptyVisit[nr][nc]:
            emptyVisit[nr][nc] = True
            empty.append((nr, nc, 0))
            Q.append((nr, nc))
ans = bfs(empty)
print(ans)