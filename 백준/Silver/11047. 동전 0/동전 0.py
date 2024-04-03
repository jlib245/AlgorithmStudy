N, K = map(int, input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
result = 0
for i in lst:
    result  += K // i
    K %= i
print(result)