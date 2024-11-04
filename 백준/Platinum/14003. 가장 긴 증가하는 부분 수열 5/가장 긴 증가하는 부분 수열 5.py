import sys
input = sys.stdin.readline

def check(x : int, li : int) -> bool:
    if LIS[li] >= x :
        return True
    return False

def binarySearch(lo : int, hi : int, x : int)-> None:
    while lo + 1 != hi :
        mid = (lo+hi)//2
        
        if check(x, mid):
            hi = mid
        else :
            lo = mid

    LIS[hi] = x
    idx.append(hi)
    return

N = int(input())
lst = list(map(int, input().split()))
LIS = [lst[0]]
idx = [0]
for i in range(1, N):
    if LIS[-1] < lst[i]:
        idx.append(len(LIS))
        LIS.append(lst[i])
    else:
        binarySearch(-1, len(LIS)-1, lst[i])

revAns = []
cnt = len(LIS)-1
for i in range(len(idx)-1, -1, -1):
    if idx[i] == cnt :
        cnt -= 1
        revAns.append(lst[i])

ans = revAns[::-1]

print(len(ans))
print(*ans)