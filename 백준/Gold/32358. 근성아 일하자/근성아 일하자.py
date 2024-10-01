import sys, heapq
input = sys.stdin.readline

def cleaning(pos) :
    res = 0
    while leftHeap or rightHeap :
        near = []
        if leftHeap :
            x = -heapq.heappop(leftHeap)
            heapq.heappush(near, (abs(pos-x), x, 0))
        if rightHeap :
            x = heapq.heappop(rightHeap)
            heapq.heappush(near, (abs(pos-x), x, 1))

        nxtDistance, nxtPos, trash = heapq.heappop(near)
        res += nxtDistance
        pos = nxtPos
        
        if near :
            # LR : L == 0, R == 1
            trash, addPos, LR = heapq.heappop(near)
            if not LR :
                heapq.heappush(leftHeap, -addPos)
            else :
                heapq.heappush(rightHeap, addPos)
    return res, pos

N = int(input())
pos = 0
leftHeap = []
rightHeap = []
ans = 0
for _ in range(N):
    s = list(map(int, input().split()))
    q = s[0]
    if q == 1 :
        x = s[1]
        if x < pos :
            heapq.heappush(leftHeap, -x)
        else :
            heapq.heappush(rightHeap, x)
    elif q == 2 :
        distance, pos = cleaning(pos)
        ans += distance
print(ans)