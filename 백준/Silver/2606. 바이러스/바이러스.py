from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N+1)]
for _ in range(int(input())):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

visited = [False] * (N+1)
visited[1] = True
queue = deque([1])
result = 0
while queue:
    x = queue.popleft()
    for nx in lst[x]:
        if not visited[nx]:
            visited[nx] = True
            queue.append(nx)
            result += 1
print(result)