from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def bfs(R : int, C : int, J : tuple, K : list) :
    q = deque(K+[J])
    dr = (0,0,-1,1)
    dc = (-1,1,0,0)
    if J[0] in (0, R-1) or J[1] in (0, C-1):
        return 1
    while q:
        r, c, literal, distance = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C :
                if literal == 'J' and miro[nr][nc] == '.':
                    miro[nr][nc] = 'J'
                    q.append((nr,nc,'J',distance+1))
                    if nr in (0,R-1) or nc in (0,C-1):
                        return distance + 2
                elif literal == 'F' and miro[nr][nc] in ".J":
                    miro[nr][nc] = 'F'
                    q.append((nr,nc,'F',-1))
    return "IMPOSSIBLE"


R, C = map(int, input().split())
miro = list(list(input()) for _ in range(R))
K = []
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            J = (i,j, 'J', 0)
        elif miro[i][j] == 'F':
            K.append((i,j, 'F', -1))
print(bfs(R, C, J, K))