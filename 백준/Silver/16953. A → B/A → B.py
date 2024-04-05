from collections import deque

A, B = map(int, input().split())

queue = deque([(A, 1)])
while queue:
    p = queue.popleft()
    x = p[0]
    cnt = p[1]
    for nx in [x*2, x*10+1]:
        if nx <= B :
            queue.append((nx, cnt+1))
            if nx == B:
                print(cnt+1)
                exit()
print(-1)