#스도쿠
def printf():
    for i in d:
        print(*i)

def init():
    global cnt
    for i in range(9):
        for j in range(9):
            t = d[i][j]
            if t:
                cnt -= 1
                s = sq(i,j)
                ver[i][t] = True
                hor[j][t] = True
                squ[s][t] = True

def nloc(x,y):
    nx = x
    ny = y + 1
    if ny == 9:
        nx += 1
        ny = 0
    return (nx,ny)

def dfs(loc):
    global cnt
    x,y = loc
    nx,ny = nloc(*loc)
    if d[x][y]:
        return dfs((nx,ny))

    s = sq(x,y)
    for t in range(1,10):
        if not ver[x][t] and not hor[y][t] and not squ[s][t]:
            ver[x][t] = True
            hor[y][t] = True
            squ[s][t] = True
            d[x][y] = t
            cnt -= 1
            if not cnt:
                printf()
                exit()
            dfs((nx,ny))
            cnt += 1
            d[x][y] = 0
            ver[x][t] = False
            hor[y][t] = False
            squ[s][t] = False

ver = [[False]*10 for _ in range(10)]
hor = [[False]*10 for _ in range(10)]
squ = [[False]*10 for _ in range(10)]
sq = lambda x,y:(x//3)*3 + y//3

d = [list(map(int,input().split())) for _ in range(9)]
cnt = 81
init()
dfs((0,0))