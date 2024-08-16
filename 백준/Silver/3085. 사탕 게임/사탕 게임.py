import sys
input = lambda : sys.stdin.readline().rstrip()

def changeAndCheck(a : tuple, b : tuple) :
    global max_
    ax, ay = a
    bx, by = b
    board[ax][ay], board[bx][by] = board[bx][by], board[ax][ay]
    for i in range(N) :
        for j in range(N) :
            cnt = 1
            a = i+1
            while a < N and board[i][j] == board[a][j] :
                cnt += 1
                a += 1
            if max_ < cnt :
                max_ = cnt
            cnt = 1
            a = j+1
            while a < N and board[i][j] == board[i][a] :
                cnt += 1
                a += 1
            if max_ < cnt :
                max_ = cnt
        
    board[ax][ay], board[bx][by] = board[bx][by], board[ax][ay]
    return


N = int(input())
board = [list(input()) for _ in range(N)]
max_ = 0
for i in range(N):
    for j in range(N):
        if i != N-1 :
            changeAndCheck((i, j), (i+1, j))
        if j != N-1 :
            changeAndCheck((i, j), (i, j+1))
ans = max_
print(ans)