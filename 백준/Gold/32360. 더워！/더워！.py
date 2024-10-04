import sys
input = lambda : sys.stdin.readline()
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(home) :
    Q = deque([home])
    B = [[100]*M for _ in range(N)]
    while Q :
        r, c, d, b = Q.popleft()
        if lst[r][c] == 'H' and 0 < b:
            nb = max(0, b-K)
            B[r][c] = nb
            Q.append((r, c, d+1, nb))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] != '#':
                if lst[nr][nc] == 'H' :
                    nb = max(0, b-K)
                else :
                    nb = min(100, b+C)
                if B[nr][nc] > nb:
                    B[nr][nc] = nb
                    Q.append((nr, nc, d+1, nb))
                    if lst[nr][nc] == 'E' :
                        return d+1
    return -1

N, M = map(int, input().split())
K, C = map(int, input().split())
lst = []
for i in range(N):
    a = list(input())
    lst.append(a)
    for j in range(M) :
        if a[j] == 'S' :
            home = (i, j, 0, 0)
print(bfs(home))