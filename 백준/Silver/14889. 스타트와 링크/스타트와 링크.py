import sys
input = lambda : sys.stdin.readline().rstrip()

def bt(n : int):
    if len(set_) == N // 2:
        res.append(set(set_))
        return res
    for i in range(n+1, N):
        set_.append(i)
        bt(i)
        set_.pop()
    return res

N = int(input())
matrx = []
for i in range(N):
    matrx.append(list(map(int,input().split())))

res = []
set_ = []
occ = bt(-1)

res = []
while occ:
    a = occ.pop()
    total1 = 0
    total2 = 0
    for i in range(N):
        for j in range(N):
            if i in a and j in a:
                total1 += matrx[i][j]
            elif not i in a and not j in a:
                total2 += matrx[i][j]
    res.append(abs(total1-total2))
print(min(res))