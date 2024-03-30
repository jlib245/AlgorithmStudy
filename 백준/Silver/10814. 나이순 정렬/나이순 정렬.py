import sys
input = sys.stdin.readline
N = int(input())
L = []
for i in range(N):
    J = input().rstrip().split()
    L.append([int(J[0]), i, J[1]])
L.sort()
for i in L:
    print(i[0], i[2])
