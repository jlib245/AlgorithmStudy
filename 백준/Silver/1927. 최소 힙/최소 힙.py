import heapq
import sys
input = sys.stdin.readline
H = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        if H == []:
            print(0)
        else:
            print(heapq.heappop(H))
    else:
        heapq.heappush(H, a)