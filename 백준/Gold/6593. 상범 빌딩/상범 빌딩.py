from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def bfs(start, end):
    Q = deque([start])
    dl = (-1,1,0,0,0,0)
    dr = (0,0,-1,1,0,0)
    dc = (0,0,0,0,-1,1)
    visit[start[0]][start[1]][start[2]] = True
    while Q:
        l,r,c,m = Q.popleft()
        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]
            nm = m + 1
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and not visit[nl][nr][nc] and building[nl][nr][nc] != '#' :
                if nl == end[0] and nr == end[1] and nc == end[2] :
                    return f"Escaped in {nm} minute(s)."
                visit[nl][nr][nc] = True
                Q.append((nl,nr,nc,nm))
    return "Trapped!"

message = []
while 1 :
    L, R, C = map(int,input().split())
    if L == R == C == 0 :
        break
    visit = [[[False]*C for _ in range(R)] for _ in range(L)]
    building = [[]for _ in range(L)]
    for l in range(L):
        for r in range(R):
            s = input()
            for c in range(C):
                if s[c] == 'S':
                    start = (l,r,c,0)
                elif s[c] == 'E':
                    end = (l,r,c)
            building[l].append(s)
        emptyLine = input()
    message.append(bfs(start,end))
print(*message, sep='\n')