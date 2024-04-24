import sys
input = sys.stdin.readline

N, M = map(int, input().split())

setN = set()
for _ in range(N):
    s = input().rstrip()
    setN.add(s)

setM = set()
cnt = 0
for _ in range(M):
    s = input().rstrip()
    if s in setN:
        cnt += 1

print(cnt)