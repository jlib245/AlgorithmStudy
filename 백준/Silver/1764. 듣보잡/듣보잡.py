import sys
N, M = map(int, input().split())
NL = []
ND = {}
result = []
for i in range(N):
    a  = sys.stdin.readline().rstrip()
    NL.append(a)
    ND[a] = 1
for i in range(M):
    a = sys.stdin.readline().rstrip()
    if a in ND.keys():
        result.append(a)
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])