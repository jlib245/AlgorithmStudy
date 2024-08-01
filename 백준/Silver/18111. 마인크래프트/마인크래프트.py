import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [list(map(int,input().split())) for _ in range(N)]
minL, maxL = land[0][0], land[0][0]
for i in range(N):
    for j in range(M):
        nl = land[i][j]
        if minL > nl:
            minL = nl
        elif maxL < nl :
            maxL = nl
resT = -1
resL = -1
for nl in range(minL, maxL+1):
    nb = B
    cnt = 0
    for i in range(N):
        for j in range(M):
            l = land[i][j]
            cha = l - nl
            if cha > 0 :
                nb += cha
                cnt += cha*2
            else :
                nb += cha
                cnt -= cha
    if nb >= 0 :
        TF = False
        if nb >= 0:
            if resT == resL == -1 :
                TF = True
            elif resT > cnt :
                TF = True
            elif resT == cnt and resL < nl :
                TF = True
        if TF :
            resT = cnt
            resL = nl

print(resT, resL)