import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mtrx1 = []
for _ in range(N):
    mtrx1.append(list(map(int,input().split())))

M, K = map(int, input().split())
mtrx2 = []
for _ in range(M):
    mtrx2.append(list(map(int,input().split())))

ans = [[0]*K for _ in range(N)]
for r in range(N):
    for c in range(K):
        tmp = 0
        for m in range(M):
            tmp += mtrx1[r][m] * mtrx2[m][c]
        ans[r][c] = tmp
        
for row in ans:
    print(*row)