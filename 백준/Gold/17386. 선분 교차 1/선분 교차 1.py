def CCW(d1, d2, d3) :
    x1, y1 = d1
    x2, y2 = d2
    x3, y3 = d3
    return x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2

def check(line1, line2):
    a, b = line1
    c, d = line2
    abc = CCW(a,b,c)
    abd = CCW(a,b,d)
    cda = CCW(c,d,a)
    cdb = CCW(c,d,b)
    if abc*abd <= 0 and cda*cdb <= 0 :
        return 1
    return 0

x1, y1, x2, y2 = map(int,input().split())
L1 = ((x1,y1),(x2,y2))
x1, y1, x2, y2 = map(int,input().split())
L2 = ((x1,y1),(x2,y2))

print(check(L1, L2))