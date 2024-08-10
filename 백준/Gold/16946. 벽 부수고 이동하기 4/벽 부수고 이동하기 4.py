from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def find(x : tuple) :
    r, c = x 
    while not (r == parent[x[0]][x[1]][0] and c == parent[x[0]][x[1]][1]) :
        r = parent[x[0]][x[1]][0]
        c = parent[x[0]][x[1]][1]
    return (r, c)

def union(x : tuple, y : tuple) :
    x = find(x)
    y = find(y)

    if x == y :
        return
    elif x < y :
        parent[y[0]][y[1]] = x
    else :
        parent[x[0]][x[1]] = y
    return

def bfs1(x : tuple) :
    Q = deque([x])
    if mtrx[x[0]][x[1]] or visit[x[0]][x[1]] :
        return
    visit[x[0]][x[1]] = True
    cnt = 1
    while Q :
        r, c = Q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not mtrx[nr][nc] and not visit[nr][nc] :
                visit[nr][nc] = True
                union(x, (nr,nc))
                Q.append((nr, nc))
                cnt += 1
    pr, pc = find(x)
    groupCnt[pr][pc] = cnt
    return

def bfs2(x : tuple):
    r, c = x
    if mtrx[r][c] == 0 :
        return 0
    set_ = set()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not mtrx[nr][nc] :
            set_.add(find((nr,nc)))
    res = 1
    for nr, nc in set_ :
        res += groupCnt[nr][nc]
    return res % 10

N, M = map(int, input().split())
mtrx = [list(map(int, input())) for _ in range(N)]
parent = [[(i, j) for j in range(M)]for i in range(N)]
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
visit = [[False]*M for _ in range(N)]
groupCnt = [[0]*M for _ in range(N)]
ans = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        bfs1((i,j))

for i in range(N):
    for j in range(M) :
        ans[i][j] = bfs2((i,j))

for row in ans :
    print(*row, sep='')