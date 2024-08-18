import sys
input = lambda : sys.stdin.readline()
from collections import deque

def bfs(N, K):
    Q = deque([(N, 0)])
    visit[N] = 1
    time[N] = 0
    if N == K :
        return 0, 1
    while Q :
        x, d = Q.popleft()
        nxt = (x-1, x+1, 2*x)
        nd = d+1
        if nd > time[K] :
            break
        for nx in nxt :
            if 0 <= nx < INF and time[nx] >= nd :
                visit[nx] += visit[x]
                if time[nx] == INF :
                    time[nx] = nd
                    if nx != K :
                        Q.append((nx, nd))             
    return time[K], visit[K]
        
N, K = map(int, input().split())

INF = 10**5+1
time = [INF]*INF
visit = [0]*INF
ans = bfs(N, K)

print(*ans, sep='\n')