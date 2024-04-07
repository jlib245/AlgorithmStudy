from collections import deque

N = int(input())
M = int(input())

#누를 수 있는 숫자 패드
num = set(range(10))
if M != 0:
    rm = set(map(int, input().split()))
    num = num - rm

visit = [-1]*11111111
queue = deque([N])
visit[N] = 0
rslt = []
while queue:
    x = queue.popleft()
    cnt = visit[x]
    # x가 100인 경우
    if x == 100:
        rslt.append(cnt)
        break
    elif x == 99 or x == 101:
        rslt.append(cnt+1)
        break
    # 리모콘으로 바로 이동 가능한 경우
    elif num:
        bl = True
        lst = list(map(int, str(x)))
        for i in lst:
            if i not in num:
                bl = False
                break
        if bl:
            rslt.append(cnt+len(str(x)))
            
    for nx in [x-1, x+1]:
        # 방문하지 않았거나 최소값으로 최신화 가능한 경우
        if nx >= 0 and (visit[nx] == -1 or visit[nx] > cnt+1):
            visit[nx] = cnt+1
            queue.append(nx)
print(min(rslt))