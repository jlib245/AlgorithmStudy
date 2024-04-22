import sys
input = sys.stdin.readline

n = int(input())

set_ = set()
for _ in range(n):
    s, q = input().split()
    
    if q == 'enter':
        set_.add(s)
    elif q == 'leave':
        set_.remove(s)

lst = list(set_)
lst.sort(reverse=True)

for i in lst:
    print(i)