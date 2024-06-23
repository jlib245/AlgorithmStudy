from collections import deque
N = int(input())
if N > 5:
    print(3)
    exit()
q = deque([1])
for i in range(2, N+1):
    cnt = 0
    nq = deque()
    while q:
        now = q.popleft()
        cnt = 1
        while q and q[0] == now:
            q.popleft()
            cnt += 1
        nq.append(now)
        nq.append(cnt)
    q = nq

print(max(q))