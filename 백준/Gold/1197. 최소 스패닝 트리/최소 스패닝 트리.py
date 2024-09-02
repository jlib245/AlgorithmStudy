import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    a = find(x)
    b = find(y)
    if a == b :
        return False
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return True

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
ans = 0
route = []
for _ in range(E):
    a, b, c = map(int, input().split())
    route.append((a, b, c))
route.sort(key=lambda x : x[2])
for a, b, c in route :
    if union(a, b) :
        ans += c
print(ans)