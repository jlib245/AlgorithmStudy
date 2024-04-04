import sys
input = sys.stdin.readline

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
    dot = newR(n*0.15)
    sum_ = 0
    cnt = 0
    for i in range(dot, n-dot):
        sum_ += lst[i]
        cnt += 1
    print(newR(sum_/cnt))