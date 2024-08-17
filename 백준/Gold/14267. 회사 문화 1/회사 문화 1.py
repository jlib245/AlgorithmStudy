import sys
input = lambda : sys.stdin.readline()
from collections import deque

def bfs():
    Q = deque([1])
    while Q :
        x = Q.popleft()
        for nx in child[x] :
            compl[nx] += compl[x]
            Q.append(nx)

n, m = map(int,input().split())
parent = [0] + list(map(int, input().split()))
child = [[] for _ in range(n+1)]
for x in range(2, n+1):
    child[parent[x]].append(x)
compl = [0 for _ in range(n+1)]
for i in range(m) :
    i, w = map(int, input().split())
    compl[i] += w
bfs()
print(*compl[1:])