import sys
input = sys.stdin.readline

N = int(input())
l = []
res = 0
for i in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l.append([q[1], q[2]])
    if l:
        l[-1][1] -= 1
        if l[-1][1] == 0:
            res += l[-1][0]
            l.pop()
print(res)