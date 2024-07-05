from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def bfs(I):
    sx, sy = I
    visit[sy][sx] = True
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    Q = deque([I])
    cnt = 0
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and lst[ny][nx] != 'X' and not visit[ny][nx]:
                visit[ny][nx] = True
                Q.append((nx, ny))
                if lst[ny][nx] == 'P':
                    cnt += 1
    return cnt

N, M = map(int,input().split())
lst = []
for i in range(N):
    s = input()
    if 'I' in s:
        I = (s.index('I'), i)
    lst.append(s)
visit = [[False]*M for _ in range(N)]
res = bfs(I)
if res:
    print(res)
else:
    print("TT")