import sys
input = sys.stdin.readline

def check(x) :
    cnt = 0
    for go in greenOnion :
        if go < x :
            break
        cnt += go // x
        if cnt >= C :
            return True
    return False

def ramen(x) :
    res = sum(greenOnion) - x * C
    return res
 
def BinarySearch(s, e) :
    if s+1 == e :
        return ramen(s)
    mid = (s + e) // 2
    if check(mid) :
        return BinarySearch(mid, e)
    return BinarySearch(s, mid)
    

S, C = map(int, input().split())
greenOnion = []
for _ in range(S) :
    L = int(input())
    greenOnion.append(L)
greenOnion.sort(reverse=True)
ans = BinarySearch(1, 10**9+1)
print(ans)