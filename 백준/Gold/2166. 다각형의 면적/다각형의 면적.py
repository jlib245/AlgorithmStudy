import sys
input = sys.stdin.readline

N = int(input())
dots = []
for _ in range(N) :
    dots.append(tuple(map(int, input().split())))

a = 0
b = 0
for i in range(N):
    a += dots[i][0]*dots[i-1][1]
    b += dots[i][1]*dots[i-1][0]

S = round(abs((a - b)) / 2, 1)
print(S)