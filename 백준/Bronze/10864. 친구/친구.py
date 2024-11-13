N, M = map(int, input().split())
lst = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    lst[A] += 1
    lst[B] += 1

for i in range(1, N+1):
    print(lst[i])