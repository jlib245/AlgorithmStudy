import sys
input = sys.stdin.readline
from collections import deque

def bfs() :
    Q = deque([(0, 0)])
    visit = [False]*N
    visit[0] = True
    while Q :
        x, d = Q.popleft()
        for i in range(1, lst[x]+1) :
            nx = x + i
            if not visit[nx] :
                visit[nx] = True
                Q.append((nx, d+1))
                if nx == N-1 :
                    return d+1
    return -1
N = int(input())
lst = list(map(int, input().split()))
if N == 1 :
    ans = 0
else :
    ans = bfs()
print(ans)