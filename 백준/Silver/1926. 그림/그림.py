import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(start):
    Q = deque([start])
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and lst[nr][nc] :
                visit[nr][nc] = True
                Q.append((nr, nc))
                cnt += 1
    return cnt

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
sketchCnt = 0
sketchMax = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and lst[i][j] :
            visit[i][j] = True
            cnt = bfs((i, j))
            if sketchMax < cnt :
                sketchMax = cnt
            sketchCnt += 1

print(sketchCnt)
print(sketchMax)