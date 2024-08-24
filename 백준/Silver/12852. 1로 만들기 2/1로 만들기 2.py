from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def bfs(N):
    visit = [False]*N
    Q = deque([(N, 0, [N])])
    while Q :
        x, d, route= Q.popleft()
        lst = []
        if x % 2 == 0 :
            lst.append(x // 2)
        if x % 3 == 0 :
            lst.append(x // 3)
        lst.append(x - 1)
        for nx in lst :
            if not visit[nx] :
                visit[nx] = True
                if nx == 1 :
                    return d+1, route+[nx]
                Q.append((nx, d+1, route+[nx]))
            

N = int(input())
if N == 1 :
    print(0)
    print(1)
    exit()
cnt, route = bfs(N)
print(cnt)
print(*route)