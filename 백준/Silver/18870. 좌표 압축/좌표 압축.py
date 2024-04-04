import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
S = list(set(X))
S.sort()
D = dict()
for i in range(len(S)):
    D[str(S[i])] = i
for i in X:
    print(D[str(i)], end=' ')