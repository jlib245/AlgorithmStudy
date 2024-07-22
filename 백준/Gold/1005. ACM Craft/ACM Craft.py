from collections import deque
import sys
input = sys.stdin.readline

def topologySort(target):
    Q = deque()
    for i in range(1, N+1):
        if not indegree[i]:
            Q.append(i)
    while Q :
        x = Q.popleft()
        t = endTime[x]
        if x == target:
            return t
        for nx in edge[x] :
            indegree[nx] -= 1
            nt = t + D[nx]
            if endTime[nx] < nt :
                endTime[nx] = nt
            if not indegree[nx] :
                Q.append(nx)
                

T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())

    D = [0] + list(map(int,input().split()))
    endTime = D[::]

    edge = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        edge[X].append(Y)
        indegree[Y] += 1
    
    target = int(input())
    res = topologySort(target)
    ans.append(res)

print(*ans, sep='\n')