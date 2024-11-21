from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs() -> int :
    Q = deque([(0,0,0)])
    dxy = (-2, -1, 0, 1, 2)
    while Q :
        x, y, d = Q.popleft()
        for i in range(5):
            for j in range(5):
                nx = x + dxy[i]
                ny = y + dxy[j]
                if (nx, ny) in visit and not visit[(nx, ny)] :
                    visit[(nx, ny)] = True
                    Q.append((nx, ny, d+1))
                    if ny == T :
                        return d+1
    return -1

n, T = map(int, input().split())
visit = defaultdict(bool)
for _ in range(n):
    x, y = map(int, input().split())
    visit[(x,y)] = False

ans = bfs()
print(ans)