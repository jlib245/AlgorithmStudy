import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(a, b, c):
    test = [lab[i][::] for i in range(N)]
    for r, c in (a, b, c) :
        test[r][c] = 1
    Q = deque(virus)
    while Q :
        r, c = Q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not test[nr][nc] :
                Q.append((nr, nc))
                test[nr][nc] = 2
    cnt = 0
    for i in range(N):
        for j in range(M) :
            if not test[i][j] :
                cnt += 1
    return cnt
        
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            empty.append((i,j))
        elif lab[i][j] == 2 :
            virus.append((i,j))

max_ = 0
for i in range(len(empty)):
    for j in range(i+1, len(empty)):
        for k in range(j+1, len(empty)):
            cnt = bfs(empty[i], empty[j], empty[k])
            if max_ < cnt :
                max_ = cnt
ans = max_
print(ans)