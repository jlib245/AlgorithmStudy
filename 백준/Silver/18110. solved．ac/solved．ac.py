import sys
input = sys.stdin.readline
from collections import deque

def newR(num):
    a = num // 1
    b = num % 1
    if b >= 0.5:
        return int(a + 1)
    else:
        return int(a)

n = int(input())
if n == 0:
    print('0')
else:
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    DQ = deque(lst)
    dot = newR(n*0.15)
    for i in range(dot):
        DQ.popleft()
        DQ.pop()
    print(newR(sum(DQ)/len(DQ)))