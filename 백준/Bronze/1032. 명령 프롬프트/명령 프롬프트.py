import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
lst = []
ans = ""
for _ in range(N) :
    lst.append(list(input()))
for i in range(len(lst[0])) :
    c = lst[0][i]
    for j in range(1, N):
        if c != lst[j][i] :
            ans += '?'
            break
    else :
        ans += c
print(ans)