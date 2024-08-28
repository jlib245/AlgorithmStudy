import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        tree[node] = (lst[s], s)
        return tree[node]
    
    mid = (s + e) // 2
    left = init(s, mid, node*2)
    right = init(mid+1, e, node*2+1)
    tree[node] = min(left, right)
    return tree[node]

def update(val, idx, s, e, node) :
    if s == e :
        lst[idx] = val
        tree[node] = (val, idx)
        return 
    mid = (s + e) // 2
    if idx <= mid :
        update(val, idx, s, mid, node*2)
    else :
        update(val, idx, mid+1, e, node*2+1)

    tree[node] = min(tree[node*2], tree[node*2+1])
    return

MAX = (10**9+1, 10**9+1)
def calc(l, r, s, e, node) :
    if r < s or e < l :
        return MAX
    if l <= s and e <= r :
        return tree[node]
    mid = (s + e) // 2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r , mid+1, e, node*2+1)
    return min(left, right)

N = int(input())
tree = [0] * N*4
lst = [0] + list(map(int, input().split()))
init(1, N, 1)
M = int(input())
for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1 :
        update(c, b, 1, N, 1)
    else :
        val, idx = calc(b, c, 1, N, 1)
        print(idx)