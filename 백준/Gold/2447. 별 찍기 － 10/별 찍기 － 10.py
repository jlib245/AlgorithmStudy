def f(n, star, start):
    r, c = start
    if n == 0:
        if star == 1:
            w[r][c] = '*'
    elif star == 1:
        nxtn = n//3
        lst = [[1,1,1],[1,0,1],[1,1,1]]
        for i in range(3):
            for j in range(3):
                nr = r+i*(nxtn)
                nc = c+j*(nxtn)
                if lst[i][j] == 1:
                    f(nxtn, 1, (nr,nc))
                else :
                    f(nxtn, 0, (nr,nc))
  
N = int(input())

w = [[' ']*N for i in range(N)]

f(N, 1, (0,0))

for i in range(N):
    for j in range(N):
        print(w[i][j], end='')
    print()