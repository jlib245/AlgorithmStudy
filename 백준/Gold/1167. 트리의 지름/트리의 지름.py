from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit((10**5)*5)

def dfs(tup:tuple):
    node, d = tup
    cnt = 0
    for nx, dd in tree[node]:
        if not visit[nx]:
            nd = d + dd
            cnt += 1
            visit[nx] = True
            dfs((nx, nd))
    if not cnt:
        res.append((d, node))
    return 


V = int(input())
tree= [[] for _ in range(V+1)]
for _ in range(V):
    q = deque(list(map(int, input().split())))
    node = q.popleft()
    while 1:
        other = q.popleft()
        if other == -1:
            break
        distance = q.popleft()
        tree[node].append((other, distance))

visit = [False for _ in range(V+1)]
visit[1] = True
res = []
dfs((1, 0))
res.sort(reverse=True)
nxt = (res[0][1], 0)
visit = [False for _ in range(V+1)]
visit[res[0][1]] = True
res = []
dfs(nxt)
print(max(res)[0])