import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    visit = [False]*(1+N)
    visit[x] = True
    cnt = 1
    Q = deque([x])
    while Q :
        x = Q.popleft()
        for nx in lst[x] :
            if not visit[nx] :
                visit[nx] = True
                Q.append(nx)
                cnt += 1
    return cnt

N, M = map(int, input().split())
lst = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    lst[B].append(A)

max_ = 0
maxL = []
for i in range(1, N+1):
    a = bfs(i)
    if max_ < a :
        max_ = a
        maxL = [i]
    elif max_ == a :
        maxL.append(i)
print(*maxL)