import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
score = [0]+list(map(int, input().split()))
max_ = 0
max_num = 10**6
for _ in range(M):
    lst = input().split()
    num = int(lst[0])
    s = 0
    for i in range(1, N+1):
        if lst[i] == 'O' :
            s += score[i]
    if max_ < s or max_ == s and max_num > num :
        max_ = s
        max_num = num
print(max_num, max_)