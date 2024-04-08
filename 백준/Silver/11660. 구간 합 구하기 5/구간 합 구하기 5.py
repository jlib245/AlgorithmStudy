import sys
input= sys.stdin.readline
N, M = map(int, input().split())

lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

sum = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:
            if i != 0:
                sum[i][j] = sum[i-1][j] + lst[i][j]
            elif j != 0:
                sum[i][j] = sum[i][j-1] + lst[i][j]
            else:
                sum[i][j] = lst[i][j]

        else:
            sum[i][j] = lst[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] 


for i in range(M):

    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if a == 0 or b == 0:
        if a != 0:
            result = sum[c][d]-sum[a-1][d]
        elif b != 0:
            result = sum[c][d]-sum[c][b-1]
        else:
            result = sum[c][d]
    else:
        result = sum[c][d] - sum[a-1][d] - sum[c][b-1] + sum[a-1][b-1]
    print(result)