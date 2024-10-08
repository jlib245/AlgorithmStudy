import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
cnt = 1
max_ = lst[0]
maxCnt = 1
prev = lst[0]
for i in range(1, N) :
    if lst[i] == prev :
        cnt += 1
    else :
        if maxCnt < cnt :
            maxCnt = cnt
            max_ = prev
        cnt = 1
        prev = lst[i]
if maxCnt < cnt :
    maxCnt = cnt
    max_ = prev
print(max_)