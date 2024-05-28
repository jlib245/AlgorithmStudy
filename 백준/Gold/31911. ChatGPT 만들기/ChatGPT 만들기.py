def f(c : chr):
    nxt = [0 for _ in range(2000)]
    for i in range(N):
        for j in range(len(lst[i])):
            if lst[i][j] == c and j+1 < len(lst[i]):
                nxt[ord(lst[i][j+1])] += 1

    llll = []
    for i in range(140):
        if nxt[i] :
            llll.append((-nxt[i], i))
    llll.sort()
    if llll:
        return chr(llll[0][1])
    else:
        return None
        
import sys
input = sys.stdin.readline
N, K, M = map(int, input().split())
lst = []
for i in range(N):
    lst.append(input().rstrip())

dd = []
for i in range(45, 140):
    dd.append(f(chr(i)))

res = '['
End = False
infin = False
for i in range(M+K):
    if not End and not infin:
        c = res[-1]
        nc = dd[ord(c)-45]
        if nc == ']':
            End = True
        if nc in res:
            infin = True
        else:
            res += nc
    elif End:
        infin = True
        Inf  = '.'
        noInf = res
        break
    else:
        for i in range(len(res)):
            if res[i] == nc:
                break
        noInf = res[:i]
        Inf = res[i:]
        break

K -= 1
O = M+K
if not infin:   
    print(res[K: M+K])
else:
    if K < len(noInf):
        t = noInf[K:]
        a = (O-len(noInf)) // len(Inf)
        b = (O-len(noInf)) % len(Inf)
        print(t, Inf*a, Inf[:b], sep='')
    else:
        a = (K-len(noInf))
        d = len(Inf) - a % len(Inf)
        b = (M-d) // len(Inf)
        c = (M-d) % len(Inf)
        print(Inf[a%len(Inf):], Inf*b, Inf[:c], sep='')