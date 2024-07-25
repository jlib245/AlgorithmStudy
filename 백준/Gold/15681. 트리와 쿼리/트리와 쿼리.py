import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def f(x):
    cnt = 1
    for nx in edge[x]:
        if not visit[nx] :
            visit[nx] = True
            cnt += f(nx)
    STV[x] = cnt
    return cnt

N, R, Q = map(int, input().split())

edge = [[] for _ in range(N+1)]
STV = [0 for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)

visit = [False]*(N+1)
visit[R] = True
f(R)

ans = []
for _ in range(Q):
    q = int(input())
    ans.append(STV[q])

print(*ans,sep='\n')