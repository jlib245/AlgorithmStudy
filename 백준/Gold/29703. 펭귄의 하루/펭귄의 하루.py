import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(start) :
    Q = deque([start])
    visit = [[[False]*2 for _ in range(M)] for _ in range(N)]
    visit[start[0]][start[1]][0] = True
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while Q :
        r, c, f, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and town[nr][nc] != 'D' and not visit[nr][nc][f] :
                visit[nr][nc][f] = True
                if not f :
                    if town[nr][nc] == 'F' :
                        visit[nr][nc][1] = True
                        Q.append((nr, nc, 1, d+1))
                    else :
                        Q.append((nr, nc, 0, d+1))
                else :
                    if town[nr][nc] == 'H' :
                        return d+1
                    Q.append((nr,nc,1,d+1))
    return -1

N, M = map(int,input().split())

town = [input() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if town[i][j] == 'S' :
            start = (i, j, 0, 0)
ans = bfs(start)
print(ans)