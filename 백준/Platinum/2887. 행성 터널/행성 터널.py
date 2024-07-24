import sys
input = sys.stdin.readline

def find(n):
    while n != parent[n]:
        n = parent[n]
    return n

def union(a, b, cost):
    a = find(a)
    b = find(b)
    if a == b :
        return 0
    elif a < b :
        parent[b] = a
    else :
        parent[a] = b
    return cost

N = int(input())

point = []
for _ in range(N):
    point.append(tuple(map(int,input().split())))
xSort = sorted([i for i in range(N)], key=lambda x : point[x][0])
ySort = sorted([i for i in range(N)], key=lambda x : point[x][1])
zSort = sorted([i for i in range(N)], key=lambda x : point[x][2])

line = []
for i in range(N-1):
    line.append((xSort[i], xSort[i+1], point[xSort[i+1]][0]-point[xSort[i]][0]))
    line.append((ySort[i], ySort[i+1], point[ySort[i+1]][1]-point[ySort[i]][1]))
    line.append((zSort[i], zSort[i+1], point[zSort[i+1]][2]-point[zSort[i]][2]))
line.sort(key=lambda x : x[2])

check = [False]*N
parent = [i for i in range(N)]
ans = 0
for p1, p2, cost in line :
    ans += union(p1, p2, cost)

print(ans)