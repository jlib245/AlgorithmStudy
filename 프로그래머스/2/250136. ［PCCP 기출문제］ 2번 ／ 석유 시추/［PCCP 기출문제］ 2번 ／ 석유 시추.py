from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(tup : tuple, n : int, m : int, land):
    set_ = set()
    Q = deque([tup])
    set_.add(tup[1])
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visit[nr][nc] and land[nr][nc]:
                Q.append((nr,nc))
                cnt += 1
                set_.add(nc)
                visit[nr][nc] = True
    return set_, cnt


def solution(land):
    n = len(land)
    m = len(land[0])
    global visit
    visit = [[False]*m for _ in range(n)]
    lst = [0 for _ in range(m)]
    for r in range(n):
        for c in range(m):
            if land[r][c] and not visit[r][c]:
                visit[r][c] = True
                a, cnt = bfs((r,c), n, m, land)
                for i in a:
                    lst[i] += cnt
    print(*lst, sep='\n')
    return max(lst)