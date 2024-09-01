import sys
input = sys.stdin.readline
from collections import deque


def getRoute(s, e):
    route = deque()
    while 1 :
        route.appendleft(e)
        if s == e :
            return route
        e = routeB[e]

def bfs(s, e):
    if s == e :
        return 0, [s]
    Q = deque([(s, 0)])
    while Q :
        x, d = Q.popleft()
        nxl = (x-1, x+1, 2*x)
        for nx in nxl :
            if 0 <= nx <= 100000 and routeB[nx] == -1 :
                routeB[nx] = x
                Q.append((nx, d+1))
                if nx == e :
                    return d+1, getRoute(s, e)

N, K = map(int, input().split())
routeB = [-1]*(100001)
ansT, ansR = bfs(N, K)
print(ansT)
print(*ansR)