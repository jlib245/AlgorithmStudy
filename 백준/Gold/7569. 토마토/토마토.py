from collections import deque
import sys
input = sys.stdin.readline

def tom():
    dx = (-1, 1, 0, 0, 0, 0)
    dy = (0, 0, -1, 1, 0, 0)
    dz = (0, 0, 0, 0, -1, 1)
    Q = deque(start)
    cnt = 0

    while Q :
        x, y, z, d= Q.popleft()
        if cnt < d:
            cnt = d
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if not lst[nz][ny][nx] :
                    Q.append((nx, ny, nz, d+1))
                    lst[nz][ny][nx] = 1
    
    return cnt

M, N, H = map(int, input().split())

lst = [[[0]*M for _ in range(N)] for i in range(H)]
start = []
onecnt = 0
for h in range(H):
    for n in range(N):
        a = list(map(int, input().split()))
        lst[h][n] = a
        for m in range(M):
            i = a[m]
            if i == 1:
                start.append((m, n, h, 0))
                onecnt += 1
            elif i == -1:
                onecnt += 1

if onecnt == M * N * H:
    print(0)
    exit()

res = tom()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if lst[h][n][m] == 0:
                print(-1)
                exit()

print(res)