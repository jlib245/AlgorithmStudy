import sys
input = sys.stdin.readline

N = int(input())

lst = []
for i in range(N):
    s, e = map(int, input().split())
    lst.append((e, s))
lst.sort()

cnt = 0
end = -1
for i in lst:
    if end <= i[1]:
        end = i[0]
        cnt += 1

print(cnt)