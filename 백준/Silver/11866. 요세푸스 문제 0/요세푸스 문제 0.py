N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
result = []
s = 0
for _ in range(N):
    s = (s+K-1)%len(lst)
    result.append(lst.pop(s))

print("<", end='')
for i in range(N-1):
    print(f"{result[i]},", end=' ')
print(result[-1], end='')
print(">")