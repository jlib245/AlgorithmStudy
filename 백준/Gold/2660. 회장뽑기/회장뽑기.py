import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    Q = deque([(num,0)])
    visit = [False for _ in range(N+1)]
    maxScore = 0
    visit[num] = True
    while Q:
        x,score = Q.popleft()

        for nx in edge[x]:
            if not visit[nx]:
                visit[nx] = True
                nScore = score + 1
                Q.append((nx,nScore))
                if maxScore < nScore:
                    maxScore = nScore

    TF = True
    return maxScore

    
N = int(input())
edge = [[] for _ in range(N+1)]
while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    edge[a].append(b)
    edge[b].append(a)

score = [10000 for _ in range(N+1)]
totalMin = 10000
for i in range(1, N+1):
    iMin = bfs(i)
    score[i] = iMin
    if totalMin > iMin:
        totalMin = iMin

res = []
cnt = 0
for i in range(1, N+1):
    if score[i] == totalMin:
        res.append(i)
        cnt += 1

print(totalMin, cnt)
print(*res)