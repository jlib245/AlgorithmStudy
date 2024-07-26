import sys
input = sys.stdin.readline

n, k = map(int,input().split())

parent = [i for i in range(n)]
for _ in range(n-1):
    p, c = map(int,input().split())
    parent[c] = p

val = list(map(int,input().split()))

for i in range(len(val)):
    if val[i] == k :
        index = i
        break

degree = 0
while index != parent[index] :
    index = parent[index]
    degree += 1
    
print(degree)