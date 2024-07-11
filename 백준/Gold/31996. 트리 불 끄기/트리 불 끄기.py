import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
def change(node, des):
    if S[node] :
        S[node] = 0
    else:
        S[node] = 1
    route.append(des)
    return

def dfs2(node : int, parent : int):
    for child in tree[node]:
        if child != parent :
            change(node, child)
            dfs2(child, node)
    if parent:
        if not S[node]:
            change(node, parent)
            change(parent, node)
        change(node, parent)
    else:
        if S[node]:
            change(node, child)
    return
        
N, a = map(int, input().split())
S = [0]+list(map(int, list(input())))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
route = []
dfs2(a, 0)

print(len(route))
print(*route)