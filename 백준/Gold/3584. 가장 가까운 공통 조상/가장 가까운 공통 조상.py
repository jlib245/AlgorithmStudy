import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
ans = []

def bfs(superParent : int) :
    Q = deque([superParent])
    while Q :
        x = Q.popleft()
        d = depth[x]
        for nx in child[x]:
            Q.append(nx)
            depth[nx] = d+1
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
for i in range(T):
    N = int(input())
    parent = [0 for _ in range(N+1)]
    child = [[] for _ in range(N+1)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
        child[A].append(B)
    
    x = 1
    while 1 :
        if parent[x] == 0 :
            superParent = x
            break
        x = parent[x]

    depth = [0 for _ in range(N+1)]
    bfs(superParent)
    A, B = map(int, input().split())
    ans.append(LCA(A, B))

print(*ans, sep='\n')