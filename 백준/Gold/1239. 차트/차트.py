from itertools import permutations

N = int(input())

lst = list(map(int, input().split()))

ans = 0
for P in permutations(lst, N) : #permutation으로 모든 경우 추출
    visit = [False]*(101)
    visit[0] = True
    cnt = 0 
    x = 0
    for dx in P :
        x += dx
        if visit[x-50] :
            cnt += 1
        else :
            visit[x] = True
    if ans < cnt :
        ans = cnt

print(ans)