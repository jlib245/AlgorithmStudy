from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

lines = []
dots = []
for i in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))
    dots.append(x)
    dots.append(y)

dots = sorted(dots)
sweep = deque()
for i in range(len(dots)-1):
    sweep.append((dots[i], dots[i+1]))
lines = deque(sorted(lines))

ans = 0
while sweep and lines :
    x, y = lines.popleft()
    while sweep :
        sx, sy = sweep.popleft()
        if y <= sx :
            sweep.appendleft((sx, sy))
            break
        
        if x <= sx and sy <= y :
            ans += sy - sx
print(ans)