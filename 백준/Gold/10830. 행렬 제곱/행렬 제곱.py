def gob(mat1, mat2):
    res = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            cc = 0
            for a in range(N):
                cc += (mat1[r][a] * mat2[a][c]) % 1000
            cc %= 1000
            res[r][c] = cc
    return res
                
def f(b):
    if b == 1:
        return gob(basis, I)
    mat1 = f(b//2)
    if b % 2 == 0:
        mat2 = mat1[::]
    else:
        mat2 = gob(mat1, basis)
    return gob(mat1, mat2)
    

N, B = map(int, input().split())

basis = []
for i in range(N):
    basis.append(list(map(int, input().split())))

I = [[0]*N for _ in range(N)]
for i in range(N):
    I[i][i] = 1

res = f(B)

for i in res:
    print(*i)

'''
b = 7이면
b = 4 + 2 + 1
b에서 시작해서
b % 2 == 0 일 때
    f(b//2) * f(b//2) 
b % 2 == 1 일 때
    f(b//2) * f(b//2+1)
'''