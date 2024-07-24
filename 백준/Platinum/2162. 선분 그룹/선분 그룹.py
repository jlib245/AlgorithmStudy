import sys
input = sys.stdin.readline

def find(n:int):
    while n != parent[n] :
        n = parent[n]
    return n

def union(a:int, b:int) :
    a, b = find(a), find(b)
    if a == b :
        return
    elif a < b :
        parent[b] = a
        group[a] += group[b]
        group[b] = 0
    else :
        parent[a] = b
        group[b] += group[a]
        group[a] = 0
    return

def CCW(a: tuple, b : tuple, c : tuple):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return x1*y2+x2*y3+x3*y1-x3*y2-x2*y1-x1*y3

def check(index1 : int, index2 : int) :
    a, b = line[index1]
    c, d = line[index2]
    abc = CCW(a,b,c)
    abd = CCW(a,b,d)
    cda = CCW(c,d,a)
    cdb = CCW(c,d,b)
    if abc*abd == cda * cdb == 0 :
        if not (min(a,b) > max(c,d) or max(a,b) < min(c,d)) :
            union(index1, index2)
    elif abc*abd <= 0 and cda * cdb <= 0 :
        union(index1, index2)
    return

N = int(input())
parent = [i for i in range(N)]
group = [1 for _ in range(N)]
line = []

for _ in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    line.append(((x1, y1),(x2, y2)))

for i in range(N):
    for j in range(i+1, N):
        check(i,j)

groupCnt = 0
groupMax = 0
for i in range(N):
    if group[i] :
        groupCnt += 1
        if groupMax < group[i]:
            groupMax = group[i]

print(groupCnt)
print(groupMax)