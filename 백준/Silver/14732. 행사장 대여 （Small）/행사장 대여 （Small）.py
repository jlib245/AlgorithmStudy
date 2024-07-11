import sys
input = sys.stdin.readline
N = int(input())
lst = []
xl = []
yl = []
for _ in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    lst.append((x1,y1,x2,y2))
    xl.append(x1)
    xl.append(x2)
    yl.append(y1)
    yl.append(y2)
xl.sort()
yl.sort()
res = 0
for i in range(len(xl)-1):
    for j in range(len(yl)-1):
        sx1, sx2 = xl[i], xl[i+1]
        sy1, sy2 = yl[j], yl[j+1]
        for x1, y1, x2, y2 in lst:
            if x1 <= sx1 and sx2 <= x2 and y1 <= sy1 and sy2 <= y2:
                square = (sx2-sx1)*(sy2-sy1)
                res += square
                break
print(res)