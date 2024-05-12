from collections import deque
import sys
input = sys.stdin.readline

def f():
    Q = deque([1])
    while Q:
        x = Q.popleft()
        for nx in lst[x]:
            if not visit[nx]:
                visit[nx] = True
                Q.append(nx)
                res[nx] = x
                
N = int(input())

lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visit = [False]*(N+1)
res = [0]*(N+1)
f()

for i in range(2, N+1):
    print(res[i])