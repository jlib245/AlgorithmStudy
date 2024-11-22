import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(9)]

ans = []

def bt_pass(r, c) :
    if 0 <= c < 8 :
        bt(r, c+1)
    elif 0 <= r < 8 :
        bt(r+1, 0)
    else :
        for row in lst :
            print(*row, sep=' ')
        exit()

def bt(r, c) :
    if lst[r][c] != 0 :
        bt_pass(r, c)
        return

    num = set(range(1,10))
    for i in range(9) :
        num.discard(lst[r][i])
        num.discard(lst[i][c])
    for i in range(3) :
        for j in range(3) :
            num.discard(lst[r//3*3+i][c//3*3+j])
    
    for x in num :
        lst[r][c] = x
        bt_pass(r, c)
        lst[r][c] = 0
    return

bt(0, 0)



'''
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''