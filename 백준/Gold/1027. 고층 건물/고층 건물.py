import sys
input = sys.stdin.readline
def made_line(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    a = (y2 - y1) / (x2 - x1)
    return a

N = int(input())
lst = []
h = [0]+list(map(int,input().split()))
for i in range(1, N+1):
    lst.append((i, h[i]))
max_ = 0
for i in range(N):
    dot1 = lst[i]
    cnt = 0
    if i >= 1:
        cnt += 1
        a = made_line(dot1, lst[i-1])
    for j in range(i-2, -1, -1):
        newline = made_line(dot1, lst[j])
        if a > newline:
            cnt += 1
            a = newline
    if i < N-1:
        cnt += 1
        a = made_line(dot1, lst[i+1])
    for j in range(i+2, N):
        newline = made_line(dot1, lst[j])
        if a < newline: 
            cnt += 1
            a = newline
    if max_ < cnt:
        max_ = cnt
print(max_)