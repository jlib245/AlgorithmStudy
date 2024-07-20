from collections import deque
import sys
input = sys.stdin.readline

def tom():
    a = [0]*22
    dm = list(a)
    dm[0:2] = -1, 1
    dn = list(a)
    dn[2:4] = -1, 1
    do = list(a)
    do[4:6] = -1, 1
    dp = list(a)
    dp[6:8] = -1, 1
    dq = list(a)
    dq[8:10] = -1, 1
    dr = list(a)
    dr[10:12] = -1, 1
    ds = list(a)
    ds[12:14] = -1, 1
    dt = list(a)
    dt[14:16] = -1, 1
    du = list(a)
    du[16:18] = -1, 1
    dv = list(a)
    dv[18:20] = -1, 1
    dw = list(a)
    dw[20:22] = -1, 1
    Queue = deque(start)
    cnt = 0

    while Queue :
        m, n, o, p, q, r, s, t, u, v, w, d= Queue.popleft()
        if cnt < d:
            cnt = d
        for i in range(22):
            nm = m + dm[i]
            nn = n + dn[i]
            no = o + do[i]
            np = p + dp[i]
            nq = q + dq[i]
            nr = r + dr[i]
            ns = s + ds[i]
            nt = t + dt[i]
            nu = u + du[i]
            nv = v + dv[i]
            nw = w + dw[i]
            if 0 <= nm < M and 0 <= nn < N and 0 <= no < O and 0 <= np < P and 0 <= nq < Q and 0 <= nr < R and 0 <= ns < S and 0 <= nt < T and 0 <= nu < U and 0 <= nv < V and 0 <= nw < W:
                if not lst[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] :
                    Queue.append((nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw, d+1))
                    lst[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
    return cnt
M, N, O, P, Q, R, S, T, U, V, W = map(int,input().split())
lst = [[[[[[[[[[list(map(int,input().split())) for _ in range(N)] for _ in range(O)] for _ in range(P)]for _ in range(Q)] for _ in range(R)] for _ in range(S)]for _ in range(T)] for _ in range(U)]for _ in range(V)] for _ in range(W)]
start = []
onecnt = 0
for w in range(W):
    for v in range(V):
        for u in range(U):
            for t in range(T):
                for s in range(S):
                    for r in range(R):
                        for q in range(Q):
                            for p in range(P):
                                for o in range(O):
                                    for n in range(N):
                                        for m in range(M):
                                            i = lst[w][v][u][t][s][r][q][p][o][n][m]
                                            if i == 1:
                                                start.append((m, n, o, p, q, r, s, t, u, v, w, 0))
                                                onecnt += 1
                                            elif i == -1:
                                                onecnt += 1

if onecnt == M*N*O*P*Q*R*S*T*U*V*W:
    print(0)
    exit()

res = tom()

for w in range(W):
    for v in range(V):
        for u in range(U):
            for t in range(T):
                for s in range(S):
                    for r in range(R):
                        for q in range(Q):
                            for p in range(P):
                                for o in range(O):
                                    for n in range(N):
                                        for m in range(M):
                                            if lst[w][v][u][t][s][r][q][p][o][n][m] == 0:
                                                print(-1)
                                                exit()

print(res)