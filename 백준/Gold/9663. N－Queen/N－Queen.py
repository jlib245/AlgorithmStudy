def f(r):
    # 백트래킹, 끝에 도달했을 때 cnt += 1
    if r == N-1:
        return 1
    
    nr = r + 1
    cnt = 0
    for nc in range(N):
        # 세로 체크 (가로는 체크할 필요 x)
        possible = True
        for i in range(nr):
            if visit[i][nc]:
                possible = False
                break
        if possible:
            # 대각선 체크
            for i in range(nr):
                c1 = nc - (nr - i)
                c2 = nc + (nr - i)
                if 0 <= c1 < N and visit[i][c1] or 0 <= c2 < N and visit[i][c2]:
                    possible = False
                    break
        if possible:
            visit[nr][nc] = True
            cnt += f(nr)
            visit[nr][nc] = False
    return cnt
    
N = int(input())

visit = [[False]*N for _ in range(N)]
cnt = f(-1)

print(cnt)