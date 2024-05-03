from collections import deque
import sys
input = sys.stdin.readline

def f() :
    dy = (1, -1)

    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + 1
            ny = y + dy[i]
            if (0<=nx<=N and 0<= ny <= nx or N<nx<=2*N and 0<= ny <= (2*N-nx)) and not X[nx][ny] and not v[nx][ny]:
                queue.append((nx, ny))
                v[nx][ny] += 1

    if v[2*N][0] == 0:
        return -1
    res = 0
    queue = deque([(2*N, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x - 1
            ny = y + dy[i]
            if (0<=nx<=N and 0<= ny <= nx or N<nx<=2*N and 0<= ny <= (2*N-nx)) and v[nx][ny] == 1:
                queue.append((nx, ny))
                v[nx][ny] += 1
                if res < ny:
                    res = ny
    return res

N, M = map(int, input().split())

X = [[False]*(N+1) for i in range(2*N+1)]
v = [[0]*(N+1) for i in range(2*N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    X[x][y] = True

print(f())