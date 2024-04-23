import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pack = 10000
one = 10000
for i in range(M):
    p, o = map(int, input().split())
    if pack > p :
        pack = p
    if one > o:
        one = o

if pack >= one * 6:
    result = one * N
else :
    a = N // 6
    b = N % 6
    if pack <= one * b:
        result = pack * (a+1)
    else :
        result = pack * a + one * b

print(result)