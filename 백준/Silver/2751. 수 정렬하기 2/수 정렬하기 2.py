import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
print(*sorted(lst))