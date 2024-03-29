A, B = input().split()
n = max(len(A), len(B))
aL = [0] * n
bL = [0] * n
for i in range(n):
    try:
        aL[i] = A[-1-i]
    except:
        aL[i] = 0
    try:
        bL[i] = B[-1-i]
    except:
        bL[i] = 0
o = 0
result = []
for i in range(n):
    hap = int(aL[i]) + int(bL[i]) + o
    result.append(hap%10)
    o = hap // 10
if o == 1:
    result.append(o)
for i in range(len(result)):
    print(result[-i-1], end = '')