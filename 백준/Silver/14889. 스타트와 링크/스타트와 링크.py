import sys
from itertools import combinations
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

res = []
for start in combinations(range(N), N//2):
    link = [i for i in range(N) if not i in start]
    startScore = 0
    linkScore = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            startScore += lst[start[i]][start[j]] + lst[start[j]][start[i]]
            linkScore += lst[link[i]][link[j]] + lst[link[j]][link[i]]
    res.append(abs(startScore-linkScore))

ans = min(res)
print(ans)