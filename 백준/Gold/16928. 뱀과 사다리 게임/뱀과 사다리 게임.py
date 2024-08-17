import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs():
    Q = deque([(1, 0)])
    while Q :
        x, d= Q.popleft()
        if x == 100 and d == cnt[100]:
            return d
        for i in range(1, 7):
            if x + i <= 100:
                nx = go[x+i]
                nd = d + 1
                if cnt[nx] > nd :
                    cnt[nx] = nd 
                    Q.append((nx, d+1))
    


N, M = map(int, input().split())
INF = 1000
go = [i for i in range(101)]
cnt = [INF for _ in range(101)]
for _ in range(N+M):
    a, b = map(int, input().split())
    go[a] = b
ans = bfs()
print(ans)