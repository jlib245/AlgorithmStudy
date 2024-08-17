import sys, heapq
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict
sys.setrecursionlimit(10**5)

def heappop(n):
    a = "pass"
    if n == 1 :
        if maxQ :
            a = -heapq.heappop(maxQ)
    elif n == -1 :
        if minQ :
            a = heapq.heappop(minQ)
    if a != "pass" :
        if not dic[a] :
            return (heappop(n))
        else :
            dic[a] -= 1
            return a
    return "pass"

ans = []
T = int(input())
for _ in range(T):
    minQ = []
    maxQ = []
    dic = defaultdict(int)
    k = int(input())
    for _ in range(k):
        s = input().split()
        q = s[0]
        n = int(s[1])
        if q == 'I':
            heapq.heappush(minQ, n)
            heapq.heappush(maxQ, -n)
            dic[n] += 1
        elif q == 'D':
            heappop(n)
    
    empty = True
    for i in dic:
        if dic[i] :
            empty = False
            break
    if empty :
        ans.append(("EMPTY", ))
    else :
        min_ = heappop(-1)
        max_ = heappop(1)
        if max_ == "pass":
            max_ = min_
        ans.append((max_, min_))

for row in ans :
    print(*row)