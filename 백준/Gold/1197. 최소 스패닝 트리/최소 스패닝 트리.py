import sys
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        a = find(parent[a])
    return a


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    edges.append(tuple(map(int ,input().split())))
edges.sort(key=lambda x : x[2])
res = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a,b)
        res += cost

print(res)