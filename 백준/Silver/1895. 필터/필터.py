import sys
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(R)]
T = int(input())
midList = []
ans = 0
for i in range(R-2):
    for j in range(C-2):
        lst = []
        for di in range(3):
            for dj in range(3):
                lst.append(mtrx[i+di][j+dj])
        lst.sort()
        mid = lst[4]
        if mid >= T :
            ans += 1
print(ans)