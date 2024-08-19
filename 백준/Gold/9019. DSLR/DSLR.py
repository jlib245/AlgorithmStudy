import sys
input = lambda : sys.stdin.readline()
from collections import deque

def D(n : int):
    return 2*n%10000

def S(n : int):
    if n == 0 :
        return 9999
    return n-1

def L(n : int):
    return n % 1000 * 10 + n // 1000

def R(n : int):
    return n % 10 * 1000 + n // 10

def DSLR(A, B):
    Q = deque([(A, "")])
    visit = set()
    while Q :
        x, q = Q.popleft()
        l = [(D(x), 'D'), (S(x), 'S'), (L(x), 'L'), (R(x), 'R')]
        for nx, dq in l :
            nq = q + dq
            if not nx in visit :
                visit.add(nx)
                Q.append((nx, nq))
                if nx == B :
                    return nq

T = int(input())
ans = []
for _ in range(T):
    A, B = map(int, input().split())
    ans.append(DSLR(A, B))

print(*ans, sep='\n')