import sys
sys.setrecursionlimit(int(1e6))

def f(start : tuple, cnt : int, dir : tuple, n : tuple):
    r, c = start
    if not (0<=r<N and 0<=c<M and lst[r][c] == 0):
        return
    
    x = abs(dir[1])
    if n[x] == 0:
        return
    
    for i in range(n[x]):
        nr = r + dir[0]*i
        nc = c + dir[1]*i
        lst[nr][nc] = cnt + i
    cnt += n[x]

    if dir[1] == 0:
        f((nr, nc-1), cnt, (0, -1), (n[0]-1, n[1]))
        f((nr, nc+1), cnt, (0, 1), (n[0]-1, n[1]))
    else :
        f((nr-1, nc), cnt, (-1, 0), (n[0], n[1]-1))
        f((nr+1, nc), cnt, (1, 0), (n[0], n[1]-1))
    return
    
N, M = map(int, input().split())

s = input()

lst = [[0]*M for _ in range(N)]
sDic = {'U':(0, M//2), 'D':(N-1, M//2),'L':(N//2, 0), 'R':(N//2, M-1)}
dDic = {'U':(1, 0), 'D':(-1, 0),'L':(0, 1), 'R':(0, -1)}

if s == 'U' or s == 'D':
    n = (N, M//2)
else :
    n = (N//2, M)

f(sDic[s], 1, dDic[s], n)

for i in range(N):
    print(*lst[i])