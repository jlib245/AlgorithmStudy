import sys
input = sys.stdin.readline

R, C, M = map(int,input().split())
shark = [0]
livingShark = [True]*(M+1)
mtrx = [[0]*(C+2) for _ in range(R+2)]
mtrx[0], mtrx[R+1] = [-1]*(R+2), [-1]*(R+2)
for i in range(1, R+1):
    mtrx[i][0] = -1
    mtrx[i][C+1] = -1
for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    mtrx[r][c] = i
    if s == 1 or s == 2:
        s %= 2*(R-1)
    elif s == 3 or s == 4:
        s %= 2*(C-1)
    shark.append((r,c,s,d,z))
move = [(-1,-1), (-1, 0), (1, 0), (0, 1), (0, -1)]
changeD = [0, 2, 1, 4, 3]
man = 0
ans = 0
for _ in range(C):
    man += 1
    for i in range(1, R+1):
        if mtrx[i][man] :
            caughtSharkNum = mtrx[i][man]
            mtrx[i][man] = 0
            livingShark[caughtSharkNum] = False
            ans += shark[caughtSharkNum][4]
            break
    for i in range(1, M+1):
        if not livingShark[i]:
            continue
        r,c,s,d,z =shark[i]
        mtrx[r][c] = 0
        remainS = s
        while remainS:
            dr, dc = move[d]
            if d == 1 :
                a = r - 1
            elif d == 2 :
                a = R - r
            elif d == 3 :
                a = C - c
            else :
                a = c - 1
            if remainS < a:
                r += dr * remainS
                c += dc * remainS
                remainS = 0
            else :
                remainS -= a
                r += dr * a
                c += dc * a
                d = changeD[d]
        shark[i] = (r,c,s,d,z)
            
    for i in range(1, M+1):
        if not livingShark[i]:
            continue
        r,c,s,d,z = shark[i]
        if 0<mtrx[r][c] < i:
            selfNum = i
            otherNum = mtrx[r][c]
            if shark[selfNum][4] < shark[otherNum][4]:
                livingShark[selfNum] = False
            else:
                livingShark[otherNum] = False
                mtrx[r][c] = i
            continue
        mtrx[r][c] = i
        
print(ans)