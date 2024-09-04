import sys
input = sys.stdin.readline
from collections import deque

def treeCheck(root):
    Q = deque([(root, 0)])
    while Q :
        x, parent = Q.popleft()
        for nx in edge[x] :
            if nx != parent :
                if not visit[nx] :
                    Q.append((nx, x))
                else :
                    return 0
    return 1
TC = 0
ans = []
while 1 :
    n, m = map(int, input().split())
    if n == m == 0 :
        break
    TC += 1
    edge = [[] for _ in range(n+1)]
    for i in range(m) :
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    visit = [False]*(n+1)
    cnt = 0
    for i in range(1, n+1) :
        if not visit[i] :
            visit[i] = True
            cnt += treeCheck(i)
    if not cnt :
        ans.append(f"Case {TC}: No trees.")
    elif cnt == 1 :
        ans.append(f"Case {TC}: There is one tree.")
    else :
        ans.append(f"Case {TC}: A forest of {cnt} trees.")
print(*ans, sep='\n')