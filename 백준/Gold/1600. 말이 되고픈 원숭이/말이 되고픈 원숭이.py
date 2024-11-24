from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(H)]
visit = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]
def bfs():
    if W == H == 1 :
        return 0
    Q = deque([(0, 0, 0, 0)])
    visit[0][0][0] = True
    dr = (-1, 1, 0, 0, -1, -2, -2, -1, 1, 2, 2, 1)
    dc = (0, 0, -1, 1, -2, -1, 1, 2, 2, 1, -1, -2)
    dh = (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1)
    
    while Q :
        r, c, h, d = Q.popleft()
        for i in range(12) :
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]
            nd = d + 1
            if 0 <= nr < H and 0 <= nc < W and nh < K+1 and not visit[nr][nc][nh] and not lst[nr][nc] :
                visit[nr][nc][nh] = True
                Q.append((nr, nc, nh, nd))
                if nr == H-1 and nc == W-1 :
                    return nd
    return -1

ans = bfs()
print(ans)