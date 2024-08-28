import sys
input = sys.stdin.readline

def dfs(x, cnt):
    visit[x] = True
    for nx in edge[x] :
        if not visit[nx] :
            if cnt == 4 :
                return True
            visit[nx] = True
            if dfs(nx, cnt+1)  :
                return True
            visit[nx] = False
            
    return False

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
for i in range(N):
    visit = [False]*N
    if dfs(i, 1) :
       print(1)
       break
else :
    print(0)