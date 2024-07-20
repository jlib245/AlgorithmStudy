import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(x, parentColor):
    xColor = C[x]
    paint = 0
    if xColor != parentColor:
        paint += 1
    for nx in edge[x]:
        if not visit[nx] :
            visit[nx] = True
            paint += dfs(nx, xColor)
    return paint
    
N = int(input())
C = [0] + list(map(int,input().split()))

edge = [[] for _ in range(N+1)]
for i in range(N-1):
    v1, v2 = map(int,input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

visit = [False]*(N+1)
visit[1] = True
ans = dfs(1, 0)

print(ans)