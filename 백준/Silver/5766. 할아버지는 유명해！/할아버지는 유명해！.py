import sys
from collections import defaultdict
input = sys.stdin.readline

while 1:
    n , m = map(int ,input().split())
    if n == m == 0:
        break
    dic = defaultdict(int)
    for _ in range(n):
        keys = list(map(int, input().split()))
        for key in keys:
            dic[key] += 1
    
    res = []
    for key, value in dic.items():
        res.append((key, value))
    res.sort(key=lambda x : (-x[1], x[0]))
    point = res[1][1]
    ans = [res[1][0]]
    for i in range(2, len(res)):
        if res[i][1] == point:
            ans.append(res[i][0])
        else:
            break
    print(*ans)