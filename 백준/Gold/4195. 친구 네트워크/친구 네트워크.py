import sys
input = lambda : sys.stdin.readline()

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(dic[a])
    b = find(dic[b])
    if a < b :
        parent[b] = a
        groupSize[a] += groupSize[b]
        groupSize[b] = 0
    elif a > b :
        parent[a] = b
        groupSize[b] += groupSize[a]
        groupSize[a] = 0
    ans.append(max(groupSize[a], groupSize[b]))
    return 
     

def checkAndAdd(x : str):
    if not x in dic :
        newIndex = len(groupSize)
        dic[x] = newIndex
        parent.append(newIndex)
        groupSize.append(1)
    return

ans = []
T = int(input())
for _ in range(T):
    F = int(input())
    dic = {}
    parent = []
    groupSize = []
    for _ in range(F):
        a, b = input().split()
        checkAndAdd(a)
        checkAndAdd(b)
        union(a, b)
        
print(*ans, sep='\n')