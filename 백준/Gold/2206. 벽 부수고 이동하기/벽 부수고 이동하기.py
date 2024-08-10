from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dr = (-1, 1, 0, 0)
dc = (0, 0,-1, 1)
def bfs():
    if n == m == 1 :
        return 1
    Q = deque([(0,0,0,1)])
    visit[0][0] = [True, True]
    while Q :
        r, c, b, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nd = d + 1
            if 0 <= nr < n and 0 <= nc < m :
                if mtrx[nr][nc] :
                    if not b :
                        visit[nr][nc][1] = True
                        Q.append((nr, nc, 1, nd))
                elif not visit[nr][nc][b]:
                    if nr == n-1 and nc == m-1 :
                        return nd
                    visit[nr][nc][b] = True
                    Q.append((nr, nc, b, nd))
    return -1

n, m = map(int, input().split())
visit = [[[False]*2 for _ in range(m)] for _ in range(n)]
mtrx = [list(map(int, input())) for _ in range(n)]
ans = bfs()
print(ans)