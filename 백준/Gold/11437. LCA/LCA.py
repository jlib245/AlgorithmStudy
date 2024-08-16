import sys
input = sys.stdin.readline
from collections import deque

ans = []

def bfs(superParent : int) :
    Q = deque([(superParent, 0)])
    while Q :
        x, p = Q.popleft()
        d = depth[x]
        for nx in child[x]:
            if nx != p :
                Q.append((nx, x))
                depth[nx] = d+1
                parent[nx] = x
    return

def LCA(a, b) :
    while a != b :
        if depth[a] > depth[b] :
            a = parent[a]
        elif depth[a] < depth[b] :
            b = parent[b]
        else :
            a = parent[a]
            b = parent[b]
    return a

N = int(input())
parent = [0 for _ in range(N+1)]
child = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    child[B].append(A)
    child[A].append(B)

depth = [0 for _ in range(N+1)]
bfs(1)
M = int(input())
for i in range(M):
    A, B = map(int, input().split())
    ans.append(LCA(A, B))

print(*ans, sep='\n')