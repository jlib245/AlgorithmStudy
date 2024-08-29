import sys
input = sys.stdin.readline

def init(s, e, node) :
    if s == e :
        tree[node] = (lst[s], lst[s])
        return tree[node]
    mid = (s+e) // 2
    leftMin, leftMax = init(s, mid, node*2)
    rightMin, rightMax = init(mid+1, e, node*2+1)
    tree[node] = (min(leftMin, rightMin), max(leftMax, rightMax))
    return tree[node]
def calc(l, r, s, e, node) :
    if e < l or r < s :
        return (INF, -1)
    if l <= s and e <= r :
        return tree[node]
    mid = (s+e)//2
    leftMin, leftMax = calc(l, r, s, mid, node*2)
    rightMin, rightMax = calc(l, r, mid+1, e, node*2+1)
    return (min(leftMin, rightMin), max(leftMax, rightMax))

N, M = map(int, input().split())
lst = [0]
for i in range(N):
    lst.append(int(input()))
tree = [0]*N*4
init(1, N, 1)
ans = []
INF = 1000000001
for i in range(M):
    a, b = map(int, input().split())
    ans.append(calc(a, b, 1, N, 1))
for row in ans :
    print(*row)