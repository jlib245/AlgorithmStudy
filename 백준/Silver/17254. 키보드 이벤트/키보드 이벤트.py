import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lst = []
for _ in range(M):
    a,b,c = input().split()
    na, nb = int(a), int(b)
    lst.append((nb,na,c))
lst.sort()
res = ''
for t1, t2, c in lst:          
    res += c

print(res)