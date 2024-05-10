n, m = map(int ,input().split())

P = 1
div = 1
for i in range(1, m+1):
    P *= n-i+1
    div *= i
    
res = P//div
print(res)