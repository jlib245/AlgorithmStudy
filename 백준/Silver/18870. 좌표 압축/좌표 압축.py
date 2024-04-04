import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
S = sorted(set(X))
D = dict()
for i in range(len(S)):
    D[S[i]] = i
for i in X:
    print(D[i], end=' ')