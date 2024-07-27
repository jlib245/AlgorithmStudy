from collections import deque
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(start):
    Q = deque([start])
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and map[nr][nc] == '1':
                visit[nr][nc] = True
                cnt += 1
                Q.append((nr,nc))
    return cnt

N = int(input())

map = [input() for _ in range(N)]
visit = [[False]*N for _ in range(N)]
res = []
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            visit[r][c] = True
            if map[r][c] == '1':
                res.append(bfs((r,c)))
res.sort()

print(len(res))
print(*res,sep='\n')