N, M = map(int, input().split())
lst = [[0]*M for _ in range(N)]
dr = (1, 1, 0, -1, -1, -1, 0, 1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)
K = 0
for r in range(N) :
    for c in range(M):
        a = 0
        TF = False
        while not TF :
            TF = True
            a += 1
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] == a :
                        TF = False
        lst[r][c] = a
        if K < a :
            K = a

print(K)
for row in lst :
    print(*row)