import sys
input = sys.stdin.readline

n = int(input())
lst = [[]]
for _ in range(n):
    lst.append(list(map(int, input().split())))

cnt = [set() for _  in range(n+1)]
for i in range(5):
    for j in range(1, n+1):
        for k in range(j+1, n+1):
            if lst[j][i] == lst[k][i]:
                cnt[j].add(k)
                cnt[k].add(j)

max_ = 0
res = 1
for i in range(1, n+1):
    if max_ < len(cnt[i]):
        max_ = len(cnt[i])
        res = i

print(res)