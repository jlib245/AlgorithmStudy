import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
def bfs(start):
    Q = deque([start])
    cnt = 1
    team = lst[start[0]][start[1]]
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visit[nr][nc] and lst[nr][nc] == team:
                visit[nr][nc] = True
                cnt += 1
                Q.append((nr,nc))
    dic[team] += cnt**2
    return
C, R = map(int, input().split())
lst = []
for i in range(R):
    lst.append(input())
visit = [[False]*C for _ in range(R)]
dic = {'W':0, 'B':0}
for r in range(R):
    for c in range(C):
        if not visit[r][c] :
            visit[r][c] = True
            bfs((r,c))
print(dic['W'], dic['B'])