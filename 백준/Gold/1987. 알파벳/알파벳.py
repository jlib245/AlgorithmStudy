import sys

dr = (0, 1, -1, 0)
dc = (-1, 0, 0, 1)

def f(r, c, cnt) :
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc <C:
            na = ord(board[nr][nc])-65
            if not alpha[na]:
                alpha[na] = True
                f(nr, nc, cnt+1)
                alpha[na] = False

    global result
    if result < cnt:
        result = cnt
    return

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(sys.stdin.readline().rstrip())

alpha = [False]*26
result = 0
alpha[ord(board[0][0])-65] = True
f(0,0, 1)
print(result)