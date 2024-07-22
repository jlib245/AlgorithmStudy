from collections import deque
import sys
input = lambda : sys.stdin.readline()

def topologySort():
    res = []
    Q = deque()
    for i in range(1, N+1):
        if not indegree[i] :
            Q.append(i)

    while Q:
        x = Q.popleft()
        res.append(x)
        for nx in edge[x]:
            indegree[nx] -= 1
            if not indegree[nx] :
                Q.append(nx)
    
    if len(res) != N :
        res = [0]

    return res

N, M = map(int, input().split())

edge = [[]for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    inp =   list(map(int,input().split()))
    length = inp[0]
    for i in range(1, length):
        now = inp[i]
        nxt = inp[i+1]
        edge[now].append(nxt)
        indegree[nxt] += 1  

ans = topologySort()
print(*ans, sep='\n')