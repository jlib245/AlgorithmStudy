import sys
input = lambda : sys.stdin.readline().rstrip().replace(' ', '')

ans = []
while 1 :
    N = int(input())
    if N == 0 :
        break
    s = input().upper()
    res = ""
    cnt = 0
    lst = ['']*len(s)
    idx = 0
    row = 0
    if N < len(s) :
        while cnt < len(s):
            a = row + idx*N
            if a < len(s) :
                lst[row + idx*N] = s[cnt]
                cnt += 1
                idx += 1
            else :
                row += 1
                idx = 0            
    else :
        lst = list(s)    
    ans.append(lst)
    
for row in ans :
    print(*row, sep='')