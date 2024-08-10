import sys
input = lambda : sys.stdin.readline()
sys.setrecursionlimit(10**5)

def find(x) :
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a == b :
        return
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return

def check(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return "YES"
    return "NO"


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

ans = []
for _ in range(m):
    q, a, b = list(map(int, input().split()))
    if not q :
        union(a, b)
    else :
        ans.append(check(a, b))

print(*ans, sep='\n')