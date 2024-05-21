def f(n):
    if n == removeNode:
        return
    cnt = 0
    for i in tree[n]:
        if i != removeNode:
            f(i)
            cnt += 1
    if not cnt:
        global res
        res+= 1
    return

N = int(input())

parent = list(map(int, input().split()))

tree = [[] for _ in range(N)]
root = 0
for i in range(N):
    if parent[i] == -1:
        root = i
        continue
    tree[parent[i]].append(i)

removeNode = int(input())
res = 0
f(root)
print(res)