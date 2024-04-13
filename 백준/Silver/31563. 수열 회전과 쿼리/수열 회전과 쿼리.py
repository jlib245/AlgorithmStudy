
import sys
input = sys.stdin.readline




N, Q = map(int, input().split())

A = list(map(int, input().split()))

for i in range(1, N):
    A[i] += A[i-1]

B = A[-1]

d = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        d += q[1]
    elif q[0] == 2:
        d -= q[1]
    else :
        si = q[1]-2-d
        ei = q[2]-1-d
        if si >= N:
            si %= N
        elif si < -N:
            si = -(-si%N)
        if ei >= N:
            ei %= N
        elif ei < -N:
            ei = -(-ei%N)
        start = A[si]
        end = A[ei]
        if end > start: 
            print(end - start)
        else:
            print(end + B - start)