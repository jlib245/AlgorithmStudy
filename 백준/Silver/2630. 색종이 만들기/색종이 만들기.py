import sys
input = sys.stdin.readline

def square(n, r, c) :
    if n == 1:
        return lst[r][c]
    
    dr = (0, 0, n//2, n//2)
    dc = (0, n//2, 0, n//2)
    sum_ = 0
    TF = True
    l = []
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        div = square(n//2, nr, nc)
        l.append(div)
        sum_ += div
        if sum_ != 0 and sum_ != (i+1):
            TF = False
            
    global white, blue
    if TF:
        if n == N:
            if sum_ == 0:
                white += 1
            else:
                blue += 1     
        return sum_//4
    else :
        for i in l:
            if i == 0:
                white += 1
            elif i == 1:
                blue += 1
        return 10

N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

white = 0
blue = 0

square(N, 0, 0)

print(white)
print(blue)