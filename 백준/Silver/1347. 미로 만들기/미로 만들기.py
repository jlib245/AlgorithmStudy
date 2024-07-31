import sys
input = lambda : sys.stdin.readline().rstrip()

def f():
    r, c = 49, 49
    visit[r][c] = True
    d = 0
    minR = 49
    minC = 49
    maxR = 49
    maxC = 49
    for i in range(N):
        q = s[i]
        if q == 'F':
            dr, dc = direction[d]
            nr, nc = r + dr, c + dc
            visit[nr][nc] = True
            r, c = nr, nc
            if minR > nr :
                minR = nr
            elif maxR < nr :
                maxR = nr
            if minC > nc :
                minC = nc
            elif maxC < nc :
                maxC = nc
        elif q == 'R':
            d = (d + 3) % 4
        else :
            d = (d + 1) % 4
    for r in range(minR, maxR+1):
        for c in range(minC, maxC+1):
            if visit[r][c] :
                print('.', end='')
            else :
                print('#', end='')
        print()
N = int(input())
s = input()
visit = [[False]*100 for _ in range(100)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
f()