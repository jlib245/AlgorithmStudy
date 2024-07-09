import sys
input = sys.stdin.readline
cnt = 1
while 1:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    a = V // P
    b = V % P
    if b > L:
        b = L
    print(f"Case {cnt}: {a*L+b}")
    cnt += 1