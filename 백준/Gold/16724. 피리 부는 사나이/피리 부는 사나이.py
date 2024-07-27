import sys
input = sys.stdin.readline

def find(r, c) :
    pr, pc = parent[r][c]
    if r == pr and c == pc :
        return r, c
    return find(pr, pc)

def union(a, b):
    a = tuple(find(a[0], a[1]))
    b = tuple(find(b[0], b[1]))
    if a == b :
        return
    a, b = sorted([a, b])
    parent[b[0]][b[1]] = a
    return
    

N, M = map(int, input().split())
move = [input() for _ in range(N)]
parent = [[(i,j) for j in range(M)] for i in range(N)]
for r in range(N):
    for c in range(M):
        m = move[r][c]
        if m == 'D':
            destin = (r+1, c)
        elif m == 'U':
            destin = (r-1, c)
        elif m == 'L' :
            destin = (r, c-1)
        else :
            destin = (r, c+1)
        union((r,c), destin)
cnt = 0
for r in range(N):
    for c in range(M):
        if parent[r][c] == (r,c):
            cnt += 1
print(cnt)