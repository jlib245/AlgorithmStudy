from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def keyOutput(key) :
    a = []
    for i in range(6):
        a.append(key%2)
        key >>= 1
    return a 

def bfs(start):
    Q = deque([start])
    visit = [[[False]*(2**6) for _ in range(M)] for _ in range(N)]
    visit[start[0]][start[1]][0] = True
    while Q:
        r, c, k, d = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nk = k
            nd = d + 1
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc][k] and miro[nr][nc] != '#':
                destin = miro[nr][nc]
                if destin == '1':
                    return nd
                elif destin == '.' :
                    Q.append((nr,nc,nk,nd))
                elif 97 <= ord(destin) <= 102 :
                    index = ord(destin)-97
                    a = keyOutput(nk)
                    if not a[index] :
                        nk += 1 << index
                    Q.append((nr, nc, nk, nd))
                else :
                    index = ord(destin)-65
                    a = keyOutput(nk)
                    if a[index] :
                        Q.append((nr,nc,nk,nd))
                visit[nr][nc][k] = True
    return -1
                    
N, M = map(int, input().split())
miro = []
for i in range(N):
    s = list(input())
    for j in range(M):
        if s[j] == '0':
            start = (i,j,0,0)
            s[j] = '.'
    miro.append(s)

ans = bfs(start)
print(ans)