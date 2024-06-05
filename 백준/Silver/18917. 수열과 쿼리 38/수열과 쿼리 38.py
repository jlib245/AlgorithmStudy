import sys
input = sys.stdin.readline

M = int(input())

xor = 0
sum_ = 0
for _ in range(M):
    Q = list(map(int ,input().split()))
    if Q[0] == 1 :
        sum_ += Q[1]
        xor ^= Q[1]
    elif Q[0] == 2:
        sum_ -= Q[1]
        xor ^= Q[1]
    elif Q[0] == 3:
        print(sum_)
    else:
        print(xor)