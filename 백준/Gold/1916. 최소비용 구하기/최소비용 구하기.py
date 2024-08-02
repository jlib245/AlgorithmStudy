import sys
import heapq 

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
        
start, end = map(int, input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
    
while heap:
    c, x = heapq.heappop(heap)
    if costs[x] < c:
        continue
    for nx, dc in graph[x]:
        nc = c + dc
        if nc >= costs[nx]:
            continue
        
        costs[nx] = nc
        heapq.heappush(heap, (nc, nx))
        
print(costs[end])