import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [0]*(N+1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        lst[n] = k

print(*lst[1:])