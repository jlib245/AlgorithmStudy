from collections import deque
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def deik():
    Q = deque([(0,0,mtrx[0][0])])
    visit[0][0] = True
    while Q:
        r, c, l = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                visit[nr][nc] = True
                nl = l + mtrx[nr][nc]
                if nr == nc == N-1:
                    return nl
                Q.append((nr,nc, nl))
                Q = deque(sorted(Q, key=lambda x : x[2]))
ans = []
while 1:
    N = int(input())
    if not N:
        break
    mtrx = []
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        mtrx.append(list(map(int,input().split())))
    res = deik()
    ans.append(res)
for i in range(len(ans)):
    print(f"Problem {i+1}: {ans[i]}")