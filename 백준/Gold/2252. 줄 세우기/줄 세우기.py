import sys
from collections import deque
input = sys.stdin.readline

def topologySort() :
    Q = deque()
    res = []
    for i in range(1, N+1) :
        if not indegree[i] :
            Q.append(i)
    while Q:
        x = Q.popleft()
        res.append(x)
        for nx in edge[x] :
            indegree[nx] -= 1
            if not indegree[nx] :
                Q.append(nx)
    return res

N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    indegree[B] += 1
    
ans = topologySort()
print(*ans)