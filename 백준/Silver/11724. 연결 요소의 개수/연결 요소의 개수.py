from collections import deque
import sys
input = sys.stdin.readline

def bfs(i) :
    queue = deque([i])
    while queue:
        x = queue.popleft()
        for nx in lst[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
    return 1

N, M = map(int, input().split())

lst = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
    
visited = [False] * (N+1)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        visited[i] = True
        cnt += bfs(i)
print(cnt)