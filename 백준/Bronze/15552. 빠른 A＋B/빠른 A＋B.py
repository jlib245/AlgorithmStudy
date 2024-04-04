import sys
N = int(input())
input = sys.stdin.readline
for i in range(N):
    a, b = map(int, input().split())
    print(a+b)