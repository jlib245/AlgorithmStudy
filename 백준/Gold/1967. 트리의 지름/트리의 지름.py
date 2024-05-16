import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def f(tup : tuple):
    node, w = tup

    if not tree[node]:
        return w
    l = []
    while tree[node] :
        t = tree[node].pop()
        dw = f(t)
        l.append(dw)
    l.sort(reverse=True)
    global res
    if len(l) == 1:
        a = l[0] + w
        if res < a:
            res = a
        return a
    a = l[0] + l[1]
    if res < a:
            res = a
    return l[0]+ w
    
n = int(input())

tree = [[] for i in range(n+1)]

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))

if n == 1:
    print(0)
    exit()

res = 0
f((1, 0))

print(res)