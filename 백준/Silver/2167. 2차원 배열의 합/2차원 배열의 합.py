N, M = map(int, input().split())
mtrx = []
for i in range(N):
    mtrx.append(list(map(int, input().split())))

sum_ = [[0]*M for i in range(N)]
sum_[0][0] = mtrx[0][0]
for j in range(1, M):
    sum_[0][j] = sum_[0][j-1] + mtrx[0][j]
    
for i in range(1, N):
    sum_[i][0] = sum_[i-1][0] + mtrx[i][0]
    for j in range(1,M):
        sum_[i][j] = sum_[i-1][j] + sum_[i][j-1] - sum_[i-1][j-1] + mtrx[i][j]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    if i == 0 or j == 0:
        if i != 0:
            rslt = sum_[x][y] - sum_[i-1][y]
        elif j != 0 :
            rslt = sum_[x][y] - sum_[x][j-1]
        else:
            rslt = sum_[x][y]
    else :
        rslt = sum_[x][y] - sum_[i-1][y] - sum_[x][j-1] + sum_[i-1][j-1]
    
    print(rslt)