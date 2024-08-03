import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    start = (0,0,0,0)
    if lst[0][0] == 2:
        start = (0,0,1,0)
    Q = deque([start])
    visit = [[[False]*2 for _ in range(M)] for _ in range(N)]
    visit[start[0]][start[1]][start[2]] = True
    while Q :
        r, c, s, t = Q.popleft()
        if t > T :
            break
        if r == N-1 and c == M-1 :
            return t
        for i in range(4):
            nr = r + dr[i] 
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc][s] :
                if not s :
                    if lst[nr][nc] == 2 :
                        visit[nr][nc][1] = True
                        visit[nr][nc][0] = True
                        Q.append((nr, nc, 1, t+1))
                    elif lst[nr][nc] == 0:
                        visit[nr][nc][0] = True
                        Q.append((nr, nc, 0, t+1))
                else :
                    visit[nr][nc][1] = True
                    Q.append((nr,nc,1,t+1))
    return "Fail"



N, M, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
print(ans)