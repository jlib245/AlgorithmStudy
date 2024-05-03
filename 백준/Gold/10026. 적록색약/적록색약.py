from collections import deque
import sys
inp = sys.stdin.readline

def f(sr, sc, dic:dict):
    if visit[sr][sc] :
        return 0
    
    queue = deque([(sr, sc)])
    visit[sr][sc] = True
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<= nr < N and 0<= nc < N and not visit[nr][nc] and lst[nr][nc] in dic[lst[sr][sc]]:
                queue.append((nr,nc))
                visit[nr][nc] = True
    return 1

N = int(inp())

lst = []
for i in range(N):
    lst.append(list(inp().rstrip()))

dicBasic = {'R' : {'R'}, 'G' : {'G'}, 'B' : {'B'}}
dicBlind = {'R' : {'R', 'G'}, 'G' : {'R', 'G'}, 'B' : {'B'}}

res = [0,0]

visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        res[0] += f(i, j, dicBasic)

visit = [[False]*N for _ in range(N)]   
for i in range(N):
    for j in range(N):
        res[1] += f(i, j, dicBlind)

print(*res)