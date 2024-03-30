def bfs(start, end):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    q = [start]
    n = 0
    while q:
        x, y = q.pop(0)       
        for i in range(8):
            if (x,y) == end:
                return visit[x][y]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < I and 0 <= ny < I and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
for i in range(int(input())):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    visit = [[0]*I for i in range(I)]
    print(bfs(start, end))