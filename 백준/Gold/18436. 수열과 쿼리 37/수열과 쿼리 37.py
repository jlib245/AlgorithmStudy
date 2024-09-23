import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        if A[s] % 2 == 0 :
            tree[node] = (1, 0)
        else :
            tree[node] = (0, 1)
        return tree[node]
    
    mid = (s+e) // 2
    left = init(s, mid, node*2)
    right = init(mid+1, e, node*2+1)
    tree[node] = tuple(sum(x) for x in zip(left, right))
    return tree[node]

def update(idx, val, s, e, node):
    if s == e :
        if val % 2 == A[idx] % 2 :
            tmp = (0, 0)
        elif val % 2 == 0 :
            tree[node] = (1, 0)
            tmp = (1, -1)
        else :
            tree[node] = (0, 1)
            tmp = (-1, 1)
        A[idx] = val
        return tmp
    
    mid = (s+e) // 2
    if idx <= mid :
        tmp = update(idx, val, s, mid, node*2)
    else :
        tmp = update(idx, val, mid+1, e, node*2+1)
    tree[node] = tuple(sum(x) for x in zip(tree[node], tmp))
    return tmp

def calc(l, r, s, e, node) :
    if r < s or e < l :
        return (0, 0)
    if l <= s and e <= r :
        return tree[node]
    
    mid = (s+e) // 2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r, mid+1, e, node*2+1)
    return tuple(sum(x) for x in zip(left, right))
        

N = int(input())
A = [0] + list(map(int, input().split()))
tree = [(0, 0)]*(N*4)
init(1, N, 1)

M = int(input())
ans = []
for _ in range(M) :
    q, a, b = map(int, input().split())
    if q == 1 :
        update(a, b, 1, N, 1)
    elif q == 2 :
        ans.append(calc(a, b, 1, N, 1)[0])
    else :
        ans.append(calc(a, b, 1, N, 1)[1])

print(*ans, sep='\n')