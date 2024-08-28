import sys, math
input = sys.stdin.readline

def find(x) :
    if not parent[x] == x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return False
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return True


n = int(input())
dot = []
for i in range(n) :
    x, y = map(float, input().split())
    dot.append((x,y))
line = []
for i in range(n):
    for j in range(i+1, n) :
        line.append((i, j, math.sqrt((dot[i][0]-dot[j][0])**2 + (dot[i][1]-dot[j][1])**2)))
line.sort(key=lambda x : x[2])

parent = [i for i in range(n)]
ans = 0
for i in range(len(line)) :
    a, b, d = line[i]
    if union(a, b) :
        ans += d
print(ans)