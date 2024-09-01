import sys
input = sys.stdin.readline

def update(idx, val, s, e, node) :
    if s == e :
        tree[node] = val
        return
    mid = (s+e) // 2
    if idx <= mid :
        update(idx, val, s, mid, node*2)
    else :
        update(idx, val, mid+1, e, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def calc(l, r, s, e, node) :
    if e < l or r < s :
        return 0
    if l <= s and e <= r :
        return tree[node]
    mid = (s+e) // 2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r, mid+1, e, node*2+1)
    return left + right

N, M = map(int, input().split())
lst = [0]*(N+1)
tree = [0]*N*4
ans = []
for _ in range(M) :
    q, a, b = map(int, input().split())
    if not q :
        if a > b :
            a, b = b, a
        ans.append(calc(a, b, 1, N, 1))
    else :
        update(a, b, 1, N, 1)
print(*ans, sep='\n')