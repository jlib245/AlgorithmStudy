import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        tree[node] = lst[s]
        return tree[node]

    mid = (s+e)//2
    left = init(s, mid, node*2)
    right = init(mid+1, e, node*2+1)
    tree[node] = left + right
    return tree[node]

def update(idx, val, s, e, node) :
    if s == e :
        tree[node] = val
        lst[idx] = val
        return
    
    mid = (s+e)//2
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
    
    mid = (s+e)//2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r, mid+1, e, node*2+1)
    return left+right

N, Q = map(int, input().split())

lst = [0] + list(map(int, input().split()))
tree = [0]*N*4
init(1, N, 1)

ans = []
for i in range(Q) :
    x, y, a, b = map(int, input().split())
    if x > y :
        x, y = y, x
    ans.append(calc(x, y, 1, N, 1))
    update(a, b, 1, N, 1)

print(*ans, sep='\n')