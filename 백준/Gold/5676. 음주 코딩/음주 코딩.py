import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        tree[node] = lst[s]
        if not tree[node] :
            return 0
        return tree[node] // abs(tree[node])
    mid = (s+e) // 2
    left = init(s, mid, node*2)
    right = init(mid+1, e, node*2+1)
    tree[node] = left * right 
    if not tree[node] :
        return 0
    return tree[node] // abs(tree[node])

def update(val, idx, s, e, node) :
    if s == e :
        tree[node] = val
        lst[idx] = val
        return
    mid = (s+e)//2
    if idx <= mid :
        update(val, idx, s, mid, node*2)
    else :
        update(val, idx, mid+1, e, node*2+1)
    a = tree[node*2] * tree[node*2+1]
    if a :
        tree[node] = a // abs(a)
    else :
        tree[node] = a
    return 

def calc(l, r, s, e, node) :
    if e < l or r < s :
        return 1
    if l <= s and e <= r :
        return tree[node]
    mid = (s+e)//2
    left = calc(l, r, s, mid, node*2)
    right = calc(l, r, mid+1, e , node*2+1)
    a = left*right
    if not a :
        return 0
    return a // abs(a)

ans = []
while 1 :
    try :
        N, K = map(int, input().split())
    except :
        break
    lst = [0] + list(map(int, input().split()))
    tree = [1]* N * 4
    init(1, N, 1)
    res = []
    for i in range(K):
        s = input().split()
        q = s[0]
        a, b = map(int, s[1:])
        if q == 'C' :
            update(b, a, 1, N, 1)
        else :
            a = calc(a, b, 1, N, 1)
            if a > 0 :
                res.append('+')
            elif a == 0 :
                res.append('0')
            else :
                res.append('-')
    ans.append(res)
for row in ans :
    print(*row, sep='')