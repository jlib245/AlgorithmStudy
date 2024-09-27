import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = [input() for _ in range(N)]
mobis = ['M', 'O', 'B', 'I', 'S']
dr = (0, -1, -1, -1, 0, 1, 1, 1)
dc = (1, 1, 0, -1, -1, -1, 0, 1)
ans = 0
for r in range(N):
    for c in range(N):
        for i in range(8):
            nr = r
            nc = c
            for j in range(5):
                if 0 <= nr < N and 0 <= nc < N :
                    if lst[nr][nc] == mobis[j] :
                        nr += dr[i]
                        nc += dc[i]
                    else :
                        break
                else :
                    break
            else :
                ans += 1
print(ans)