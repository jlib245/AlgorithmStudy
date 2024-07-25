import sys
input = lambda : sys.stdin.readline().rstrip()

def btPass(r, c):
    if c < 8 :
        bt(r, c+1)
    elif r < 8 :
        bt(r+1, 0)
    else :
        for row in puzzle:
            print(*row, sep='')
        exit()
    return

def possible(r, c) :
    num = [True]*10
    for i in range(9):
        num[puzzle[r][i]] = False
    for i in range(9):
        num[puzzle[i][c]] = False
    for i in range(3):
        for j in range(3):
            num[puzzle[r//3*3+i][c//3*3+j]] = False
    res = []
    for i in range(1, 10):
        if num[i] :
            res.append(i)
    return res
    
def change(r, c, n):
    if n == 0 :
        if puzzle[r][c] :
            puzzle[r][c] = n
        else :
            print(f'{r}행 {c}열, 기존 {puzzle[r][c]}, {n}로 변경 불가')
    else :
        if not puzzle[r][c] :
            puzzle[r][c] = n
        else :
            print(f'{r}행 {c}열, 기존 {puzzle[r][c]}, {n}로 변경 불가')        
    return

def bt(r, c):
    if puzzle[r][c] :
        btPass(r, c)
        return
    possibleNum = possible(r, c)
    for i in possibleNum :
        change(r, c, i)
        btPass(r, c)
        change(r, c, 0)
    return

puzzle = []
for i in range(9):
    puzzle.append(list(map(int,list(input()))))
bt(0,0)