from collections import deque
lst = deque(input().split())
n = int(lst.popleft())
res = []
while lst:
    res.append(int(lst.popleft()[::-1]))
while len(res) < n:
    lst = deque(input().split())
    while lst:
        res.append(int(lst.popleft()[::-1]))
res.sort()
print(*res, sep='\n')    