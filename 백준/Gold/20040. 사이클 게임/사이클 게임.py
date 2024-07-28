import sys
input = sys.stdin.readline

def find(x):
    while x != parent[x] :
        x = parent[x]
    return x

def cycle(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        return True
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return False

n, m = map(int, input().split())

parent = [i for i in range(n)]
q = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(m):
    a, b = q[i]
    if cycle(a, b) :
        print(i+1)
        break
else :
    print(0)