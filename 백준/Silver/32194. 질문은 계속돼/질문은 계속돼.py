import sys
input = sys.stdin.readline

N = int(input())
lst = [0, 1]
for i in range(N):
    c, x, y = map(int, input().split())
    if c == 1 :
        if lst[y] - lst[x-1] == y - x + 1 :
            res = True
        else :
            res = False
    else :
        if lst[y] == lst[x-1] :
            res = True
        else :
            res = False
    
    if res :
        print("Yes")
        lst.append(lst[-1]+1)
    else :
        print("No")
        lst.append(lst[-1])