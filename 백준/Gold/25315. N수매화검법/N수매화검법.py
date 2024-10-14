import sys
input = sys.stdin.readline

def check(x, y):
    a, b = cut[x][0], cut[x][1]
    c, d = cut[y][0], cut[y][1]
    abc = CCW(a,b,c)
    abd = CCW(a,b,d)
    cda = CCW(c,d,a)
    cdb = CCW(c,d,b)
    if abc*abd <= 0 and cda*cdb <= 0 :
        return 1
    return 0


def CCW(d1, d2, d3) :
    x1, y1 = d1
    x2, y2 = d2
    x3, y3 = d3
    return x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2

N = int(input())
cut = []
m = [0]*N
edge = [[]*N for i in range(N)]

for i in range(N):
    sx, sy, ex, ey, w = map(int, input().split())
    cut.append(((sx, sy), (ex, ey), w, i))
for i in range(N):
    for j in range(i+1, N):
        if check(i, j):
            m[i] += 1
            m[j] += 1
            edge[i].append(j)
            edge[j].append(i)

ans = 0
sequence = sorted(cut, key=lambda x : x[2])
for trash, trash, w, i in sequence :
    ans += (m[i]+1)*w
    for rel in edge[i] :
        m[rel] -= 1
print(ans)