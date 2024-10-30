import sys, heapq
input = lambda:sys.stdin.readline().rstrip()

def dijkstra(s : tuple, e : tuple) -> int :
    Heap = []
    dr = (-1, 0, 1, 0)
    dc = (0, -1, 0, 1)
    INF = 10001
    mirror = [[[INF]*4 for i in range(C)] for i in range(R)]
    mirror[s[0]][s[1]] = [0,0,0,0]
    for di in range(4):
        nr = s[0] + dr[di]
        nc = s[1] + dc[di]
        if 0 <= nr < R and 0 <= nc < C :
            if lst[nr][nc] == 'C' :
                return 0
            elif lst[nr][nc] == '.':
                heapq.heappush(Heap, (0, nr, nc, di))
    while Heap :
        cnt, r, c, di = heapq.heappop(Heap)
        if r == e[0] and c == e[1] :
            return cnt
        for ndi in range(4):
            nr = r + dr[ndi]
            nc = c + dc[ndi]
            if di == ndi :
                ncnt = cnt
            elif di % 2 == ndi % 2 :
                continue
            else :
                ncnt = cnt + 1
            if 0 <= nr < R and 0 <= nc < C and lst[nr][nc] != '*' and ncnt < mirror[nr][nc][ndi] :
                mirror[nr][nc][ndi] = ncnt
                heapq.heappush(Heap, (ncnt, nr, nc, ndi))

C, R = map(int, input().split())
c = []
lst = []
for i in range(R):
    s = input()
    for j in range(C):
        if s[j] == 'C':
            c.append((i,j))
    lst.append(s)
ans = dijkstra(c[0], c[1])
print(ans)