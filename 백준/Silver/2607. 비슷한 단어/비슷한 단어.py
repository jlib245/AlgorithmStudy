N = int(input())
first = input()
firstLst = [0 for _ in range(26)]
for c in first:
    firstLst[ord(c)-65] += 1

res = 0
for _ in range(N-1):
    newLst = [0 for _ in range(26)]
    new = input()
    for c in new:
        newLst[ord(c)-65] += 1
    
    similar = True
    plus = 0
    minus = 0
    for i in range(26):
        cha = firstLst[i] - newLst[i]
        if cha == 1:
            minus += 1
        elif cha == -1:
            plus += 1
        elif cha == 0:
            pass
        else:
            similar = False
            break
    if similar and plus <= 1 and minus <= 1:
        res += 1

print(res)