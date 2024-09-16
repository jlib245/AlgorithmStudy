import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    if x == y :
        return
    if x > y :
        parent[x] = y
    else :
        parent[y] = x
    return

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
g = [int(input()) for _ in range(P)]
for i in range(P):
    a = find(g[i])
    if not a :
        ans = i
        break
    union(a, a-1)
else :
    ans = P
    
print(ans)