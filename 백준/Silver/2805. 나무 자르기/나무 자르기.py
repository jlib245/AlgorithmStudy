def check(num):
    take = 0
    for i in lst:
        if i - num > 0:
            take += i - num
    if take >= M:
        return True
    return False

def binarySearch(lo, hi):
    if lo + 1 == hi:
        return lo
    mid = (lo+hi)//2
    if check(mid) :
        lo = mid
    else :
        hi = mid
    return binarySearch(lo, hi)

N, M = map(int, input().split())
lst = list(map(int, input().split()))

res = binarySearch(0, 2000000001)
print(res)