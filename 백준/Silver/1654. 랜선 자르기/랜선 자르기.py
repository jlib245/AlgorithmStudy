import sys
input = sys.stdin.readline

def check(n, min_):
    res = 0
    for i in range(K):
        res += have[i] // n
    if res < min_:
        return False
    else:
        return True

def search(lo, hi, min_):
    if lo + 1 == hi:
        return lo
    mid = (lo + hi) // 2
    if check(mid, min_) :
        lo = mid
    else :
        hi = mid
    return search(lo, hi, min_)


K, N = map(int, input().split())
have = []
max_ = 0
for i in range(K):
    n = int(input())
    if max_ < n:
        max_ = n
    have.append(n)

res = search(1, max_+1, N)
print(res)