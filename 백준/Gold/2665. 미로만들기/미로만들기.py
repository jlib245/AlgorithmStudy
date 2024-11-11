import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

def bfs() :
    H = []
    heapq.heappush(H, (0, 0, 0))
    visit[0][0] = True
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    while H :
        d, r, c = heapq.heappop(H)
        if r == n-1 and c == n-1 :
            return d
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
                if lst[nr][nc] == '1' :
                    visit[nr][nc] = True
                    heapq.heappush(H,(d, nr, nc))
                else :
                    visit[nr][nc] = True
                    heapq.heappush(H, (d+1, nr, nc))
                
n = int(input())
lst = [input() for _ in range(n)]

visit = [[False]*n for _ in range(n)]
ans = bfs()
print(ans)