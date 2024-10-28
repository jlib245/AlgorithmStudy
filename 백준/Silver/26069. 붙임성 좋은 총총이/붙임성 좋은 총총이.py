import sys
input = lambda : sys.stdin.readline().rstrip()

set_ = {"ChongChong"}
N = int(input())
for _ in range(N):
    a, b = input().split()
    if a in set_ :
        set_.add(b)
    elif b in set_ :
        set_.add(a)

print(len(set_))