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
    if abc*abd == cda*cdb == 0 :
        if not (max(a,b) < min (c,d) or min(a,b) > max(c,d)):
            return 1
    elif abc*abd <= 0 and cda*cdb <= 0 :
        return 1
    return 0

def makeLine(dot1, dot2) :
    x1, y1 = dot1
    x2, y2 = dot2
    if x1 == x2 :
        return False
    a = (y2-y1) / (x2-x1) 
    b = y1 - a*x1
    return (a, b)

def crossDot(line1, line2) :
    a1, b1 = line1
    a2, b2 = line2
    x = (b1-b2) / (a2-a1)
    y = a1 * x + b1
    return (x, y)

def specialCase(x, line2):
    a, b = line2
    y = a*x + b
    return x, y

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
dot1, dot2 = (x1, y1), (x2, y2)
dot3, dot4 = (x3, y3), (x4, y4)

L1 = ((x1,y1),(x2,y2))
L2 = ((x3,y3),(x4,y4))

cross = check(L1, L2)
print(cross)

if cross :
    line1 = makeLine(dot1, dot2)
    line2 = makeLine(dot3, dot4)
    dots1 = sorted([dot1, dot2])
    dots2 = sorted([dot3, dot4])
    if not line1 and not line2 :
        for i in range(2):
            for j in range(2):
                if dots1[i] == dots2[j] and i != j :
                    print(*dots1[i])
    elif not line1  :
        print(*specialCase(x1, line2))
    elif not line2 :
        print(*specialCase(x3, line1))
    elif line1[0] != line2[0] :
        print(*crossDot(line1, line2))
    else :
        for i in range(2):
            for j in range(2):
                if dots1[i] == dots2[j] and i != j :
                    print(*dots1[i])