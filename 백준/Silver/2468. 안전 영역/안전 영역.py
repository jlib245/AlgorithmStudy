import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(rc : tuple, h : int):
    r,c = rc
    if matrix[r][c] <= h or visit[r][c] :
        return 0
    Q = deque([rc])
    visit[r][c] = True
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] > h and not visit[nr][nc] :
                visit[nr][nc] = True
                Q.append((nr,nc))
    return 1
    
def ifh(n):
    global visit
    visit = [[False]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            cnt += bfs((r,c), n)
    return cnt

def result():
    max_ = 0
    for i in range(101):
        casei = ifh(i)
        if max_ < casei:
            max_ = casei
    return max_

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

res = result()
print(res)