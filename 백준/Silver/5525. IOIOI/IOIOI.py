N = int(input())
M = int(input())
A = input()
P = ('IO'*(N+1))[:-1]
result = 0
for i in range(M):
    if A[i] == 'I' and A[i:i+1+N*2] == P:
        result += 1
print(result)