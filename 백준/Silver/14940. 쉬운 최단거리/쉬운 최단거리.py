from collections import deque
import sys
input = sys.stdin.readline


def bfs(destination : tuple):
    Q = deque([destination])
    dr = (-1, 1 ,0, 0)
    dc = (0, 0, -1, 1)

    while Q:
        r, c, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nd = d + 1
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and mat[nr][nc]:
                mat[nr][nc] = nd
                visit[nr][nc] = True
                Q.append((nr,nc,nd))

                


n, m = map(int, input().split())
mat = []
visit = [[False]*m for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    
    for j in range(m):
        if a[j] == 2:
            destination = (i, j, 0)
        else:
            a[j] = -a[j]
    mat.append(a)
visit[destination[0]][destination[1]] = True
mat[destination[0]][destination[1]] = 0
bfs(destination)

for i in mat:
    print(*i)