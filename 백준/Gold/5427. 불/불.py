import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs(start : tuple, fire : list) :
    Q = deque(fire+[start])
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while Q :
        r, c, t = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h and 0 <= nc < w and building[nr][nc] != '#' :
                if nr == 0 or nr == h-1 or nc == 0 or nc == w-1 :
                    if t >= 0 and building[nr][nc] != '*':
                        return t+2
                    elif building[nr][nc] != '*':
                        building[nr][nc] = '*'
                        Q.append((nr,nc,t))
                elif t < 0 and building[nr][nc] != '*':
                    building[nr][nc] = '*'
                    Q.append((nr,nc,t))
                elif t >= 0 and building[nr][nc] == '.' :
                    building[nr][nc] = '@'
                    Q.append((nr,nc,t+1))
    return 'IMPOSSIBLE'

T = int(input())
ans = []
for _ in range(T):
    w, h = map(int, input().split())
    building = []
    fire = []
    for i in range(h):
        a = list(input())
        for j in range(w):
            if a[j] == '@':
                start = (i,j, 0)
            elif a[j] == '*':
                fire.append((i,j, -1))
        building.append(a)
    if start[0] == 0 or start[1] == 0 or start[0] == h-1 or start[1] == w-1 :
        ans.append(1)
        continue
    ans.append(bfs(start,fire))
print(*ans, sep='\n')