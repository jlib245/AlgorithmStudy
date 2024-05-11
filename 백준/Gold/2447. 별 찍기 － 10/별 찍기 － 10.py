def f(n, star, start):
    r, c = start
    if n == 0:
        if star == 1:
            w[r][c] = '*'
    elif star == 1:
        nxtn = n//3
        for i in range(3):
            for j in range(3):
                nr = r+i*(nxtn)
                nc = c+j*(nxtn)
                f(nxtn, lst[i][j], (nr,nc))
  
N = int(input())

w = [[' ']*N for i in range(N)]
lst = [[1,1,1],[1,0,1],[1,1,1]]
f(N, 1, (0,0))

for i in w:
    print(*i, sep='')