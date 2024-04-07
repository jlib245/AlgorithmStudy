from collections import deque

M, N = map(int, input().split())
tom= []

queue = deque([])

for i in range(N):
    newL = list(map(int, input().split()))
    tom.append(newL)
    
    for j in range(M):
        if newL[j] == 1:
            queue.append((i,j))        

dy = [0,1,0,-1]
dx = [1,0,-1,0]

while queue:
    y,x = queue.popleft()
    d = tom[y][x]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny< N and 0 <= nx < M and tom[ny][nx] == 0:
            tom[ny][nx] = d + 1
            queue.append((ny, nx))

mx = 0
every = True
for i in range(N):
    for j in range(M):
        this = tom[i][j]
        if mx < this:
            mx = this
        elif this == 0:
            every = False

if not every:
    print(-1)
else:
    print(mx-1)