import sys
sys.setrecursionlimit(110000)
input = lambda : sys.stdin.readline().rstrip()

def find(x: int):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(x : int, y : int):
    x = find(x)
    y = find(y)
    if x == y :
        return
    if (x < y) :
        parent[y] = x
    else :
        parent[x] = y
    return

def checkUnion(x : int, y : int) :
    return find(x) == find(y)


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    union(x,y)
calendar = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    if not checkUnion(calendar[i], calendar[i+1]):
        cnt += 1
print(cnt)