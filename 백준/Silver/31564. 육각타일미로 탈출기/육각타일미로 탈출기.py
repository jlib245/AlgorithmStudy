from collections import deque
import sys
input = sys.stdin.readline

N, M, K= map(int, input().split())
cnt = [[0]*M for _ in range(N)]

for _ in range(K):
    Yk, Xk = map(int, input().split())
    cnt[Yk][Xk] = -1

dy = [0,1,1,0,-1,-1]
dx1 = [1,1,0,-1,0,1]
dx2 = [1,0,-1,-1,-1,0,1]
queue = deque([(0,0)])
while queue:
    y, x = queue.popleft()
    if y == N-1 and x == M-1:
        print(cnt[y][x])
        exit()
    for i in range(6):
        ny = y + dy[i]
        if y % 2 == 1:
            nx = x + dx1[i]
        else :
            nx = x + dx2[i]
        if 0 <= ny < N and 0 <= nx < M and cnt[ny][nx] == 0:
            cnt[ny][nx] = cnt[y][x] + 1
            queue.append((ny,nx))
print(-1)