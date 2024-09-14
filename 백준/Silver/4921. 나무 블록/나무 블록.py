import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

ans = []
while 1 :
    lst = list(map(int, list(input())))
    if lst == [0] :
        break

    if lst[0] != 1 or lst[-1] != 2 :
        ans.append("NOT")
        continue
    prev = [[], [], [4, 6], [4, 6], [1, 3], [1, 3], [8], [8], [5, 7]]
    for i in range(1, len(lst)) :
        if not lst[i-1] in prev[lst[i]] :
            ans.append("NOT")
            break
    else :
        ans.append("VALID")
for i in range(len(ans)) :
    print(f"{i+1}. {ans[i]}")