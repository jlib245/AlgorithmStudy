import sys

def dfs(g, v, vi):
    vi[v] = True
    print(v, end = ' ')
    for i in g[v]:
        if not vi[i]:
            dfs(g, i, vi)
def bfs(g, start, vi):
    q = [start]
    vi[start] = True
    while q:
        v = q.pop(0)
        print(v, end = ' ')
        for i in g[v]:
            if not vi[i]:
                q.append(i)
                vi[i] = True

N, M, V = map(int,input().split())
g = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
for i in range(N+1):
    g[i].sort()
dfs(g, V, [False]*(N+1))
print()
bfs(g, V, [False]*(N+1))