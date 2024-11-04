import sys
input = sys.stdin.readline

def check(x : int, li : int) -> bool:
    if LIS[li] >= x :
        return True
    return False

def binarySearch(lo : int, hi : int, x : int)-> None:
    if lo + 1 == hi :
        LIS[hi] = x
        return
    
    mid = (lo+hi)//2
    
    if check(x, mid):
        hi = mid
    else :
        lo = mid

    binarySearch(lo, hi, x)
    return

N = int(input())
lst = list(map(int, input().split()))
LIS = [lst[0]]
for i in range(1, N):
    if LIS[-1] < lst[i]:
        LIS.append(lst[i])
    else:
        binarySearch(-1, len(LIS)-1, lst[i])

ans = len(LIS)
print(ans)