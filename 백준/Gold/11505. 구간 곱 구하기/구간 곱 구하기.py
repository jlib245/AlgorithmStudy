import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        tree[node] = lst[s]
        return tree[node]
    
    mid = (s + e) // 2
    left = init(s, mid, node*2)
    right = init(mid+1, e, node*2+1)
    tree[node] = left * right % MAX
    return tree[node]

def update(val, idx, s, e, node) :
    if s == e :
        tree[node] = val
        lst[idx] = val
        return
    mid = (s+e) // 2
    if idx <= mid :
        update(val, idx, s, mid, node*2)
    else :
        update(val, idx, mid+1, e, node*2+1)
    tree[node] = tree[node*2] * tree[node*2+1] % MAX
    return

def calc(l, r, s, e, node) :
    if e < l or r < s :
        return 1
    if l <= s and e <= r :
        return tree[node]
    mid = (s+e) // 2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r, mid+1, e, node*2+1)
    return left * right % MAX

N, M, K = map(int, input().split())
tree = [1]* N*4
lst = [0]
for i in range(N):
    lst.append(int(input()))
MAX = 1000000007
init(1, N, 1)
for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1 :
        update(c, b, 1, N, 1)
    else :
        print(calc(b, c, 1, N, 1))