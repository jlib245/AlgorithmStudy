def num(n):
    res = 0
    for i in range(K):
        res += have[i] // n
    return res

def search(min_, start, end):
    mid = (start+end)//2

    a = num(mid)

    if a < min_:
        ns = start
        ne = mid - 1
    else:
        ns = mid
        ne = end
        
    if start == ns and end == ne:
        if num(end) >= min_:
            return end
        else:
            return start

    return search(min_, ns, ne)

K, N = map(int, input().split())

have = []
max_ = 0
for i in range(K):
    n = int(input())
    if max_ < n:
        max_ = n
    have.append(n)

res = search(N, 1, max_)
print(res)