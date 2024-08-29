import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b, cost) :
    a = find(a)
    b = find(b)
    if a == b :
        return 0
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return cost
    

N, M = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
edge.sort(key = lambda x : x[2])
cost = 0
total = 0
for a, b, c in edge :
    total += c
    cost += union(a, b, c)
if sum(find(i) for i in range(1, N+1)) == N :
    ans = total - cost
    print(ans)
else :
    print(-1)