import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 

def same_parent(a, b):
    return find(a) == find(b)

N, M = map(int, input().split())

edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]

res = 0
last = 0
for a, b, c in edges:
    if not same_parent(a,b):
        union(a,b)
        res += c
        last = c        
res -= last

print(res)