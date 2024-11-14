import sys
input = sys.stdin.readline

N = int(input())
lst = list()
for i in range(N):
    x, r = map(int, input().split())
    lst.append((x-r, x, r, i))
    lst.append((x+r, x, r, i))

lst.sort()

def check(a : tuple, b : tuple) -> bool:
    if a[3] == b[3] :
        return True
    
    tr1, x1, r1, tr2 = a
    tr1, x2, r2, tr2 = b
    d = abs(x1-x2)

    if abs(r1-r2) <= d <= r1 + r2 :
        return False
    return True
    
    
for i in range(1, 2*N-1):
    if not (check(lst[i-1], lst[i]) and check(lst[i], lst[i+1])) :
        print("NO")
        break
else :
    print("YES")