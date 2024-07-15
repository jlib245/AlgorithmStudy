import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visit = [False]*(V+1)
    set_ = [False]*(V+1)
    visit[0] = True
    for i in range(1, V+1):
        if not visit[i] :
            visit[i] = True
            Q = deque([i])
        else :
            continue
        while Q:
            this = Q.popleft()
            for near in edge[this]:
                if not visit[near]:
                    visit[near] = True
                    set_[near] = not set_[this]
                    Q.append(near)
                elif set_[near] != set_[this]:
                    continue
                else:
                    return "NO"
    return "YES"
K = int(input())
ans = []
for _ in range(K):
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        edge[v1].append(v2)
        edge[v2].append(v1)
    ans.append(bfs())
print(*ans, sep='\n')