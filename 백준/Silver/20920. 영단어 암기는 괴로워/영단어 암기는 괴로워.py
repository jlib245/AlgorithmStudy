import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

dic = defaultdict(int)
N, M = map(int, input().split())
set_ = set()
for i in range(N):
    s = input()
    if len(s) >= M :
        set_.add(s)
        dic[s] += 1
word = sorted(list(set_), key=lambda x : (-dic[x], -len(x), x))
print(*word, sep='\n')